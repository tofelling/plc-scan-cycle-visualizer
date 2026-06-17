from typing import Callable, Dict, Tuple


ScenarioResult = Tuple[Dict[str, bool], str]
ScenarioFunction = Callable[[Dict[str, bool], Dict[str, bool]], ScenarioResult]


def _as_bool(value: object) -> bool:
    return bool(value)


def run_single_button(input_image: Dict[str, bool], previous_outputs: Dict[str, bool]) -> ScenarioResult:
    button = _as_bool(input_image.get("BUTTON", False))
    motor = button

    if motor:
        explanation = "BUTTON is true, so the output coil MOTOR becomes true during this scan."
    else:
        explanation = "BUTTON is false, so the output coil MOTOR becomes false during this scan."

    return {"MOTOR": motor}, explanation


def run_start_stop_latch(input_image: Dict[str, bool], previous_outputs: Dict[str, bool]) -> ScenarioResult:
    start = _as_bool(input_image.get("START", False))
    stop = _as_bool(input_image.get("STOP", True))
    previous_motor = _as_bool(previous_outputs.get("MOTOR", False))

    motor = stop and (start or previous_motor)

    if not stop:
        explanation = "STOP is false, meaning the stop circuit is broken, so MOTOR is forced off."
    elif start:
        explanation = "STOP is healthy and START is pressed, so MOTOR turns on."
    elif previous_motor:
        explanation = "START is released, but previous MOTOR was true, so the latch keeps MOTOR on."
    else:
        explanation = "STOP is healthy, but START is not pressed and the latch was not active, so MOTOR stays off."

    return {"MOTOR": motor}, explanation


def run_emergency_stop(input_image: Dict[str, bool], previous_outputs: Dict[str, bool]) -> ScenarioResult:
    start = _as_bool(input_image.get("START", False))
    stop = _as_bool(input_image.get("STOP", True))
    e_stop = _as_bool(input_image.get("E_STOP", True))
    previous_motor = _as_bool(previous_outputs.get("MOTOR", False))

    # Teaching rule: emergency stop has priority over both START and the latch.
    # Once E_STOP forces MOTOR off, the latch memory is gone because previous MOTOR
    # becomes false in the next scan. After E_STOP is reset, START must be pressed
    # again to energize MOTOR.
    if not e_stop:
        return (
            {"MOTOR": False},
            "E_STOP is false, so emergency stop overrides START and latch memory. MOTOR is forced off.",
        )

    motor = stop and (start or previous_motor)

    if not stop:
        explanation = "E_STOP is healthy, but STOP is false, so MOTOR is forced off."
    elif start:
        explanation = "E_STOP and STOP are healthy, and START is pressed, so MOTOR turns on."
    elif previous_motor:
        explanation = "E_STOP and STOP are healthy, START is released, and the previous MOTOR state holds the latch."
    else:
        explanation = (
            "E_STOP is reset and STOP is healthy, but MOTOR does not restart automatically. "
            "START must be pressed again."
        )

    return {"MOTOR": motor}, explanation


SCENARIOS: Dict[str, ScenarioFunction] = {
    "single_button": run_single_button,
    "start_stop_latch": run_start_stop_latch,
    "emergency_stop": run_emergency_stop,
}


def get_scenario(scenario_type: str) -> ScenarioFunction:
    try:
        return SCENARIOS[scenario_type]
    except KeyError as error:
        available = ", ".join(sorted(SCENARIOS))
        raise ValueError(f"Unknown scenario_type '{scenario_type}'. Available types: {available}.") from error

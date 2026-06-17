from dataclasses import dataclass
from typing import Any, Dict, List

from .scenarios import get_scenario


@dataclass
class ScanCycleResult:
    cycle_number: int
    input_image: Dict[str, bool]
    previous_output_state: Dict[str, bool]
    explanation: str
    new_output_state: Dict[str, bool]


def run_scan_cycles(example: Dict[str, Any]) -> List[ScanCycleResult]:
    scenario = get_scenario(example["scenario_type"])
    default_inputs = dict(example.get("inputs", {}))
    current_outputs = dict(example.get("outputs", {}))
    results: List[ScanCycleResult] = []

    for cycle_number, cycle_inputs in enumerate(example["cycles"], start=1):
        input_image = default_inputs.copy()
        input_image.update(cycle_inputs)

        previous_output_state = current_outputs.copy()
        new_output_state, explanation = scenario(input_image, previous_output_state)

        results.append(
            ScanCycleResult(
                cycle_number=cycle_number,
                input_image=input_image,
                previous_output_state=previous_output_state,
                explanation=explanation,
                new_output_state=new_output_state,
            )
        )

        current_outputs = new_output_state

    return results

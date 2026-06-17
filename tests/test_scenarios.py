from src.scenarios import run_start_stop_latch, run_ton_timer


def test_start_stop_latch_start_turns_motor_on():
    output_state, _ = run_start_stop_latch(
        {"START": True, "STOP": True},
        {"MOTOR": False},
        {},
    )

    assert output_state["MOTOR"] is True


def test_start_stop_latch_previous_motor_holds_latch():
    output_state, _ = run_start_stop_latch(
        {"START": False, "STOP": True},
        {"MOTOR": True},
        {},
    )

    assert output_state["MOTOR"] is True


def test_start_stop_latch_stop_forces_motor_off():
    output_state, _ = run_start_stop_latch(
        {"START": True, "STOP": False},
        {"MOTOR": True},
        {},
    )

    assert output_state["MOTOR"] is False


def test_ton_timer_increments_et_before_preset():
    output_state, _ = run_ton_timer(
        {"IN": True},
        {"ET": 1, "Q": False},
        {"timer": {"PT": 3, "cycle_time": 1}},
    )

    assert output_state["ET"] == 2
    assert output_state["Q"] is False


def test_ton_timer_sets_q_when_et_reaches_preset():
    output_state, _ = run_ton_timer(
        {"IN": True},
        {"ET": 2, "Q": False},
        {"timer": {"PT": 3, "cycle_time": 1}},
    )

    assert output_state["ET"] == 3
    assert output_state["Q"] is True


def test_ton_timer_resets_when_input_is_false():
    output_state, _ = run_ton_timer(
        {"IN": False},
        {"ET": 3, "Q": True},
        {"timer": {"PT": 3, "cycle_time": 1}},
    )

    assert output_state["ET"] == 0
    assert output_state["Q"] is False

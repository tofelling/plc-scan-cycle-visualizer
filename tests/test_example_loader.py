from pathlib import Path

from src.example_loader import load_example


EXAMPLE_FILES = [
    "examples/01_single_button.yaml",
    "examples/02_start_stop_latch.yaml",
    "examples/03_emergency_stop.yaml",
    "examples/04_ton_timer.yaml",
]


def test_all_examples_can_be_loaded():
    for example_file in EXAMPLE_FILES:
        example = load_example(Path(example_file))

        assert example["name"]
        assert example["description"]
        assert example["scenario_type"]
        assert example["cycles"]

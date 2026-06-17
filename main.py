from pathlib import Path
import sys

from src.example_loader import ExampleValidationError, load_example
from src.logger import format_scan_cycle_log
from src.scan_cycle import run_scan_cycles


DEFAULT_EXAMPLE = "examples/02_start_stop_latch.yaml"


def main() -> int:
    example_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(DEFAULT_EXAMPLE)

    if not example_path.exists():
        print(f"Error: example file not found: {example_path}")
        print("Try one of these:")
        print("  python main.py examples/01_single_button.yaml")
        print("  python main.py examples/02_start_stop_latch.yaml")
        print("  python main.py examples/03_emergency_stop.yaml")
        return 1

    try:
        example = load_example(example_path)
        results = run_scan_cycles(example)
    except ExampleValidationError as error:
        print(f"Error: invalid example file: {error}")
        return 1
    except ValueError as error:
        print(f"Error: {error}")
        return 1

    print(format_scan_cycle_log(example, results))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

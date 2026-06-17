import argparse
from pathlib import Path

from src.example_loader import ExampleValidationError, load_example
from src.logger import format_scan_cycle_log
from src.scan_cycle import run_scan_cycles
from src.timing_diagram import generate_timing_diagram


DEFAULT_EXAMPLE = "examples/02_start_stop_latch.yaml"
ALL_EXAMPLES = [
    "examples/01_single_button.yaml",
    "examples/02_start_stop_latch.yaml",
    "examples/03_emergency_stop.yaml",
    "examples/04_ton_timer.yaml",
]


def output_path_for(example_path: Path) -> Path:
    return Path("outputs") / f"{example_path.stem}_timing.png"


def run_example(example_path: Path, plot: bool = False) -> int:
    if not example_path.exists():
        print(f"Error: example file not found: {example_path}")
        print("Try one of these:")
        print("  python main.py examples/01_single_button.yaml")
        print("  python main.py examples/02_start_stop_latch.yaml")
        print("  python main.py examples/03_emergency_stop.yaml")
        print("  python main.py examples/04_ton_timer.yaml")
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

    if plot:
        output_path = generate_timing_diagram(example, results, str(output_path_for(example_path)))
        print()
        print(f"Timing diagram saved to: {output_path}")

    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run PLC scan cycle teaching examples and optionally generate timing diagrams."
    )
    parser.add_argument("example_path", nargs="?", help="Path to one YAML example file.")
    parser.add_argument("--plot", action="store_true", help="Generate a timing diagram for the selected example.")
    parser.add_argument("--plot-all", action="store_true", help="Run all examples and generate all timing diagrams.")
    args = parser.parse_args()

    if args.plot_all:
        exit_code = 0
        for index, example_name in enumerate(ALL_EXAMPLES):
            if index:
                print()
                print("=" * 72)
                print()
            exit_code = max(exit_code, run_example(Path(example_name), plot=True))
        return exit_code

    example_path = Path(args.example_path) if args.example_path else Path(DEFAULT_EXAMPLE)
    return run_example(example_path, plot=args.plot)


if __name__ == "__main__":
    raise SystemExit(main())

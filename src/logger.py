from .scan_cycle import ScanCycleResult


def _format_state(state):
    if not state:
        return "(none)"
    return ", ".join(f"{name}={value}" for name, value in state.items())


def format_example_header(example):
    lines = [
        f"Example: {example['name']}",
        f"Description: {example['description']}",
        f"Scenario type: {example['scenario_type']}",
    ]
    return "\n".join(lines)


def format_cycle_log(result: ScanCycleResult) -> str:
    lines = [
        f"Cycle {result.cycle_number}",
        f"  Input scan: {_format_state(result.input_image)}",
        f"  Previous state: {_format_state(result.previous_output_state)}",
        f"  Program execution: {result.explanation}",
        f"  Output update: {_format_state(result.new_output_state)}",
    ]
    return "\n".join(lines)


def format_scan_cycle_log(example, results):
    sections = [format_example_header(example), ""]

    for result in results:
        sections.append(format_cycle_log(result))
        sections.append("")

    return "\n".join(sections).rstrip()

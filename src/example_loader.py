from pathlib import Path
from typing import Any, Dict, Union

import yaml


REQUIRED_FIELDS = ["name", "description", "scenario_type", "cycles"]


class ExampleValidationError(ValueError):
    """Raised when an example YAML file is missing required teaching data."""


def load_example(path: Union[str, Path]) -> Dict[str, Any]:
    example_path = Path(path)
    with example_path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    if not isinstance(data, dict):
        raise ExampleValidationError("Example file must contain a YAML mapping at the top level.")

    missing_fields = [field for field in REQUIRED_FIELDS if field not in data]
    if missing_fields:
        joined = ", ".join(missing_fields)
        raise ExampleValidationError(f"Example file is missing required field(s): {joined}.")

    if not isinstance(data["cycles"], list) or not data["cycles"]:
        raise ExampleValidationError("Field 'cycles' must be a non-empty list of scan input states.")

    for index, cycle in enumerate(data["cycles"], start=1):
        if not isinstance(cycle, dict):
            raise ExampleValidationError(f"Cycle {index} must be a mapping of input names to values.")

    data.setdefault("inputs", {})
    data.setdefault("outputs", {})

    if not isinstance(data["inputs"], dict):
        raise ExampleValidationError("Field 'inputs' must be a mapping of input names to default values.")

    if not isinstance(data["outputs"], dict):
        raise ExampleValidationError("Field 'outputs' must be a mapping of output names to initial values.")

    return data

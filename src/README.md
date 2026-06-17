# Source Directory

This directory contains the small v0.1 runtime.

The implementation is intentionally small and focused:

- load one YAML example;
- print a readable scan cycle log;
- avoid building a full PLC simulator;
- avoid building a ladder editor or GUI.

Current modules:

- `example_loader.py`: loads and validates YAML examples.
- `scenarios.py`: contains the three fixed teaching scenarios.
- `scan_cycle.py`: runs input scan, program execution, and output update.
- `logger.py`: formats scan cycle results as readable teaching logs.

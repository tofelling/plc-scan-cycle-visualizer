# PLC Scan Cycle Visualizer

A beginner-friendly Python learning tool for visualizing how a PLC scan cycle turns input states into output states.

## Who Is This For?

- Automation engineering students learning PLC basics.
- PLC beginners who know ladder logic terms but do not yet understand execution timing.
- Students preparing portfolio projects for internships or entry-level automation roles.
- Teachers or lab assistants who need small, hardware-free teaching examples.

## What Problem Does It Solve?

Many students can recite the PLC scan cycle, but still feel confused by practical questions:

- Why does an input change not always affect an output immediately?
- Why can a start/stop latch keep a motor running after the start button is released?
- Why should stop and emergency stop conditions be placed carefully in control logic?
- Why does a PLC execute logic scan by scan instead of reacting like an ordinary interactive Python script?

This project is not an industrial PLC simulator. It is a small teaching tool focused on making the scan cycle visible.

## What Is a PLC Scan Cycle?

A PLC usually repeats three basic steps:

1. Input scan: read physical input states into memory.
2. Program execution: run the control logic using the stored input image.
3. Output update: write the computed output states to the real outputs.

The key idea is that logic is evaluated in repeated cycles. This timing model explains many beginner surprises in latch, interlock, and emergency stop examples.

## MVP Examples

The first version will only cover three teaching cases:

v0.1 supports three fixed teaching scenarios: `single_button`, `start_stop_latch`, and `emergency_stop`.

| Example | Purpose |
|---|---|
| `01_single_button.yaml` | Show how one input button controls one output coil across scan cycles. |
| `02_start_stop_latch.yaml` | Show why a motor latch remains on after the start button is released. |
| `03_emergency_stop.yaml` | Show how an emergency stop condition overrides normal start logic. |

The current version uses fixed scenario logic, not a general ladder logic parser.

## Quick Start

Install dependencies and run the start-stop latch example:

```bash
pip install -r requirements.txt
python main.py examples/02_start_stop_latch.yaml
```

You can also run `python main.py` to use the default start-stop latch example.

## v0.1 Output Example

The v0.1 output is a text-based scan cycle log. For the start-stop latch example, the output looks like this:

```text
Example: Start Stop Motor Latch
Description: Demonstrates how a motor latch holds its output across scan cycles.
Scenario type: start_stop_latch

Cycle 1
  Input scan: START=False, STOP=True
  Previous state: MOTOR=False
  Program execution: STOP is healthy, but START is not pressed and the latch was not active, so MOTOR stays off.
  Output update: MOTOR=False

Cycle 2
  Input scan: START=True, STOP=True
  Previous state: MOTOR=False
  Program execution: STOP is healthy and START is pressed, so MOTOR turns on.
  Output update: MOTOR=True

Cycle 3
  Input scan: START=False, STOP=True
  Previous state: MOTOR=True
  Program execution: START is released, but previous MOTOR was true, so the latch keeps MOTOR on.
  Output update: MOTOR=True

Cycle 4
  Input scan: START=False, STOP=False
  Previous state: MOTOR=True
  Program execution: STOP is false, meaning the stop circuit is broken, so MOTOR is forced off.
  Output update: MOTOR=False

Cycle 5
  Input scan: START=False, STOP=True
  Previous state: MOTOR=False
  Program execution: STOP is healthy, but START is not pressed and the latch was not active, so MOTOR stays off.
  Output update: MOTOR=False
```

Later versions may generate timing diagrams showing input states, internal logic states, and output states across multiple scan cycles.

## Core Logic

The start-stop latch example uses this teaching rule:

```text
MOTOR = STOP and (START or previous MOTOR)
```

Where:

- `STOP=True` means the stop circuit is healthy.
- `STOP=False` means the stop button is pressed or the stop circuit is broken.
- `previous MOTOR=True` allows the latch to hold after `START` is released.

This is fixed scenario logic for teaching scan cycles. It is not a full ladder logic interpreter.

## Project Roadmap

- v0.1: Display scan cycle logs for the three MVP examples. Implemented.
- v0.2: Generate timing diagrams from example data.
- v0.3: Add a basic TON timer teaching example.
- v0.4: Add practice questions and expected answers.
- v1.0: Become a small, teachable, demo-ready PLC scan cycle learning tool.

See [roadmap.md](roadmap.md) for more detail.

## Why This Project Is Useful for Automation Students

This project connects classroom PLC concepts to visible behavior. Instead of only reading ladder diagrams, students can inspect how input states, internal logic, and output states change from scan to scan.

It is intentionally limited:

- No complete ladder editor.
- No complete IEC 61131-3 parser.
- No real PLC communication.
- No hardware connection.
- No complex GUI.

That narrow scope makes the project realistic for a student portfolio while still staying close to real automation concepts.

## Current Status

v0.1 implemented.

The repository can load the three YAML examples and print beginner-friendly scan cycle logs in the terminal.

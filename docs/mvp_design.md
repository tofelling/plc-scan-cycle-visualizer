# MVP Design

The MVP should be small enough to build and explain clearly. It should teach PLC scan cycle behavior, not behave like a full PLC development environment.

## 1. MVP Input Format

The planned input format is a simple YAML file.

Each example file should describe:

- `name`: human-readable example name.
- `description`: what the example teaches.
- `inputs`: input devices used by the example.
- `outputs`: output devices controlled by the example.
- `logic_description`: plain-English logic rules.
- `expected_behavior`: scan-by-scan expected states.

The current YAML files are design drafts. They are not required to be executable yet.

## 2. MVP Output Format

The first implementation should produce a text-based scan cycle log.

Planned output fields:

- cycle number;
- input scan values;
- previous output or memory state when needed;
- program execution explanation;
- output update result.

Example style:

```text
Cycle 2
Input scan: START=True, STOP=True
Previous state: MOTOR=False
Program execution: STOP is healthy and START is pressed, so MOTOR becomes True
Output update: MOTOR=True
```

In v0.2, the same data may be used to generate timing diagrams.

## 3. What the Three Examples Show

### Example 1: Single Button Controls One Coil

Shows the basic relationship between one input and one output.

Teaching point:

- The input is sampled first.
- The logic is evaluated next.
- The output is updated at the end of the scan.

### Example 2: Start Stop Motor Latch

Shows how a motor output can remain on after the START button is released.

Teaching point:

- The latch depends on previous output state.
- STOP breaks the latch.
- The scan cycle explains why the behavior is predictable.

### Example 3: Emergency Stop Interlock

Shows how an emergency stop condition should override normal start and latch logic.

Teaching point:

- E_STOP false forces MOTOR false.
- The motor should not automatically restart after the emergency stop is reset.
- Safety-related logic should be easy to inspect and explain.

## 4. Features for Later

The following features are intentionally postponed:

- complete ladder diagram editor;
- IEC 61131-3 parser;
- real PLC communication;
- Modbus or OPC UA integration;
- hardware input/output;
- complex GUI;
- full timer and counter instruction set;
- user-defined ladder networks.

These may be interesting later, but they would make the first version too large.

## 5. Why Not Build a Full Ladder Editor Now?

A full ladder editor is a much bigger project than this MVP. It would require:

- a visual editor;
- ladder diagram parsing;
- instruction validation;
- execution semantics;
- a project file format;
- many edge cases from real PLC systems.

That would distract from the first learning goal: making the PLC scan cycle visible.

The first version should stay narrow. If students can understand input scan, program execution, output update, latch behavior, and emergency stop override, the MVP has already succeeded.

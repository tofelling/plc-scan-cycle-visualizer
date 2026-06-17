# PLC Scan Cycle Concept

This document explains the PLC scan cycle in beginner-friendly terms. It is written for students who are learning PLC logic without real hardware.

## 1. Input Scan

During the input scan, the PLC reads the current state of input devices such as push buttons, limit switches, and sensors.

The important detail is that the PLC stores these states in memory. The control program usually works with this stored input image during the current scan.

Example:

- A START button is physically pressed.
- During input scan, the PLC records `START = True`.
- The program uses that recorded value while executing this scan.

## 2. Program Execution

During program execution, the PLC evaluates the control logic.

For a beginner, it helps to imagine that the PLC asks:

- What were the input states at the start of this scan?
- What were the previous internal or output states?
- Based on the logic, what should the new output states become?

In ladder logic, this is where contacts, coils, latches, interlocks, and timers are evaluated.

## 3. Output Update

During output update, the PLC writes the computed output states to physical outputs.

This means the real output changes after the program has finished evaluating the logic for the current scan.

Example:

- The program decides `MOTOR = True`.
- During output update, the motor output is turned on.

## 4. Why Scan Cycle Matters

The scan cycle matters because PLC logic is not usually evaluated as a continuous instant reaction. It is evaluated repeatedly, scan by scan.

This explains several beginner-level questions:

- An input change affects the logic when the PLC reads it during an input scan.
- Output changes are applied during the output update step.
- A latch can use the previous output state to keep an output on.
- Stop and emergency stop logic must be evaluated in the correct control path so unsafe commands do not keep outputs energized.

Understanding scan cycles helps students reason about timing, memory, and safety-related logic.

## 5. Intuitive Start-Stop Motor Latch Explanation

Consider a simple motor latch with:

- `START`: a normally open start button.
- `STOP`: a normally closed stop button.
- `MOTOR`: an output coil.

The basic idea is:

```text
MOTOR turns on when STOP is healthy and START is pressed.
MOTOR stays on when STOP is healthy and MOTOR was already on.
MOTOR turns off when STOP is pressed.
```

The latch works because the program uses the previous `MOTOR` state during the next scan.

One possible sequence:

| Scan | START | STOP | Previous MOTOR | New MOTOR | Meaning |
|---|---|---|---|---|---|
| 1 | False | True | False | False | Nothing starts. |
| 2 | True | True | False | True | START turns MOTOR on. |
| 3 | False | True | True | True | MOTOR holds itself on. |
| 4 | False | False | True | False | STOP breaks the latch. |

The main lesson: the motor does not stay on because the START button is still pressed. It stays on because the logic includes the previous motor state as a holding condition.

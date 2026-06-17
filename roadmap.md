# Project Roadmap

This roadmap keeps the project small and useful. The goal is not to build a full PLC platform, but to make PLC scan cycle behavior understandable for beginners.

## v0.1: Scan Cycle Logs for Three Examples

Status: Implemented.

Goal: show how input states, program logic, and output states change across scan cycles.

Planned scope:

- Load three example design files.
- Represent each example as a fixed teaching scenario.
- Print a readable log for each scan cycle.
- Cover only:
  - single button to coil;
  - start/stop motor latch;
  - emergency stop interlock.

Success criteria:

- A beginner can read the output and explain what happened in each cycle.
- The README can show one complete example log.

## v0.2: Timing Diagram Output

Status: Implemented.

Goal: turn scan cycle logs into simple timing diagrams.

Planned scope:

- Plot input and output states over cycle number.
- Use clear labels for START, STOP, E_STOP, and MOTOR.
- Export a static image for README usage.

Success criteria:

- Each MVP example has one timing diagram.
- The diagrams can be used in class notes or a portfolio README.

## v0.3: Basic TON Timer

Status: Implemented.

Goal: introduce one common PLC timer concept without implementing a full PLC instruction set.

Planned scope:

- Add one teaching example for TON timer behavior.
- Show preset time, elapsed time, enable input, and done bit.
- Explain why timer state depends on repeated scans.

Success criteria:

- The timer example is understandable without real hardware.
- The output log clearly shows when the timer becomes done.

## v0.4: Practice Questions and Answers

Status: Implemented.

Goal: make the project useful as a learning resource, not only a demo.

Planned scope:

- Add beginner exercises for each example.
- Include expected answers.
- Ask students to predict outputs before reading the log.

Success criteria:

- The project can be used as a small self-study module.
- Each example has at least three practice questions.

## v1.0: Teachable Demo Tool

Goal: form a stable, small tool for explaining PLC scan cycles.

Planned scope:

- Clean project structure.
- Reliable example loading.
- Clear documentation.
- Scan cycle logs and timing diagrams.
- Beginner exercises.

Success criteria:

- A new user can run the examples in under 10 minutes.
- The project clearly states what it does and does not do.
- The tool is suitable for an automation student portfolio.

# Project Showcase

## What This Project Demonstrates

PLC Scan Cycle Visualizer is a small Python teaching tool for automation students. It demonstrates how scan-cycle thinking connects inputs, previous states, program logic, and outputs.

The project focuses on learning value:

- scan cycle logs in the terminal;
- static timing diagrams for README and class notes;
- fixed teaching scenarios instead of a full PLC runtime;
- practice questions that ask learners to predict outputs first;
- pytest tests and GitHub Actions CI for core behavior.

如果你是自动化专业学生，这个项目可以用来展示你不仅会写 Python，还能把 PLC 扫描周期、自锁和定时器这些专业概念做成可运行、可解释、可测试的小工具。

## Four Teaching Examples

| Example | Main idea |
|---|---|
| `01_single_button.yaml` | Current input directly controls output. |
| `02_start_stop_latch.yaml` | Previous output state can hold a latch. |
| `03_emergency_stop.yaml` | Emergency stop overrides normal start logic. |
| `04_ton_timer.yaml` | TON timer accumulates `ET` before `Q=True`. |

## Start/Stop Latch Walkthrough

The start-stop latch example uses:

```text
MOTOR = STOP and (START or previous MOTOR)
```

In the timing diagram, `START` is only true during Cycle 2. `MOTOR` remains true in Cycle 3 because `previous MOTOR=True` keeps the latch active. When `STOP=False` in Cycle 4, `MOTOR` is forced off.

![Start Stop Latch Timing Diagram](../outputs/02_start_stop_latch_timing.png)

## TON Timer Walkthrough

The TON timer example shows why timer outputs depend on continuous scan cycles.

```text
If IN=False:
  ET = 0
  Q = False

If IN=True:
  ET = min(previous ET + cycle_time, PT)
  Q = ET >= PT
```

`Q` does not become true immediately when `IN=True`. `ET` must accumulate until it reaches `PT`. If `IN=False`, the timer resets.

![TON Timer Timing Diagram](../outputs/04_ton_timer_timing.png)

## Practice Questions

The exercises turn the project from a demo into a small learning loop:

1. Read the YAML example.
2. Predict the output for a scan cycle.
3. Run `main.py`.
4. Compare your prediction with the answer.
5. Check the timing diagram.

Practice files:

- [Single Button Practice](../exercises/01_single_button_questions.md)
- [Start/Stop Latch Practice](../exercises/02_start_stop_latch_questions.md)
- [Emergency Stop Practice](../exercises/03_emergency_stop_questions.md)
- [TON Timer Practice](../exercises/04_ton_timer_questions.md)

## How This Can Be Used in a Portfolio

- Built a Python-based PLC scan cycle learning tool for automation students.
- Implemented scan cycle logs, timing diagram generation, fixed teaching scenarios, and practice questions.
- Added pytest tests and GitHub Actions CI to protect core teaching logic.

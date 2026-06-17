# PLC Scan Cycle Visualizer

[![Release](https://img.shields.io/github/v/release/tofelling/plc-scan-cycle-visualizer)](https://github.com/tofelling/plc-scan-cycle-visualizer/releases)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Status](https://img.shields.io/badge/status-v0.6.0-green)
![Focus](https://img.shields.io/badge/focus-PLC%20scan%20cycle-orange)

A small Python learning tool that makes PLC scan cycles visible through logs, timing diagrams, and practice questions.

适合刚开始学习 PLC 的自动化学生：不用真实硬件，也能看清输入扫描、逻辑执行、输出刷新、自锁、急停和 TON 定时器是怎么一步步发生的。

![Start Stop Latch Timing Diagram](outputs/02_start_stop_latch_timing.png)

## Quick Start / 快速开始

```bash
pip install -r requirements.txt
python main.py examples/02_start_stop_latch.yaml
```

Generate a timing diagram:

```bash
python main.py examples/02_start_stop_latch.yaml --plot
```

Generate all timing diagrams:

```bash
python main.py --plot-all
```

[中文说明](docs/README.zh-CN.md) | [Project Showcase](docs/showcase.md)

## What It Includes

- Scan cycle logs
- Timing diagrams
- Four fixed teaching examples
- Practice questions
- Tests and CI

## Who Is This For? / 适合谁？

- Automation engineering students learning PLC basics.
- PLC beginners who know ladder logic terms but do not yet understand execution timing.
- Students preparing portfolio projects for internships or entry-level automation roles.
- Teachers or lab assistants who need small, hardware-free teaching examples.

如果你是自动化专业学生，或者刚开始学 PLC，这个项目可以作为一个不需要硬件的小练习环境。

## Teaching Examples

| Example | Purpose |
|---|---|
| `01_single_button.yaml` | Show how one input button controls one output coil across scan cycles. |
| `02_start_stop_latch.yaml` | Show why a motor latch remains on after the start button is released. |
| `03_emergency_stop.yaml` | Show how an emergency stop condition overrides normal start logic. |
| `04_ton_timer.yaml` | Show how a TON timer accumulates elapsed time before `Q` becomes true. |

The current version uses fixed scenario logic, not a general ladder logic parser.

## Output Preview

The terminal log shows the three basic scan-cycle steps: `Input scan`, `Program execution`, and `Output update`.

```text
Cycle 2
  Input scan: START=True, STOP=True
  Previous state: MOTOR=False
  Program execution: STOP is healthy and START is pressed, so MOTOR turns on.
  Output update: MOTOR=True
```

## Timing Diagram Preview / 时序图预览

In the start-stop latch example, `START` is pressed only during Cycle 2, but `MOTOR` remains on in Cycle 3 because the latch uses the previous `MOTOR` state. When `STOP` becomes false in Cycle 4, `MOTOR` is forced off.

在这个例子中，START 只在第 2 个扫描周期被按下，但 MOTOR 在第 3 个周期仍然保持开启，因为自锁逻辑使用了上一轮的 MOTOR 状态。

![Start Stop Latch Timing Diagram](outputs/02_start_stop_latch_timing.png)

## TON Timer Preview

The TON timer diagram shows that `Q` does not become true immediately when `IN=True`. The timer must accumulate `ET` across continuous scan cycles until `ET` reaches `PT`.

TON 延时定时器在 IN=True 后不会立刻 Q=True；它需要在连续扫描周期中累计 ET，达到 PT 后 Q 才会变为 True。

![TON Timer Timing Diagram](outputs/04_ton_timer_timing.png)

## Practice Questions / 练习题

Practice questions let learners predict outputs before checking the answer and explanation.

练习题的用法很简单：先根据当前输入和上一轮状态预测输出，再对照答案解释。这样比直接看结论更容易理解 scan cycle、自锁、急停和 TON 定时器。

- [Single Button Practice](exercises/01_single_button_questions.md)
- [Start/Stop Latch Practice](exercises/02_start_stop_latch_questions.md)
- [Emergency Stop Practice](exercises/03_emergency_stop_questions.md)
- [TON Timer Practice](exercises/04_ton_timer_questions.md)
- [Practice Guide](docs/practice_guide.md)

## Core Logic / 核心逻辑

The start-stop latch example uses this teaching rule:

```text
MOTOR = STOP and (START or previous MOTOR)
```

- `STOP=True` means the stop circuit is healthy.
- `STOP=False` means the stop button is pressed or the stop circuit is broken.
- `previous MOTOR=True` allows the latch to hold after `START` is released.

STOP=True 表示停止回路正常；previous MOTOR=True 表示上一轮电机已经开启。因此松开 START 后，MOTOR 仍然可以通过自锁逻辑保持开启。

## Development / 开发

```bash
pip install -r requirements-dev.txt
pytest
```

## Continuous Integration / CI

This project uses GitHub Actions to run the pytest suite on push and pull request events.

## Project Scope

This project is intentionally limited:

- No complete ladder editor.
- No complete IEC 61131-3 parser.
- No real PLC communication.
- No hardware connection.
- No complex GUI.

## Current Status / 当前状态

v0.6 implemented.

The repository can load four YAML examples, print beginner-friendly scan cycle logs, generate static timing diagrams, provide practice questions, and run pytest checks in CI.

当前版本已经包含四个教学案例、scan cycle logs、timing diagrams、配套练习题，以及基础测试和 CI。

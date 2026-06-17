# Practice Guide

This guide explains how to use the practice questions as a learning loop, not as a memorization checklist.

中文说明：这个练习模块的目的不是刷题，而是训练学生理解每一轮 scan cycle 中输入、上一轮状态、程序逻辑和输出之间的关系。

## How to Use the Practice Questions

Each exercise file focuses on one teaching example. Read the question, inspect the given state or cycle, and write your prediction before checking the answer.

Recommended order:

1. Open the matching YAML file in `examples/`.
2. Read the input sequence for the target cycle.
3. Predict the output state before running the example.
4. Run `main.py` to view the scan cycle log.
5. Compare your prediction with the answer and explanation.
6. View the timing diagram to connect the text log with signal changes.

## Recommended Learning Flow

Start with `01_single_button.yaml`, then move to `02_start_stop_latch.yaml`, `03_emergency_stop.yaml`, and finally `04_ton_timer.yaml`.

This order is intentional:

- single button: current input directly controls output;
- start-stop latch: previous output state matters;
- emergency stop: override logic matters;
- TON timer: internal elapsed time matters across scans.

## Step 1: Read the YAML First

Before running the program, open the example file and inspect:

- `scenario_type`;
- default `inputs`;
- default `outputs`;
- `cycles`;
- `timer` fields for the TON example.

## Step 2: Predict the Output

For each question, pause at the `Your prediction` section. Write down what you think the output should be.

Do not worry about being wrong. The goal is to notice which part of the scan cycle you misunderstood.

## Step 3: Run the Scan Cycle Log

Run the matching example:

```bash
python main.py examples/02_start_stop_latch.yaml
```

For the TON example:

```bash
python main.py examples/04_ton_timer.yaml
```

Look for:

- `Input scan`;
- `Previous state`;
- `Program execution`;
- `Output update`.

## Step 4: Check the Answer Explanation

Return to the exercise file and compare your prediction with the answer.

If your prediction was wrong, ask:

- Did I use the current input image?
- Did I consider the previous output state?
- Did I apply stop or emergency stop override first?
- Did I track `ET` correctly for the TON timer?

## Step 5: View the Timing Diagram

Generate the timing diagram:

```bash
python main.py --plot-all
```

Then compare the graph with the text log. The diagram is useful for seeing when a signal changes and whether the output changes immediately or after one or more scan cycles.

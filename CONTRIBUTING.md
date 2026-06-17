# Contributing

Thanks for considering a contribution. This project is intentionally small: it is a beginner-friendly teaching tool for PLC scan cycle concepts, not an industrial PLC runtime.

## Project Scope

The project helps automation students understand:

- input scan;
- program execution;
- output update;
- latch behavior;
- emergency stop override;
- basic TON timer behavior.

## What Contributions Are Welcome

- improving examples;
- improving documentation;
- adding beginner-friendly practice questions;
- fixing bugs;
- improving timing diagram readability;
- improving Chinese explanations.

## What Contributions Are Not in Scope Yet

- full ladder editor;
- real PLC communication;
- full IEC 61131-3 runtime;
- industrial PLC simulator claims.

## How to Run the Project Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the default example:

```bash
python main.py
```

Run a specific example:

```bash
python main.py examples/04_ton_timer.yaml --plot
```

Generate all timing diagrams:

```bash
python main.py --plot-all
```

## How to Run Tests

Install development dependencies:

```bash
pip install -r requirements-dev.txt
```

Run tests:

```bash
pytest
```

## Suggested Issue Types

- unclear explanation;
- typo or translation improvement;
- beginner exercise idea;
- YAML example issue;
- scan cycle log bug;
- timing diagram readability issue.

## Note for Chinese Learners

如果你主要用中文学习 PLC，也可以贡献中文文档、练习题和案例解释。这个项目欢迎中文学习者参与，但请不要把它扩展成工业级 PLC 仿真器。

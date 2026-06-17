# PLC Scan Cycle Visualizer 中文说明

这是一个面向自动化学生和 PLC 初学者的 Python 教学小工具，用来演示 PLC 扫描周期如何把输入状态变成输出状态。它不是工业级 PLC 仿真器，而是一个小而清晰的学习项目。

## 项目是什么

项目读取 `examples/*.yaml` 中的教学示例，运行固定的教学逻辑，然后在终端输出 scan cycle logs。v0.2 开始可以生成静态 timing diagrams，v0.3 新增了一个基础 TON 延时定时器示例。

## 适合谁

- 自动化专业学生；
- PLC 初学者；
- 想理解自锁、互锁、急停和定时器逻辑的人；
- 想做一个小型 GitHub 自动化方向作品集项目的人。

## 解决什么问题

很多初学者会背 PLC 扫描周期，但不理解输入和输出为什么不是“随时立即变化”。这个项目用几个小例子展示输入采样、程序执行、输出刷新，以及上一轮输出状态或定时器状态如何影响本轮逻辑。

## PLC 扫描周期是什么

一个简化的 PLC 扫描周期可以理解为三步：

1. `Input scan`：读取输入状态，例如 `START`、`STOP`、`E_STOP`、`IN`。
2. `Program execution`：根据当前输入、上一轮状态和固定教学逻辑进行计算。
3. `Output update`：更新输出，例如 `MOTOR`、`Q`、`ET`。

重点是：PLC 通常是一轮一轮扫描执行，而不是像普通交互程序那样随时响应。

## 如何运行

安装依赖：

```bash
pip install -r requirements.txt
```

运行默认示例：

```bash
python main.py
```

运行 start-stop latch 示例：

```bash
python main.py examples/02_start_stop_latch.yaml
```

运行 TON timer 示例并生成时序图：

```bash
python main.py examples/04_ton_timer.yaml --plot
```

生成全部时序图：

```bash
python main.py --plot-all
```

## 四个示例说明

| 示例 | 说明 |
|---|---|
| `01_single_button.yaml` | 展示 `BUTTON` 如何直接控制 `MOTOR`。 |
| `02_start_stop_latch.yaml` | 展示 `START`、`STOP` 和 `previous MOTOR` 如何形成自锁。 |
| `03_emergency_stop.yaml` | 展示 `E_STOP=False` 时如何强制关闭 `MOTOR`，并且恢复后不会自动重启。 |
| `04_ton_timer.yaml` | 展示 TON 定时器如何在连续扫描周期中累计 `ET`，直到 `Q=True`。 |

## 时序图怎么看

横轴是扫描周期编号，纵轴是信号名称或数值状态。`START`、`STOP`、`MOTOR`、`IN`、`Q` 这类信号通常用 0/1 阶梯线表示。

在 start-stop latch 示例中，`START` 只在 Cycle 2 为 True，但 `MOTOR` 在 Cycle 3 仍保持 True，因为逻辑使用了上一轮的 `MOTOR` 状态。当 `STOP` 在 Cycle 4 变为 False 时，`MOTOR` 被强制关闭。

## TON 定时器是什么

TON 是 on-delay timer，也就是“接通延时定时器”。它常用于表示：输入条件持续满足一段时间后，输出完成位才变为 True。

在这个项目里：

- `IN`：定时器输入；
- `PT`：preset time，预设时间；
- `ET`：elapsed time，已经累计的时间；
- `Q`：done bit，定时完成位。

教学逻辑是：

```text
If IN=False:
  ET = 0
  Q = False

If IN=True:
  ET = min(previous ET + cycle_time, PT)
  Q = ET >= PT
```

这能体现 scan cycle 的原因是：`ET` 不是一次性跳到 `PT`，而是在连续扫描周期中一轮一轮累加。如果 `IN=False`，定时器复位，`ET` 回到 0，`Q=False`。

## 练习题模块

v0.4 新增了配套练习题。建议先读题并预测输出，再运行程序查看 scan cycle log，最后对照答案和解释。

- [Single Button Practice](../exercises/01_single_button_questions.md)
- [Start/Stop Latch Practice](../exercises/02_start_stop_latch_questions.md)
- [Emergency Stop Practice](../exercises/03_emergency_stop_questions.md)
- [TON Timer Practice](../exercises/04_ton_timer_questions.md)
- [Practice Guide](practice_guide.md)

## 核心自锁逻辑

start-stop latch 的教学逻辑是：

```text
MOTOR = STOP and (START or previous MOTOR)
```

其中：

- `STOP=True` 表示停止回路正常；
- `STOP=False` 表示停止按钮被按下或停止回路断开；
- `previous MOTOR=True` 表示上一轮电机已经开启，因此松开 `START` 后仍可以保持。

## 当前项目不是什么

当前项目不是：

- 完整 PLC 仿真器；
- 完整 ladder editor；
- IEC 61131-3 解释器；
- 真实 PLC 通信工具；
- 硬件连接项目；
- 复杂 GUI 软件。

它只使用固定场景逻辑来解释 PLC scan cycle。

## 当前状态和下一步计划

当前状态：v0.4 implemented。

现在已经可以：

- 读取四个 YAML 示例；
- 输出 scan cycle logs；
- 生成 timing diagram PNG 图片；
- 演示基础 TON timer 行为；
- 提供四组配套练习题和答案解释。

下一步 v1.0 计划整理项目结构、最终文档和示例展示，让项目更适合作为教学和作品集展示工具。

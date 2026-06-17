from pathlib import Path
from typing import Any, Dict, List

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from .scan_cycle import ScanCycleResult


def _signal_names(example: Dict[str, Any], results: List[ScanCycleResult]) -> List[str]:
    names: List[str] = []

    for group in ("inputs", "outputs"):
        for name in example.get(group, {}):
            if name not in names:
                names.append(name)

    for result in results:
        for state in (result.input_image, result.new_output_state):
            for name in state:
                if name not in names:
                    names.append(name)

    return names


def _signal_value(result: ScanCycleResult, signal_name: str) -> bool:
    if signal_name in result.input_image:
        return bool(result.input_image[signal_name])
    if signal_name in result.new_output_state:
        return bool(result.new_output_state[signal_name])
    return False


def _ton_value(result: ScanCycleResult, signal_name: str) -> float:
    if signal_name in result.input_image:
        return float(result.input_image[signal_name])
    if signal_name in result.new_output_state:
        return float(result.new_output_state[signal_name])
    return 0


def _diagram_title(example: Dict[str, Any]) -> str:
    title = str(example["name"])
    if example.get("scenario_type") == "ton_timer":
        return title.replace("T O N", "TON")
    return title


def _generate_ton_timer_diagram(
    example: Dict[str, Any],
    results: List[ScanCycleResult],
    output: Path,
) -> Path:
    cycles = [result.cycle_number for result in results]
    x_values = cycles + [cycles[-1] + 1]
    timer = example.get("timer", {})
    pt = float(timer.get("PT", 3))

    fig, (ax_signals, ax_et) = plt.subplots(
        2,
        1,
        figsize=(9, 5.4),
        sharex=True,
        gridspec_kw={"height_ratios": [1, 1.15]},
    )

    for index, signal_name in enumerate(["IN", "Q"]):
        values = [_ton_value(result, signal_name) + index * 1.5 for result in results]
        values.append(values[-1])
        ax_signals.step(x_values, values, where="post", linewidth=2.2, label=signal_name)

    ax_signals.set_title(_diagram_title(example), fontsize=14, pad=14)
    ax_signals.set_yticks([0.5, 2.0])
    ax_signals.set_yticklabels(["IN", "Q"])
    ax_signals.set_ylim(-0.25, 2.75)
    ax_signals.grid(axis="x", linestyle="--", alpha=0.35)
    ax_signals.spines["top"].set_visible(False)
    ax_signals.spines["right"].set_visible(False)

    et_values = [_ton_value(result, "ET") for result in results]
    et_values.append(et_values[-1])
    ax_et.step(x_values, et_values, where="post", linewidth=2.2, color="#2ca02c", label="ET")
    ax_et.axhline(pt, color="#d62728", linestyle="--", linewidth=1.5, label=f"PT={int(pt)}")
    ax_et.set_ylabel("ET")
    ax_et.set_xlabel("Cycle")
    ax_et.set_xticks(cycles)
    ax_et.set_xlim(cycles[0], cycles[-1] + 1)
    ax_et.set_ylim(-0.2, max(pt + 0.8, max(et_values) + 0.8))
    ax_et.grid(axis="x", linestyle="--", alpha=0.35)
    ax_et.legend(loc="upper right", frameon=False)
    ax_et.spines["top"].set_visible(False)
    ax_et.spines["right"].set_visible(False)

    fig.tight_layout()
    fig.savefig(output, dpi=160)
    plt.close(fig)

    return output


def generate_timing_diagram(
    example: Dict[str, Any],
    results: List[ScanCycleResult],
    output_path: str,
) -> Path:
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    if example["scenario_type"] == "ton_timer":
        return _generate_ton_timer_diagram(example, results, output)

    signal_names = _signal_names(example, results)
    cycles = [result.cycle_number for result in results]
    x_values = cycles + [cycles[-1] + 1]

    fig_height = max(3.5, len(signal_names) * 0.85)
    fig, ax = plt.subplots(figsize=(9, fig_height))

    colors = plt.get_cmap("tab10")
    row_gap = 1.6
    high_level = 0.8

    for index, signal_name in enumerate(signal_names):
        offset = index * row_gap
        values = [
            offset + (high_level if _signal_value(result, signal_name) else 0)
            for result in results
        ]
        values.append(values[-1])

        ax.step(
            x_values,
            values,
            where="post",
            linewidth=2.2,
            color=colors(index % 10),
        )
        ax.hlines(offset, x_values[0], x_values[-1], color="#d8dee9", linewidth=0.8)
        ax.hlines(offset + high_level, x_values[0], x_values[-1], color="#edf2f7", linewidth=0.8)

    ax.set_title(_diagram_title(example), fontsize=14, pad=14)
    ax.set_xlabel("Cycle")
    ax.set_xticks(cycles)
    ax.set_xlim(cycles[0], cycles[-1] + 1)
    ax.set_yticks([index * row_gap + high_level / 2 for index in range(len(signal_names))])
    ax.set_yticklabels(signal_names)
    ax.set_ylim(-0.4, (len(signal_names) - 1) * row_gap + high_level + 0.4)
    ax.grid(axis="x", linestyle="--", alpha=0.35)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    fig.tight_layout()
    fig.savefig(output, dpi=160)
    plt.close(fig)

    return output

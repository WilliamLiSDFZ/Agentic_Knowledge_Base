"""One set of solution-diversity figures, with tasks and experimental batches explicit."""

from collections import defaultdict
import math
import textwrap


def plotting_rows(scores, comparisons):
    """Return exact data for run curves, within-batch effects, and paired endpoints."""
    pairs = [row for row in comparisons if row["kind"] == "pair" and row.get("delta") is not None]
    paired_groups = {(row["task"], row["batch"], row["arm"], row["baseline"]) for row in pairs}
    effects = pairs + [row for row in comparisons
                      if row["kind"] == "unpaired_mean" and row.get("delta") is not None
                      and (row["task"], row["batch"], row["arm"], row["baseline"]) not in paired_groups]
    endpoints = [row for row in pairs if row["m"] == row["task_common_m"]]
    return list(scores), effects, endpoints


def write_plot_data(out, scores, comparisons):
    """Export plotting data even when figure rendering is disabled."""
    from .runtime import write_csv

    out.mkdir(parents=True, exist_ok=True)
    data = dict(zip(("vendi", "effect", "paired"), plotting_rows(scores, comparisons)))
    for name, rows in data.items():
        write_csv(out / f"{name}.csv", rows, ["task", "batch", "run_id", "arm", "m", "vendi"]
                  if name == "vendi" else ["task", "batch", "pair_id", "baseline", "arm", "m", "delta"])
    return data


def plot_results(out, scores, comparisons):
    """Write three PNG/PDF figures and their exact CSV data, including empty views."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.ticker import MaxNLocator
    data = write_plot_data(out, scores, comparisons)
    curves, effects, endpoints = (data[name] for name in ("vendi", "effect", "paired"))
    artifacts = [f"{name}.csv" for name in data]

    facets = sorted({(row["task"], row["batch"]) for row in scores + comparisons})
    tasks = sorted({task for task, _ in facets})
    arms = sorted({row["arm"] for row in scores})
    batches = sorted({batch for _, batch in facets})
    batch_colors = {batch: plt.get_cmap("tab10")(i % 10) for i, batch in enumerate(batches)}
    markers = ("o", "s", "^", "D", "v", "P", "X", "<", ">")
    styles = ("-", "--", "-.", ":")
    arm_styles = {arm: styles[i % len(styles)] for i, arm in enumerate(arms)}
    batch_markers = {batch: markers[i % len(markers)] for i, batch in enumerate(batches)}

    def identity(row):
        return row["task"], row["batch"], row.get("pair_id") or row.get("run_id", "")

    identities = sorted({identity(row) for row in curves + effects})
    curve_colors = {key: plt.get_cmap("tab10")(i % 10) for i, key in enumerate(identities)}

    def figure(keys, title, empty_message="No comparable candidates", panel_size=(9, 4.8)):
        columns = min(2, max(1, len(keys)))
        rows = math.ceil(max(1, len(keys)) / columns)
        fig, axes = plt.subplots(rows, columns, figsize=(panel_size[0] * columns, panel_size[1] * rows), squeeze=False)
        flat = list(axes.flat)
        for ax in flat[len(keys):]:
            ax.set_visible(False)
        if not keys:
            flat[0].set_visible(True)
            flat[0].text(.5, .5, empty_message, transform=flat[0].transAxes, ha="center")
            flat[0].set_axis_off()
        fig.suptitle(title)
        return fig, flat

    def save(fig, name, note):
        fig.text(.02, .015, note, fontsize=9)
        fig.tight_layout(rect=(0, .055, 1, .95))
        for extension in ("png", "pdf"):
            filename = f"{name}.{extension}"
            fig.savefig(out / filename, bbox_inches="tight", dpi=160)
            artifacts.append(filename)
        plt.close(fig)

    fig, axes = figure(tasks, "Complete solution Vendi", panel_size=(16, 8))
    for ax, task in zip(axes, tasks):
        grouped = defaultdict(list)
        for row in curves:
            if row["task"] == task:
                grouped[(row["batch"], row.get("pair_id", ""), row["arm"], row["run_id"])].append(row)
        for (batch, pair_id, arm, run_id), rows in sorted(grouped.items()):
            rows.sort(key=lambda row: row["m"])
            name = pair_id or run_id.rsplit("_", 1)[-1]
            label = f"{batch} | {name} | {arm} (n={rows[0]['n_total']})"
            ax.plot([row["m"] for row in rows], [row["vendi"] for row in rows],
                    color=curve_colors[identity(rows[0])], marker=batch_markers[batch],
                    linestyle=arm_styles[arm], label=label, alpha=.85)
        ax.set(title=textwrap.fill(task, 85), xlabel="Candidates per run (matched m)",
               ylabel="Vendi score (q=1)")
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        ax.grid(alpha=.2)
        if grouped:
            ax.legend(fontsize=9, loc="upper left", bbox_to_anchor=(1.02, 1),
                      title="Batch | Pair / run | Arm (candidates)")
        else:
            ax.text(.5, .5, "No runs with at least two available candidates", transform=ax.transAxes, ha="center")
    save(fig, "vendi", "Color identifies the experiment pair; line style identifies the arm. Each line is one run, with matched candidate counts across batches.")

    fig, axes = figure(tasks, "Vendi differences vs baseline", panel_size=(16, 7))
    for ax, task in zip(axes, tasks):
        grouped = defaultdict(list)
        for row in effects:
            if row["task"] == task:
                grouped[(row["batch"], row["arm"], row["baseline"], row["kind"], row.get("pair_id", ""))].append(row)
        for (batch, arm, baseline, kind, pair_id), rows in sorted(grouped.items()):
            rows.sort(key=lambda row: row["m"])
            name = pair_id if kind == "pair" else "batch mean (unpaired)"
            label = f"{batch} | {name} | {arm} − {baseline}"
            ax.plot([row["m"] for row in rows], [row["delta"] for row in rows], label=label,
                    color=curve_colors[identity(rows[0])], marker=batch_markers[batch])
        ax.axhline(0, color="black", linewidth=.8)
        ax.set(title=textwrap.fill(task, 85), xlabel="Candidates per run (matched m)",
               ylabel="Vendi difference vs baseline")
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        ax.grid(alpha=.2)
        if grouped:
            ax.legend(fontsize=9, loc="upper left", bbox_to_anchor=(1.02, 1),
                      title="Batch | Pair | Difference")
        else:
            ax.text(.5, .5, "No within-batch comparison available", transform=ax.transAxes, ha="center")
    save(fig, "effect", "Explicit-pair differences where available; otherwise descriptive batch means. No cross-batch mean or effect confidence intervals.")

    fig, axes = figure(tasks, "Explicit paired runs at the common candidate count", "No complete explicit pairs")
    for ax, task in zip(axes, tasks):
        selected = [row for row in endpoints if row["task"] == task]
        baselines = sorted({row["baseline"] for row in selected})
        labels = baselines + sorted({row["arm"] for row in selected} - set(baselines))
        for index, row in enumerate(selected):
            x = [labels.index(row["baseline"]), labels.index(row["arm"])]
            ax.plot(x, [row["baseline_vendi"], row["arm_vendi"]],
                    color=batch_colors[row["batch"]], marker=markers[index % len(markers)],
                    alpha=.85, label=f"{row['batch']} | {row['pair_id']}")
        common = sorted({row["task_common_m"] for row in scores if row["task"] == task})
        title = task + (f" | m={common[0]}" if common else "")
        ax.set(title=textwrap.fill(title, 65), ylabel="Vendi score (q=1)", xlabel="Experiment arm")
        ax.grid(axis="y", alpha=.2)
        if selected:
            ax.set_xticks(range(len(labels)), labels)
            ax.set_xlim(-.2, len(labels) - .8)
            ax.legend(fontsize=7)
        else:
            ax.text(.5, .5, "No complete explicit pairs", transform=ax.transAxes, ha="center")
            ax.set_xticks([])
    save(fig, "paired", "Each line joins explicitly paired runs; colors identify batches. Unpaired runs are not connected or borrowed.")
    return artifacts

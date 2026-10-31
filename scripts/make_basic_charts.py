#!/usr/bin/env python3
"""CSV → 论文风格柱状/折线/饼图。CSV需含表头；不发明数据。"""
from __future__ import annotations

import argparse
import csv
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib import font_manager


def setup_font():
    for name in [
        "Noto Sans CJK SC",
        "Source Han Sans SC",
        "SimHei",
        "PingFang SC",
        "Arial Unicode MS",
    ]:
        if any(name in f.name for f in font_manager.fontManager.ttflist):
            plt.rcParams["font.family"] = name
            break
    plt.rcParams["axes.unicode_minus"] = False


def load(path: Path):
    with path.open(newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        raise SystemExit("empty csv")
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv")
    ap.add_argument("--type", choices=["bar", "line", "pie", "grouped_bar"], default="bar")
    ap.add_argument("--x", required=True, help="category column")
    ap.add_argument("--y", required=True, help="value column, or comma-separated for grouped_bar")
    ap.add_argument("-t", "--title", default="")
    ap.add_argument("-o", "--out", default="chart.png")
    ap.add_argument("--xlabel", default="")
    ap.add_argument("--ylabel", default="")
    args = ap.parse_args()

    setup_font()
    rows = load(Path(args.csv))
    xs = [r[args.x] for r in rows]
    fig, ax = plt.subplots(figsize=(7.2, 4.2), dpi=200)

    if args.type == "bar":
        ys = [float(r[args.y]) for r in rows]
        ax.bar(xs, ys, color="#4A4A4A", edgecolor="black", linewidth=0.4)
    elif args.type == "line":
        ys = [float(r[args.y]) for r in rows]
        ax.plot(xs, ys, color="#222222", marker="o", linewidth=1.5)
    elif args.type == "pie":
        ys = [float(r[args.y]) for r in rows]
        ax.pie(ys, labels=xs, autopct="%1.1f%%", startangle=90, textprops={"fontsize": 9})
        ax.axis("equal")
    else:
        series = [s.strip() for s in args.y.split(",")]
        import numpy as np
        n, m = len(xs), len(series)
        w = 0.8 / m
        idx = np.arange(n)
        for i, s in enumerate(series):
            ys = [float(r[s]) for r in rows]
            ax.bar(idx + i * w, ys, width=w, label=s, edgecolor="black", linewidth=0.3)
        ax.set_xticks(idx + w * (m - 1) / 2)
        ax.set_xticklabels(xs)
        ax.legend(frameon=False, fontsize=8)

    if args.type != "pie":
        ax.set_xlabel(args.xlabel or args.x)
        ax.set_ylabel(args.ylabel or args.y)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.tick_params(labelsize=9)
        plt.xticks(rotation=20, ha="right")

    if args.title:
        ax.set_title(args.title, fontsize=12, pad=10)
    fig.tight_layout()
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", out)


if __name__ == "__main__":
    main()

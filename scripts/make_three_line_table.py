#!/usr/bin/env python3
"""CSV → 论文三线表 docx + 预览 png。不发明数据。"""
from __future__ import annotations

import argparse
import csv
from pathlib import Path


def read_csv(path: Path):
    with path.open(newline="", encoding="utf-8-sig") as f:
        rows = list(csv.reader(f))
    if not rows:
        raise SystemExit("empty csv")
    return rows[0], rows[1:]


def write_docx(header, body, out: Path, title: str | None):
    from docx import Document
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Pt
    from docx.enum.text import WD_ALIGN_PARAGRAPH

    def set_run_font(run, size=10.5, bold=False):
        run.font.size = Pt(size)
        run.font.bold = bold
        run.font.name = "Times New Roman"
        rPr = run._element.get_or_add_rPr()
        ea = OxmlElement("w:eastAsia")
        ea.set(qn("w:val"), "宋体")
        rPr.append(ea)

    def set_cell_border(cell, **edges):
        tc = cell._tc
        tcPr = tc.get_or_add_tcPr()
        # remove existing borders
        for child in list(tcPr):
            if child.tag == qn("w:tcBorders"):
                tcPr.remove(child)
        tcBorders = OxmlElement("w:tcBorders")
        for edge, val in edges.items():
            el = OxmlElement(f"w:{edge}")
            el.set(qn("w:val"), val.get("val", "single"))
            el.set(qn("w:sz"), str(val.get("sz", 8)))
            el.set(qn("w:space"), "0")
            el.set(qn("w:color"), val.get("color", "000000"))
            tcBorders.append(el)
        tcPr.append(tcBorders)

    doc = Document()
    if title:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(title)
        set_run_font(r, 10.5, True)

    cols = len(header)
    table = doc.add_table(rows=1 + len(body), cols=cols)

    thick = {"val": "single", "sz": 12, "color": "000000"}
    thin = {"val": "single", "sz": 8, "color": "000000"}
    none = {"val": "nil", "sz": 0, "color": "000000"}

    for j, h in enumerate(header):
        cell = table.rows[0].cells[j]
        cell.text = ""
        r = cell.paragraphs[0].add_run(str(h))
        set_run_font(r, 10.5, True)
        cell.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        set_cell_border(cell, top=thick, bottom=thin, left=none, right=none)

    for i, row in enumerate(body):
        is_last = i == len(body) - 1
        for j in range(cols):
            val = row[j] if j < len(row) else ""
            cell = table.rows[i + 1].cells[j]
            cell.text = ""
            r = cell.paragraphs[0].add_run(str(val))
            set_run_font(r, 10.5, False)
            set_cell_border(
                cell,
                top=none,
                bottom=thick if is_last else none,
                left=none,
                right=none,
            )

    doc.save(out)


def write_png(header, body, out: Path, title: str | None):
    import matplotlib.pyplot as plt
    from matplotlib import font_manager

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

    nrows, ncols = len(body) + 1, len(header)
    fig_h = max(1.2, 0.45 * nrows + (0.55 if title else 0.25))
    fig_w = max(6, 1.3 * ncols)
    fig, ax = plt.subplots(figsize=(fig_w, fig_h), dpi=200)
    ax.axis("off")
    if title:
        ax.set_title(title, fontsize=12, pad=14)

    data = [header] + body
    table = ax.table(cellText=data, loc="center", cellLoc="center")
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1, 1.45)

    for (r, c), cell in table.get_celld().items():
        cell.set_edgecolor("black")
        cell.set_linewidth(1.0)
        if r == 0:
            cell.visible_edges = "TB"
            cell.get_text().set_fontweight("bold")
        elif r == nrows - 1:
            cell.visible_edges = "B"
        else:
            cell.visible_edges = ""

    fig.tight_layout()
    fig.savefig(out, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def main():
    ap = argparse.ArgumentParser(description="CSV to three-line table")
    ap.add_argument("csv")
    ap.add_argument("-o", "--outdir", default=".")
    ap.add_argument("-t", "--title", default="")
    ap.add_argument("--prefix", default="table")
    args = ap.parse_args()
    header, body = read_csv(Path(args.csv))
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    title = args.title or None
    docx_path = outdir / f"{args.prefix}.docx"
    png_path = outdir / f"{args.prefix}.png"
    try:
        write_docx(header, body, docx_path, title)
        print("wrote", docx_path)
    except Exception as e:
        print("docx skipped:", e)
    write_png(header, body, png_path, title)
    print("wrote", png_path)


if __name__ == "__main__":
    main()

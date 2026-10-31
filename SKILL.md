---
name: mem-thesis-rearch
description: 专硕/MEM一体包（徐迪）：选题→素材关卡→分章写作→文献检索催上传→论文图与三线表→初稿后自动导师审查并改出完整粗稿。禁止编造企业数据与文献。选题、写论文、做图表、要粗稿时使用。
---

# mem-thesis-rearch（写作 + 图表 + 导师审查一体）

You help the user **research, write, illustrate, and advisor-review** a Chinese **专业硕士学位论文** (MEM etc.) with 徐迪 methodology. One skill covers the full path to a **完整粗稿**.

## Non-negotiables

1. **Never invent** enterprise facts, metrics, interview quotes, implementation logs, effect numbers, or citation metadata.
2. At each material gate, **stop and ask**; until then only outlines / `【待用户补充：…】`.
3. Path: practice problem → causes → management topic → solution → effect.
4. Professional master's: practice significance enough; do not force theoretical innovation.
5. School formatting wins on layout/citation; Xu Di wins on problem logic.
6. After any substantial draft, **run the advisor-review loop** (`references/advisor-review-loop.md`) before ending — user should receive a reviewed 粗稿, not a raw dump.
7. Simplified Chinese unless asked otherwise.

## Read first (this folder)

- `references/topic-workshop.md`
- `references/material-gates.md`
- `references/chapter-outline.md`（默认第2章独立文献综述）
- `references/literature-assist.md`（自动检索 + 催上传）
- `references/three-line-table.md` / `figure-types.md` / `caption-style.md`
- `references/review-checklist.md` / `rubric-notes.md`
- `references/advisor-review-loop.md`（初稿后自动审查+修订+交付）
- `scripts/make_three_line_table.py` / `make_basic_charts.py`
- Optional: `articles/`

## Phase 0 — State

A 未定题 → Phase 1；B 缺结构 → Phase 2；C 已有稿要改 → Phase 4–6；D 只写一章 → 该章关卡后写，章末仍跑审查；E 只要图表 → Phase 5（G6）。

## Phase 1 — 选题工坊

Use `topic-workshop.md`. Separate problem / causes / topic. Propose 2–3 titles (`Z公司T管理改进研究`). Record title, org, problems, evidence, methods. Then continue.

## Phase 2 — 大纲

Map `chapter-outline.md`. **Default independent Chapter 2 = 文献综述/研究现状** (not 理论基础). Mark gates G1–G6. School five-chapter: state mapping on line 1. OK before long draft.

## Phase 3 — 分章写作（gated）

1. Check `material-gates.md`; missing → list uploads; wait.
2. **Before Ch.2:** run `literature-assist.md` (candidate table + ask upload PDFs/RIS); no upload → no fake review prose.
3. Draft thesis voice; specific methods only (ban 文献研究法/案例研究法/定性定量相结合).
4. After each chapter: 已用素材 / 仍缺 / 下一关卡；then **mini advisor pass** on that chapter (R1; auto-fix safe items).

## Phase 4 — 连贯修订

Unify terms; Ch.1 problems match later chapters; solutions 1:1; effects close loop. Unverified numbers → `【待用户补充】`.

## Phase 5 — 图与三线表（原独立 figtable，现内置）

When G6 triggers or user asks for figures/tables:

1. Collect user data/sketches only; confirm fields/nodes.
2. **Tables:** three-line only (`three-line-table.md`); prefer `scripts/make_three_line_table.py` → docx + png preview.
3. **Figures:** `figure-types.md` + `make_basic_charts.py` or careful redraw; caption below; ≥200dpi PNG.
4. Deliver file + 题注 + 正文引用句 + 数据来源文件名.

## Phase 6 — 导师评价闭环 → 完整粗稿（必做）

When a chapter set or full draft exists, **must** run `advisor-review-loop.md`:

1. R1 自动审查（致命 / 应改 / 通过）  
2. R2 能改的自动改；缺料的汇总，不编造  
3. R3 一次交付：**粗稿正文 + 导师评价 + 图表清单 + 待补料/下一步**

Do not end on “初稿已生成，请自行审阅” alone.

## Defense PPT (optional)

四块：问题与意义 → 研究现状 → 内容方法过程 → 结论与展望.

## Install

Folder/`name:` = `mem-thesis-rearch`.

- **Codex / Agents:** `~/.agents/skills/mem-thesis-rearch/` or repo `.agents/skills/mem-thesis-rearch/`；调用 `$mem-thesis-rearch`。
- **WorkBuddy:** 上传同一内容的 WorkBuddy ZIP；调用 `/mem-thesis-rearch`。

Charts need `pip install python-docx matplotlib numpy` when running scripts.

## Attribution

徐迪「管理学学位论文写作」系列与《管理学学位论文写作》(清华大学出版社, 2023). User owns facts and integrity.

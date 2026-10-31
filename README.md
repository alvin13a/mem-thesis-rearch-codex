# mem-thesis-rearch

面向 **Codex / Cursor Agents** 的中国**专业硕士学位论文（MEM 等）**一体 Skill：选题工坊 → 素材关卡写作 → 文献检索与催上传 → 论文图与**三线表** → 初稿后**自动导师审查**并交付完整粗稿。

> **重要说明：**本 Skill 的写作标准、问题导向逻辑、章节与自检要点，系根据**徐迪老师微信公众号「管理学学位论文写作」系列文章**整理、归纳而成（并可对照其著作《管理学学位论文写作》，清华大学出版社，2023）。Skill 是写作与审查助手，**不代替**学校格式规定，也**不构成**徐迪老师或任何机构的官方授权课程；事实与学术诚信由使用者本人负责。

## 功能概览

| 模块 | 做什么 |
|------|--------|
| 选题工坊 | 拆清 problem / causes / topic，给出题目候选 |
| 素材关卡 G0–G6 | 缺真实企业材料就停，禁止编造数据 |
| 默认大纲 | **第2章独立文献综述/研究现状**（勿「理论基础」灌水） |
| 文献协助 | 自动检索候选文献表 + 明确提示用户上传 PDF/题录 |
| 图表 | 用户数据 → 论文图 + 标准三线表（`scripts/`） |
| 导师审查闭环 | 初稿后对照徐迪式清单自动审查，能改的改，缺料单列，交付完整粗稿 |

## 安装（Codex / Agents）

解压本仓库（或 clone 后）到：

```text
~/.agents/skills/mem-thesis-rearch/
```

或项目内：

```text
.agents/skills/mem-thesis-rearch/
```

`SKILL.md` 的 `name:` 须为 `mem-thesis-rearch`。调用：`$mem-thesis-rearch`。

### 图表脚本依赖

```bash
pip install python-docx matplotlib numpy
```

## 目录

```text
mem-thesis-rearch/
├── SKILL.md                 # 主流程
├── INSTALL.md
├── README.md                # 本文件
├── references/              # 细则与徐迪标准提炼
│   ├── topic-workshop.md
│   ├── material-gates.md
│   ├── chapter-outline.md
│   ├── literature-assist.md
│   ├── advisor-review-loop.md
│   ├── review-checklist.md
│   ├── rubric-notes.md
│   ├── three-line-table.md
│   ├── figure-types.md
│   ├── caption-style.md
│   └── sources.md           # 公众号原文链接索引
├── scripts/
│   ├── make_three_line_table.py
│   └── make_basic_charts.py
└── articles/                # 可选：公众号导出正文（公开仓库可不收录）
```

公开 GitHub 默认可不包含 `articles/`（版权与篇幅考虑）；保留 `references/sources.md` 中的原文链接即可追溯。本仓库若含 `articles/`，仅作个人学习备份用途。

## 方法来源与致谢

- **主要整理依据：**徐迪微信公众号「管理学学位论文写作」系列（问题导向、专硕与学硕差异、导论与文献综述、研究方法表述、本论结构、结论与答辩、专业学位论文自检表等）。具体篇目见 [`references/sources.md`](references/sources.md)。
- **延伸对照：**徐迪《管理学学位论文写作》，清华大学出版社，2023。
- 本仓库为社区/个人整理的 **Agent Skill 封装**，便于在 Codex 等工具中按同一套标准写作与自检；**非**徐迪老师官方发布。

## 使用注意

1. **禁止编造**企业数据、效果数字、文献条目。  
2. 学校学位论文格式手册优先于本 Skill 的排版建议。  
3. 初稿生成后 Skill 应自动进入「导师审查」再交付粗稿，而不是把审稿完全甩给用户。

## License

整理文档与脚本：可按仓库 LICENSE 使用（若未附 LICENSE，默认仅供学习交流）。徐迪公众号原文与图书版权归原作者及出版社所有；请通过正式渠道阅读原文，勿将 `articles/` 用于商业传播。

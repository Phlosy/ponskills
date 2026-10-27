# Visual Hierarchy, Typography & Template Contract (`视觉层级、80/20 色彩重心、去框套框与母版契约`)

## 1. `⛔ BLOCKING GATE 1`: Pure Background Master Template First & Official Logo Cutout Rule (`纯母版先行审阅与官方 Logo 透明抠图铁律`)

1. **Creating a New PPT Style from Scratch (`新建 PPT 必须“纯母版先行审阅” — ⛔ BLOCKING GATE 1`)**:
   - **STRICT BLOCKING RULE**: After the user approves the Gate 0 outline, **never jump straight into generating body slides**. You must first generate a **Pure Background Master Template PPT (`<机构/用途>_纯母版模板_供审阅.pptx`)** and 16:9 PNG previews containing **only** the master background plates (Cover background, Content slide header/footer bar, decorative accent lines, and transparent-cutout Official Logo—with **zero body content**; optionally providing candidate schemes `方案 A / B / C`).
   - **HARD STOP**: Present the pure master template `.pptx` and preview images to the user and **wait for explicit confirmation** (e.g., `"确认"`, `"可以用方案A"`) before authoring any body slides.
2. **Domain-Agnostic Official Logo Transparent Cutout Rule (`官方 Logo 必须原图透明抠图嵌入，严禁系统字体手打或手绘简图`)**:
   - Whenever an institution, university, research institute, enterprise, or laboratory has an official Logo (emblem + official custom/calligraphic logotype), **strictly forbid typing the organization name with standard system fonts or drawing simplified vector approximations**.
   - Always obtain high-resolution official source images, extract a clean RGBA transparent background (`cutout`), and prepare surface-matched variants:
     - **Dark Master Cover**: High-contrast white logotype + official emblem.
     - **Light Content Slide Header**: Deep brand primary color logotype + official emblem.
3. **Iterating on an Existing Approved Version (`基于已锁定母版迭代，如 v5.0 → v6.0`)**:
   - **STRICT RULE**: When revising content, adjusting layouts, or updating figures on top of an approved deck version, **preserve 100% of the approved visual master template** (cover background, official logo placement, header/footer bar). Never replace the locked master theme during content revisions.

---

## 2. Cover Minimalism, Direct Entry & Zero Micro-Footnotes (`封面极简要素、按需直入正题与去左下角微缩附注`)

1. **Cover Three-Element Minimalism (`封面极简三要素`)**:
   - Keep covers clean and dignified with $\ge 65\%$ breathing room: **(1) Main Presentation Title**, **(2) Approved Master Background + Official Cutout Logo**, and **(3) Concise Bottom Metadata** (either a clean single line `汇报人 | 单位 | 时间` for public academic reports, or a `2×2` block `答辩人 / 指导老师 / 专业 / 汇报时间` for degree thesis defenses).
   - Never place technical architecture diagrams or cluttered spoilers on the cover slide.
2. **Direct Content Entry for Public Reports (`公开汇报按需省略目录页与章节过渡页`)**:
   - For concise public academic reports or executive briefings (e.g., 10–15 slides), omit redundant TOC and Section Divider slides when direct entry from the Cover (Slide 1) into Content P1 (Slide 2) is preferred.
3. **Zero Illegible Bottom-Left Micro-Footnotes (`全局去除左下角微缩附注`)**:
   - Strictly omit small source/supplementary footnotes in the bottom-left corner of content slides (`左下角看不清的补充小字一律取消`). Put detailed data citations in the standalone `<题目>_权威数据来源与测算依据.md` file instead.

---

## 3. Logic-Driven Adaptive Top/Bottom Anchor Bars (`打破“每页必有上下双框”机械教条，改为按逻辑按需配置`)

1. **Adaptive Single vs. Dual Anchor Configuration (`按逻辑决定单框或双框，绝不上下重复`)**:
   - **Core Principle**: Every content slide must retain **at least one** summary anchor bar (either Top or Bottom) to distill the core takeaway of the slide, but **never force both Top and Bottom bars when they repeat the same point**.
   - **When to use a Single Anchor Bar (`仅顶部框` or `仅底部框`)**:
     - When the slide presents a single-layer status quo, exponential trend, scale calculation, or direct structural comparison (e.g., constellation growth trend, network vs. city throughput benchmark, geometric cone inversion).
   - **When to use Dual Anchor Bars (`顶部框 + 底部框`)**:
     - Only when the slide embodies a genuine **two-level progressive or pivot relationship (`上表征/正面工程目标 → 下底层规律/思维转折`)** (e.g., Top states how Pbps data volume sets three communication engineering design boundaries, while Bottom executes a conceptual pivot asking whether it can reshape the satellite service paradigm).
2. **Adaptive Sizing & Multi-Line Support (`顶/底框高度与字号按实际内容弹性适配，支持多行核心拆解`)**:
   - Size bar height and font size adaptively according to actual content density so the takeaway is immediately legible from a distance (significantly larger than body text, e.g., `56–58px` height with `17.5–18pt` bold left badge and `19–19.5pt` bold summary text for single-line bars).
   - When the top bar needs to convey a two-line structured definition (e.g., Line 1: `核心需求`, Line 2: `核心架构`), expand it cleanly into a full-width two-line container (`~72px` height) without squeezing extra side boxes next to it.
3. **Rigorous Academic Tag Naming (`标签用词严谨化：去感性夸张与去泛化“矛盾”`)**:
   - Avoid sensational or colloquial badge labels in formal academic venues (e.g., use `规模测算` instead of `量级震撼`).
   - Do not mechanically label every bottom conclusion as `本质矛盾` when the statement is an evolutionary conclusion or insight—use accurate labels (`核心结论` / `核心洞察` / `范式转变` / `思维转折`).

---

## 4. Strict Anti-Nested-Boxes & Visual-First Single-Line Captions (`严禁卡片内部“方框套方框”与“少字多图 + 图下单行精炼说明”`)

1. **Strictly Forbid Nested Sub-Boxes (`严禁卡片内部“方框套线框再套方框”`)**:
   - Inside a content card, **never nest multi-layered colored sub-boxes, pill boxes, or dual-grid mini-cards**.
   - For text-heavy or capability/metric cards (such as multi-domain simulation breakdowns or platform performance metrics), use a **single clean white card + sequence prefix markers (`●` or official emblem prefix) + hierarchical font sizes, bold keywords, and comfortable line spacing**, establishing visual order through typography and whitespace rather than nested boxes.
2. **Visual-First Middle Area & Single-Line Figure Captions (`中部少字多图，每图下方仅配单行精炼说明`)**:
   - Keep the middle canvas visual-first with minimal internal descriptive text so the speaker has room to elaborate orally.
   - Below each figure inside a card, separate with a thin horizontal divider line (`#E2E8F0`) and place **at most a single bold summary line (`~14.5pt`)**, replacing legacy two-box caption grids.

---

## 5. Abstracted "80% Restrained Base + 20% High-Contrast Visual Focal Point" Color Hierarchy (`“80% 克制底色 + 20% 鲜明视觉重心”色彩层级法则`)

Every slide must balance **overall visual elegance (no rainbow clutter)** with **an unmistakable visual center of gravity (no flat monotony)**:

1. **80% Restrained Base Palette (`80% 克制基础色，防凌乱与审美疲劳`)**:
   - Never use 5–6 bright saturated colors (red, orange, green, cyan, blue, purple) across a single slide.
   - Use **1 primary deep academic base color** (e.g., Deep Academic Navy `#1B365D`) paired with **1 muted secondary slate tone** (`#334155` / `#475569`) for ~80% of standard card headers, borders, and body text.
2. **20% Vibrant Visual Focal Point (`20% 鲜明视觉重心，“一页一视觉重心”，拒绝全浅或全深`)**:
   - Restraint must **never** result in a flat, lifeless slide where everything is equally light or equally dark.
   - **Every slide must have a single unmistakable Visual Focal Point (`视觉重心`)**, highlighted using a **vibrant focal accent color (e.g., Vibrant Red `#D9232E` / `#C81E2B` solid card header + `2px` focal border + bold red key phrases/metrics)** so the audience's eye locks onto the most important card/module of the slide within one second.
3. **Vivid Contrast in Comparative Sub-Figures (`对比型子图保留鲜明色彩反差`)**:
   - In comparative charts, bars, or mechanism diagrams contrasting legacy bottlenecks against proposed breakthroughs, render legacy/idle/wasted portions in muted cool gray (`#64748B` / `#CBD5E1`) and highlight the core breakthrough/value-add portions with **vivid contrast colors** (Vibrant Red `#D9232E`, Bright Blue `#2563EB`, Amber Gold `#D97706`).

---

## 6. Related Work Table & Paradigm Comparison Matrix Rules (`现状表格与流派对比表专项规范`)

When a full defense deck includes dedicated Related Work tables:
- **Five-Column Related Work Table**: Expand to full height (`y = 70..582`, `512px`) and use `13.5px–14px` font in analytical columns (`已解痛点与实现机理`、`既有前提与局限`、`适配瓶颈与切入`).
- **Paradigm Comparison Summary Table**: Keep as a clean standard table with 3-color semantic font colors (`✓` Emerald Green Bold `#15803D`, `△` Amber Yellow `#D97706`, `×` Light Gray `#94A3B8`) and no redundant mini-cards below the table.

---

## 7. Formal Document & Deliverable Naming Convention (`正式文档统一命名规范`)

1. **Topic-Specific Formal Deliverables**:
   - Format: **`<题目名>_<文档类型>_v<X.Y>.<后缀>`** (e.g., `AI赋能海量卫星数据价值挖掘与复用的考虑_公开学术报告_v6.0.pptx`).
   - Always preserve prior major versions (`v1.0` .. `v{N-1}.0`) non-destructively when exporting a new version.
2. **Pure Master Templates for Gate 1 Review**:
   - Format: **`<机构/用途>_纯母版模板_供审阅.pptx`**.

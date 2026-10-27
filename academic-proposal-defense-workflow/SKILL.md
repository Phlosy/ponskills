---
name: academic-proposal-defense-workflow
description: >-
  End-to-end standardized workflow and meta-orchestrator for authoring academic
  reports (PhD/Master thesis proposals, midterm reports, technical reports) and
  preparing defense, award, or public academic presentation PPTs. Enforces hard
  blocking user-confirmation gates (Gate 0: Core Claim & Outline Skeleton;
  Gate 1: Pure Background Master Template & Official Logo Cutout; Gate 2: Full
  Deck Visual/Collision/Multimedia QA), a domain-agnostic Nine-Ring Narrative
  Methodology, an 80/20 Restrained-Base + Vibrant-Focal-Accent visual hierarchy,
  anti-nested-box typography, purpose-driven figure modality selection, and
  multi-skill orchestration (EvoSkills, humanizer, docx-template-report,
  ppt-master). Activate whenever the user asks to write, restructure, or polish
  an academic proposal/report, design a defense/public report PPT outline, or
  generate/update a formal PPTX.
---

# Academic Proposal, Report & Presentation PPT Standardized Workflow (`academic-proposal-defense-workflow`)

This skill governs the end-to-end authoring of formal academic reports (`.docx` / LaTeX) and the preparation of defense, award, or public academic presentation decks (`.pptx`). It acts as a **domain-agnostic methodology and multi-skill orchestrator** so that every report and slide deck exhibits a rigorous, closed-loop narrative chain, an unmistakable per-slide visual focal point, and publication-grade clarity.

---

## 1. Companion Skills & Repository Registry (`协同自研技能与第三方依赖技能目录机制`)

This skill resides inside the self-developed **`ponskills`** repository (`git@github.com:Phlosy/ponskills.git`). It coordinates with one sibling self-developed skill in the same repository ([`../docx-template-report`](../docx-template-report/SKILL.md)) and three external third-party companion skills. Following the `ponskills` convention (similar to pulling third-party libraries into `third_party/` in software projects), external third-party skills are NOT bundled inside `ponskills`; instead, after cloning `ponskills`, they are pulled into a dedicated **`third_party_skills/`** directory in the workspace via [`scripts/ensure_dependent_skills.sh`](./scripts/ensure_dependent_skills.sh).

| Companion Skill | Ownership / Type | Canonical Git Repository URL | Default Path | Role in This Workflow |
| :--- | :--- | :--- | :--- | :--- |
| **`docx-template-report`** | **Self-Developed (`ponskills` In-Repo)** | `git@github.com:Phlosy/ponskills.git` (`docx-template-report/`) | `ponskills/docx-template-report` | Deterministic OOXML `.docx` report generation that strictly preserves template `styles.xml`, numbering, and layout contracts. |
| **`EvoSkills`** | **Third-Party (`third_party_skills/`)** | `https://github.com/EvoScientist/EvoSkills.git` | `third_party_skills/EvoSkills/skills/*` | Narrative planning (`paper-planning`), progressive literature chains (`research-survey`), mathematical rigor (`evomath-tao`), manuscript drafting (`paper-writing`), and slide structure (`academic-slides`). |
| **`humanizer`** | **Third-Party (`third_party_skills/`)** | `https://github.com/blader/humanizer.git` | `third_party_skills/humanizer` | Eliminating AI tells, mechanical literal translations, colloquialisms, and inflated filler while preserving recognized domain acronyms. |
| **`ppt-master`** | **Third-Party (`third_party_skills/`)** | `https://github.com/hugohe3/ppt-master.git` | `third_party_skills/ppt-master/skills/ppt-master` (or `../skills/ppt-master/skills/ppt-master`) | Compiling canonical 16:9 SVGs and speaker notes (`notes/total.md`) into native editable DrawingML `.pptx` decks with quality gates. |

Verify companion skill availability before execution:

```bash
bash ponskills/academic-proposal-defense-workflow/scripts/ensure_dependent_skills.sh --check
```

If any third-party companion skill is missing, run `bash ponskills/academic-proposal-defense-workflow/scripts/ensure_dependent_skills.sh --install` to create `third_party_skills/` in the workspace and clone it automatically.

---

## 2. Global Execution Discipline & Mandatory Blocking Gates (`全局串行执行纪律与强制人工确认门禁`)

Every workflow route MUST obey the following five global execution rules:

1. **Serial Execution (`严格串行推进`)** — Execute stages strictly in order. Never skip ahead.
2. **Blocking Means Hard Stop (`⛔ BLOCKING 门禁必须暂停等待用户确认`)** — At every stage marked **`⛔ BLOCKING GATE`**, you **MUST STOP IMMEDIATELY** after generating that stage's review artifact, present it clearly to the user, and **wait for explicit user confirmation** (e.g., `"确认"`, `"确认继续"`, `"可以用方案A"`, or specific revision instructions) before starting the next stage. Never decide on the user's behalf.
3. **No Cross-Gate Bundling (`严禁跨门禁打包抢跑`)** — Even if the user's initial prompt asks to "make a PPT from this document", do **NOT** bundle Outline + Template + Full Slide Generation in one turn. Close each `⛔ BLOCKING GATE` with the user one by one.
4. **Gate Before Entry (`前置条件核验`)** — Verify that the preceding gate's artifact has been explicitly approved by the user before entering any downstream stage.
5. **Act at the Owning Layer (`按归属层修复`)** — When user feedback modifies a specific layer (e.g., template background, a single figure's modality, or color hierarchy), repair at that owning layer while preserving locked upstream/sibling assets.

### Summary of Mandatory Blocking Gates

| Gate ID | Gate Name | Required Artifact(s) Delivered to User | Exit Condition (Hard Stop Until...) |
| :--- | :--- | :--- | :--- |
| **`⛔ BLOCKING GATE 0`** | **Core Claim Skeleton, Slide Outline & Data Basis Review**<br>*(核心论点骨架、逐页大纲概要与数据依据审阅门禁)* | 1. `核心论点与逐页大纲审阅单` (single core claim per slide, top/bottom anchor plan, figure modality plan)<br>2. `标准术语与页面标题对照表`<br>3. `<题目>_权威数据来源与测算依据.md` (when public data survey/calculation is involved) | User explicitly confirms the outline skeleton and data basis (e.g., `"确认"`, `"大纲没问题，继续"`). |
| **`⛔ BLOCKING GATE 1`** | **Pure Background Master Template & Official Logo Review**<br>*(纯背景母版方案与官方 Logo 抠图审阅门禁)* | 1. Pure Background Master Template PPTX (`<机构/用途>_纯母版模板_供审阅.pptx`, containing **only** Cover background, Content header/footer, decorative lines, and transparent-cutout Official Logo—**zero body content**; may offer candidate schemes `方案 A/B`)<br>2. 16:9 rendered preview images | User explicitly approves the template or selects a scheme (e.g., `"确认"`, `"可以用方案A"`). *(Skipped only when iterating on an already locked template version)* |
| **`⛔ BLOCKING GATE 2`** | **Full Deck Visual, Collision & Multimedia QA Review**<br>*(全量页面视觉重心、零重叠、16:9 渲染与多媒体质检门禁)* | 1. Native editable `<题目>_<文档类型>_v<X.Y>.pptx` (with embedded playable videos/media preserved if applicable)<br>2. 16:9 full-canvas single-slide PNGs & `preview_contact_sheet.png` rendered via Headless Chrome (`1280×720`) | User confirms final acceptance or provides iterative page-level refinement instructions. |

---

## 3. Mandatory Gate 0: Core Claim Skeleton & Outline Review (`⛔ BLOCKING GATE 0：先定核心论点与逐页大纲，用户确认后再进入下一阶段`)

> **CRITICAL RULE (`⛔ BLOCKING`)**: Never jump straight into writing full report chapters or generating PPT slides. Every chapter, section, narrative ring, or slide exists solely to serve **one core claim (`核心论点`)**.

Before creating any template or slides, you **MUST** first produce a concise **Core Claim & Slide-by-Slide Outline Review Sheet (`核心论点与逐页大纲审阅单`)** using [`templates/core_claim_skeleton_template.md`](./templates/core_claim_skeleton_template.md), initialize a **Controlled Terminology & Title Dictionary** using [`templates/controlled_glossary_and_titles_template.md`](./templates/controlled_glossary_and_titles_template.md), and (if public data research/calculation is requested) compile a standalone **Authoritative Data Sources & Calculation Basis Document (`<题目>_权威数据来源与测算依据.md`)**, then **STOP and wait for user approval**:

1. **Overarching Thesis (`全篇唯一总论点`)**: State the single core question that the entire report or presentation resolves.
2. **Node-by-Node Core Claims & Anchor Configuration (`逐节/逐页唯一核心论点与顶/底框配置计划`)**:
   - Do **not** expand detailed body text yet.
   - For each section or slide, specify its **single Core Claim**, whether it uses a **Top-only**, **Bottom-only**, or **Dual (Top + Bottom)** summary bar, its **single Visual Focal Point (`本页唯一视觉重心`)**, and its planned **Figure Modality** (real photo, pure geometric vector schematic, multi-element scene composite, or data chart).
   - If a slide or section tries to make two distinct claims, split it into two sequential nodes immediately.
3. **Explicit Inter-Claim Connectors (`相邻论点串联逻辑`)**:
   - Between every pair of adjacent claims, explicitly write **`[串联关系：为什么上一核心论点必然引出下一核心论点？]`**.
   - Insert dedicated **Bridge Nodes (`承上启下桥梁节/页`)** wherever a conceptual leap occurs.
4. **Horizontal Sub-Module Indispensability (`子内容必然拆解与缺一不可关系`)**:
   - Explicitly explain **why** the overarching problem decomposes into the proposed $K$ research contents and prove why removing any single one breaks the forward or feedback loop.
5. **Controlled Glossary & Three-Tier Slide Title Governance (`受控术语表与三元页面标题治理规范`)**:
   - Lock standard academic translations and anti-colloquialism replacements in a single source of truth.
   - Govern slide titles according to their **three distinct narrative roles**:
     - **Tier A — Background Argumentation & Problem-Inducing Slides (`前期背景铺垫与矛盾引出论述页`)**: Use **descriptive, trait-specific titles (`具象论述式`)** to preserve the evolutionary trajectory and failure context.
     - **Tier B — Core Technical Analysis, Multi-Dimensional Comparison & Structural Synthesis Slides (`核心内容分析比对、综述归纳与架构导引页`)**: Use **condensed, structured noun-phrase titles (`凝练结构式`, 8–16 chars)**.
     - **Tier C — Official Research Content Heading Slides (`研究内容核心展开页：冒号后 1:1 原版呈现`)**: For `研究内容一/二/三：...`, the text **after the colon (`：`) is the canonical name of the core research content / sub-content and MUST NEVER be omitted or abbreviated**—it must be presented **1:1 with the original Research Content headings**.

> **⛔ GATE 0 STOP**: Output the Gate 0 outline & data basis summary and ask the user to confirm before proceeding to Gate 1.

Read [references/00-core-claim-skeleton-gate.md](references/00-core-claim-skeleton-gate.md) and [references/06-controlled-glossary-and-title-stylebook.md](references/06-controlled-glossary-and-title-stylebook.md) for the complete Stage 0 and terminology/title protocols.

---

## 4. Universal Nine-Ring Narrative Methodology (`跨课题通用的九环行文逻辑`)

For full-length academic proposals, technical reports, and thesis defense decks, follow the **domain-agnostic Nine-Ring Closed-Loop Narrative Spine** (detailed in [references/01-universal-nine-ring-narrative.md](references/01-universal-nine-ring-narrative.md)). For focused public academic talks or executive technical reports, adapt the relevant subset of rings while maintaining strict causal connectors between adjacent slides:

| Ring | Universal Narrative Stage | Core Claim Pattern (Domain-Agnostic) |
| :---: | :--- | :--- |
| **Ring 1** | **Morphology Evolution & Structural Shift**<br>*(形态演进与同构/异构边界)* | Early/legacy architecture $A_0$ is structurally isomorphic to mature baseline systems $S_{\text{base}}$ (allowing direct migration of legacy workloads/protocols). Evolving to target architecture $A_{\text{new}}$ is superficially a form change, but **fundamentally an order-of-magnitude leap in topological complexity, dynamism, and interaction scale that transforms underlying operating logic**. |
| **Ring 2** | **Intrinsic System Nature vs. Concrete Scenario Demands**<br>*(内生系统状态本质与具体场景公认指标失配)* | Synthesize specific disturbances with the **scale-probability compounding law ($1-(1-p)^N \to 1$)** into one unified intrinsic system state (e.g., perpetual non-stationarity). Contrast this against **widely recognized concrete application scenario metrics** to expose the fundamental conflict. |
| **Ring 3** | **Tri-System Comparison & Multi-Layer Cascading Failure**<br>*(三态体系对比与既有方案多层连锁失灵)* | Compare **Baseline System vs. Transitional System (why current industry deployments still work) vs. Target System (why legacy schemes fail completely)**. Demonstrate how bottom-up physical constraints penetrate upward across layers. |
| **Ring 4** | **Paradigm Shift & Core Technical Problems**<br>*(范式转型与核心技术问题提炼)* | Show why traditional paradigms fail and why a **new service or closed-loop co-design paradigm** is required (Node A), then extract the **Core Technical Problems** blocking that paradigm (Node B). |
| **Ring 5** | **Problem Summary Bridge & Related Work Pairing**<br>*(承上启下问题汇总与国内外研究现状剖析)* | Summarize the Core Problems and map them 1-to-1 to existing research streams. Pair **`【已解痛点】`** with **`【未解局限】`**, concluding with a **3-color semantic font comparison table (`✓` Emerald Green `#15803D` / `△` Amber Yellow `#D97706` / `×` Light Gray `#94A3B8`)**. |
| **Ring 6** | **Single Core Question & 1-to-1 Aligned Objectives**<br>*(唯一核心问题与一一对应研究目标定位)* | Converge on one overarching Core Question and Research Objectives that map strictly 1-to-1 to the Core Problems. |
| **Ring 7** | **Necessary Decomposition & Indispensability Bridge**<br>*(核心问题的必然拆解与子内容“缺一不可”关系)* | Prove **why solving the overarching Core Question necessarily decomposes into the proposed Research Contents / System Modules**, and why every part is indispensable. |
| **Ring 8** | **Four-Layer Architecture Matrix & Embedded Innovations**<br>*(四层总体架构矩阵与内嵌式机理展开)* | Present a structured architecture matrix and embed key mechanisms/innovations naturally inside each module's discussion. |
| **Ring 9** | **1-to-1 Feasibility Verification, Platform Capabilities & Live Demo**<br>*(可行性验证、平台核心指标与实景演示)* | Verify feasibility and system capabilities with clear quantitative metrics and real prototype/simulation demonstrations (including native playable demo videos where available). |

---

## 5. End-to-End Execution Pipeline

### Branch A: Authoring or Revising Formal Academic Reports (`.docx` / LaTeX)
1. **Run `⛔ BLOCKING GATE 0`**: Produce the chapter/section Core Claim Skeleton and **STOP to obtain explicit user approval**.
2. **Structure & Literature Chain**: Read `EvoSkills/skills/paper-planning/SKILL.md` and `EvoSkills/skills/research-survey/SKILL.md` to build the 9-Ring outline and progressive literature table.
3. **Drafting & Mathematical Consistency**: Read `EvoSkills/skills/evomath-tao/SKILL.md` and `EvoSkills/skills/paper-writing/SKILL.md` to draft chapters with a unified global symbol table.
4. **Academic Language Polishing**: Read `skills/humanizer/SKILL.md` and apply the domain-balanced de-AI rules in [references/01-universal-nine-ring-narrative.md](references/01-universal-nine-ring-narrative.md).
5. **Deterministic Template Rendering**: If generating a `.docx` deliverable, follow `skills/docx-template-report/SKILL.md` (`inspect_docx.py` $\rightarrow$ `render_docx.py`), keeping `word-baselines/` read-only and naming deliverables `<题目名>_<文档类型>_v<X.Y>.docx`.

---

### Branch B: Preparing or Iterating Academic Defense & Public Report PPTs (`.pptx`)

#### Step 1 — Run `⛔ BLOCKING GATE 0` (Outline & Data Basis Gate)
- Read [references/02-ppt-decomposition-and-bridge-patterns.md](references/02-ppt-decomposition-and-bridge-patterns.md), generate the slide-by-slide Core Claim & Relational Outline (plus `<题目>_权威数据来源与测算依据.md` if public data research is involved), and **STOP to wait for explicit user approval**.

#### Step 2 — Run `⛔ BLOCKING GATE 1` (Pure Background Master Template & Official Logo Gate)
Read [references/03-visual-hierarchy-and-template-contract.md](references/03-visual-hierarchy-and-template-contract.md):
- **New presentation style from scratch**:
  1. **Pure Background Master Template First (`纯背景母版先行审阅`)**: Never populate body content before the master template is approved. First generate a pure background master template PPT (`<机构/用途>_纯母版模板_供审阅.pptx` and 16:9 PNG previews) containing **only** the Cover background, Content header/footer, decorative lines, and Official Logo (no body content; optionally provide candidate schemes `方案 A / B / C`).
  2. **Official Logo Transparent Cutout Rule (`官方 Logo 必须原图透明抠图嵌入 — 跨机构通用铁律`)**: Whenever the presentation features an official institutional/university/corporate/lab Logo (emblem + official custom/calligraphic standard logotype), **strictly forbid typing the organization name with standard system fonts or hand-drawing simplified vector approximations**. Always acquire high-resolution official source images, extract a clean RGBA transparent background, and adapt color variants to the surface (e.g., white logotype + emblem on dark covers; deep brand color + emblem on light content slide headers).
  3. **Cover Minimalism & Direct Entry (`封面极简三要素与按需直入正题`)**: Keep covers clean and minimal (Main Title, Master Background + Official Logo, and a concise presenter/affiliation/date metadata line or `2×2` block). For public academic talks or concise briefings, omit TOC and section divider pages when direct entry into Slide 1 of content is preferred. Globally omit illegible bottom-left micro-footnotes on content slides.
  4. **⛔ GATE 1 STOP**: Present the pure master template `.pptx` and preview images to the user and **STOP until the user confirms** before generating body slides.
- **Iterating on an already approved version (e.g., `v5.0` $\rightarrow$ `v6.0`)**:
  - **Strictly preserve 100% of the approved visual master template** (cover background, official logo placement, header/footer bar). Never swap out the locked master theme during content revisions.

#### Step 3 — Author Canonical SVGs, Visual Figures & Speaker Notes
Read [references/03-visual-hierarchy-and-template-contract.md](references/03-visual-hierarchy-and-template-contract.md) and [references/04-educational-visuals-and-gif-pipeline.md](references/04-educational-visuals-and-gif-pipeline.md), enforcing all five core visual and typographic rules below:

1. **Logic-Driven Adaptive Top/Bottom Anchor Bars (`打破“每页必有上下双框”机械教条，改为按逻辑按需配置`)**:
   - **Core Principle**: Every content slide must retain **at least one** summary bar (Top or Bottom) to distill the core message of the slide, but **never force both Top and Bottom bars if they repeat the same point**.
   - **When to use a Single Anchor Bar (Top-only or Bottom-only)**: When a slide presents a single-layer phenomenon, status quo, scale calculation, or direct structural comparison (where top and bottom would say the same thing), use only one bar.
   - **When to use Dual Anchor Bars (Both Top & Bottom)**: Use both bars **only** when the slide expresses a true two-level progression or conceptual pivot (`上表征/正面工程目标 → 下底层规律/思维转折`).
   - **Adaptive Dimensions, Multi-Line Support & Rigorous Tag Naming**:
     - Scale box height and font size adaptively according to actual content so the core statement stands out prominently above body text. When the top bar needs to present a two-line structured definition (e.g., Line 1: `核心需求`, Line 2: `核心架构`), expand it into a clean full-width two-line container without squeezing extra side boxes next to it.
     - Use rigorous academic tag labels: avoid sensational terms (`量级震撼` $\rightarrow$ `规模测算`), and never label non-contradictory conclusions as `本质矛盾` (use `核心结论` / `核心洞察` / `范式转变` / `思维转折`).

2. **Strict Anti-Nested-Boxes & Visual-First Single-Line Captions (`严禁卡片内部“方框套方框”与“少字多图 + 图下单行精炼说明”`)**:
   - **No Nested Sub-Boxes (`去框套框`)**: Inside a content card, strictly forbid nesting multi-layered colored sub-boxes, pill boxes, or dual-grid mini-cards.
   - **Clean Un-Nested Bulleted Lists for Text/Metric Cards**: For multi-item text or capability/metric cards, use a **single clean white card + sequence prefix markers (`●` or official emblem prefix) + hierarchical font sizes, bold keywords, and comfortable line spacing**, relying on typographic hierarchy and whitespace rather than nested borders.
   - **Visual-First Middle Area & Single-Line Captions**: Keep middle cards visual-first with minimal internal descriptive text so the presenter has room to elaborate orally. Below each figure inside a card, separate with a thin horizontal divider line and place **at most a single bold summary line**.

3. **"80% Restrained Base + 20% High-Contrast Visual Focal Point" Color Hierarchy (`“80% 克制底色 + 20% 鲜明视觉重心”色彩层级法则 — 跨主题通用`)**:
   - **80% Restrained Base Palette (`防凌乱与防审美疲劳`)**: Never use 5–6 bright saturated colors on a single slide. Use 1 primary deep academic base color (e.g., Deep Navy `#1B365D`) and 1 muted secondary neutral/slate tone (`#334155` / `#475569`) across ~80% of standard containers, borders, and body text.
   - **20% Vibrant Visual Focal Point (`“一页一视觉重心”，拒绝全浅或全深`)**: Restraint must never result in a flat, monotonous all-light or all-dark slide. **Every slide must establish a single unmistakable Visual Focal Point (`视觉重心`)**, highlighted with a **vibrant focal accent color (e.g., Vibrant Focal Red `#D9232E` / `#C81E2B` solid card header + bold focal-color key phrases/metrics)** so the audience's eye locks onto the slide's core takeaway at first glance.
   - **Vivid Contrast in Comparative Sub-Figures**: In charts or bars comparing legacy bottlenecks against proposed breakthroughs, render legacy/idle/wasted portions in muted cool gray and highlight the core breakthrough/value-add portions with vivid contrast colors (vibrant red, bright blue, amber gold).

4. **Purpose-Driven Figure Modality Selection & Quantitative Data Rigor (`配图形式“因表达目的制宜”与数据刻度/溯源铁律`)**:
   - **Match Visual Modality to Communicative Purpose**:
     - *Real-World Engineering Systems / Constellations / Hardware*: Use authentic high-resolution public photos/renderings cropped clean of watermarks or irrelevant English text overlays, rather than crude self-drawn cartoons.
     - *Pure Geometric / Topological Inversion Comparisons*: Use **symmetric, high-contrast pure geometric vector schematics** (e.g., upright cone vs. inverted cone) so structural/geometric contrasts are immediately obvious without perspective photo distortion.
     - *Multi-Element Operational Scenarios*: Use realistic multi-element composite scenes that strictly obey physical common sense (e.g., fixed ground base stations must stand on the ground, never float in the sky).
   - **Equidistant Axis Scales & Sourced Metrics vs. Qualitative Schematics**:
     - *Equidistant Time/Value Axes*: Chart axes must maintain strictly uniform intervals (e.g., 2-year steps `2018, 2020, ..., 2028E, 2030E`; never jump from 2-year steps to a 4-year step on uniform spacing).
     - *Sourced Numbers vs. Qualitative Bars*: Document all quantitative data sources and derivation formulas in a standalone `<题目>_权威数据来源与测算依据.md` file while keeping the slide canvas clean; for purely conceptual/qualitative comparison bars without hard empirical percentages, **hide unverified percentage numbers** and express the contrast through bar lengths and text labels.

5. **Native Playable Multimedia Embedding (`实景演示视频等多媒体无损原生内嵌`)**:
   - When a slide includes a live demo video (`.mp4`), strictly preserve its native aspect ratio in the layout and automatically inject the original video stream (`ppt/media/media*.mp4`), poster frame, and OOXML `<p:timing>` interactive click-to-play triggers into the compiled `.pptx`.

#### Step 4 — Run `⛔ BLOCKING GATE 2` (Automated Geometric + 16:9 Chrome Visual + Multimedia QA)
- Read [references/05-common-pitfalls-and-dual-qa-gate.md](references/05-common-pitfalls-and-dual-qa-gate.md) and [references/06-controlled-glossary-and-title-stylebook.md](references/06-controlled-glossary-and-title-stylebook.md).
- Run `check_terminology_and_titles.py`, `check_svg_collisions_and_bounds.py`, and `svg_quality_checker.py`.
- Compile native editable DrawingML `.pptx` via `total_md_split.py` and `svg_to_pptx.py --quick-generate --with-notes` (injecting native playable video streams where applicable), saving to `<题目名>_<文档类型>_v<X.Y>.pptx` while preserving all prior versions (`v1.0` .. `v{N-1}.0`).
- **16:9 Full-Canvas Headless Chrome Rendering Rule**: Render all single-slide PNGs and `preview_contact_sheet.png` using **Headless Chrome `--window-size=1280,720`** (strictly forbid macOS `qlmanage -t`, which crops 16:9 slides into 1:1 squares), inspect the rendered PNGs via `read_file`, and present the deliverables to the user at `⛔ BLOCKING GATE 2`.

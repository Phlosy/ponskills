# Historical Pitfalls Ledger & Triple QA Gate (`历史审阅避坑台账与三重质检门禁`)

This file records the **38 concrete issues** identified and corrected across formal academic defense and public report PPT iterations, along with the mandatory **Triple QA Gate (`⛔ BLOCKING GATE 2`)** that prevents any regression.

---

## 1. Complete 38-Item Pitfall & Correction Ledger (`历史审阅校正台账`)

| # | Category | Historical Defect | Mandatory Rule |
| :---: | :--- | :--- | :--- |
| **01** | Narrative | Jumping straight into technical details without macro context | Follow the **Universal Nine-Ring Narrative Spine** (`Ring 1` $\to$ `Ring 9`) or its causally connected subset. |
| **02** | Blocking Gates | Generating templates or full slides before aligning on the slide-by-slide outline, or generating body slides before the master template is approved | Enforce **`⛔ BLOCKING GATE 0` (Outline & Data Basis)** and **`⛔ BLOCKING GATE 1` (Pure Background Master Template)**. Hard-stop and wait for explicit user confirmation at every gate. |
| **03** | TOC & Entry | Using informal chapter titles in thesis defenses, or forcing unnecessary TOC/divider slides in concise public talks | In thesis defenses, title Slide 02 **`目 录`** with standard chapter titles; in concise public academic reports, omit TOC and section dividers to enter content directly on Slide 2. |
| **04** | Micro-Footnotes | Placing tiny source/time/meta footnotes (`"本页来源..."`,左下角微缩补充小字) at the bottom-left of slides | **100% prohibited**. Eliminate illegible bottom-left micro-footnotes globally; document sources in `<题目>_权威数据来源与测算依据.md`. |
| **05** | Cover Slide | Cluttering cover with diagrams or excessive metadata fields | Keep cover minimal with **only 3 core elements**: Main Title, Approved Master Background + Official Cutout Logo, and concise Presenter/Affiliation/Date metadata. |
| **06** | Official Logo | Typing institutional/university/corporate names with standard system fonts or drawing simplified vector logos | **100% prohibited**. Always extract a **clean transparent-background (`RGBA`) cutout from the official high-resolution Logo + custom logotype image** and adapt colors for dark covers vs. light headers. |
| **07** | Template Lock | Changing the overall slide visual style during a content revision (`v5` $\to$ `v6`) | **100% lock the approved master template style** when iterating on content. |
| **08** | Top/Bottom Bars | Mechanically forcing both Top and Bottom anchor bars on every single slide, causing top and bottom to repeat the same point | **Adaptive Top/Bottom Anchor Rule**: Keep **at least one** bar per slide, use **a single bar (Top or Bottom)** when expressing one layer of fact/trend/scale, and use **both bars only** when a genuine two-level progression/pivot (`上表征/工程目标 → 下底层规律/思维转折`) exists. |
| **09** | Bar Sizing & Split | Making top/bottom summary bars too narrow with small text, or squeezing side boxes next to a multi-line top bar | Size top/bottom bar height and font size prominently (`18–19.5pt` bold); when the top bar carries `核心需求` + `核心架构`, format as a clean **full-width 2-line container** without side boxes. |
| **10** | Tag Naming | Using sensational tags (`量级震撼`) or mislabeling non-contradictory insights as `本质矛盾` | Use rigorous academic tags (`规模测算`, `核心结论`, `核心洞察`, `范式转变`, `思维转折`). |
| **11** | Nested Boxes | Nesting boxes inside boxes (`方框套线框再套方框`: multi-colored sub-cards, pills, and dual caption boxes inside cards) | **Strictly forbid nested sub-boxes**. Use a single clean white card + sequence prefix markers (`●` or official emblem) + hierarchical font sizes and line spacing; use a single bold line below a thin divider for figure captions. |
| **12** | Color Clutter vs. Flatness | Either using 5–6 bright saturated colors per slide (visual chaos) or making the entire slide uniformly pale/dark (no focal point) | Enforce the **80/20 Color Hierarchy**: **80% Restrained Base** (Deep Navy `#1B365D` + Slate `#334155`) to prevent fatigue + **20% Vibrant Visual Focal Point** (`#D9232E` / `#C81E2B` red card header & bold red key text/metrics) so every slide has one unmistakable center of gravity (`一页一视觉重心`). |
| **13** | Comparative Contrast | Making comparative charts/bars monochrome so legacy waste and new breakthroughs look identical | In comparative sub-figures (e.g., resource utilization / value uplift bars), use muted cool gray for legacy idle/waste and **vivid contrast colors (Vibrant Red, Bright Blue, Amber Gold)** for the breakthrough portion. |
| **14** | Figure Modality | Drawing crude cartoons for real constellations, or using oblique photos where pure geometric symmetry (upright vs. inverted cone) is required | **Purpose-Driven Modality**: Use **real public photos** (cleaned of watermarks) for engineering entities, **symmetric pure geometric vector schematics** for geometric/topological inversions (`正锥形 vs. 倒锥形`), and **physically accurate realistic scene composites** (e.g., base stations on the ground, never in the sky) for operational scenarios. |
| **15** | Chart Axes & Unverified % | Jumping from 2-year axis steps to a 4-year step (`2024, 2026, 2030E`), or displaying unverified `%` numbers on qualitative comparison bars | Keep time/value axes **strictly equidistant** (e.g., `2018..2026, 2028E, 2030E`); document sourced numbers in `<题目>_权威数据来源与测算依据.md`, and **hide unverified `%` numbers** on qualitative conceptual comparison bars. |
| **16** | Video Preservation | Losing embedded `.mp4` videos or distorting video aspect ratio when regenerating PPTX from SVG | Lock native video aspect ratio in the slide layout and automatically re-inject `ppt/media/media*.mp4`, poster frame, and `<p:timing>` click-to-play triggers into the exported `.pptx`. |
| **17** | Preview Cropping | Using macOS `qlmanage -t` to render slide previews, which crops 16:9 slides into 1:1 squares | **Always render 16:9 (`1280×720`) PNG previews and contact sheets via Headless Chrome**. |
| **18** | Ring 1 Logic | Omitting why legacy bent-pipe satellite networks could reuse ground protocols | Explicitly note that **legacy bent-pipe networks are structurally isomorphic to ground networks**, whereas multi-shell heterogeneous networks push routing/queuing to space. |
| **19** | Ring 2 Consolidation | Splitting periodic switching and scale-failure probability ($1-(1-p)^N \to 1$) or omitting the latter | **Merge into one unified non-stationary essence**, explicitly including $1-(1-p)^N \to 1$. |
| **20** | Ring 2 Demands | Citing unimplemented 3GPP/ITU standard numbers that feel abstract | Replace with **concrete application scenarios and universally recognized metrics**. |
| **21** | Ring 2 Precision | Calling SLA failure `"✗ 现实失配"` when current bent-pipe Starlink works in reality | Use **`"✗ 异构失配"`** (`未来多壳层异构组网失配`). |
| **22** | Ring 3 Bridge | Failing to explain why current Starlink is usable while future multi-shell networks fail | Insert a **Tri-System Comparison Slide** (`Ground vs. Bent-Pipe vs. Multi-Shell Heterogeneous`). |
| **23** | Ring 3 Visuals | Explaining OSPF micro-loops and TCP collapse with dense text and static boxes | Use **educational dynamic GIFs / micro-architecture diagrams** + a cross-layer seesaw diagram. |
| **24** | Ring 3 GIF Pacing | Rendering protocol failure GIFs with too few frames (playing too fast to follow) | Render multi-phase protocol GIFs with **$\ge 48$ frames at `165ms` ($\approx 7.92\text{ s}$ cycle)** plus explicit top stage indicator tabs. |
| **25** | Ring 4 Density | Cramming "Paradigm Shift" and "Three Core Problems" onto one slide | **Split into two dedicated slides**. |
| **26** | Ring 5 Bridge | Entering Chapter 2 without summarizing Chapter 1's problems | Insert a concise **Problem $\to$ Required Capability $\to$ Survey Direction Roadmap Slide**. |
| **27** | Ring 5 Table Layout | Column 3 text bleeding into Column 4 | Widen Column 3 and verify $\ge 12\text{px}$ horizontal clearance before Column 4. |
| **28** | Ring 5 Phrasing | Phrasing "what prior work solved" as another vague problem statement | Explicitly pair **`【已解痛点】`** with **`【未解局限】`**. |
| **29** | Ring 5 Matrix | Using noisy colors for unachieved cells in the literature comparison matrix | Color cell font directly: **Emerald Green Bold (`#15803D`) for `✓`**, **Amber Yellow (`#D97706`) for `△`**, and **Light Gray (`#94A3B8`) for `×`**. |
| **30** | Ring 6 Objectives | Listing 1-2-3 execution steps or ungrounded project metrics in Research Objectives | State only **`【核心解决的问题】` + `【研究目标定位】` + `【对总核心问题的支撑产出】`**. |
| **31** | Ring 7 Bridge | Jumping from Objectives to Research Contents without explaining why they split into $K$ parts | Insert a **Necessary Decomposition & Indispensability Slide**. |
| **32** | Ring 8 Architecture | Putting "Key Scientific Questions & Innovations" on a separate standalone slide | Use a **4-Layer Matrix** and embed innovations inside each Research Content. |
| **33** | Ring 9 Feasibility | Listing disconnected pilot experiments without mapping to Research Contents | Prove feasibility **1-to-1 for each Research Content / Innovation** or present unified platform capabilities + live demo. |
| **34** | Title Governance | Using rhetorical questions (`为什么...？`) or inconsistent title lengths | Enforce **Three-Tier Slide Title Governance** (Tier A descriptive, Tier B condensed `8–16 chars`, Tier C 1:1 after colon). |
| **35** | Body Register (`humanizer`) | Using colloquial slang (`按下葫芦浮起瓢`, `乒乓打转`) or stiff literal translations | Run a full `humanizer` pass while retaining standard domain acronyms. |
| **36** | File Naming | Verbose or inconsistent file names (`..._版本A_终版.pptx`) | Strictly name deliverables **`<题目名>_<文档类型>_v<X.Y>.<后缀>`** and preserve prior versions. |
| **37** | Skill Portability | Referencing external skills without linking their repositories | Include a repository manifest and bootstrap script (`scripts/ensure_dependent_skills.sh`). |
| **38** | Speculative Bundling | Generating outline + template + full deck in one turn without waiting for user review | Treat **Gate 0** and **Gate 1** as hard `⛔ BLOCKING` stops—never advance without explicit user confirmation. |

---

## 2. Mandatory Gate 2: Triple Automated Geometric + 16:9 Visual + Multimedia QA Gate (`三重质检门禁`)

Before delivering any `.pptx` file at `⛔ BLOCKING GATE 2`, all three checks below must pass:

### Check 2A: Automated SVG Collision, Terminology & Quality Scanner
1. Run [`../scripts/check_svg_collisions_and_bounds.py`](../scripts/check_svg_collisions_and_bounds.py) on `svg_output/` to verify zero right-border overflow, zero column bleed, and zero unintended text/shape collisions.
2. Run `svg_quality_checker.py <project_dir> --quick-generate --canonical-authoring --stage final --json` before `total_md_split.py` and `svg_to_pptx.py`.

### Check 2B: Native Multimedia & Version Archiving Verification
- Verify that any embedded `.mp4` video on slides is packaged with its raw media stream (`ppt/media/media*.mp4`), poster image, and `<p:timing>` interactive playback node, and that previous `.pptx` versions (`v1.0` .. `v{N-1}.0`) remain intact.

### Check 2C: Headless Chrome 16:9 Full-Canvas Contact-Sheet Visual Inspection
- Render all slide PNGs at `1280×720` via **Headless Chrome** (never `qlmanage -t`) and assemble `preview_contact_sheet.png`.
- Visually inspect the rendered PNGs via `read_file` to verify:
  - 100% adherence to the locked Master Template and transparent-cutout Official Logo;
  - Unmistakable **80/20 Visual Focal Point (`一页一视觉重心`)** with vibrant focal red highlights and vivid comparison charts;
  - Clean un-nested card typography (`去框套框`) and equidistant chart axes;
  - Zero text, formula, or figure overlap.

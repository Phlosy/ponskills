# Controlled Terminology Glossary, Academic Phrasing & Three-Tier Slide Title Stylebook (`标准术语表、学术表述规范与三元页面标题字典`)

## 1. Why a Unified Glossary & Three-Tier Title Stylebook Is Mandatory

Across multi-round iterations of an academic proposal report and defense PPT, three recurring language and title problems arise if terminology and slide titles are not governed by a single source of truth:
1. **Colloquial / Slang Regression (`口语化与俗语回潮`)**: Conversational questions (`为什么...走不通？`, `为什么拆成这三块？`) or informal idioms (`按下葫芦浮起瓢`, `来回乒乓打转`, `瞬间塞爆`, `死胡同`) creep into slide headers, cards, or figure labels.
2. **Stiff Literal Translation & Ambiguous Terms (`生硬直译与概念歧义`)**: Mechanical translations (`守卫事件`, `横截性跃变`, `流生包`, `零假阳性`) or imprecise terms (`多域异构` instead of `多壳层异构组网`, `现实失配` instead of `异构失配`) confuse defense committee members.
3. **Failure to Distinguish Narrative Roles in Slide Titles (`未能按页面叙事职能区分标题形态`)**:
   - **Rule A — Background Argumentation & Problem-Inducing Slides (`前期背景论述与问题引出页` $\rightarrow$ 具象特质型标题)**: In the opening background section, slides that narrate morphological evolution, expose physical-vs-demand conflicts, explain cross-layer protocol failures, or induce a paradigm shift **must use descriptive, trait-specific titles** (`天基网络形态演进：从单星弯管透传到天地一体化多壳层异构组网`, `传统地面网络协议在多壳层异构网络中的跨层连锁失配`) so the evolutionary trajectory and failure context are vivid and complete.
   - **Rule B — Core Technical Analysis, Multi-Dimensional Comparison & Structural Synthesis Slides (`核心分析比对、研究现状、目标拆解与架构归纳页` $\rightarrow$ 凝练结构式标题)**: Once the presentation enters systematic analysis, multi-dimensional comparison, literature survey, target formulation, architectural decomposition, and feasibility evaluation, the titles **must shift to a condensed, structured noun-phrase pattern (`凝练结构式`, 8–16 chars)** (`三类网络体系特征对比`, `闭环逆向求解面临的核心问题`, `核心问题与国内外研究现状`, `国内外研究现状总结与对比`, `研究内容拆解逻辑与协同关系`, `总体研究架构与四层映射`).
   - **Rule C — Research Content Heading 1:1 Fidelity Law (`研究内容标题“冒号后 1:1 原版呈现”铁律`)**: For all Research Content slides (`研究内容一：...`, `研究内容二：...`, `研究内容三：...`), the text **after the colon (`：`) is the canonical name of the core research content / sub-content and MUST NEVER be omitted or abbreviated**—it must be presented **1:1 with the official Research Content headings in the proposal report**!

---

## 2. Table 1 — Controlled Technical Terminology (`专有名词与去生硬直译受控词表`)

| Forbidden / Stiff Literal / Obscure Term (`禁用/生硬直译/晦涩词`) | Mandatory Controlled Academic Term (`标准受控学术表述`) | Context & Rationale (`适用语境与规范说明`) |
| :--- | :--- | :--- |
| `守卫事件` / `Guard 事件` | **`状态转移触发条件`**（首次出现可括号注 `Guarded-EFSM`） | 避免直接生造“守卫事件”；明确其物理含义是协议定时器超时或队列越界等触发离散状态跳变的条件。 |
| `横截性条件` / `横截性跃变` (`Transversality`) | **`状态转移触发边界的清晰可分性`** / **`临界状态跳变`** | 避免纯微分几何黑话；直观表达状态轨迹穿过触发阈值面时不发生切向粘连、灵敏度导数可解析求解。 |
| `流生包` / `包归流` | **`流体排队模型与离散包级状态的双向转换`**（简写：**`流—包状态互转`**） | 消除口语化造词；明确是在宏观流体常微分方程（ODE）与微观逐包离散事件（DES）边界处做状态映射。 |
| `零假阳性` / `Zero False Positive` | **`确保所选配置实际达标`** / **`杜绝违约配置误入选`** | “假阳性”在网络配置求逆中易引发歧义；直接表述为“不把违约配置误判为达标配置”。 |
| `因果锥` (`Causal Cone`) | **`局部扰动传播域`** ($R_{\text{prop}}$) | 避免相对论物理借词造成理解隔阂；直接指明是链路切换或故障扰动在有限时间内波及的局部拓扑子图。 |
| `混杂自动机` / `混杂状态机` | **`耦合连续排队动态的扩展有限状态机`** (`Guarded-EFSM`) | 明确“离散控制状态转移 + 连续浅缓存排队微分方程”的灰盒耦合结构。 |
| `版本空间` / `观测等价类` | **`被动观测等效参数集`** | 直观说明当仅靠被动边缘观测时，多组内部参数可能产生相同外部轨迹，从而需要主动微突发探针消歧。 |
| `商空间划分` | **`机制与参数空间正交划分`** / **`三级改造代价分层建模`** | 避免纯抽象代数术语淹没工程含义。 |

---

## 3. Table 2 — Anti-Colloquialism, Disambiguation & Visual Semantic Rules (`去口语化、概念消歧与表格视觉规范表`)

| Colloquial / Ambiguous / Imprecise Expression (`禁用口语/俗语/歧义项`) | Mandatory Controlled Academic Expression (`标准受控学术规范`) | Why It Was Corrected (`修正原因与历史教训`) |
| :--- | :--- | :--- |
| `汇报提纲` | **`目 录`** | 答辩 PPT 第 02 页标准名称应为《目 录》，而非讨论稿式的“汇报提纲”。 |
| `为什么传统方案走不通？` / `为什么必然拆成这三块？` | **`传统地面网络协议在多壳层异构网络中的跨层连锁失配`** / **`研究内容拆解逻辑与协同关系`** | 页面顶部主标题与卡片标题严禁使用口语化设问句，统一使用陈述性学术名词短语。 |
| `按下葫芦浮起瓢` | **`单层参数调整的跨层制约`** / **`跨层孤立调参冲突`** | 消除俗语；精准表达路由层定时器与传输层缓存门限之间的跨层跷跷板制约机理。 |
| `来回乒乓打转` / `乒乓微环` | **`报文往返环路转发`** / **`异步转发微环`** | 消除口语化“乒乓打转”；准确描述相邻卫星异步更新转发表（FIB）引发的瞬态转发环路。 |
| `瞬间塞爆` / `瞬间爆满` | **`超出星载浅缓存容量上限`** / **`触发浅缓存溢出丢包`** | 消除夸张口语；突出星载交换机受功耗体积（SWaP）受限导致的浅缓存溢出物理机制。 |
| `走入死胡同` / `死胡同` | **`面临高维空间收敛瓶颈`** / **`难以遍历寻优`** | 消除口语化比喻，改用严谨的优化与复杂度表述。 |
| `多域异构组网` | **`多壳层异构组网`** / **`天地一体化多壳层异构网络`** | 在网络领域“多域（Multi-domain）”极易与地面自治域（BGP AS）混淆；本课题特指高低轨多壳层（LEO/MEO/GEO）立体交织组网。 |
| `差速机动` / `差速运动` | **`星间相对运动`** / **`星间相对运动导致的拓扑链路断裂`** | 卫星在轨运行遵循轨道动力学相对运动，并非主动推进变轨意义上的“差速机动”；统一表述为“星间相对运动导致拓扑链路断裂与周期切换”。 |
| `反噬`（如“单层孤立调参引发跨层反噬”） | **`跨层连锁恶化`** / **`顾此失彼引发跨层性能恶化`** | “反噬”带有文学修辞色彩且不够直观；统一改为“跨层连锁恶化”或“顾此失彼引发他层性能恶化”。 |
| `✗ 现实失配：`（第 05 页业务需求对比） | **`✗ 异构失配：`** | 当前主流商用星座（如 Starlink）采用弯管透传与星地同构控制，在现实中可用；真正无法满足高可靠低时延需求的是**未来多壳层星上路由异构网络**，故称“异构失配”。 |
| 文献流派对比矩阵（第 15 页）中“未达到 `×`”使用红色 | **纯表格三色字体（无胶囊背景）：**<br>· 已具备 `✓`：**翠绿加粗 (`#15803D`)**<br>· 部分具备 `△`：**浅黄/琥珀色 (`#D97706`)**<br>· 未达到 `×`：**浅灰色 (`#94A3B8`)** | 在研究现状综合对比表（第 15 页）中，既有方法“未达到/不具备（`×`）”用**浅灰色 (`#94A3B8`)** 视觉后退，从而让本课题“全维度达到（翠绿 `✓`）”与局部短板形成清晰、克制的视觉层次。 |

---

## 4. In-Figure Text De-duplication & Bottom Anchor Calibration Rules (`配图内文字去重极简化与底部锚点定性规范`)

1. **Zero Redundant Top Titles Inside Figures (`配图内部严禁重复卡片标题`)**:
   - When an image/GIF (`fig*.png` / `fig*.gif`) is placed inside a slide card whose header bar already states the card title (e.g., `一、传统单星弯管透传模式...` or `一、面向性能敏感变量的协议栈源码静态切片（2.1）`), the canvas figure **must NOT draw a duplicate top title bar/line** inside the image.
2. **Move Bottom `核心特征` Summary Out of the Figure into the Card Box (`配图底部“核心特征”总结外移替代重复条目`)**:
   - Do NOT draw a bottom `核心特征：...` or `⇒ 外显恶果：...` summary bar inside the image while simultaneously putting 2–3 bullet lines in the SVG card box below the image.
   - Instead, **remove the bottom summary bar from inside the image** so the visual stays clean and uncluttered, and **use that single direct `核心特征：...` sentence in the SVG card box below the image** (replacing repetitive bullet points).
3. **Minimal In-Figure Box Text (`配图内部模块文字极简化`)**:
   - Multi-box diagrams inside figures (such as Slide 05's 4 endogenous root causes or Slide 18's 3-stage pipeline) must contain at most **1 bold header + 1 concise phrase** per box, leaving detailed explanation to the speaker.
4. **Bottom Anchor Left Badge Calibration & Right Prefix Removal (`底部框“核心矛盾 vs. 核心结论”精准定性与右侧去重`)**:
   - Only slides that genuinely expose an unresolved conflict (`P05, P09`) use the left badge `核心矛盾`; slides that state an analytical, architectural, or methodological takeaway (`P04, P06, P07, P08, P11, P15, P16, P18–P30`) use `核心结论`.
   - Because the left badge of `bottom-core-anchor` already displays `核心矛盾` / `核心结论` / `现状局限一` / `可行性结论一`, the right-hand text **must NEVER repeat** `★ 核心矛盾：...` or `★ 核心结论：...`—start directly with `★ ...`!

---

## 5. Table 3 — Three-Tier Slide Title Rules & Full 36-Slide Dictionary (`三元页面标题设计准则与全篇 36 页标准字典`)

### 4.1 The Three-Tier Slide Title Governance Principle (`页面标题“三元治理”通则`)

| Title Tier | Narrative Role in Deck | Title Construction Rule | Representative Slides |
| :--- | :--- | :--- | :--- |
| **Tier A: Background & Problem-Inducing Argumentation Slides**<br>(`前期背景铺垫与矛盾引出论述页`) | Early slides that narrate **how the system evolved, why physical reality conflicts with demands, why legacy protocols fail across layers, and how the design paradigm shifts** (e.g., Slides 04, 05, 07, 08). | **Descriptive & Trait-Specific (`具象论述式`)**: Retain the specific evolutionary trajectory (`从 X 到 Y`), network regime (`多壳层异构网络`), and failure trait (`跨层连锁失配`) in the title so key argumentative context is never lost. | · **P04**：`天基网络形态演进：从单星弯管透传到天地一体化多壳层异构组网`<br>· **P05**：`多壳层异构网络非稳态特征与典型业务指标需求失配`<br>· **P07**：`传统地面网络协议在多壳层异构网络中的跨层连锁失配`<br>· **P08**：`网络体系设计范式演进：从正向开环试错到闭环逆向求解` |
| **Tier B: Core Analysis, Multi-Dimensional Comparison & Structural Synthesis Slides**<br>(`核心技术/内容分析比对、综述归纳与架构导引页`) | Slides that perform **systematic multi-dimensional comparison, problem/literature synthesis, target positioning, architectural mapping, and feasibility evaluation** (e.g., Slides 06, 09, 11–16, 18–19, 32–35). | **Condensed & Structural (`凝练结构式`, 8–18 chars)**: Because multi-dimensional comparisons or analytical structures cannot be listed in a single header, use a crisp, structured noun phrase; put detailed dimensions in the table/cards and mapping dictionary. | · **P06**：`三类网络体系特征对比`<br>· **P09**：`闭环逆向求解面临的核心问题`<br>· **P11**：`核心问题与国内外研究现状`<br>· **P12–14**：`研究现状一/二/三：...`<br>· **P15**：`国内外研究现状总结与对比`<br>· **P18–19**：`研究内容拆解逻辑与协同关系` / `总体研究架构与四层映射` |
| **Tier C: Official Research Content Heading Slides**<br>(`研究内容核心展开页：冒号后 1:1 原版呈现`) | Slides that present the **core Research Contents (`研究内容一/二/三：...`, Slides 20–30)**. | **Strict 1:1 Official Title Preservation (`冒号后禁止省略，1:1 呈现原版标题`)**: The text after `研究内容X：` is the canonical title of the research content/sub-content itself and **must never be abbreviated or paraphrased**. Strip only mechanical section numbers like `（1.2）`. | · **P20**：`研究内容一：跨层非稳态耦合机理与参数化扩展有限状态机表征`<br>· **P21**：`研究内容一：多时间尺度正交解耦与序贯参数辨识`<br>· **P25**：`研究内容二：局部扰动传播域动态定界与混合粒度推演`<br>· **P29**：`研究内容三：嵌入误差裕度的保守下界剪枝与最优性间隙分析` |

### 4.2 Full 36-Slide Canonical Title & Semantic Mapping Dictionary

| Slide | SVG File | Title Tier | **Canonical Slide Title (`标准页面标题`)** | Full Semantic Scope & Key Traits (`完整语义内涵与页面核心特质记录`) |
| :---: | :--- | :---: | :--- | :--- |
| **01** | `01_cover.svg` | Cover | **大规模异构卫星网络体系闭环逆向求解方法研究** | 博士学位论文开题报告答辩封面（答辩人、指导老师、专业、汇报时间） |
| **02** | `02_toc.svg` | TOC | **目 录** | 01 研究背景与核心问题 · 02 国内外研究现状与研究目标 · 03 研究内容 · 04 可行性分析与工作计划 |
| **03** | `03_section_background.svg` | Divider | **研究背景与核心问题** | 第一部分章节过渡页 |
| **04** | `04_morphology_evolution.svg` | **Tier A (背景具象论述)** | **天基网络形态演进：从单星弯管透传到天地一体化多壳层异构组网** | 标题直接体现形态演进的起点（与地面同构的单星弯管透传）与终点（多壳层异构组网），正文聚焦规模与耦合复杂度的数量级跃迁 |
| **05** | `05_nonstationary_and_demands.svg` | **Tier A (背景具象论述)** | **多壳层异构网络非稳态特征与典型业务指标需求失配** | 标题直接点明“多壳层异构网络”的“非稳态特征”（周期切换 + $1-(1-p)^N \to 1$ 规模故障率）与“典型业务指标需求”之间的异构失配 |
| **06** | `06_three_networks_comparison.svg` | **Tier B (分析比对结构式)** | **三类网络体系特征对比** | 汇总对比地面网、弯管卫星网（当前 Starlink）与多壳层异构网的多维体制特征，标题简洁凝练，具体维度在表格中完整呈现 |
| **07** | `07_ground_schemes_failure.svg` | **Tier A (背景具象论述)** | **传统地面网络协议在多壳层异构网络中的跨层连锁失配** | 标题明确限定“传统地面网络协议”在“多壳层异构网络”中的“跨层连锁失配”（路由保活黑洞与异步微环、拥塞窗口误判塌缩、单层调参跨层制约） |
| **08** | `08_paradigm_shift.svg` | **Tier A (背景具象论述)** | **网络体系设计范式演进：从正向开环试错到闭环逆向求解** | 标题直接点明网络设计范式从“正向开环经验试错”向“面向业务 SLA 的双闭环逆向求解”的转型特质 |
| **09** | `09_three_core_problems.svg` | **Tier B (分析比对结构式)** | **闭环逆向求解面临的核心问题** | 归纳总结闭环逆向求解在机理建模、前向推演、逆向寻优三环节面临的三大核心技术问题 |
| **10** | `10_section_related_work.svg` | Divider | **国内外研究现状与研究目标** | 第二部分章节过渡页 |
| **11** | `11_problem_summary_and_mapping.svg` | **Tier B (分析比对结构式)** | **核心问题与国内外研究现状** | 承上启下导引页：汇总三大核心问题 $\to$ 提炼亟需具备的三大关键能力 $\to$ 引出后续三大研究现状调研方向 |
| **12** | `12_related_work_rc1.svg` | **Tier B (分析比对结构式)** | **研究现状一：网络测量与状态辨识** | 面向核心问题一：剖析星地端到端黑盒实测、网络层析成像与主动自动机学习的【已解痛点】、【实现机理】与非稳态跨层辨识局限 |
| **13** | `13_related_work_rc2.svg` | **Tier B (分析比对结构式)** | **研究现状二：网络仿真与性能推演** | 面向核心问题二：剖析逐包/容器仿真、稳态流体近似与数据驱动深度代理模型的【已解痛点】、【实现机理】与大规模瞬态带界推演局限 |
| **14** | `14_related_work_rc3.svg` | **Tier B (分析比对结构式)** | **研究现状三：拓扑规划与配置综合** | 面向核心问题三：剖析星座构型设计、时变图路由规划与地面形式化配置综合的【已解痛点】、【实现机理】与高维非凸带界求逆局限 |
| **15** | `15_paradigm_comparison_and_gaps.svg` | **Tier B (分析比对结构式)** | **国内外研究现状总结与对比** | 四大主流技术流派五维综合对比矩阵（`✓` 翠绿 `#15803D` / `△` 浅黄 `#D97706` / `×` 未达到用**浅灰 `#94A3B8`**）与三大研究切入点 |
| **16** | `16_core_question_and_targets.svg` | **Tier B (分析比对结构式)** | **核心科学问题与研究目标** | 课题唯一核心科学问题与 1 对 1 靶向解决三大核心问题的三项研究目标 |
| **17** | `17_section_research_content.svg` | Divider | **研究内容** | 第三部分章节过渡页 |
| **18** | `18_overall_framework_4layers.svg` | **Tier B (分析比对结构式)** | **总体研究架构与四层映射** | 研究目标 $\to$ 核心问题 $\to$ 研究内容 $\to$ 核心创新点的四层大字极简映射矩阵与全链路双闭环技术路线 |
| **19** | `19_rc1_overview.svg` | **Tier C (研究内容总览)** | **研究内容一：跨层非稳态灰盒机理建模与参数辨识方法** | 研究内容一总览页：围绕核心解决目标的总结性方法名称，清晰交代解决什么问题、提出什么创新点、子内容 1.1–1.4 递进关系与交付产出 |
| **20** | `20_rc1_1_efsm.svg` | **Tier C (子内容 1:1)** | **研究内容 1.1：跨层非稳态耦合机理与参数化扩展有限状态机表征** | 采用 `研究内容 1.1` 明确子内容层级，冒号后 1:1 完整保留子内容 1.1 标题 |
| **21** | `21_rc1_2_multiscale_decoupling.svg` | **Tier C (子内容 1:1)** | **研究内容 1.2：多时间尺度正交解耦与序贯参数辨识** | 采用 `研究内容 1.2` 明确子内容层级，冒号后 1:1 完整保留子内容 1.2 标题 |
| **22** | `22_rc1_3_degradation_attribution.svg` | **Tier C (子内容 1:1)** | **研究内容 1.3：跨层性能退化正交归因与可复用机理算子构建** | 采用 `研究内容 1.3` 明确子内容层级，冒号后 1:1 完整保留子内容 1.3 标题 |
| **23** | `23_rc1_4_identifiability_and_probing.svg` | **Tier C (子内容 1:1)** | **研究内容 1.4：混合可辨识性边界与双流微突发主动探测消歧** | 采用 `研究内容 1.4` 明确子内容层级，冒号后 1:1 完整保留子内容 1.4 标题 |
| **24** | `24_rc2_overview.svg` | **Tier C (研究内容总览)** | **研究内容二：基于局部扰动传播域的混合性能推演与误差定界方法** | 研究内容二总览页：围绕核心解决目标的总结性方法名称，清晰交代解决什么问题、提出什么创新点、子内容 2.1–2.4 递进关系与交付产出 |
| **25** | `25_rc2_1_slicing.svg` | **Tier C (子内容 1:1)** | **研究内容 2.1：协议栈静态程序切片与行为一致性标定** | 采用 `研究内容 2.1` 明确子内容层级，冒号后 1:1 完整保留子内容 2.1 标题 |
| **26** | `26_rc2_2_causal_cone_hybrid.svg` | **Tier C (子内容 1:1)** | **研究内容 2.2：局部扰动传播域动态定界与混合粒度推演** | 采用 `研究内容 2.2` 明确子内容层级，冒号后 1:1 完整保留子内容 2.2 标题 |
| **27** | `27_rc2_3_sensitivity_and_error_bound.svg` | **Tier C (子内容 1:1)** | **研究内容 2.3：跨层事件图伴随灵敏度分析与多源误差定界** | 采用 `研究内容 2.3` 明确子内容层级，冒号后 1:1 完整保留子内容 2.3 标题 |
| **28** | `28_rc2_4_multiscale_fidelity.svg` | **Tier C (子内容 1:1)** | **研究内容 2.4：多尺度推演精度传递机制与跨规模一致性验证** | 采用 `研究内容 2.4` 明确子内容层级，冒号后 1:1 完整保留子内容 2.4 标题 |
| **29** | `29_rc3_overview.svg` | **Tier C (研究内容总览)** | **研究内容三：嵌入误差裕度的分级代价跨层配置逆向综合方法** | 研究内容三总览页：围绕核心解决目标的总结性方法名称，清晰交代解决什么问题、提出什么创新点、子内容 3.1–3.3 递进关系与交付产出 |
| **30** | `30_rc3_1_cost_hierarchy.svg` | **Tier C (子内容 1:1)** | **研究内容 3.1：三级工程改造代价空间建模与按需升维策略** | 采用 `研究内容 3.1` 明确子内容层级，冒号后 1:1 完整保留子内容 3.1 标题 |
| **31** | `31_rc3_2_robust_pruning_and_optimality.svg` | **Tier C (子内容 1:1)** | **研究内容 3.2：嵌入误差裕度的保守下界剪枝与最优性间隙分析** | 采用 `研究内容 3.2` 明确子内容层级，冒号后 1:1 完整保留子内容 3.2 标题 |
| **32** | `32_rc3_3_pareto_and_verification.svg` | **Tier C (子内容 1:1)** | **研究内容 3.3：多目标帕累托配置前沿生成与闭环反馈核验** | 采用 `研究内容 3.3` 明确子内容层级，冒号后 1:1 完整保留子内容 3.3 标题 |
| **33** | `33_section_feasibility_and_plan.svg` | Divider | **可行性分析与工作计划** | 第四部分章节过渡页 |
| **34** | `34_feasibility_rc1_identification.svg` | **Tier B (分析比对结构式)** | **可行性验证一：跨层状态解耦辨识** | 面向研究内容一（创新点 1、2）的可行性分析与实证对比（凝练结构式标题，详细实验配置在卡片内展开） |
| **35** | `35_feasibility_rc2_hybrid_deduction.svg` | **Tier B (分析比对结构式)** | **可行性验证二：局部传播域混合推演** | 面向研究内容二（创新点 3）的可行性分析与实证对比（凝练结构式标题） |
| **36** | `36_feasibility_rc3_inverse_pruning.svg` | **Tier B (分析比对结构式)** | **可行性验证三：分级代价逆向剪枝** | 面向研究内容三（创新点 4）的可行性分析与实证对比（凝练结构式标题） |
| **37** | `37_feasibility_matrix_and_schedule.svg` | **Tier B (分析比对结构式)** | **总体可行性矩阵与工作计划** | 理论/工具/实验三维完备性矩阵、2026–2028 四阶段研发进度甘特图与预期成果 |
| **38** | `38_closing_thank_you.svg` | Closing | **敬请各位评审专家批评指正** | 致谢与答辩问答页 |

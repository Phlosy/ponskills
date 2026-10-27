# PPT Decomposition, Slide Splitting & Bridge Patterns (`从报告到 PPT 的转化、拆页与三大必配桥梁页规范`)

## 1. Standard Defense Chapter Naming (`目录与四章节标准命名规范`)

Formal defense PPT decks must use formal presentation titles rather than conversational or exploratory phrasing:

- **Slide 02 Title**: Always use **`目 录`** (with subtitle `CONTENTS`). Never use `"汇报提纲"`, `"PPT 汇报提纲与全篇逻辑脉络"`, or include speaking-time annotations (`"约 3.5 分钟 | P03–P07"`) on the slide canvas.
- **Four Canonical Chapters**:
  1. **`01 研究背景与核心问题`** (`PART 01`)
  2. **`02 国内外研究现状与研究目标`** (`PART 02`)
  3. **`03 研究内容`** (`PART 03`)
  4. **`04 可行性分析与工作计划`** (`PART 04`)

---

## 2. One Core Claim per Slide & Splitting Rules (`一页一核心论点与拆页准则`)

Each slide must serve **only one core claim (`唯一核心论点`)**:

1. **When to Keep on One Slide (`合并/保持单页`)**:
   - When two pages are essentially arguing the **exact same underlying phenomenon** (for example, "dynamic switching disturbances" and "large-scale failure probability compounding $1-(1-p)^N \to 1$" both establish that the system is perpetually non-stationary), merge them into a single cohesive slide ("Intrinsic Non-Stationary Nature vs. Concrete Scenario Demands").
2. **When to Split into Multiple Slides (`拆分为多页`)**:
   - **Paradigm vs. Problems**: Never cram "Open-Loop vs. Closed-Loop Paradigm Shift" and "Three Core Technical Problems" onto a single slide. Split them into **Slide A (Paradigm Shift)** and **Slide B (Three Core Technical Problems)**.
   - **Research Content Expansion (`1 页总览 + 2~3 页展开`)**: Unlike post-completion award slides that only state final outcomes, a proposal or method defense must explain the methodology clearly. Structure each Research Content as:
     - **1 Overview Slide**: Core challenge + solution idea in the Top Anchor, overall mechanism architecture + formal operator definition in the middle, and key output in the Bottom Anchor.
     - **2–3 Detail Slides**: Each detail slide unpacks **one** core mathematical decomposition, algorithm, or theorem (e.g., multi-timescale orthogonal decoupling, local disturbance domain activation, conservative lower-bound pruning inequality) with generous whitespace and large diagrams.

---

## 3. Three Mandatory Bridge Slides (`三大必配逻辑桥梁页`)

To prevent logical leaps between sections, every comprehensive defense deck must include three dedicated bridge slides:

| Bridge Slide | Location in Deck | Core Purpose & Layout Structure |
| :--- | :--- | :--- |
| **Bridge 1: Tri-System Feature Comparison**<br>*(三类体系特征对比页)* | Inside `01 研究背景与核心问题` (before showing protocol failures) | Compares **Baseline System vs. Transitional System vs. Target System** across 6 dimensions. Explains why transitional commercial systems remain usable (structurally isomorphic to baseline) while the target system is fundamentally heterogeneous and causes legacy schemes to fail. |
| **Bridge 2: Problem Summary & Literature Mapping**<br>*(承上启下：核心问题总结与现状解决脉络)* | First content slide of `02 国内外研究现状与研究目标` | Summarizes the 3 Core Problems from Part 01 on the left, maps them 1-to-1 to the 3 Related Work streams in the middle (`【已解部分】`), and highlights the remaining gap (`【未解局限】`) on the right. |
| **Bridge 3: Necessary Decomposition & Indispensability**<br>*(唯一核心问题的必然拆解与三大研究内容“缺一不可”关系)* | First content slide of `03 研究内容` (before the 4-layer matrix) | Proves why solving the overarching Core Question necessarily requires decomposing into Research Contents 1, 2, and 3, showing both the **forward dependency chain** (what breaks if any part is missing) and the **dual-loop feedback calibration**. |

---

## 4. Four-Layer Architecture Matrix & Embedded Innovations (`四层总体架构矩阵与内嵌创新点`)

- **Four-Layer Vertical Flow**: On the Overall Research Architecture slide, organize the rows strictly top-to-bottom as:
  1. **Row 1 (`第一层：业务保障需求`)**: Concrete application scenario requirements;
  2. **Row 2 (`第二层：核心技术问题`)**: The 3 Core Problems induced by those requirements;
  3. **Row 3 (`第三层：核心研究内容`)**: Research Contents 1, 2, and 3 (with sub-tasks);
  4. **Row 4 (`第四层：关键科学问题与创新点`)**: The corresponding Scientific Questions and Innovations.
- **No Standalone Innovation List Slide**: Omit standalone text-only slides listing "Key Scientific Questions and Innovations." Instead, embed them naturally into Row 4 of the Overall Architecture Matrix and into the headers/anchors of the individual Research Content slides.

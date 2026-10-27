# `ponskills` — 个人自研 AI Agent 技能集合仓库 (Personal Self-Developed Skills Collection)

`ponskills`（`git@github.com:Phlosy/ponskills.git`）是用于统一沉淀、管理与持续迭代**自主研发 AI Agent Skills** 的个人技能集合仓库（Skills Monorepo）。

> **核心定位**：
> 1. **非单一 Skill 仓库**：本仓库构建的是一整套自主实现的个人 Skills 体系，每个一级子目录代表一个独立的自研 Skill（例如 [`academic-proposal-defense-workflow/`](./academic-proposal-defense-workflow/SKILL.md)），后续新增的自研 Skills 均在此仓库下统一纳管。
> 2. **自研编排与第三方 Skill 解耦（类似软件工程 `third_party/` 第三方依赖库机制）**：本仓库仅维护**自主实现**的 Skills；当某些自研 Skill（作为顶层工作流或编排器）需要调用外部开源或配套的第三方 Skills 时，不在本仓库内冗余拷贝第三方代码，而是在拉取本项目后，在工作区内建立专门的 **`third_party_skills/`（第三方技能目录）** 拉取外部依赖，再基于本仓库的自研 Skill 调度第三方 Skills 完成任务。

---

## 一、 仓库架构与第三方技能协同机制

在复杂任务中，自研 Skill 往往承担**领域方法论、强制审批门禁（`⛔ BLOCKING GATES`）、质量准则与顶层多步编排**职责，并按需调用外部成熟的专项第三方 Skill（如原生 PPTX 编译、Word 模板渲染、文本去 AI 化等）。

推荐的标准工作区目录结构如下：

```text
<your-project-workspace>/
├── ponskills/                                 # 【自研技能库】克隆自 git@github.com:Phlosy/ponskills.git
│   ├── README.md                              # 本说明文档
│   ├── academic-proposal-defense-workflow/    # 自研 Skill 1：学术报告与答辩/公开汇报 PPT 全流程编排
│   │   ├── SKILL.md                           # 技能主入口与强制门禁规范
│   │   ├── references/                        # 领域方法论、视觉层级与避坑台账
│   │   ├── scripts/                           # 第三方依赖检查/拉取脚本、几何碰撞与渲染质检脚本
│   │   └── templates/                         # 大纲审阅单、术语表与母版模板
│   └── <future-self-developed-skill>/         # 自研 Skill N：后续扩展的其他自主研发技能
│
├── third_party_skills/                        # 【第三方依赖技能目录】类似软件项目的 third_party/ 或 vendor/
│   ├── ppt-master/                            # 第三方依赖示例：SVG 转原生可编辑 DrawingML PPTX
│   ├── EvoSkills/                             # 第三方依赖示例：论文规划、文献综述与数学推导辅助
│   ├── humanizer/                             # 第三方依赖示例：学术文本去 AI 痕迹与自然化润色
│   └── docx-template-report/                  # 第三方依赖示例：严格遵循母版样式的 DOCX 报告渲染
│
└── <your-project-deliverables>/               # 当前课题/项目的文档、代码与产出物
```

---

## 二、 快速开始（Quickstart）

### 1. 拉取本自研技能仓库

在任意项目工作区（Workspace）下克隆 `ponskills`：

```bash
git clone git@github.com:Phlosy/ponskills.git
```

### 2. 建立并拉取第三方依赖技能（`third_party_skills/`）

当所使用的自研 Skill 需要调用外部第三方 Skills 时，可在工作区下创建 `third_party_skills/` 目录并拉取对应依赖（或直接运行自研 Skill 内置的依赖引导脚本一键完成）：

```bash
# 方式 A：使用自研 Skill 内置脚本检查并一键拉取至 <workspace>/third_party_skills/
bash ponskills/academic-proposal-defense-workflow/scripts/ensure_dependent_skills.sh --check
bash ponskills/academic-proposal-defense-workflow/scripts/ensure_dependent_skills.sh --install

# 方式 B：手动在工作区创建 third_party_skills/ 并按需克隆第三方库
mkdir -p third_party_skills
git clone https://github.com/hugohe3/ppt-master.git third_party_skills/ppt-master
git clone https://github.com/EvoScientist/EvoSkills.git third_party_skills/EvoSkills
git clone https://github.com/blader/humanizer.git third_party_skills/humanizer
```

### 3. 调用自研 Skill 执行任务

在对话中指定使用 `ponskills/<skill-name>/SKILL.md`，Agent 将严格按照自研 Skill 定义的流程门禁（如先审阅大纲、再审阅纯母版模板、最后生成正片与全画幅质检）推进，并在底层自动寻址调用 `third_party_skills/` 中的配套工具。

---

## 三、 当前已收录的自研 Skills 列表

| 自研 Skill 名称 | 路径 | 核心功能与定位 | 协同调用的第三方 Skills（存放在 `third_party_skills/`） |
| :--- | :--- | :--- | :--- |
| **`academic-proposal-defense-workflow`** | [`./academic-proposal-defense-workflow/`](./academic-proposal-defense-workflow/SKILL.md) | 学术报告（开题/中期/技术报告 `.docx`/LaTeX）与答辩/公开学术汇报 PPT（`.pptx`）端到端标准化工作流。<br>内置三大强制人工确认门禁（`⛔ BLOCKING GATE 0/1/2`）、九环叙事法、`80/20` 视觉重心色彩法则、去框套框排版与因页制宜配图规范。 | `ppt-master`<br>`EvoSkills`<br>`humanizer`<br>`docx-template-report` |

---

## 四、 新增与维护自研 Skill 的约定

1. **只入库自研部分**：每个新增的自研 Skill 在仓库根目录下新建独立文件夹 `<skill-name>/`，包含 `SKILL.md` 及配套的 `references/`、`scripts/`、`templates/`。
2. **第三方依赖外置声明**：若新自研 Skill 需要依赖外部第三方 Skill，请在 `<skill-name>/SKILL.md` 中列出第三方仓库的 Git 地址，并通过脚本或配置统一指向工作区的 `third_party_skills/` 目录，严禁将第三方仓库直接混入 `ponskills` 的 Git 版本树中。

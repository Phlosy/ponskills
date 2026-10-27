#!/usr/bin/env python3
"""Automated Linter for Controlled Terminology & Three-Tier Slide Title Governance.

Scans all SVG slides in a directory to enforce:
1. Zero forbidden colloquial/slang/literal-translation/ambiguous expressions
   (as defined in references/06-controlled-glossary-and-title-stylebook.md).
2. Three-Tier Slide Title Governance (<g id="page-header">):
   - Zero rhetorical question marks ('？' or '?') or conversational '为什么'
   - Zero verbose section numbers in parentheses like '（1.2）' or '（1.3–1.4）'
   - Tier A (Background & problem-inducing argumentation slides: 04, 05, 07, 08)
     must retain their descriptive evolutionary/mismatch traits (>= 18 chars).
   - Tier B (Core analysis, multi-dimensional comparison, survey, architecture & feasibility slides:
     06, 09, 11, 12-16, 18, 19, 32-35) must use condensed structural titles (<= 16 chars).
   - Tier C (Research Content slides: 20-30) must preserve 1:1 the official Research Content
     title after '研究内容X：' without abbreviation.
3. On Slide 15 (15_paradigm_comparison_and_gaps.svg), verify that '×' unachieved cells use
   Light Gray (#94A3B8) rather than red (#EF4444).
"""
import glob
import os
import re
import sys
import xml.etree.ElementTree as ET

FORBIDDEN_TERMS = {
    "汇报提纲": "目 录",
    "按下葫芦浮起瓢": "单层参数调整的跨层制约 / 跨层孤立调参冲突",
    "乒乓打转": "报文往返环路转发 / 异步转发微环",
    "来回乒乓": "往返环路转发",
    "瞬间塞爆": "超出星载浅缓存容量上限 / 浅缓存溢出",
    "塞爆": "缓存溢出",
    "死胡同": "高维空间收敛瓶颈",
    "走不通": "发生跨层机理失配",
    "拆成这三块": "拆解为三大研究内容",
    "守卫事件": "状态转移触发条件",
    "横截性跃变": "临界状态跳变 / 状态转移触发边界的清晰可分性",
    "流生包": "流体排队与离散包级状态互转",
    "包归流": "离散包级与流体排队状态互转",
    "零假阳性": "确保所选配置实际达标",
    "现实失配": "异构失配",
    "多域异构": "多壳层异构",
    "靶向": "研究内容一/二/三可行性验证 / 严格一一对应",
    "验证别人未试过的点": "补齐未知配置验证空白",
    "反噬": "跨层连锁恶化 / 顾此失彼",
    "差速机动": "星间相对运动",
    "差速运动": "星间相对运动",
}

TIER_A_PREFIXES = ("04_", "05_", "07_", "08_")
TIER_B_PREFIXES = (
    "06_", "09_", "11_", "12_", "13_", "14_", "15_", "16_", "18_",
    "34_", "35_", "36_", "37_"
)
TIER_B_MAX_LEN = 16

TIER_C_EXACT_TITLES = {
    "19_rc1_overview.svg": "研究内容一：跨层非稳态灰盒机理建模与参数辨识方法",
    "20_rc1_1_efsm.svg": "研究内容 1.1：跨层非稳态耦合机理与参数化扩展有限状态机表征",
    "21_rc1_2_multiscale_decoupling.svg": "研究内容 1.2：多时间尺度正交解耦与序贯参数辨识",
    "22_rc1_3_degradation_attribution.svg": "研究内容 1.3：跨层性能退化正交归因与可复用机理算子构建",
    "23_rc1_4_identifiability_and_probing.svg": "研究内容 1.4：混合可辨识性边界与双流微突发主动探测消歧",
    "24_rc2_overview.svg": "研究内容二：基于局部扰动传播域的混合性能推演与误差定界方法",
    "25_rc2_1_slicing.svg": "研究内容 2.1：协议栈静态程序切片与行为一致性标定",
    "26_rc2_2_causal_cone_hybrid.svg": "研究内容 2.2：局部扰动传播域动态定界与混合粒度推演",
    "27_rc2_3_sensitivity_and_error_bound.svg": "研究内容 2.3：跨层事件图伴随灵敏度分析与多源误差定界",
    "28_rc2_4_multiscale_fidelity.svg": "研究内容 2.4：多尺度推演精度传递机制与跨规模一致性验证",
    "29_rc3_overview.svg": "研究内容三：嵌入误差裕度的分级代价跨层配置逆向综合方法",
    "30_rc3_1_cost_hierarchy.svg": "研究内容 3.1：三级工程改造代价空间建模与按需升维策略",
    "31_rc3_2_robust_pruning_and_optimality.svg": "研究内容 3.2：嵌入误差裕度的保守下界剪枝与最优性间隙分析",
    "32_rc3_3_pareto_and_verification.svg": "研究内容 3.3：多目标帕累托配置前沿生成与闭环反馈核验",
}


def strip_ns(tag: str) -> str:
    return tag.split("}", 1)[-1] if "}" in tag else tag


def elem_text(el: ET.Element) -> str:
    return "".join(el.itertext()).strip()


def check_svg_file(path: str) -> list[str]:
    issues = []
    fname = os.path.basename(path)
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()

    # 1. Check forbidden terms across entire SVG text
    for bad, good in FORBIDDEN_TERMS.items():
        if bad in raw:
            issues.append(f"[TERM] {fname}: contains forbidden term '{bad}' -> use '{good}'")

    # 2. Check Slide 15 '×' cell color (must be light gray #94A3B8, not #EF4444)
    if fname.startswith("15_"):
        if 'fill="#EF4444" text-anchor="middle">×' in raw:
            issues.append(f"[MATRIX-COLOR] {fname}: '×' unachieved cells must use light gray (#94A3B8), not #EF4444")

    # 3. Check <g id="page-header"> title style and Tier A / Tier B / Tier C rules
    try:
        root = ET.fromstring(raw)
    except ET.ParseError as e:
        issues.append(f"[XML] {fname}: parse error {e}")
        return issues

    for g in root.iter():
        if strip_ns(g.tag) == "g" and g.attrib.get("id") == "page-header":
            texts = [elem_text(t) for t in g.iter() if strip_ns(t.tag) == "text"]
            if texts:
                main_title = texts[0]
                if "？" in main_title or "?" in main_title or "为什么" in main_title:
                    issues.append(f"[TITLE-STYLE] {fname}: rhetorical question in title '{main_title}'")
                if re.search(r"[（(]\d+\.\d+", main_title):
                    issues.append(f"[TITLE-NUM] {fname}: verbose section number in title '{main_title}'")
                if fname.startswith(TIER_A_PREFIXES) and len(main_title) < 18:
                    issues.append(
                        f"[TITLE-TIER-A] {fname}: background argumentation title '{main_title}' is {len(main_title)} chars "
                        f"(too short; Tier A slides must retain descriptive evolution/mismatch traits)"
                    )
                if fname.startswith(TIER_B_PREFIXES) and len(main_title) > TIER_B_MAX_LEN:
                    issues.append(
                        f"[TITLE-TIER-B] {fname}: structural/comparison/analysis title '{main_title}' is {len(main_title)} chars "
                        f"(exceeds max {TIER_B_MAX_LEN} chars for Tier B condensed structural headers)"
                    )
                if fname in TIER_C_EXACT_TITLES and main_title != TIER_C_EXACT_TITLES[fname]:
                    issues.append(
                        f"[TITLE-TIER-C] {fname}: Research Content title '{main_title}' does not match 1:1 "
                        f"canonical title '{TIER_C_EXACT_TITLES[fname]}'"
                    )
        if strip_ns(g.tag) == "g" and g.attrib.get("id") == "bottom-core-anchor":
            texts = [elem_text(t) for t in g.iter() if strip_ns(t.tag) == "text"]
            if len(texts) >= 3:
                body_txt = texts[2]
                if re.search(r"^★\s*(核心矛盾|核心结论|核心推论|现状局限[一二三]|现有研究共性问题|共性问题|可行性结论[一二三]?|全篇总结)[：:]", body_txt):
                    issues.append(
                        f"[REDUNDANT-BOTTOM-PREFIX] {fname}: bottom anchor text repeats badge label '{body_txt[:24]}...'"
                    )
    return issues


def main():
    if len(sys.argv) < 2:
        print("Usage: check_terminology_and_titles.py <svg_output_dir>")
        sys.exit(2)
    svg_dir = sys.argv[1]
    svg_files = sorted(glob.glob(os.path.join(svg_dir, "*.svg")))
    all_issues = []
    for f in svg_files:
        all_issues.extend(check_svg_file(f))

    print(
        f"Scanned {len(svg_files)} SVG slides in {svg_dir} for terminology & Three-Tier title governance. "
        f"Issues found: {len(all_issues)}"
    )
    for iss in all_issues:
        print("  -", iss)
    sys.exit(1 if all_issues else 0)


if __name__ == "__main__":
    main()

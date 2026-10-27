#!/usr/bin/env python3
"""
Reusable Academic Navy & Warm Gold SVG Slide Component Library (v6.0/v7.0 Locked Style).
Used by `academic-proposal-defense-workflow` to guarantee 100% template consistency.
"""
import re


def fit_font_size(txt: str, max_px: float = 1015.0, base_fs: float = 18.5) -> float:
    """Auto-scale font size for long anchor lines so text never overflows x=1240."""
    plain = re.sub(r"<[^>]+>", "", txt)
    plain = (
        plain.replace("&lt;", "<")
        .replace("&gt;", ">")
        .replace("&amp;", "&")
        .replace("&#8722;", "-")
    )
    w = sum(1.03 if ord(c) > 127 else 0.58 for c in plain)
    if w * base_fs > max_px:
        return round(max(15.2, max_px / w), 1)
    return base_fs


def common_defs() -> str:
    return """  <defs>
    <linearGradient id="headerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1B365D"/>
      <stop offset="100%" stop-color="#234575"/>
    </linearGradient>
    <linearGradient id="coverBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F2342"/>
      <stop offset="60%" stop-color="#1B365D"/>
      <stop offset="100%" stop-color="#234575"/>
    </linearGradient>
    <filter id="cardShadow" x="-2%" y="-2%" width="104%" height="106%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.06"/>
    </filter>
    <filter id="anchorShadow" x="-2%" y="-4%" width="104%" height="112%">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#1B365D" flood-opacity="0.10"/>
    </filter>
  </defs>"""


def page_header(title: str, breadcrumb: str) -> str:
    return f"""{common_defs()}
  <rect id="bg" width="1280" height="720" fill="#FAFBFD"/>
  <g id="header-bar" data-pptx-bounds="0 0 1280 56">
    <rect x="0" y="0" width="1280" height="54" fill="url(#headerGrad)"/>
    <rect x="0" y="54" width="1280" height="2" fill="#C59B27"/>
    <text x="40" y="35" font-size="21" font-weight="bold" fill="#FFFFFF">{title}</text>
    <text x="1240" y="34" font-size="13" font-weight="bold" fill="#CBD5E1" text-anchor="end">{breadcrumb}</text>
  </g>"""


def top_anchor_a(badge_zh: str, badge_en: str, surface_line: str, essence_line: str) -> str:
    """Mode A1 Top Anchor: 14px secondary surface line + 18.5px bold essence line with #DC2626 red highlights."""
    fs = fit_font_size(essence_line, 1015.0, 18.5)
    return f"""  <g id="top-core-anchor" data-pptx-bounds="40 68 1200 84">
    <rect x="40" y="68" width="1200" height="84" rx="8" fill="#EDF4FC" stroke="#1B365D" stroke-width="2.2" filter="url(#anchorShadow)"/>
    <rect x="40" y="68" width="126" height="84" rx="8" fill="#1B365D"/>
    <text x="103" y="106" font-size="16" font-weight="bold" fill="#FFFFFF" text-anchor="middle">{badge_zh}</text>
    <text x="103" y="128" font-size="11" font-weight="bold" fill="#C59B27" text-anchor="middle">{badge_en}</text>
    <text x="186" y="96" font-size="14" fill="#475569">{surface_line}</text>
    <text x="186" y="131" font-size="{fs}" font-weight="bold" fill="#0F172A">{essence_line}</text>
  </g>"""


def top_anchor_c(pain_line: str, idea_line: str, badge1_cn: str = "核心问题", badge2_cn: str = "解决思路") -> str:
    """Mode A2 Top Anchor: Dual-badge Problem + Solution anchor box."""
    fs = fit_font_size(idea_line, 1015.0, 17.5)
    return f"""  <g id="top-core-anchor" data-pptx-bounds="40 68 1200 88">
    <rect x="40" y="68" width="1200" height="88" rx="8" fill="#FFFFFF" stroke="#1B365D" stroke-width="2.2" filter="url(#anchorShadow)"/>
    <rect x="40" y="68" width="8" height="88" rx="4" fill="#1B365D"/>
    <rect x="62" y="78" width="108" height="30" rx="5" fill="#1B365D"/>
    <text x="116" y="99" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">{badge1_cn}</text>
    <text x="184" y="99" font-size="14.5" font-weight="bold" fill="#334155">{pain_line}</text>
    <line x1="62" y1="114" x2="1220" y2="114" stroke="#E2E8F0" stroke-width="1"/>
    <rect x="62" y="120" width="108" height="30" rx="5" fill="#B45309"/>
    <text x="116" y="141" font-size="14" font-weight="bold" fill="#FFFFFF" text-anchor="middle">{badge2_cn}</text>
    <text x="184" y="141" font-size="{fs}" font-weight="bold" fill="#0F172A">{idea_line}</text>
  </g>"""


def bottom_anchor_a(badge_zh: str, badge_en: str, essence_line: str, surface_line: str = "") -> str:
    """Mode A Bottom Takeaway Anchor."""
    fs = fit_font_size(essence_line, 1015.0, 18.5)
    if surface_line:
        text_block = f"""    <text x="186" y="620" font-size="13.5" fill="#475569">{surface_line}</text>
    <text x="186" y="655" font-size="{fs}" font-weight="bold" fill="#0F172A">{essence_line}</text>"""
    else:
        text_block = f"""    <text x="186" y="641" font-size="{fs}" font-weight="bold" fill="#0F172A">{essence_line}</text>"""
    return f"""  <g id="bottom-core-anchor" data-pptx-bounds="40 592 1200 82">
    <rect x="40" y="592" width="1200" height="82" rx="8" fill="#FFFBEB" stroke="#B45309" stroke-width="2.2" filter="url(#anchorShadow)"/>
    <rect x="40" y="592" width="126" height="82" rx="8" fill="#B45309"/>
    <text x="103" y="630" font-size="16" font-weight="bold" fill="#FFFFFF" text-anchor="middle">{badge_zh}</text>
    <text x="103" y="650" font-size="10.5" font-weight="bold" fill="#FEF3C7" text-anchor="middle">{badge_en}</text>
{text_block}
  </g>"""


def bottom_anchor_b(badge_l1: str, badge_l2: str, headline: str, pt1: str, pt2: str) -> str:
    """Mode B Bottom Single-Climax Anchor (height 132px, for Related Work Master Tables)."""
    fs = fit_font_size(headline, 995.0, 19.5)
    return f"""  <g id="bottom-only-anchor" data-pptx-bounds="40 544 1200 132">
    <rect x="40" y="544" width="1200" height="132" rx="8" fill="#FFFBEB" stroke="#1B365D" stroke-width="2.5" filter="url(#anchorShadow)"/>
    <rect x="40" y="544" width="154" height="132" rx="8" fill="#1B365D"/>
    <rect x="190" y="544" width="5" height="132" fill="#C59B27"/>
    <text x="115" y="598" font-size="17" font-weight="bold" fill="#FFFFFF" text-anchor="middle">{badge_l1}</text>
    <text x="115" y="624" font-size="15" font-weight="bold" fill="#C59B27" text-anchor="middle">&amp; {badge_l2}</text>
    <text x="216" y="582" font-size="{fs}" font-weight="bold" fill="#0F172A">{headline}</text>
    <line x1="216" y1="596" x2="1216" y2="596" stroke="#FDE68A" stroke-width="1.5"/>
    <text x="216" y="626" font-size="14.5" font-weight="bold" fill="#334155">{pt1}</text>
    <text x="216" y="656" font-size="14.5" font-weight="bold" fill="#B45309">{pt2}</text>
  </g>"""


def table_cell_yes(x: int, y: int, text: str) -> str:
    """Standard PPT table cell with Emerald Green Bold font (NO capsule rect)."""
    return f'    <text x="{x}" y="{y}" font-size="12.5" font-weight="bold" fill="#15803D" text-anchor="middle">✓ {text}</text>'


def table_cell_no(x: int, y: int, text: str) -> str:
    """Standard PPT table cell with Soft Red font (NO capsule rect)."""
    return f'    <text x="{x}" y="{y}" font-size="12.5" fill="#EF4444" text-anchor="middle">× {text}</text>'


def table_cell_warn(x: int, y: int, text: str) -> str:
    """Standard PPT table cell with Amber Yellow font (NO capsule rect)."""
    return f'    <text x="{x}" y="{y}" font-size="12.5" fill="#D97706" text-anchor="middle">△ {text}</text>'

#!/usr/bin/env python3
"""
Automated Geometric Boundary, Table Column Bleed, and Vertical Overlap Scanner
for 1280x720 Canonical SVG Slides (`academic-proposal-defense-workflow` Gate 2A).
"""
import glob
import os
import re
import sys
import xml.etree.ElementTree as ET


def estimate_text_width(text: str, font_size: float) -> float:
    return sum(font_size * (1.02 if ord(ch) > 127 else 0.56) for ch in text)


def scan_svg_dir(svg_dir: str) -> int:
    files = sorted(glob.glob(os.path.join(svg_dir, "*.svg")))
    if not files:
        print(f"[ERROR] No SVG files found in {svg_dir}")
        return 1

    issues = []

    for path in files:
        fname = os.path.basename(path)
        tree = ET.parse(path)
        root = tree.getroot()
        texts = []
        # Dynamically extract vertical table column divider x-coordinates from <line> elements
        vert_lines = [40.0, 1240.0]
        for el in root.iter():
            if el.tag.endswith("line"):
                x1_l = float(el.attrib.get("x1", "0"))
                x2_l = float(el.attrib.get("x2", "0"))
                y1_l = float(el.attrib.get("y1", "0"))
                y2_l = float(el.attrib.get("y2", "0"))
                if abs(x1_l - x2_l) < 1.0 and abs(y2_l - y1_l) > 250.0:
                    vert_lines.append(x1_l)
        rw_cols = sorted(set(vert_lines))

        for el in root.iter():
            if el.tag.endswith("text"):
                txt = "".join(el.itertext()).strip()
                if not txt:
                    continue
                x = float(el.attrib.get("x", "0"))
                y = float(el.attrib.get("y", "0"))
                fs = float(el.attrib.get("font-size", "13"))
                anchor = el.attrib.get("text-anchor", "start")
                w = estimate_text_width(txt, fs)
                x0 = x - w / 2 if anchor == "middle" else (x - w if anchor == "end" else x)
                x1 = x + w / 2 if anchor == "middle" else (x if anchor == "end" else x + w)
                texts.append((x0, x1, y, fs, txt, x, anchor))

                # 1. Right canvas boundary check
                if x1 > 1265:
                    issues.append(f"[OVERFLOW-X] {fname} (x={x}, y={y}, end={x1:.1f}): {txt[:36]}")

                # 2. Related Work 5-column bleed check (against actual vertical divider lines)
                if "related_work_" in fname and 115 <= y <= 580 and anchor == "start" and len(rw_cols) >= 5:
                    for i in range(len(rw_cols) - 1):
                        if rw_cols[i] <= x < rw_cols[i + 1] - 6:
                            limit = rw_cols[i + 1] - 4
                            if x1 > limit:
                                issues.append(
                                    f"[TABLE-COL-BLEED] {fname} Col{i+1}->Col{i+2} "
                                    f"(x1={x1:.1f} > {limit}, y={y}): {txt[:40]}"
                                )

        # 3. Vertical collision check for left-aligned texts in same column
        for i in range(len(texts)):
            for j in range(i + 1, len(texts)):
                a, b = texts[i], texts[j]
                if abs(a[5] - b[5]) < 8 and a[6] == "start" and b[6] == "start":
                    dy = abs(a[2] - b[2])
                    min_dy = max(a[3], b[3]) * 0.82
                    if 0 < dy < min_dy:
                        issues.append(
                            f"[VERTICAL-OVERLAP] {fname} x={a[5]} y1={a[2]} y2={b[2]} "
                            f"(dy={dy:.1f} < {min_dy:.1f}): '{a[4][:20]}' vs '{b[4][:20]}'"
                        )

    print(f"Scanned {len(files)} SVG slides in {svg_dir}. Issues found: {len(issues)}")
    for item in issues:
        print("  ", item)
    return 1 if issues else 0


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    sys.exit(scan_svg_dir(target))

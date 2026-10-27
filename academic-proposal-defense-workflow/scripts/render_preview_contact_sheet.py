#!/usr/bin/env python3
"""
Render 16:9 full-canvas single-slide PNG previews (`rendered_png/*.png` at 1280x720)
and a high-resolution grid contact sheet (`preview_contact_sheet.png`) of all SVG
slides in a `ppt-master` project using Headless Google Chrome (`Gate 2C`).
Never uses `qlmanage -t` (which crops 16:9 slides into 1:1 square thumbnails).
"""
import glob
import math
import os
import subprocess
import sys

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def render_contact_sheet(project_dir: str, cols: int = 3) -> str:
    svg_dir = os.path.join(project_dir, "svg_output")
    png_dir = os.path.join(project_dir, "rendered_png")
    os.makedirs(png_dir, exist_ok=True)

    svgs = sorted(glob.glob(os.path.join(svg_dir, "*.svg")))
    if not svgs:
        raise RuntimeError(f"No SVGs found in {svg_dir}")

    # 1. Render each individual slide at 1280x720 (16:9 full canvas)
    rendered_pngs = []
    for s in svgs:
        out_png = os.path.join(png_dir, os.path.basename(s).replace(".svg", ".png"))
        subprocess.run(
            [
                CHROME,
                "--headless=new",
                "--disable-gpu",
                "--hide-scrollbars",
                "--window-size=1280,720",
                f"--screenshot={out_png}",
                f"file://{s}",
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True,
        )
        rendered_pngs.append(out_png)

    # 2. Assemble grid contact sheet
    rows = math.ceil(len(svgs) / cols)
    card_w, card_h, gap, pad = 640, 360, 12, 16
    win_w = pad * 2 + cols * card_w + (cols - 1) * gap
    win_h = pad * 2 + rows * card_h + (rows - 1) * gap

    html_path = os.path.join(project_dir, "preview_contact_sheet.html")
    png_path = os.path.join(project_dir, "preview_contact_sheet.png")

    items = "\n".join(
        f'<div class="s"><img src="file://{p}"/></div>' for p in rendered_pngs
    )
    html = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: #0F172A; padding: {pad}px;
      display: grid; grid-template-columns: repeat({cols}, {card_w}px);
      gap: {gap}px; width: {win_w}px;
    }}
    .s {{ width: {card_w}px; height: {card_h}px; background: #FFF; overflow: hidden; border: 1px solid #334155; }}
    .s img {{ width: 100%; height: 100%; display: block; }}
    </style></head><body>{items}</body></html>"""

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)

    subprocess.run(
        [
            CHROME,
            "--headless=new",
            "--disable-gpu",
            "--hide-scrollbars",
            f"--window-size={win_w},{win_h}",
            "--device-scale-factor=1",
            f"--screenshot={png_path}",
            f"file://{html_path}",
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=True,
    )
    os.remove(html_path)
    print(f"[OK] Rendered {len(rendered_pngs)} 16:9 PNGs -> {png_dir}")
    print(f"[OK] Rendered contact sheet ({len(svgs)} slides) -> {png_path}")
    return png_path


if __name__ == "__main__":
    proj = sys.argv[1] if len(sys.argv) > 1 else "."
    render_contact_sheet(os.path.abspath(proj))

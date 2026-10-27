# Scientific Figures, Modality Selection, Quantitative Rigor & Multimedia Pipeline (`配图选型、数据刻度溯源、动态 GIF 与原生视频内嵌规范`)

## 1. Purpose-Driven Figure Modality Selection (`配图形式“因表达目的制宜”准则`)

Never apply a single visual style blindly across all slides. Select the figure modality that communicates each slide's core mechanism most intuitively:

1. **Authentic High-Resolution Photos/Renderings for Real-World Engineering Entities (`现实工程系统与硬件优先用公开高清真图`)**:
   - When illustrating existing real-world systems, constellations, hardware payloads, or physical topologies (e.g., Starlink, Starshield, optical inter-satellite laser terminals, Walker constellation shells, real digital twin interfaces), **acquire authentic high-resolution public images** rather than drawing crude cartoon approximations.
   - **Clean Cropping Rule**: Crop or mask out distracting third-party watermarks and irrelevant English text banners so the visual integrates cleanly into the card.
2. **Symmetric Pure Geometric Vector Schematics for Structural/Topological Inversion (`纯几何拓扑反转对比必须采用高对比度几何矢量示意图`)**:
   - When the primary goal of a side-by-side comparison is to demonstrate a **fundamental geometric or topological inversion** (such as contrasting an **upright downward cone [正锥形]** from a fixed apex to moving ground users against an **inverted upward cone [倒锥形]** from a quasi-static ground region to multiple moving satellites), use **symmetric, high-contrast pure geometric vector schematics on a clean background**.
   - Do **not** replace clear geometric cones/topologies with oblique perspective photos when perspective distortion obscures the upright vs. inverted geometric contrast.
3. **Realistic Multi-Element Scene Composites for Complex Operational Scenarios (`复杂业务交互场景采用符合物理常识的多要素真实感场景图`)**:
   - When illustrating multi-node operational workflows (e.g., supply-side multi-satellite selection, on-orbit AI extraction, space-ground collaborative coverage), combine realistic space/Earth horizons with clean transparent-cutout or high-detail assets.
   - **Physical Common-Sense Rule**: Every element's placement must strictly obey physical reality (e.g., fixed terrestrial base stations must stand firmly on the ground, never float in the sky; orbital satellites move along the upper orbital shell).

---

## 2. Quantitative Chart Rigor: Equidistant Axes & Sourced vs. Qualitative Data (`数据图表刻度等距与“实测数据 vs. 定性示意”铁律`)

1. **Strictly Equidistant Axis Intervals (`坐标轴时间/数值刻度必须严格等距`)**:
   - On time-series bar/line charts, the horizontal axis intervals must be **strictly uniform** (for example, 2-year equidistant ticks: `2018, 2020, 2022, 2024, 2026, 2028E, 2030E`).
   - **Strictly forbidden**: Using 2-year steps for the first five ticks (`2018–2026`) and suddenly jumping 4 years (`2026–2030E`) at the same pixel spacing, which distorts the visual growth slope.
2. **Strict Separation Between Sourced Quantitative Metrics and Qualitative Conceptual Bars (`严格区分“有权威出处的定量数据”与“定性机理对比条”`)**:
   - **Sourced Quantitative Data**: Every concrete number, throughput figure, or projection displayed on a slide must be backed by a verifiable source (ITU, FCC, 3GPP, peer-reviewed literature, official filings) documented in the standalone **`<题目>_权威数据来源与测算依据.md`** file. Display the numbers cleanly on the slide without cluttering the slide canvas with citation footnotes.
   - **Qualitative Conceptual Comparison Bars**: When a horizontal stacked bar or comparison chart is intended only to illustrate a **qualitative structural shift** (e.g., "legacy single-pipe mode leaves most passing satellites idle" vs. "supply-side multi-satellite selection unlocks collaborative value") and no hard empirical percentage exists in public literature, **hide unverified percentage numbers (`隐去无实据支撑的具体百分比数值`)** and express the contrast purely through proportional bar segments, vivid contrast colors, and clear text labels.

---

## 3. Educational Dynamic GIF Design Rules (`教学视频级动态 GIF 设计准则`)

When dynamic GIFs are requested for mechanism/protocol slides:
- **Spatial / Constellation / Network Topology Animations**:
  - Use thin dashed lines (`1.0px`) for reference orbital planes and thin solid lines (`1.4px`) for active links.
  - Render **28–36 frames** ($\approx 4.5\text{ s}$ loop) showing the complete lifecycle (`Normal Coordination → Critical Stretch & Link Break → Handover & Re-establishment`).
- **Protocol & Mechanism Failure Animations**:
  - Render **at least 48 frames at `165ms` per frame ($\approx 7.92\text{ s}$ full cycle)** with an explicit top stage indicator bar so viewers have ample time (`~2.6s` per phase) to follow each transition.

---

## 4. Native Playable Video Embedding & 16:9 Headless Chrome Rendering (`原生可播放视频无损内嵌与 16:9 全画幅渲染质检`)

1. **Native Playable Video Preservation (`实景演示视频 .mp4 原生可播放内嵌`)**:
   - When a slide includes a live demonstration video (e.g., `ppt/media/media1.mp4`), strictly lock its native aspect ratio (`W : H`) when sizing the video frame on the slide.
   - After compiling SVGs to native DrawingML `.pptx` via `svg_to_pptx.py`, automatically inject:
     - The raw video binary (`ppt/media/media1.mp4`, stored uncompressed `ZIP_STORED`);
     - The video poster frame image (`ppt/media/image*_poster.png`);
     - The relationship entries (`video`, `media`, `image`, `tags`) in `ppt/slides/_rels/slide<N>.xml.rels` and `[Content_Types].xml`;
     - The `<p:pic>` video shape and `<p:timing>` interactive click-to-play sequence in `ppt/slides/slide<N>.xml`.
2. **Full 16:9 Headless Chrome Rendering (`强制使用 Headless Chrome 1280×720 渲染预览，严禁用 qlmanage`)**:
   - Never use macOS `qlmanage -t` to generate slide previews, as `qlmanage` crops 16:9 SVGs into 1:1 square thumbnails.
   - Always render 16:9 PNG previews and contact sheets via Headless Chrome:
     ```bash
     "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
       --headless=new --disable-gpu --hide-scrollbars \
       --window-size=1280,720 --screenshot="${OUT_PNG}" "file://${SVG_FILE}"
     ```

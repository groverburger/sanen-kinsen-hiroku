"""
Crop key diagrams from the Sanen Kinsen Hiroku manuscript pages.
Source images are 1525x1024 two-page spreads from Kyoto University Library.
"""
from pathlib import Path
from PIL import Image

SRC_DIR = Path("D:/projects-2025/japanese-image-parsing/original-manuscript")
OUT_DIR = Path("D:/projects-2025/japanese-image-parsing/diagrams")
OUT_DIR.mkdir(exist_ok=True)

crops = [
    # Page 12: Two tree diagrams across the full spread
    # Right page: 500-ryō buy tree; Left page: 100-ryō sell tree with title box
    # Trim worn outer borders, keep full spread content
    {
        "src": "page_00012.jpg",
        "out": "fig1_tree_positions.jpg",
        "box": (55, 55, 1470, 975),
        "desc": "Position-scaling tree diagrams (full spread)",
    },
    # Page 13: Right page has the 2000-ryō sell / 1000-ryō buy tree diagram
    # Crop just the right page area with the tree and its labels
    {
        "src": "page_00013.jpg",
        "out": "fig2_tree_scaling.jpg",
        "box": (660, 45, 1470, 660),
        "desc": "2000-ryo sell / 1000-ryo buy tree diagram",
    },
    # Page 21: Left page has the circular Three Levels diagram (世の中三段之圖)
    # Including the ceiling/floor/middle-star annotations below it
    {
        "src": "page_00021.jpg",
        "out": "fig3_three_levels.jpg",
        "box": (35, 40, 730, 975),
        "desc": "Three Levels diagram with ceiling/floor/middle star",
    },
    # Page 28: Left page has the Grand Radial Diagram (上割三下割之圖)
    # Main radial chart at top, yin/yang supplementary tables at bottom
    {
        "src": "page_00028.jpg",
        "out": "fig4_grand_chart.jpg",
        "box": (30, 25, 745, 985),
        "desc": "Grand seasonal trading diagram with yin/yang sections",
    },
]

print("Cropping diagrams from manuscript images...\n")
for c in crops:
    img = Image.open(SRC_DIR / c["src"])
    cropped = img.crop(c["box"])
    out_path = OUT_DIR / c["out"]
    cropped.save(out_path, "JPEG", quality=95)
    w, h = cropped.size
    fsize = out_path.stat().st_size // 1024
    print(f"  {c['out']:35s}  {w}x{h}  ({fsize} KB)  — {c['desc']}")

print("\nDone.")

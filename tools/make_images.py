#!/usr/bin/env python3
"""Derive every delivered image from the high-resolution masters in
assets/img/src.

Hard rule: downscale only. Each target asserts that the master is at least as
large as the requested size, so a soft, upscaled image can never ship again.
"""
import os
from PIL import Image, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "assets/img/src")
OUT = os.path.join(ROOT, "assets/img")

# target path, master, width, height, vertical anchor (0 = top, .5 = centre)
TARGETS = [
    ("hero/h1_hero1.jpg",   "hero1",     1376, 768, .5),
    ("hero/h1_hero2.jpg",   "hero2",     1376, 768, .5),
    ("hero/h1_hero3.jpg",   "hero3",     1376, 768, .5),
    ("hero/hero2.jpg",      "hero1",     1376, 768, .5),
    ("banner/bradcam.jpg",  "banner",    1408, 520, .45),
    ("banner/bradcam2.jpg", "banner",    1408, 520, .45),
    ("banner/bradcam3.jpg", "banner",    1408, 520, .45),
    ("gallery/prog-education.jpg", "education", 1120, 610, .5),
    ("gallery/prog-water.jpg",     "water",     1120, 610, .5),
    ("gallery/prog-women.jpg",     "women",     1120, 610, .5),
    ("gallery/prog-health.jpg",    "health",    1120, 610, .5),
    ("gallery/prog-climate.jpg",   "climate",   1120, 610, .5),
    ("gallery/case1.jpg", "education", 760, 460, .5),
    ("gallery/case2.jpg", "water",     760, 460, .5),
    ("gallery/case3.jpg", "women",     760, 460, .5),
    ("gallery/case4.jpg", "health",    760, 460, .5),
    ("gallery/case5.jpg", "climate",   760, 460, .5),
    ("gallery/case6.jpg", "mentor",    760, 460, .5),
    ("gallery/services1.jpg", "education", 760, 490, .5),
    ("gallery/services2.jpg", "water",     760, 490, .5),
    ("gallery/services3.jpg", "women",     760, 490, .5),
    ("gallery/home-blog1.jpg", "climate", 1120, 610, .5),
    ("gallery/home-blog2.jpg", "health",  1120, 610, .5),
    ("gallery/safe_in.jpg", "person1", 900, 1005, .1),
    ("gallery/visit_bg.jpg", "person2", 881, 990, .1),
    ("gallery/team1.jpg", "person1", 560, 640, .08),
    ("gallery/team2.jpg", "person2", 560, 640, .08),
    ("gallery/team3.jpg", "person3", 560, 640, .08),
    ("gallery/team4.jpg", "person4", 560, 640, .08),
    ("blog/single_blog_1.jpg", "education", 1100, 550, .5),
    ("blog/single_blog_2.jpg", "water",     1100, 550, .5),
    ("blog/single_blog_3.jpg", "women",     1100, 550, .5),
    ("blog/single_blog_4.jpg", "health",    1100, 550, .5),
    ("blog/single_blog_5.jpg", "climate",   1100, 550, .5),
]
POST_MASTERS = ["education", "water", "women", "health", "climate",
                "mentor", "hero1", "hero2", "hero3", "banner"]
for i, m in enumerate(POST_MASTERS, 1):
    TARGETS.append(("post/post_%d.jpg" % i, m, 160, 160, .35))

# heroes and breadcrumbs are full-bleed, so they get a little more quality
QUALITY = {"hero": 86, "banner": 86}


def cover(im, w, h, ay):
    """Crop to the target aspect ratio, then downscale. Never enlarges."""
    sw, sh = im.size
    assert sw >= w and sh >= h, "would upscale: %dx%d -> %dx%d" % (sw, sh, w, h)
    scale = max(w / sw, h / sh)          # <= 1 because of the assert above
    cw, ch = w / scale, h / scale
    x = (sw - cw) / 2
    y = (sh - ch) * ay
    im = im.crop((int(x), int(y), int(x + cw), int(y + ch)))
    if im.size != (w, h):
        im = im.resize((w, h), Image.LANCZOS)
    return im


def main():
    cache = {}
    for rel, master, w, h, ay in TARGETS:
        if master not in cache:
            cache[master] = Image.open(os.path.join(SRC, master + ".jpg")).convert("RGB")
        im = cover(cache[master].copy(), w, h, ay)
        # a touch of sharpening to recover the softness that resampling costs
        im = im.filter(ImageFilter.UnsharpMask(radius=1.1, percent=62, threshold=3))
        dst = os.path.join(OUT, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        q = QUALITY.get(rel.split("/")[0], 82)
        im.save(dst, "JPEG", quality=q, optimize=True, progressive=True)
        print("%-34s %-10s %4dx%-4d q%d  %5.0f KB"
              % (rel, master, w, h, q, os.path.getsize(dst) / 1024))


if __name__ == "__main__":
    main()

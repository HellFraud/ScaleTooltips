from pathlib import Path
import math
import random

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
W, H = 400, 225
SCALE = 4
random.seed(21)

image = Image.new("RGB", (W, H), "#0b1020")
draw = ImageDraw.Draw(image)

for y in range(H):
    t = y / H
    r = int(10 + 23 * t)
    g = int(14 + 35 * t)
    b = int(34 + 45 * t)
    draw.line((0, y, W, y), fill=(r, g, b))

for x, y in [(22, 30), (62, 17), (102, 41), (202, 22), (230, 48), (357, 27), (382, 64), (191, 62)]:
    draw.rectangle((x, y, x + 1, y + 1), fill="#8295bb")
    if x % 2 == 0:
        draw.point((x + 2, y), fill="#526588")

draw.rectangle((19, 48, 38, 67), fill="#d9e5dc")
draw.rectangle((19, 48, 23, 67), fill="#aabcc2")
draw.rectangle((31, 51, 38, 57), fill="#b8cbc9")
draw.rectangle((24, 59, 29, 64), fill="#c1d2ce")

mountains = [
    ([(0, 161), (0, 121), (25, 105), (44, 127), (71, 91), (110, 139), (145, 111), (184, 151), (184, 181)], "#182b43"),
    ([(0, 179), (0, 145), (35, 128), (67, 157), (105, 126), (150, 164), (205, 132), (251, 176), (251, 197)], "#203951"),
    ([(245, 178), (277, 129), (300, 145), (331, 105), (366, 146), (400, 119), (400, 196)], "#1b3048"),
]
for points, color in mountains:
    draw.polygon(points, fill=color)

for x, y, h in [(12, 169, 36), (47, 177, 28), (83, 169, 40), (213, 174, 31), (363, 170, 42), (390, 179, 29)]:
    draw.rectangle((x - 2, y - h // 3, x + 2, y), fill="#101d2a")
    for level in range(3):
        top = y - h + level * h // 4
        half = 5 + level * 4
        draw.polygon([(x, top), (x - half, top + h // 2), (x + half, top + h // 2)], fill="#142b35")

draw.rectangle((0, 192, W, H), fill="#17251f")
draw.rectangle((0, 192, W, 196), fill="#365c42")
draw.rectangle((0, 196, W, 199), fill="#274433")
for x in range(0, W, 16):
    draw.rectangle((x, 200, x + 15, 215), fill="#26372b" if (x // 16) % 2 else "#2b3c2e")
    draw.rectangle((x + 3, 204, x + 6, 207), fill="#354b36")
    draw.line((x, 216, x + 15, 216), fill="#111d19")
for x in [5, 31, 74, 99, 224, 349, 378]:
    draw.line((x, 192, x + 2, 187), fill="#52714a", width=2)
    draw.line((x + 2, 192, x + 6, 189), fill="#456540", width=2)


def tooltip_segment(points, rows):
    draw.polygon(points, fill="#10091f", outline="#8f5ac2", width=3)
    inner = [(x + (2 if x < 300 else -2), y + (3 if y < 105 else -3)) for x, y in points]
    draw.line(inner + [inner[0]], fill="#392052", width=1)
    for y, left, right, color in rows:
        draw.rectangle((left, y, right, y + 3), fill=color)
        draw.rectangle((left, y + 4, right - 8, y + 4), fill="#2b1941")


tooltip_segment(
    [(257, -66), (320, -66), (317, 91), (308, 99), (299, 94), (289, 104), (280, 96), (269, 103), (253, 94)],
    [(y, 263 + (y % 3), 310 - (y % 4), "#bda4db" if y == 4 else "#77658f") for y in range(4, 89, 13)],
)
tooltip_segment(
    [(273, 117), (284, 110), (294, 119), (304, 109), (314, 116), (325, 108), (337, 118), (337, 252), (273, 252)],
    [(y, 281, 328 - (y % 5), "#a98bc9" if y == 130 else "#705d87") for y in range(130, 218, 13)],
)

for x, y in [(278, 16), (296, 43), (269, 70), (307, 151), (286, 182), (319, 207)]:
    draw.line((x, y, x + 7, y - 5), fill="#69458a", width=1)

# Steve is drawn in the same chunky grid as the world.
draw.polygon([(135, 106), (164, 101), (181, 119), (174, 151), (141, 151), (130, 129)], fill="#168c96")
draw.polygon([(141, 107), (164, 103), (174, 113), (143, 119)], fill="#28b7b4")
draw.rectangle((140, 143, 176, 155), fill="#253c91")
draw.polygon([(144, 151), (160, 153), (147, 181), (132, 190), (120, 184), (135, 172)], fill="#3549a9")
draw.polygon([(162, 151), (177, 150), (185, 174), (204, 184), (199, 193), (176, 184), (166, 170)], fill="#293d91")
draw.rectangle((116, 181, 134, 190), fill="#252a3e")
draw.rectangle((197, 184, 212, 193), fill="#24293a")
draw.rectangle((120, 181, 134, 184), fill="#444b60")
draw.rectangle((198, 184, 209, 187), fill="#444b60")

draw.polygon([(135, 111), (126, 112), (115, 140), (124, 145), (139, 124)], fill="#0d747f")
draw.polygon([(116, 134), (126, 138), (121, 153), (111, 151)], fill="#b87855")
draw.rectangle((112, 148, 121, 154), fill="#91583f")

draw.rectangle((130, 63, 168, 103), fill="#bd805c")
draw.rectangle((126, 69, 132, 96), fill="#9a6147")
draw.rectangle((130, 60, 165, 69), fill="#3c271f")
draw.rectangle((126, 65, 137, 80), fill="#3c271f")
draw.rectangle((134, 58, 157, 63), fill="#4a3023")
draw.rectangle((160, 65, 168, 76), fill="#4b3024")
draw.rectangle((165, 78, 172, 89), fill="#b27351")
draw.rectangle((169, 82, 174, 88), fill="#c88d66")
draw.rectangle((151, 76, 158, 81), fill="#eee9dc")
draw.rectangle((155, 77, 160, 82), fill="#574485")
draw.rectangle((163, 77, 168, 82), fill="#eee9dc")
draw.rectangle((166, 78, 170, 82), fill="#493b73")
draw.rectangle((153, 91, 166, 96), fill="#87523f")
draw.rectangle((157, 94, 168, 99), fill="#5d3a31")
draw.rectangle((130, 98, 151, 104), fill="#a66a4e")

draw.polygon([(164, 108), (180, 108), (197, 103), (199, 116), (177, 127), (166, 123)], fill="#1aa4a8")
draw.polygon([(194, 103), (231, 98), (235, 111), (198, 117)], fill="#bd805c")
draw.polygon([(196, 103), (230, 98), (230, 103), (197, 109)], fill="#d3956c")
draw.polygon([(230, 94), (250, 94), (259, 101), (257, 114), (246, 119), (231, 112)], fill="#c88a62")
draw.rectangle((239, 94, 251, 99), fill="#dfa67c")
draw.rectangle((250, 101, 260, 109), fill="#ad6c4f")
draw.line((236, 99, 236, 111), fill="#9f6248", width=1)
draw.line((243, 98, 243, 114), fill="#aa6c4e", width=1)

for points in [
    [(186, 92), (218, 86), (230, 87)],
    [(190, 126), (218, 125), (231, 121)],
    [(207, 78), (235, 73)],
]:
    draw.line(points, fill="#7dd9d2", width=2)

impact = (264, 106)
for angle in range(0, 360, 30):
    a = math.radians(angle)
    inner = 9 + (angle % 3)
    outer = 23 if angle % 60 else 31
    p1 = (impact[0] + math.cos(a - 0.12) * inner, impact[1] + math.sin(a - 0.12) * inner)
    p2 = (impact[0] + math.cos(a) * outer, impact[1] + math.sin(a) * outer)
    p3 = (impact[0] + math.cos(a + 0.12) * inner, impact[1] + math.sin(a + 0.12) * inner)
    draw.polygon([impact, p1, p2, p3], fill="#f8e6a7" if angle % 60 else "#ffffff")
draw.rectangle((259, 101, 268, 110), fill="#fff8d6")

cracks = [
    [(278, 106), (286, 94), (283, 83), (294, 69), (291, 54)],
    [(280, 108), (294, 112), (300, 126), (312, 132), (309, 148)],
    [(282, 103), (297, 96), (307, 98), (316, 88)],
    [(276, 112), (282, 128), (278, 139), (289, 157), (285, 173)],
]
for points in cracks:
    draw.line(points, fill="#efe4ff", width=2)
    draw.line([(x + 2, y) for x, y in points], fill="#734493", width=1)

for x, y, size, angle in [(292, 77, 6, 20), (328, 91, 8, 45), (337, 127, 7, 15), (303, 152, 5, 35), (258, 64, 5, 50), (346, 66, 4, 0), (264, 139, 6, 30)]:
    shard = Image.new("RGBA", (18, 18))
    sd = ImageDraw.Draw(shard)
    sd.polygon([(4, 2), (14, 5), (12, 15), (3, 11)], fill="#171027", outline="#b175dc", width=1)
    shard = shard.rotate(angle, resample=Image.Resampling.NEAREST)
    image.paste(shard, (x, y), shard)

for x, y in [(246, 47), (327, 47), (351, 106), (242, 155), (314, 170)]:
    draw.line((x - 3, y, x + 3, y), fill="#d9c3ef", width=1)
    draw.line((x, y - 3, x, y + 3), fill="#d9c3ef", width=1)

image = image.resize((W * SCALE, H * SCALE), Image.Resampling.NEAREST)
draw = ImageDraw.Draw(image)
font_dir = Path("C:/Windows/Fonts")
title_font = ImageFont.truetype(str(font_dir / "impact.ttf"), 104)
subtitle_font = ImageFont.truetype(str(font_dir / "consola.ttf"), 25)
badge_font = ImageFont.truetype(str(font_dir / "arialbd.ttf"), 22)

draw.text((67, 52), "SCALE TOOLTIPS", font=title_font, fill="#090d1b", stroke_width=7, stroke_fill="#090d1b")
draw.text((64, 47), "SCALE TOOLTIPS", font=title_font, fill="#f2f5ff", stroke_width=2, stroke_fill="#9adbd7")
draw.text((72, 161), "BIG LORE.  ONE SCREEN.", font=subtitle_font, fill="#b8c9dc")

badge = (67, 810, 580, 854)
draw.rounded_rectangle(badge, radius=6, fill="#10192b", outline="#4c6b78", width=2)
draw.text((86, 819), "CLIENT SIDE  /  NEOFORGE + FABRIC", font=badge_font, fill="#b9d9d4")
draw.text((1370, 829), "HELL_FRAUD", font=badge_font, fill="#7e91aa")

image.save(ROOT / "cover.png", optimize=True)
icon = image.crop((650, 0, 1550, 900)).resize((256, 256), Image.Resampling.LANCZOS)
icon.save(ROOT / "icon.png", optimize=True)
print(ROOT / "cover.png")
print(ROOT / "icon.png")

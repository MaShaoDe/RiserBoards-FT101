#!/usr/bin/env python3
# Copyright 2026 FerienBSD aka Marcel Sauder (MaShaoDe), CERN-OHL-P-2.0
# https://github.com/MaShaoDe/RiserBoards-FT101
"""Generate a KiCad board file (KiCad 8 format, opens in KiCad 9) for an
FT-101 riser board RBxx.

Usage: python3 gen_riser.py 18 [outdir]

Coordinates: board origin at the top centre (connector edge), y grows
towards the finger tip. All values in mm.
"""
import sys
import uuid
from pathlib import Path

VERSION = "V0.3"
DATE = "2026-11-25"

PITCH = 3.96
LENGTH = 105.0          # finger tip to connector edge
FINGER_ZONE = 11.0      # straight finger zone at the tip
EXTRA = 5.0             # upper part is this much wider in total
STEP = EXTRA / 2        # 45 degree step per side
CORNER_R = 1.5          # rounded corners at the connector edge
TIP_CHAMFER = 0.5       # small chamfer at the finger corners

FINGER_W, FINGER_L, FINGER_GAP = 2.0, 9.0, 0.6     # gap = set back from tip
CONN_W, CONN_L, CONN_GAP = 2.0, 5.0, 0.5           # gap = set back from top edge
TRACE_W = 2.0
TP_D, TP_Y = 2.6, 12.0

VARIANTS = {
    10: dict(width=42.0, cards="PB-1292"),
    14: dict(width=57.0, cards="PB-1184"),
    18: dict(width=73.0, cards="PB-1180  PB-1181  PB-1314"),
    22: dict(width=89.0, cards="PB-1183  PB-1315"),
}

RIGHT = "GitHub: RiserBoards-FT101"   # short, people search for it
COPY1 = "Copyright 2026"
COPY2 = "FerienBSD aka Marcel Sauder"
LIC = f"{VERSION}  CERN-OHL-P-2.0"

# centre silkscreen: (text, y, size, thickness or None)
SIDE_SIZE = 2.2
CHAR_W = 1.0   # KiCad stroke font: text width is about chars x size


def centre_lines(n, side, usable=None):
    """Centre texts of one side ("F" or "B").

    Entries: (text, y, size, thickness or None, group). Lines of the same
    group share one size; a line is scaled down if wider than usable.
    """
    if side == "F":     # component side: short and clear
        lines = [
            (f"RB{n}", 26, 7.0, 1.0, "rb"),
            ("RISERBOARD FOR", 37, 3.5, 0.5, "title"),
            ("YAESU TRANSCEIVERS", 42, 3.5, 0.5, "title"),
            ("COMPONENT SIDE", 57, 4.5, 0.6, "side"),
            ("TO RADIO", 79, 3.5, 0.5, "radio"),
        ]
    else:               # rear side: all details in small, calm text
        lines = [
            (f"RB{n}", 24, 2.5, 0.35, "head"),
            ("RISERBOARD FOR", 28.5, 2.5, 0.35, "head"),
            ("YAESU TRANSCEIVERS", 32, 2.5, 0.35, "head"),
            ("FT-101 SERIES", 36.5, 2.5, 0.35, "head"),
            ("SOMMERKAMP FT-277 SERIES", 40, 2.5, 0.35, "head"),
            (COPY1, 46, 1.5, None, "copy"),
            (COPY2, 48.5, 1.5, None, "copy"),
            (LIC, 51, 1.5, None, "copy"),
            ("REAR SIDE", 62, 4.5, 0.6, "side"),
            ("TO RADIO", 83, 3.5, 0.5, "radio"),
        ]
    if usable is None:
        return [l[:4] for l in lines]
    k = {}
    for t, y, size, th, g in lines:
        k[g] = min(k.get(g, 1.0), usable / (len(t) * size * CHAR_W))
    return [(t, y, round(size * min(1.0, k[g]), 2),
             None if th is None else round(th * min(1.0, k[g]), 2))
            for t, y, size, th, g in lines]


def side_size(t, length):
    """Side text size, scaled down if the text is longer than the edge."""
    return round(min(SIDE_SIZE, length / (len(t) * CHAR_W)), 2)


def usable_width(xs, ht, side="B"):
    if side == "F":                 # no side texts on the component side
        return 2 * (ht - 2.0)
    side_x = (xs[-1] + TRACE_W / 2 + ht) / 2
    return 2 * (side_x - SIDE_SIZE / 2 - 1.0)
ARROWS = {"F": ((0, 62), (0, 74.5), 2.5), "B": ((0, 67), (0, 78.5), 2.5)}   # start, tip, head

OX, OY = 100.0, 40.0    # placement on the KiCad sheet


def u():
    return str(uuid.uuid4())


def f(v):
    return f"{v:.4f}".rstrip("0").rstrip(".")


def P(x, y):
    return f"{f(OX + x)} {f(OY + y)}"


def build(n):
    v = VARIANTS[n]
    wf = v["width"]
    wt = wf + EXTRA
    hf, ht = wf / 2, wt / 2
    y_step_end = LENGTH - FINGER_ZONE          # 94
    y_step_start = y_step_end - STEP           # 91.5
    xs = [(i - (n + 1) / 2) * PITCH for i in range(1, n + 1)]

    out = []
    w = out.append

    # nets
    nets = ["".strip()]
    for i in range(1, n + 1):
        nets.append(f"POS{i:02d}F")
        nets.append(f"POS{i:02d}B")
    netno = {name: k for k, name in enumerate(nets)}

    w('(kicad_pcb (version 20240108) (generator "gen_riser") (generator_version "8.0")')
    w('  (general (thickness 1.6) (legacy_teardrops no))')
    w('  (paper "A4")')
    w('  (title_block (title "RB%d riser board for Yaesu FT-101") (date "%s") (rev "%s") (company "FerienBSD aka Marcel Sauder") (comment 1 "Author: Marcel Sauder (MaShaoDe)") (comment 2 "License: CERN-OHL-P-2.0") (comment 3 "github.com/MaShaoDe/RiserBoards-FT101"))' % (n, DATE, VERSION))
    w('''  (layers
    (0 "F.Cu" signal) (31 "B.Cu" signal)
    (32 "B.Adhes" user "B.Adhesive") (33 "F.Adhes" user "F.Adhesive")
    (34 "B.Paste" user) (35 "F.Paste" user)
    (36 "B.SilkS" user "B.Silkscreen") (37 "F.SilkS" user "F.Silkscreen")
    (38 "B.Mask" user) (39 "F.Mask" user)
    (40 "Dwgs.User" user "User.Drawings") (41 "Cmts.User" user "User.Comments")
    (42 "Eco1.User" user "User.Eco1") (43 "Eco2.User" user "User.Eco2")
    (44 "Edge.Cuts" user) (45 "Margin" user)
    (46 "B.CrtYd" user "B.Courtyard") (47 "F.CrtYd" user "F.Courtyard")
    (48 "B.Fab" user) (49 "F.Fab" user))''')
    w('''  (setup
    (pad_to_mask_clearance 0)
    (allow_soldermask_bridges_in_footprints no))''')
    for k, name in enumerate(nets):
        w(f'  (net {k} "{name}")')

    # footprints: fingers, connector pads, test pads (pads on both sides)
    def footprint(name, ref, pads):
        w(f'  (footprint "riser:{name}" (layer "F.Cu") (uuid "{u()}") (at {P(0, 0)})')
        w(f'    (property "Reference" "{ref}" (at 0 -3 0) (layer "F.Fab") (uuid "{u()}") (effects (font (size 1 1) (thickness 0.15))))')
        w(f'    (property "Value" "{name}" (at 0 -5 0) (layer "F.Fab") (uuid "{u()}") (effects (font (size 1 1) (thickness 0.15))))')
        w('    (attr smd board_only exclude_from_pos_files exclude_from_bom)')
        for p in pads:
            w(p)
        w('  )')

    def pad(num, shape, x, y, sx, sy, side, net):
        cu, mask = ("F.Cu", "F.Mask") if side == "F" else ("B.Cu", "B.Mask")
        return (f'    (pad "{num}" smd {shape} (at {f(x)} {f(y)}) (size {f(sx)} {f(sy)}) '
                f'(layers "{cu}" "{mask}") (net {netno[net]} "{net}") (uuid "{u()}"))')

    fy = LENGTH - FINGER_GAP - FINGER_L / 2
    cy = CONN_GAP + CONN_L / 2
    for name, ref, shape, y, sx, sy in (
        (f"EdgeFingers_2x{n}", "J1", "rect", fy, FINGER_W, FINGER_L),
        (f"ConnectorPads_2x{n}", "J2", "rect", cy, CONN_W, CONN_L),
        (f"TestPads_2x{n}", "TP1", "circle", TP_Y, TP_D, TP_D),
    ):
        pads = []
        for i, x in enumerate(xs, 1):
            pads.append(pad(f"{i}", shape, x, y, sx, sy, "F", f"POS{i:02d}F"))
            pads.append(pad(f"{i}B", shape, x, y, sx, sy, "B", f"POS{i:02d}B"))
        footprint(name, ref, pads)

    # tracks
    for i, x in enumerate(xs, 1):
        for side in ("F", "B"):
            net = f"POS{i:02d}{side}"
            w(f'  (segment (start {P(x, cy)}) (end {P(x, fy)}) (width {f(TRACE_W)}) '
              f'(layer "{side}.Cu") (net {netno[net]}) (uuid "{u()}"))')

    # outline
    r, c = CORNER_R, TIP_CHAMFER
    k = 0.70710678
    pts = [(-ht + r, 0), (ht - r, 0)]
    arcs = []
    seq = [
        (ht, r), (ht, y_step_start), (hf, y_step_end), (hf, LENGTH - c),
        (hf - c, LENGTH), (-hf + c, LENGTH), (-hf, LENGTH - c), (-hf, y_step_end),
        (-ht, y_step_start), (-ht, r),
    ]
    edge = 'stroke (width 0.1) (type default)) (layer "Edge.Cuts") (uuid "%s"))'
    w(f'  (gr_line (start {P(-ht + r, 0)}) (end {P(ht - r, 0)}) ({edge % u()}')
    w(f'  (gr_arc (start {P(ht - r, 0)}) (mid {P(ht - r + k * r, r - k * r)}) (end {P(ht, r)}) ({edge % u()}')
    for a, b in zip(seq, seq[1:]):
        w(f'  (gr_line (start {P(*a)}) (end {P(*b)}) ({edge % u()}')
    w(f'  (gr_arc (start {P(-ht, r)}) (mid {P(-ht + r - k * r, r - k * r)}) (end {P(-ht + r, 0)}) ({edge % u()}')

    # silkscreen
    def text(s, x, y, size, layer, angle=0, thick=None):
        thick = thick or round(size * 0.15, 2)
        mirror = " (justify mirror)" if layer.startswith("B.") else ""
        w(f'  (gr_text "{s}" (at {P(x, y)} {angle}) (layer "{layer}") (uuid "{u()}") '
          f'(effects (font (size {f(size)} {f(size)}) (thickness {f(thick)})){mirror}))')

    def silk_line(a, b, layer, width=0.3):
        w(f'  (gr_line (start {P(*a)}) (end {P(*b)}) (stroke (width {width}) (type default)) '
          f'(layer "{layer}") (uuid "{u()}"))')

    side_x = (xs[-1] + TRACE_W / 2 + ht) / 2      # middle of the side margin
    side_y = (TP_Y + TP_D / 2 + y_step_start) / 2
    side_len = y_step_start - (TP_Y + TP_D / 2) - 2.0   # 1 mm free at both ends
    for side, layer in (("F", "F.SilkS"), ("B", "B.SilkS")):
        sgn = -1                                  # side texts only on the back
        for t, y, size, th in centre_lines(n, side, usable_width(xs, ht, side)):
            text(t, 0, y, size, layer, thick=th)
        (ax0, ay0), (ax1, ay1), hs = ARROWS[side]
        silk_line((ax0, ay0), (ax1, ay1), layer, 0.5)
        silk_line((-hs, ay1 - hs), (ax1, ay1), layer, 0.5)
        silk_line((hs, ay1 - hs), (ax1, ay1), layer, 0.5)
        if side == "B":
            for t, sx_ in ((v["cards"], -sgn * side_x), (RIGHT, sgn * side_x)):
                text(t, sx_, side_y, side_size(t, side_len), layer, angle=90)

    # fabrication notes outside the board
    notes = "\\n".join([
        f"RB{n} {VERSION} FABRICATION NOTES",
        "FR4 1.6 mm, 2 layers, 1 oz copper",
        "Solder mask both sides, green or black",
        "Silkscreen both sides, white",
        "Edge fingers: hard gold (Gold Fingers option), 30 deg bevel at the tip",
        "Other pads: lead free HASL or ENIG",
        "Bare boards only, connector soldered by hand",
        f"Board: {f(wf)} mm finger zone, {f(wt)} mm upper part, {f(LENGTH)} mm long",
    ])
    w(f'  (gr_text "{notes}" (at {P(ht + 10, 10)} 0) (layer "Cmts.User") (uuid "{u()}") '
      f'(effects (font (size 1.5 1.5) (thickness 0.2)) (justify left top)))')

    w(')')
    return "\n".join(out) + "\n", dict(xs=xs, wf=wf, wt=wt, fy=fy, cy=cy,
                                       y1=y_step_start, y2=y_step_end, cards=v["cards"])


def check_parens(s):
    depth, instr, esc = 0, False, False
    for ch in s:
        if instr:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                instr = False
        elif ch == '"':
            instr = True
        elif ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
            assert depth >= 0, "unbalanced"
    assert depth == 0 and not instr, "unbalanced"


def preview(n, g, path):
    """Both sides; the rear side is drawn as seen from the back."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import Rectangle, Circle, Polygon

    hf, ht = g["wf"] / 2, g["wt"] / 2
    outline = [(-ht, 0), (ht, 0), (ht, g["y1"]), (hf, g["y2"]), (hf, LENGTH),
               (-hf, LENGTH), (-hf, g["y2"]), (-ht, g["y1"])]
    fig, axs = plt.subplots(1, 2, figsize=(12, 9))
    kw = dict(color="white", ha="center", va="center", family="monospace")
    k = 7.4   # mm cap height to points (approx.)
    for ax, side, name in zip(axs, "FB", ("component side", "rear side, seen from the back")):
        ax.add_patch(Polygon(outline, closed=True, fc="#1f3b2d", ec="black", lw=1.5))
        for x in g["xs"]:
            ax.add_patch(Rectangle((x - TRACE_W / 2, g["cy"]), TRACE_W, g["fy"] - g["cy"], fc="#3f6b52", ec="none"))
            ax.add_patch(Rectangle((x - FINGER_W / 2, g["fy"] - FINGER_L / 2), FINGER_W, FINGER_L, fc="#d4af37", ec="none"))
            ax.add_patch(Rectangle((x - CONN_W / 2, g["cy"] - CONN_L / 2), CONN_W, CONN_L, fc="#c0c0c0", ec="none"))
            ax.add_patch(Circle((x, TP_Y), TP_D / 2, fc="#c0c0c0", ec="none"))
        for t, y, size, th in centre_lines(n, side, usable_width(g["xs"], ht, side)):
            ax.text(0, y, t, fontsize=size * k, weight="bold" if size >= 3.5 else "normal", **kw)
        (ax0, ay0), (ax1, ay1), hs = ARROWS[side]
        ax.annotate("", xy=(ax1, ay1), xytext=(ax0, ay0),
                    arrowprops=dict(arrowstyle="-|>", color="white", lw=2.5, mutation_scale=20))
        if side == "B":
            sx = (g["xs"][-1] + TRACE_W / 2 + ht) / 2
            sy = (TP_Y + TP_D / 2 + g["y1"]) / 2
            sl = g["y1"] - (TP_Y + TP_D / 2) - 2.0
            ax.text(-sx, sy, g["cards"], fontsize=side_size(g["cards"], sl) * k, rotation=90, **kw)
            ax.text(sx, sy, RIGHT, fontsize=side_size(RIGHT, sl) * k, rotation=90, **kw)
        ax.set_xlim(-ht - 6, ht + 6)
        ax.set_ylim(LENGTH + 5, -8)
        ax.set_aspect("equal")
        ax.set_title(f"RB{n} {VERSION}, {name}", fontsize=10)
    fig.tight_layout()
    fig.savefig(path, dpi=130)


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 18
    outdir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(__file__).resolve().parent.parent / f"riser-2x{n}"
    outdir.mkdir(parents=True, exist_ok=True)
    s, g = build(n)
    check_parens(s)
    # V0.1 files keep their old names, newer versions carry the version
    (outdir / f"riser-2x{n}_{VERSION}.kicad_pcb").write_text(s)
    preview(n, g, outdir / f"preview_{VERSION}.png")
    print("written", outdir)


if __name__ == "__main__":
    main()

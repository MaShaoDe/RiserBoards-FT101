# Changelog

## V0.3 (KiCad files generated, DRC and Gerber export pending)

Less is more: the RB18 V0.1 prototype showed that the silkscreen was too busy.

- Component side: only the type (e.g. RB18), "RISERBOARD FOR / YAESU TRANSCEIVERS", "COMPONENT SIDE" with arrow and "TO RADIO". Model line, copyright and side texts removed.
- Rear side, calm and small: type, "RISERBOARD FOR / YAESU TRANSCEIVERS" and "FT-101 SERIES / SOMMERKAMP FT-277 SERIES", all in the same 2.5 mm text; copyright and license in 1.5 mm; then with more space "REAR SIDE", arrow, "TO RADIO". Side edges: card names and "GitHub: RiserBoards-FT101". The rear side looks clearly different from the component side.
- Card names without revision letter: PB-1180, PB-1181, PB-1183, PB-1184, PB-1315 (fits all revisions).
- Generator preview shows both sides.
- New files per variant: `riser-2xNN_V0.3.kicad_pcb` and `preview_V0.3.png`. V0.2 was never produced and is replaced by V0.3.

## V0.2 (KiCad files generated, DRC and Gerber export pending)

- Silkscreen: copyright on two lines, "Copyright 2026" and "FerienBSD aka Marcel Sauder", so it stays at least 1.4 mm high even on the narrow RB10.
- Silkscreen side edge: "GitHub: RiserBoards-FT101" instead of the full link. The full link was about 81 mm long at 2.2 mm text and ran past the board edge; nobody types a URL from a PCB anyway, a search finds the repository.
- Side texts are scaled down automatically if they do not fit the edge (currently not needed on any variant).
- KiCad title block: company "FerienBSD aka Marcel Sauder", link github.com/MaShaoDe/RiserBoards-FT101, date 2026-11-12.
- New files per variant: `riser-2xNN_V0.2.kicad_pcb` and `preview_V0.2.png`. The V0.1 files keep their names.
- To do: DRC and Gerber export in KiCad 9 for RB10, RB14, RB18, RB22, then Gerber ZIPs and renders.

## V0.1

First release. The boards already in production keep their silkscreen as produced:
"Copyright 2026 Marcel Sauder" and github.com/MaShaoDe/HAM-Radio. The files in `hardware/riser-2x*/` are V0.1 and stay unchanged.

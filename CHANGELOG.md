# Changelog

## V0.3 (in production since 2026-11-25)

All four variants RB10, RB14, RB18, RB22 ordered: FR-4 1.6 mm, ENIG, hard gold fingers, 30 degree bevel. From this version on only the Gerber files are published (`hardware/riser-2xNN/RBNN_V0.3_gerber.zip`), not the design files. The fabrication specification for any PCB maker is in `docs/ordering.md`.


Less is more: the RB18 V0.1 prototype showed that the silkscreen was too busy.

- Component side: only the type (e.g. RB18), "RISERBOARD FOR / YAESU TRANSCEIVERS", "COMPONENT SIDE" with arrow and "TO RADIO". Model line, copyright and side texts removed.
- Rear side, calm and small: type, "RISERBOARD FOR / YAESU TRANSCEIVERS" and "FT-101 SERIES / SOMMERKAMP FT-277 SERIES", all in the same 2.5 mm text; copyright and license in 1.5 mm; then with more space "REAR SIDE", arrow, "TO RADIO". Side edges: card names and "github.com/MaShaoDe" (link to the GitHub user page). The rear side looks clearly different from the component side.
- Card names without revision letter: PB-1180, PB-1181, PB-1183, PB-1184, PB-1315 (fits all revisions).
- V0.2 was never produced and is replaced by V0.3.

## V0.2 (never produced)

- Silkscreen: copyright on two lines, "Copyright 2026" and "FerienBSD aka Marcel Sauder", so it stays at least 1.4 mm high even on the narrow RB10.
- Silkscreen side edge: "GitHub: RiserBoards-FT101" instead of the full link. The full link was about 81 mm long at 2.2 mm text and ran past the board edge; nobody types a URL from a PCB anyway, a search finds the repository.
- Side texts are scaled down automatically if they do not fit the edge (currently not needed on any variant).
- KiCad title block: company "FerienBSD aka Marcel Sauder", link github.com/MaShaoDe/RiserBoards-FT101, date 2026-11-12.

## V0.1

First release. RB18: 5 prototypes produced with ENIG surface, without the hard gold finger option and without bevel; built and working. Gerber ZIP in `hardware/archive/`. The boards already in production keep their silkscreen as produced:
"Copyright 2026 Marcel Sauder" and github.com/MaShaoDe/HAM-Radio. The files in `hardware/riser-2x*/` are V0.1 and stay unchanged.

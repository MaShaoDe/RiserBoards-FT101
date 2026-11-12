# Changelog

## V0.2 (generator ready, Gerber files not yet generated)

- Silkscreen: copyright line "Copyright 2026 FerienBSD aka Marcel Sauder" and repository link github.com/MaShaoDe/RiserBoards-FT101.
- KiCad title block: company "FerienBSD aka Marcel Sauder".
- `hardware/tools/gen_riser.py` now generates V0.2. Fits on all 4 variants (checked with the RB10 preview, the narrowest board). The copyright line is scaled down on narrow boards: check legibility against the JLCPCB minimum silkscreen size before ordering.
- To do before the next batch: generate KiCad files, previews and Gerber ZIPs for RB10, RB14, RB18, RB22 and update the documentation images.

## V0.1

First release. The boards already in production keep their silkscreen as produced:
"Copyright 2026 Marcel Sauder" and github.com/MaShaoDe/HAM-Radio. The files in `hardware/riser-2x*/` are V0.1 and stay unchanged.

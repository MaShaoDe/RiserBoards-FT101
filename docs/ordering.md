# Ordering the boards

How to order bare riser boards at JLCPCB. Other makers (PCBWay, Elecrow) offer the same options under similar names.

## 1. Get the Gerber files

Either use the ready ZIP in the variant folder (for example `hardware/riser-2x18/RB18_V0.1_gerber.zip`), or export it yourself from KiCad 9:

1. Open the `.kicad_pcb` file and run the DRC (Inspect > Design Rules Checker). Expected: no errors. Three warnings "footprint library riser not found" are harmless, the footprints are stored in the board.
2. File > Fabrication Outputs > Gerbers.
3. Layers: F.Cu, B.Cu, F.Silkscreen, B.Silkscreen, F.Mask, B.Mask, Edge.Cuts.
4. Tick "Use Protel filename extensions", untick "Include netlist attributes". Click Plot.
5. In the same window: Generate Drill Files, Excellon, millimetres. The board has no holes, the drill files stay empty.
6. Pack all files into one ZIP. On a Mac leave out the `__MACOSX` folder:
   `zip -r RB18_gerber.zip . -x "__MACOSX/*" -x ".DS_Store"`

## 2. Order settings (JLCPCB)

| Setting | Value | Note |
|---|---|---|
| Base material | FR-4 | |
| Layers | 2 | |
| Dimensions | detected from the ZIP (RB18: 78 x 105 mm) | |
| PCB Qty | 5 | minimum quantity |
| Different design | 1 | |
| Delivery format | Single PCB | |
| PCB thickness | 1.6 mm | must fit the radio socket |
| PCB color | Green or Black | matt is not offered in the standard service |
| Silkscreen | White | |
| Surface finish | LeadFree HASL or ENIG | not OSP. ENIG gives flat test pads. |
| Outer copper weight | 1 oz | |
| Via covering | Tented | no vias on the board |
| Confirm production file | Yes | recommended for the first order |
| Mark on PCB | Remove Mark | keeps the silkscreen clean |
| Electrical test | Flying probe | |
| **Gold fingers** | **Yes** | hard gold on the edge fingers |
| Finger bevel | 30 degree if offered, 45 degree is fine too | |
| Castellated holes, edge plating | No | |
| PCB assembly | No | the connector is soldered by hand |

With gold fingers the price for 5 boards is roughly 20 to 40 USD plus shipping (status 2026-11).

## 3. Check before paying

In the online Gerber viewer check:

- Edge fingers on both sides without solder mask
- Traces covered by solder mask, test pads and connector pads open
- Silkscreen readable, "COMPONENT SIDE" on top, "REAR SIDE" on the bottom
- Outline: narrow finger zone at the bottom, wider upper part, rounded corners at the connector edge

## 4. Connector

Order separately, see [bom.md](bom.md). Soldering and use: [assembly.md](assembly.md).

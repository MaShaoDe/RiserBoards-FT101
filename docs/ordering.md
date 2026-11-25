# Ordering the boards

The Gerber ZIPs work with any PCB maker: JLCPCB, PCBWay, Elecrow, Aisler, your local shop, whoever you like. The boards are simple 2 layer boards; the only special option is the gold finger edge.

## 1. Pick the ZIP

| Riser | Gerber ZIP | Outline |
|---|---|---|
| RB10 | [RB10_V0.3_gerber.zip](../hardware/riser-2x10/RB10_V0.3_gerber.zip) | 47 x 105 mm |
| RB14 | [RB14_V0.3_gerber.zip](../hardware/riser-2x14/RB14_V0.3_gerber.zip) | 62 x 105 mm |
| RB18 | [RB18_V0.3_gerber.zip](../hardware/riser-2x18/RB18_V0.3_gerber.zip) | 78 x 105 mm |
| RB22 | [RB22_V0.3_gerber.zip](../hardware/riser-2x22/RB22_V0.3_gerber.zip) | 94 x 105 mm |

Each ZIP contains copper, solder mask and silkscreen for both sides, the board outline, a drill file (empty, the board has no holes) and a Gerber job file. Upload it unchanged.

## 2. Fabrication specification

This is how the V0.3 boards are made. Use the same values at any maker.

| Item | Value | Why |
|---|---|---|
| Material | FR-4 | |
| Layers | 2 | |
| Thickness | **1.6 mm** | must fit the card edge socket of the radio |
| Copper | 1 oz (35 µm) outer layers | |
| Solder mask | both sides, any colour (green or black recommended) | protects the traces |
| Silkscreen | both sides, white | |
| Surface finish | **ENIG** | flat, durable test pads; many makers require it together with gold fingers |
| Gold fingers | **yes, hard gold** on the edge fingers | many plug cycles |
| Finger bevel | **30 degrees** | slides into the socket easily |
| Outline tolerance | standard (±0.2 mm) | |
| Electrical test | yes (flying probe), if offered | |
| Order number on the board | remove, if offered | keeps the silkscreen clean |
| Assembly | none | the connector is soldered by hand |

## 3. Notes for some makers

- **JLCPCB** (as of November 2026): gold fingers can only be selected together with ENIG. Some makers bevel only from a minimum finger edge length (for example 50 mm); the RB10 finger edge is 42 mm. If the bevel is refused, order without it and break the edge by hand (see [assembly.md](assembly.md)). Choose "Confirm production file: Yes" to see the production data before the board is made.
- **Other makers**: look for options named "gold fingers", "hard gold plating", "edge connector" or "bevelling". If unsure, send the table above with your order.
- Typical cost for 5 boards with gold fingers: about 20 to 40 USD plus shipping per variant (November 2026).

## 4. Check before paying

In the online Gerber viewer:

- Edge fingers on both sides without solder mask
- Traces covered, test pads and connector pads open
- Component side: type (e.g. RB18), "RISERBOARD FOR YAESU TRANSCEIVERS", "COMPONENT SIDE", arrow, "TO RADIO"
- Rear side: small text block, "REAR SIDE", card names and github.com/MaShaoDe on the edges
- Outline: narrow finger zone at one end, wider part with rounded corners at the other

## 5. Connector

Order separately, see [bom.md](bom.md). Soldering and use: [assembly.md](assembly.md).

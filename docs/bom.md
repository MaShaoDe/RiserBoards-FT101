# Bill of materials

Short list, because a riser is mostly copper and good intentions.

## Per board

| Qty | Part | Note |
|---|---|---|
| 1 | Riser PCB (RB10, RB14, RB18 or RB22) | ordered bare, see [ordering.md](ordering.md) |
| 1 | Card edge connector, 3.96 mm (0.156") pitch, dual readout, for 1.57 mm boards | contact count see below |

## Connector

Requirements:

- Pitch 3.96 mm (0.156"), two rows (dual readout)
- Card thickness 1.57 mm nominal (1.37 to 1.78 mm)
- Gold plated contacts
- Solder tails: straight PC tails, solder eyelets or card extender tails. All work, see [assembly.md](assembly.md).
- Mounting ears are optional, they stay free beside the board.

| Riser | Contacts | Examples (check availability) |
|---|---|---|
| RB10 | 20 (2x10) | EDAC 307-020-520-20x, Sullins EBM10DRXH |
| RB14 | 28 (2x14) | not a common size, ask the distributor or the manufacturer; generic 28 pin types are offered on marketplaces |
| RB18 | 36 (2x18) | EDAC 307-036-520-201 (PC tail, gold), Sullins EBM18DRXH, EDAC 857-036-455-204 (card extender), Sullins EMPP-6156-18-DPE-1EG (card extender, eyelets) |
| RB22 | 44 (2x22) | EDAC 307-044-520-20x, Sullins EBM22DRXH |

Sources: Digikey, Mouser, Farnell, LCSC. Generic "3.96 mm edge connector 2xNN" parts from marketplaces work as well. The prototype uses such a part with straight pins (about 1 mm wide, 3.8 mm long, 3 mm gap between the rows).

Avoid tin plated contacts if you can. They work, but gold makes friends with the gold fingers of your cards for much longer.

## Consumables

- Solder, 0.5 to 0.8 mm, leaded or lead free
- Flux (no clean)
- Isopropyl alcohol for cleaning
- Optional: kapton tape to hold the connector while tacking

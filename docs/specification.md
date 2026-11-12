# Specification

Date: 2026-11-11. Sources: measurements of the original cards and the datasheet of a 3.96 mm pitch card edge connector.

## Measured data (original cards)

| Riser | Contacts | Cards | Width at connector | Length | Thickness | Pitch |
|---|---|---|---|---|---|---|
| 2x10 | 20 | PB-1292 (noise blanker unit) | 42 mm | 105 mm | 1.6 mm | 3.96 mm |
| 2x14 | 28 | PB-1184A (modulator) | 57 mm | 105 mm | 1.6 mm | 3.96 mm |
| 2x18 | 36 | PB-1181 (RF amplifier), PB-1314 (regulator) | 73 mm | 105 mm | 1.6 mm | 3.96 mm |
| 2x22 | 44 | PB-1183 (LO/IF), PB-1315A | 89 mm | 105 mm | 1.6 mm | 3.96 mm |

Further data:
- Both sides connected, soldered mounting, no coding (no notches or slots).
- Insertion depth 9 to 10 mm maximum.
- Pin tip: 1.02 mm (2x10), 1.6 mm (others). Meaning still to be clarified.
- Trace width probably 2 mm.

## Plausibility check

Contact field = (contacts per side minus 1) x 3.96 mm. The measured widths leave 2.8 to 3.2 mm margin per side.

| Riser | Contact field | Margin per side |
|---|---|---|
| 2x10 | 35.64 mm | 3.18 mm |
| 2x14 | 51.48 mm | 2.76 mm |
| 2x18 | 67.32 mm | 2.84 mm |
| 2x22 | 83.16 mm | 2.92 mm |

## Card edge connector (3.96 mm pitch)

A = overall length with ears, B = ear hole spacing (hole diameter 3.4 mm), C = contact slot length, D = housing length.

| Riser | A | B | C | D | C minus card width |
|---|---|---|---|---|---|
| 2x10 | 60.68 | 54.18 | 43.68 | 46.98 | 1.68 mm |
| 2x14 | 76.52* | 70.02* | 59.52* | 62.82* | 2.52 mm* |
| 2x18 | 92.36 | 85.86 | 75.36 | 78.66 | 2.36 mm |
| 2x22 | 108.20** | 101.70 | 91.20 | 94.50** | 2.20 mm |

\* Not in the datasheet. Calculated with A = 3.96 x contacts per side + 21.08. Measure the real part.
\** The datasheet table has A and D swapped for 44 contacts (it lists A 94.50 and D 108.20). The assignment above follows the formula and the other rows.

All card widths fit into the slot C.

## Proposed board width

The measured widths (42, 57, 73, 89 mm) are the widths of the finger zone that goes into the socket. The original cards are wider above that zone.

Finger zone: 11 mm long (insertion depth 8 to 10 mm plus 1 mm reserve), measured width. Above it: plus 5 mm in total (2.5 mm per side, confirmed), with a 45 degree step. Not wider than needed for the side labels.

| Riser | Finger zone | Upper part | Housing D | Contact field | Margin per side (finger zone / upper part) |
|---|---|---|---|---|---|
| RB10 | 42 mm | 47 mm | 46.98 mm | 35.6 mm | 3.2 / 5.7 mm |
| RB14 | 57 mm | 62 mm | 62.82 mm | 51.5 mm | 2.8 / 5.3 mm |
| RB18 | 73 mm | 78 mm | 78.66 mm | 67.3 mm | 2.8 / 5.3 mm |
| RB22 | 89 mm | 94 mm | 94.50 mm | 83.2 mm | 2.9 / 5.4 mm |

## Design decisions (2026-11-11)

| Topic | Decision |
|---|---|
| Layout | In line: the card stands straight above the riser |
| Connector | Card extender tails (straddle mount on the board edge), no mounting ears, 3.96 mm pitch, 0.25 um gold. The ear data above applies only to straight tail connectors and is kept for reference. |
| Length | 105 mm from finger tip to the end of the board that carries the connector |
| Width | Measured finger zone width in the first 11 mm, plus 5 mm in total above that |
| Test points | One solder pad per contact on both sides, in line with the connector contact. No extra ground pads: use the test pad of a ground pin. |
| Pin numbers | Not printed. The technician reads the number at the pin of the plugged card. Reason: the numbering direction differs between cards (see below) and card revisions are unknown. |
| Type names | RB10, RB14, RB18, RB22 (RB = riser board, number = contacts per side) |
| Silkscreen, centre | Large type name (e.g. RB18), line 1 "RISERBOARD FOR YAESU TRANSCEIVERS", line 2 "FT-101 B E EE EX F FE FX / SOMMERKAMP FT-277", COMPONENT SIDE with arrow towards the radio |
| Silkscreen, side edges | Rotated 90 degrees along the edge, about 1.5 mm high, at least 0.3 mm from the edge. Left: card names of the variant. Right: version, CERN-OHL-P-2.0, github.com/MaShaoDe/HAM-Radio |
| Silkscreen, back | Same content, mirrored so it reads from the back. Nothing in the finger area. |
| Insulation | Solder mask on both sides over all traces, green or black (matt is not offered in the JLCPCB standard service). Open only at fingers, connector pads and test pads. No extra lacquer needed. Protects against scratches and accidental touch at low voltage, it is not a high voltage insulation. |
| Robustness | 2 mm traces, copper at least 0.5 mm from the board edge (KiCad default), rounded corners |
| Fingers | Electroplated hard gold on nickel, 30 degree chamfer, no solder mask, pads 0.6 mm back from the tip |
| Manufacturing | Shenzhen PCB makers (JLCPCB, PCBWay), bare boards only |
| Assembly | Connectors bought from a distributor and soldered by hand by the builder. Reason: JLCPCB requires 2.5 mm from part body to board edge and has no 3.96 mm extender connector in its library. |
| Copyright notice | Copyright 2026 Marcel Sauder, CERN-OHL-P-2.0 (silkscreen) |

## Compatible radios

Plug-in cards with a single edge connector into the chassis exist in the original FT-101 series up to the F models:

- Yaesu FT-101 (Mk I, Mk II), FT-101B, FT-101E, FT-101EE, FT-101EX, FT-101F, FT-101FE, FT-101FX (BS and ES for the Japanese market)
- Sommerkamp FT-277, FT-277B, FT-277E, FT-277EE (European versions of the FT-101B and FT-101E)

Not compatible: FT-101Z and FT-101ZD (no plug-in cards). FT-901/902 use other cards (PB-17xx, PB-19xx), not checked. Early and late cards are not always interchangeable; the riser only depends on the socket size.

## Cards and pin numbering

Names from the FT-101E manual (circuit diagram). The manual numbers the pins 1 to n per module, one number per contact pair (position on both sides).

| Card | Unit | Contacts per side | Pin 1 seen from component side (finger down) |
|---|---|---|---|
| PB-1292 | noise blanker | 10 | left |
| PB-1184A | modulator and oscillator | 14 | left |
| PB-1180B | HF IF unit | 18 | not yet checked |
| PB-1181B | HF (RF) unit | 18 | right |
| PB-1314 | regulator and calibration | 18 | left |
| PB-1183B | IF unit | 22 | right |
| PB-1315A | AF unit | 22 | left |

Pin 1 positions are derived from the numbers printed on the cards (measured by the maintainer). The numbering direction differs between cards that share a riser size (2x18: PB-1181B and PB-1314, 2x22: PB-1183B and PB-1315A), which is why the risers carry no pin numbers.

PB-1180B has 36 contacts (2x18) and fits the 2x18 riser. PB-1534 (fix and RF processor unit) is in the circuit diagram but not in the manual's list of plug-in modules. For any other card, measure the width at the edge: 42, 57, 73 or 89 mm selects the matching riser.

## Limits for RF and IF cards

A riser makes the signal path about 100 mm longer. This is fine for DC, audio and level checks (regulator, AF, modulator, noise blanker). Tuned RF and IF cards (PB-1180B, PB-1181B, PB-1183B) can change their alignment or become unstable. Use the riser there for measuring supply and bias, not for aligning tuned circuits, and re-check the alignment afterwards. Measured results are welcome.

## Open questions

1. Chosen connector part for each variant (extender tail, no ears) and its pad geometry.
2. Pin 1 side of PB-1180B and whether PB-1534 is a plug-in card.
3. Confirm that the top and bottom contact of a position carry the same signal on the original cards.

## Manufacturing (proposal)

- FR4 1.6 mm, 2 layers, 1:1 straight through, carry every ground contact.
- Edge fingers: electroplated hard gold on nickel, about 0.8 to 1.3 um, 30 degree chamfer at the insertion edge, no solder mask on the fingers. ENIG is too thin for edge fingers.
- Rest of the pads: lead free HASL or ENIG.
- Insulation: solder mask (green or black) on both sides, open only at fingers, connector pads and test pads.
- Silkscreen: see design decisions.
- Order bare boards, solder the connector by hand.
- Keep traces short and parallel. Plan a re-alignment for RF and IF cards.

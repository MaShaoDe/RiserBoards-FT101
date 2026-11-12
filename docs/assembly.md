# Building and using the riser

The boards arrived from Shenzhen, they smell faintly of new PCB, and you are QRV to measure something. Here is how to get there in about half an hour.

## What you need

- The riser PCB and the matching connector (see [bom.md](bom.md))
- Soldering iron with a chisel tip, about 350 degrees C
- Solder, flux, isopropyl alcohol
- Flat nose pliers
- Magnifier and an ohmmeter (or a multimeter that beeps)

## 1. Inspect the boards

Before you heat anything, take a good look:

- Gold fingers clean, smooth and bevelled at the tip
- No solder mask on the fingers, test pads and connector pads
- Traces fully covered by solder mask
- Silkscreen readable: "COMPONENT SIDE" on top, "REAR SIDE" below

![Boards as delivered](images/01-boards-delivered.jpg)

## 2. Fit the connector

The connector sits on the top edge of the board (the end opposite the gold fingers). Its two pin rows grip the board from above and below.

1. Push the connector onto the board edge. The pins lie over the connector pads, one row on each side.
2. The gap between the rows (about 3 mm) is wider than the board (1.6 mm). Bend each row about 0.7 mm inwards with flat pliers, so the pins rest flat on the pads on both sides. Bending both rows a little keeps the connector centred. Bending one row a lot works too, but then your card leans like a tired antenna mast.
3. Check from the side: connector straight, centred on the board thickness, pins on their pads.

![Connector fitted, side view](images/02-connector-fitted.jpg)

## 3. Solder

1. Tack the two outermost pins on the component side.
2. Check the alignment once more. Now is the last cheap moment to correct it.
3. Solder all pins on the component side, then turn the board and solder the rear side.
4. Use a little flux, short heat, small fillets. The pads are big, they forgive a lot.
5. Clean off the flux with isopropyl alcohol.

![Soldered connector](images/03-soldered.jpg)

## 4. Check

- Magnifier: no bridges between neighbouring pins.
- Ohmmeter: every gold finger to its connector contact, top and bottom separately. Beep. And no beep to the neighbour.
- A riser with a short circuit is a great way to find out how good the fuses in your radio are. Better check now.

## 5. Use

1. **Switch the radio off and pull the mains plug.** The FT-101 has high voltage in the PA section and it does not care that you are only "quickly checking".
2. Pull the card out of its socket. Note which way the component side faces.
3. Plug the riser into the socket with **COMPONENT SIDE** facing the same direction as the component side of the card. The arrow points towards the radio.
4. Plug the card into the riser, same orientation.
5. Switch on and measure. Each test pad belongs to one contact, top pads to the top contacts, rear pads to the rear contacts.
6. Pin numbers are not printed on the riser. The cards number their pins in different directions, so read the number on the card and count along.

![Riser in use in an FT-101](images/04-in-use.jpg)

## Good to know

- RF and IF cards (PB-1180B, PB-1181B, PB-1183B): measure voltages and levels with the riser, do the fine alignment without it.
- Do not use the riser as a permanent extension. It is a service tool.
- The edge fingers are gold, but not immortal. Plug gently, and put the riser back in its bag when you are done.

Found a mistake or a better way? Open an issue. Photos of your riser at work are very welcome.

Good luck on the bench, and see you on the bands. 73!

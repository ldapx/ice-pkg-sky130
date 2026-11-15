# SkyWater SKY130 package

This package provides the SkyWater SKY130 130 nm CMOS open-source PDK
definition for ICE. It points to the upstream PDK repository:

<https://github.com/google/skywater-pdk>

The package also contains the Sky130 ngspice simulation subset under
`libs.tech/ngspice` and `libs.ref/sky130_fd_pr/spice`, plus the
`sky130_fd_sc_hd` standard-cell implementation set under `implementation/`.
Simulation and physical implementation depend only on this ICE package, not on
Volare, CIEL, `PDK_ROOT`, or an external OpenROAD-flow-scripts checkout.

## PDK metadata

The package declares the main SKY130 drawing layers in `package.toml` under
`[pdk]`. ICE uses these layers when the package technology is activated for a
project. The default schematic name is `sky130_top`.

## Schematic symbols

The package ships sidecar definitions for core SKY130 devices:

- 1.8 V NMOS and PMOS
- 5.0 V NPN
- 5.5 V diode
- Poly resistor
- MIM capacitor

The sidecars reference ICE's shared artwork with `generic:<file>.svg`, so the
package does not include duplicate SVG files.

## Layout PCells

The package ships ICE-native PCell replicas under `layout/`:

- `layout/pcells.py` implements the SKY130 PCell families with the
  `icepy.pcells` layout builder API (MOS, BJT, resistors, capacitors, diodes,
  RF devices, via stacks, and guard rings).
- `layout/devices.json` indexes the device library used by the Devices panel.
  Every device is a real layout cell stored as
  `layout/devices/<name>.icelay`; the index carries categories and generator
  bindings.
- `layout/device_generator.py` regenerates geometry when a parameter changes.
- `layout/generate_devices.py` rebuilds the library from the PCell definitions.

The device library also records the SKY130 purpose datatypes (`drawing` uses
datatype 20; `pin`, `label`, `boundary`, `net`, `blockage`, and marker purposes
use their PDK datatypes). ICE groups these under their base layer number and
keeps non-drawing purposes hidden by default.

The PCells do not require KLayout, gdsfactory, Volare, CIEL, or `PDK_ROOT`.
Regenerate the library after editing `layout/pcells.py`:

```text
PYTHONPATH=<ice>/build/linux/x86_64/release:<ice>/python \
  python3 layout/generate_devices.py
```

## Physical implementation

`package.toml` declares explicit implementation data for the high-density
`sky130_fd_sc_hd` standard-cell library:

- `implementation/lef/` — technology LEF and merged cell LEF;
- `implementation/lib/` — `tt_025C_1v80` Liberty;
- `implementation/gds/` — merged standard-cell GDS and the KLayout DEF-to-GDS
  layer map;
- `implementation/rcx/` — nominal OpenRCX extraction rules;
- `implementation/tapcell.tcl` and `implementation/pdn.tcl` — tapcell and
  best-effort power-grid hooks used during floorplan.

The default placement site is `unithd` and the default corner is `tt`. No
`OPENROAD_FLOW_SCRIPTS` environment variable is needed.

## Simulation

The package declares `[pdk.simulation]` in `package.toml`: `.option scale=1u`,
`sky130.lib.spice`, section `tt`, and the Sky130 NMOS/PMOS device names. Verify
with `ice-cli pdk-info sky130A --probe`.

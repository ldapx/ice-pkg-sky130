# SkyWater SKY130 package

This package provides the SkyWater SKY130 130 nm CMOS open-source PDK
definition for ICE. It points to the upstream PDK repository:

<https://github.com/google/skywater-pdk>

The package also contains the Sky130 ngspice simulation subset under
`simulation/ngspice` (including the device models in
`simulation/ngspice/models`), plus the `sky130_fd_sc_hd` standard-cell
implementation set under `implementation/`.
Simulation and physical implementation depend only on this ICE package, not on
Volare, CIEL, `PDK_ROOT`, or an external OpenROAD-flow-scripts checkout.

## PDK metadata

The package declares a 5 nm manufacturing grid (`manufacturing_grid = 5`).
ICE uses it as the default layout grid for new layouts.

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

The package ships ICE-native PCell replicas under `layout/devices/`:

- `layout/devices/pcell/pcells.py` implements the SKY130 PCell families with the
  `icepy.pcells` layout builder API (MOS, BJT, resistors, capacitors, diodes,
  RF devices, via stacks, and guard rings).
- `layout/devices/index.json` indexes the parameterized device library used by
  the Devices panel. These PCells are implemented by
  `layout/devices/pcell/pcells.py` and `layout/devices/generator.py`, so they
  have no stored geometry snapshot. Fixed devices, when present, are stored as
  `layout/devices/fixed/*.icelay`.
- `layout/devices/generator.py` regenerates geometry when a parameter changes.
- `layout/devices/build.py` rebuilds the index from the PCell definitions.

The device library also records the SKY130 purpose datatypes (`drawing` uses
datatype 20; `pin`, `label`, `boundary`, `net`, `blockage`, and marker purposes
use their PDK datatypes). ICE groups these under their base layer number and
keeps non-drawing purposes hidden by default.

The PCells do not require KLayout, gdsfactory, Volare, CIEL, or `PDK_ROOT`.
Regenerate the library after editing `layout/devices/pcell/pcells.py`:

```text
PYTHONPATH=<ice>/build/linux/x86_64/release:<ice>/python \
  python3 layout/devices/build.py
```

## Physical implementation

`package.toml` declares explicit implementation data for the high-density
`sky130_fd_sc_hd` standard-cell library:

- `implementation/common/cells.lef` — merged cell LEF;
- `implementation/common/lib/tt.lib.gz` — `tt_025C_1v80` Liberty;
- `implementation/common/stdcells.gds` — merged standard-cell GDS;
- `implementation/common/layer.map` — KLayout DEF-to-GDS layer map;
- `implementation/common/scripts/tapcell.tcl` and
  `implementation/common/scripts/pdn.tcl` — tapcell and best-effort power-grid
  hooks used during floorplan;
- `implementation/stacks/default/tech.lef` and `rcx.rules` — technology LEF and
  nominal OpenRCX extraction rules.

The default placement site is `unithd` and the default corner is `tt`. No
`OPENROAD_FLOW_SCRIPTS` environment variable is needed.

## Simulation

The package declares `[pdk.simulation]` in `package.toml`: `.option scale=1u`,
`sky130.lib.spice`, section `tt`, and the Sky130 NMOS/PMOS device names. Verify
with `ice-cli pdk-info sky130A --probe`.

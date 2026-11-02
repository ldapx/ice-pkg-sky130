# SkyWater SKY130 package

This package provides the SkyWater SKY130 130 nm CMOS open-source PDK
definition for ICE. It points to the upstream PDK repository:

<https://github.com/google/skywater-pdk>

The package also contains the Sky130 ngspice simulation subset under
`libs.tech/ngspice` and `libs.ref/sky130_fd_pr/spice`. Simulation depends only
on this ICE package, not on Volare, CIEL, or `PDK_ROOT`.

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
- `layout/devices.json` is the generated ICE layout device library used by the
  Devices panel. It contains default geometry, parameter metadata, and
  generator bindings.
- `layout/device_generator.py` regenerates geometry when a parameter changes.
- `layout/generate_devices.py` rebuilds the library from the PCell definitions.

The PCells do not require KLayout, gdsfactory, Volare, CIEL, or `PDK_ROOT`.
Regenerate the library after editing `layout/pcells.py`:

```text
PYTHONPATH=<ice>/build/linux/x86_64/release:<ice>/python \
  python3 layout/generate_devices.py
```

## Simulation

The package declares `[pdk.simulation]` in `package.toml`: `.option scale=1u`,
`sky130.lib.spice`, section `tt`, and the Sky130 NMOS/PMOS device names. Verify
with `ice-cli pdk-info sky130A --probe`.

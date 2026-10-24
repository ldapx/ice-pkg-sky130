# SkyWater SKY130 package

This package provides the SkyWater SKY130 130 nm CMOS open-source PDK
definition for ICE. It points to the upstream PDK repository:

<https://github.com/google/skywater-pdk>

The upstream PDK is treated as an external package source and remains subject
to its own Apache-2.0 license, installation prerequisites, and verification
status.

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

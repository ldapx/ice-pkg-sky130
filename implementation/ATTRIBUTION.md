# Implementation data attribution

The files under `implementation/lef`, `implementation/lib`,
`implementation/gds`, `implementation/rcx`, `implementation/tapcell.tcl`, and
`implementation/pdn.tcl` are derived from the SkyWater SKY130 open-source PDK
and the OpenROAD-flow-scripts SKY130 HD platform.

- SkyWater SKY130 PDK / open_pdks: https://github.com/google/skywater-pdk
  and https://github.com/RTimothyEdwards/open_pdks (Apache-2.0)
- OpenROAD-flow-scripts: https://github.com/The-OpenROAD-Project/OpenROAD-flow-scripts
  (Apache-2.0)

The `sky130A.map` file is the SKY130 KLayout DEF-to-GDS layer map.

They are bundled with this ICE package so the physical implementation flow does
not depend on an external `OPENROAD_FLOW_SCRIPTS` checkout or a Volare install.

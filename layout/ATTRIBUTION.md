# Layout PCell attribution

The PCell definitions in `pcells.py` are ICE-native replicas of the SkyWater
SKY130 device generators. Layer numbers and device names follow the
open-source SKY130 PDK:

- Project: SkyWater PDK / open_pdks
- Source: https://github.com/google/skywater-pdk
- License: Apache-2.0

The geometry is produced entirely by the ICE `icepy.pcells` layout builder.
`devices.json` is generated from these definitions and contains default
parameter values and flattened polygons for the Devices panel.

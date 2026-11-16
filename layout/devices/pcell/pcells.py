"""SkyWater SKY130 PCells implemented with the ICE layout API.

The classes in this module are package-local replicas of the core SKY130
devices. They only depend on ``icepy.pcells`` (the ICE layout builder runtime),
so ICE can generate, edit, and preview them without KLayout, gdsfactory, or a
global PDK installation.
"""

from __future__ import annotations

from icepy import pcells


PDK = "sky130A"

LAYERS = {
    "nwell": ("nwell.drawing", 64, 20),
    "pwell": ("pwell.drawing", 64, 44),
    "diff": ("diff.drawing", 65, 20),
    "tap": ("tap.drawing", 65, 44),
    "poly": ("poly.drawing", 66, 20),
    "licon1": ("licon1.drawing", 66, 44),
    "li1": ("li1.drawing", 67, 20),
    "mcon": ("mcon.drawing", 67, 44),
    "met1": ("met1.drawing", 68, 20),
    "via": ("via.drawing", 68, 44),
    "met2": ("met2.drawing", 69, 20),
    "via2": ("via2.drawing", 69, 44),
    "met3": ("met3.drawing", 70, 20),
    "via3": ("via3.drawing", 70, 44),
    "met4": ("met4.drawing", 71, 20),
    "via4": ("via4.drawing", 71, 44),
    "met5": ("met5.drawing", 72, 20),
    "pad": ("pad.drawing", 76, 20),
    "capm": ("capm.drawing", 89, 44),
    "cap2m": ("cap2m.drawing", 97, 44),
    "nsdm": ("nsdm.drawing", 93, 44),
    "psdm": ("psdm.drawing", 94, 20),
    "npc": ("npc.drawing", 95, 20),
}

# Additional PDK purposes exposed in the Layers panel. The base drawing
# layers above are used by the PCell templates; these entries document the
# remaining GDS datatypes from the SKY130 layer map.
EXTRA_LAYER_STREAMS = [
    ("nwell.pin", 64, 16),
    ("nwell.label", 64, 5),
    ("diff.pin", 65, 16),
    ("diff.label", 65, 6),
    ("diff.boundary", 65, 4),
    ("diff.res", 65, 13),
    ("diff.cut", 65, 14),
    ("diff.hv", 65, 8),
    ("diff.net", 65, 23),
    ("poly.pin", 66, 16),
    ("poly.label", 66, 5),
    ("poly.boundary", 66, 4),
    ("poly.res", 66, 13),
    ("poly.cut", 66, 14),
    ("poly.gate", 66, 9),
    ("poly.short", 66, 15),
    ("poly.net", 66, 23),
    ("poly.probe", 66, 25),
    ("poly.model", 66, 83),
    ("li1.pin", 67, 16),
    ("li1.label", 67, 5),
    ("li1.boundary", 67, 4),
    ("li1.blockage", 67, 10),
    ("li1.res", 67, 13),
    ("li1.cut", 67, 14),
    ("li1.short", 67, 15),
    ("li1.net", 67, 23),
    ("li1.probe", 67, 25),
    ("met1.pin", 68, 16),
    ("met1.label", 68, 5),
    ("met1.boundary", 68, 4),
    ("met1.blockage", 68, 10),
    ("met1.res", 68, 13),
    ("met1.cut", 68, 14),
    ("met1.short", 68, 15),
    ("met1.net", 68, 23),
    ("met1.probe", 68, 25),
    ("met2.pin", 69, 16),
    ("met2.label", 69, 5),
    ("met2.boundary", 69, 4),
    ("met2.blockage", 69, 10),
    ("met2.res", 69, 13),
    ("met2.cut", 69, 14),
    ("met2.short", 69, 15),
    ("met2.net", 69, 23),
    ("met2.probe", 69, 25),
    ("met3.pin", 70, 16),
    ("met3.label", 70, 5),
    ("met3.boundary", 70, 4),
    ("met3.blockage", 70, 10),
    ("met3.res", 70, 13),
    ("met3.cut", 70, 14),
    ("met3.short", 70, 15),
    ("met3.net", 70, 23),
    ("met3.probe", 70, 25),
    ("met3.fuse", 70, 17),
    ("met4.pin", 71, 16),
    ("met4.label", 71, 5),
    ("met4.boundary", 71, 4),
    ("met4.blockage", 71, 10),
    ("met4.res", 71, 13),
    ("met4.cut", 71, 14),
    ("met4.short", 71, 15),
    ("met4.net", 71, 23),
    ("met4.probe", 71, 25),
    ("met4.fuse", 71, 17),
    ("met5.pin", 72, 16),
    ("met5.label", 72, 5),
    ("met5.boundary", 72, 4),
    ("met5.blockage", 72, 10),
    ("met5.res", 72, 13),
    ("met5.cut", 72, 14),
    ("met5.short", 72, 15),
    ("met5.net", 72, 23),
    ("met5.probe", 72, 25),
    ("met5.fuse", 72, 17),
    ("pad.pin", 76, 16),
    ("pad.label", 76, 5),
]


def parameter(name: str, value: str, description: str) -> dict[str, str]:
    return {"name": name, "value": value, "description": description}


MOS_PARAMETERS = [
    parameter("model", "sky130_fd_pr__nfet_01v8", "Device model"),
    parameter("w", "1u", "Width"),
    parameter("l", "0.15u", "Length"),
    parameter("nf", "1", "Number of fingers"),
    parameter("m", "1", "Multiplier"),
    parameter("bulk", "None", "Bulk connection"),
    parameter("guard_ring", "false", "Draw a guard ring"),
]

PASSIVE_PARAMETERS = [
    parameter("model", "sky130_fd_pr__res_high_po", "Device model"),
    parameter("w", "0.5u", "Width"),
    parameter("l", "2u", "Length"),
    parameter("resistance", "1k", "Target resistance"),
]

CAP_PARAMETERS = [
    parameter("model", "sky130_fd_pr__cap_mim_m3_1", "Device model"),
    parameter("w", "2u", "Plate width"),
    parameter("h", "2u", "Plate height"),
    parameter("l", "2u", "Plate length"),
]

DIODE_PARAMETERS = [
    parameter("model", "sky130_fd_pr__diode_pw2nd_05v5", "Device model"),
    parameter("w", "2u", "Anode width"),
    parameter("h", "2u", "Anode height"),
]

BJT_PARAMETERS = [
    parameter("model", "sky130_fd_pr__npn_05v5_W1p00L1p00", "Device model"),
    parameter("w", "1u", "Base width"),
    parameter("l", "1u", "Base length"),
]

VIA_PARAMETERS = [
    parameter("w", "1u", "Via stack width"),
    parameter("h", "1u", "Via stack height"),
]

RING_PARAMETERS = [
    parameter("w", "20u", "Guard ring width"),
    parameter("h", "20u", "Guard ring height"),
]

COIL_PARAMETERS = [
    parameter("turns", "2", "Number of turns"),
    parameter("pitch", "2u", "Turn pitch"),
    parameter("w", "1u", "Trace width"),
]


class _SkyPcell(pcells.PackagePcell):
    pdk = PDK
    layers = LAYERS


class nfet(_SkyPcell):
    name = "nfet"
    category = "Transistors"
    family = "mos"
    parameters = MOS_PARAMETERS


class pfet(_SkyPcell):
    name = "pfet"
    category = "Transistors"
    family = "mos"
    pmos = True
    parameters = [
        parameter("model", "sky130_fd_pr__pfet_01v8", "Device model"),
        *MOS_PARAMETERS[1:],
    ]


class npn_bjt(_SkyPcell):
    name = "npn_bjt"
    category = "Bipolar"
    family = "bjt"
    doping = "n"
    parameters = BJT_PARAMETERS


class pnp_bjt(_SkyPcell):
    name = "pnp_bjt"
    category = "Bipolar"
    family = "bjt"
    doping = "p"
    parameters = [
        parameter("model", "sky130_fd_pr__pnp_05v5_W0p68L0p68", "Device model"),
        *BJT_PARAMETERS[1:],
    ]


class res_poly(_SkyPcell):
    name = "res_poly"
    category = "Passives"
    family = "resistor"
    body_layer = "poly"
    res_layer = "poly.res"
    doping = "n"
    parameters = PASSIVE_PARAMETERS


class res_diff(_SkyPcell):
    name = "res_diff"
    category = "Passives"
    family = "resistor"
    body_layer = "diff"
    res_layer = "diff.res"
    doping = "n"
    parameters = PASSIVE_PARAMETERS


class res_metal(_SkyPcell):
    name = "res_metal"
    category = "Passives"
    family = "resistor"
    body_layer = "met1"
    res_layer = "met1.res"
    doping = ""
    parameters = PASSIVE_PARAMETERS


class mim_cap(_SkyPcell):
    name = "mim_cap"
    category = "Passives"
    family = "mim_cap"
    cap_bottom = "met1"
    cap_top = "met2"
    cap_marker = "capm"
    parameters = CAP_PARAMETERS


class cap_vpp(_SkyPcell):
    name = "cap_vpp"
    category = "Passives"
    family = "vpp_cap"
    parameters = CAP_PARAMETERS


class cap_var(_SkyPcell):
    name = "cap_var"
    category = "Passives"
    family = "var_cap"
    parameters = CAP_PARAMETERS


class photo_diode(_SkyPcell):
    name = "photo_diode"
    category = "Diodes"
    family = "diode"
    doping = "n"
    parameters = DIODE_PARAMETERS


class n_diode(_SkyPcell):
    name = "n_diode"
    category = "Diodes"
    family = "diode"
    doping = "n"
    parameters = DIODE_PARAMETERS


class p_diode(_SkyPcell):
    name = "p_diode"
    category = "Diodes"
    family = "diode"
    doping = "p"
    parameters = [
        parameter("model", "sky130_fd_pr__diode_pd2nw_05v5", "Device model"),
        *DIODE_PARAMETERS[1:],
    ]


class rf_mosfet(_SkyPcell):
    name = "rf_mosfet"
    category = "RF"
    family = "mos"
    guard_ring = True
    parameters = MOS_PARAMETERS


class rf_bjt(_SkyPcell):
    name = "rf_bjt"
    category = "RF"
    family = "bjt"
    doping = "n"
    parameters = BJT_PARAMETERS


class rf_coils(_SkyPcell):
    name = "rf_coils"
    category = "RF"
    family = "spiral"
    parameters = COIL_PARAMETERS


class vias_gen(_SkyPcell):
    name = "vias_gen"
    category = "Via Stacks"
    family = "via_stack"
    stack_layers = ("met1", "met2", "met3", "met4", "met5")
    parameters = VIA_PARAMETERS


class guard_ring_gen(_SkyPcell):
    name = "guard_ring_gen"
    category = "Guard Rings"
    family = "guard_ring_cell"
    parameters = RING_PARAMETERS


PCELLS = [
    nfet,
    pfet,
    npn_bjt,
    pnp_bjt,
    res_poly,
    res_diff,
    res_metal,
    mim_cap,
    cap_vpp,
    cap_var,
    photo_diode,
    n_diode,
    p_diode,
    rf_mosfet,
    rf_bjt,
    rf_coils,
    vias_gen,
    guard_ring_gen,
]

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
    "nwell": ("nwell", 64),
    "diff": ("diff", 65),
    "poly": ("poly", 66),
    "li1": ("li1", 67),
    "met1": ("met1", 68),
    "met2": ("met2", 69),
    "met3": ("met3", 70),
    "met4": ("met4", 71),
    "met5": ("met5", 72),
    "pad": ("pad", 76),
    "capm": ("capm", 89),
    "cap2m": ("cap2m", 97),
    "res": ("res", 65),
}


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
    parameter("model", "sky130_fd_pr__npn_05v5", "Device model"),
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
    doping = "n"
    parameters = PASSIVE_PARAMETERS


class res_diff(_SkyPcell):
    name = "res_diff"
    category = "Passives"
    family = "resistor"
    body_layer = "diff"
    doping = "n"
    parameters = PASSIVE_PARAMETERS


class res_metal(_SkyPcell):
    name = "res_metal"
    category = "Passives"
    family = "resistor"
    body_layer = "met1"
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

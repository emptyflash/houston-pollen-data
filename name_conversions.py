scientific_to_common = {
    # Tree
    "Acer": "Maple",
    "Morus": "Mulberry",
    "Alnus": "Alder",
    "Pinaceae": "Pine",
    "Betula": "Birch",
    "Platanus": "Sycamore",
    "Carya": "Hickory, Pecan",
    "Populus": "Cottonwood",
    "Celtis": "Hackberry",
    "Quercus": "Oak",
    "Corylus": "Hazelnut",
    "Salix": "Willow",
    "Cupressaceae": "Cedar",
    "Tilia": "Linden",
    "Fraxinus": "Ashe Juniper / Bald Cypress",
    "Ulmus": "Elm",
    "Juglans": "Walnut",
    "Liquidamber": "Sweet Gum",

    # Weed/Grass
    "Ambrosia": "Ragweed",
    "Plantago": "Plantain",
    "Artemeisia": "Sage",
    "Rumex": "Sheep",
    "Asteraceae": "Aster",
    "Typha": "Cattail",
    "Amaranthaceae": "Amaranth",
    "Urticaceae": "Nettle",
    "Cyperaceae": "Sedge",
}

common_to_scientific = { v: k for k, v in scientific_to_common.items() }

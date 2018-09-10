"""Turn old defaults into [none]. Run in mudbot-discord directory."""

import os
import json

dirs = os.listdir("userdata")

defaults = ["Fedora of Staunch Odor",
            "\"Eat. Sleep. Play Fortnite.\" T-Shirt of Purity",
            "Fingerless Gloves of Dexterity",
            "Minor Cargo Shorts of Celibacy",
            "Combat Boots of Charm Resistance",
            "Hatsune Miku Vintage Body Pillow (quality: used)",
            "Word of Power Learned: Repel, Attractive Woman",
            "Empowered Nintendo 3DS of Pokemon Husbandry"]

for filename in dirs:
    if not filename.endswith(".json"):
        continue

    with open("userdata/{}".format(filename)) as f:
        data = json.load(f)

    for slot in data["chest"]["loadout"]:
        if data["chest"]["loadout"][slot] in defaults:
            data["chest"]["loadout"][slot] = "[none]"

    with open("userdata/{}".format(filename), "w") as f:
        json.dump(data, f)

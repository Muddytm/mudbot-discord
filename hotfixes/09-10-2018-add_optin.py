"""Add optin = True to all userdata. Run in mudbot-discord directory.

Can also be used to make everyone opt in to Chest again."""

import os
import json

dirs = os.listdir("userdata")

for filename in dirs:
    if not filename.endswith(".json"):
        continue

    with open("userdata/{}".format(filename)) as f:
        data = json.load(f)

    if "chest" in data:
        data["chest"]["optin"] = True

    with open("userdata/{}".format(filename), "w") as f:
        json.dump(data, f)

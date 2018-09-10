"""Return an object from TES_ItemsBot. Requires a key."""

import os

if not os.path.isfile("configs/chest_config.py"):
    with open("configs/chest_config.py", "w") as f:
        f.write("CONSUMER_KEY = \"\"\n"
                "CONSUMER_SECRET = \"\"\n"
                "ACCESS_TOKEN_KEY = \"\"\n"
                "ACCESS_TOKEN_SECRET = \"\"\n"
                "key_counter_threshold = \"30\"")

import configs.chest_config as config
import json
import random
import twitter

api = twitter.Api(consumer_key=config.CONSUMER_KEY,
                  consumer_secret=config.CONSUMER_SECRET,
                  access_token_key=config.ACCESS_TOKEN_KEY,
                  access_token_secret=config.ACCESS_TOKEN_SECRET)

dirs = os.listdir("mudules/items_glossary")
glossary = {}
for filename in dirs:
    glossary[filename.replace(".txt", "")] = []
    with open("mudules/items_glossary/{}".format(filename)) as f:
        lines = f.readlines()
        for line in lines:
            if line.strip():
                glossary[filename.replace(".txt", "")].append(line.strip())


def clean(name):
    """Cleans name of ASCII values for storage."""
    for ch in name:
        if ord(ch) < 34 or ord(ch) > 127:
            name = name.replace(ch, "")

    return name


def chest(ctx):
    """Query TES_ItemsBot."""
    name = clean(ctx.message.author.name)
    name_full = ctx.message.author.name
    id = ctx.message.author.id

    try:
        search = api.GetUserTimeline(screen_name="TES_ItemsBot", count=200)
    except twitter.error.TwitterError as e:
        return ("Twitter error: {}".format(e))
    except Exception as e:
        return ("I AM ERROR, BEEP BOOP:\n```{}```".format(e.message))

    with open("userdata/{}_{}.json".format(name, id)) as f:
        data = json.load(f)

    if data["chest"]["keys"] > 0:
        data["chest"]["keys"] -= 1

        item_list = []
        for tweet in search:
            item_list.append(tweet.text)

        found_item = random.choice(item_list)

        with open("userdata/{}_{}.json".format(name, id), "w") as f:
            json.dump(data, f)

        slot = equip(found_item, name, id)
        return ("{} found...{}!\nIt was equipped to your \"{}\" slot. "
                "Type !loadout to check it out.".format(name_full, found_item,
                                                        slot))
    else:
        return ("{} has no keys to open the chest with.".format(name_full))


def chest_key(message):
    """Increment the counter, and if the counter is high enough, get a key!"""
    name = clean(message.author.name)
    name_full = message.author.name
    id = message.author.id

    try:
        int(config.key_counter_threshold)
    except ValueError:
        return ("The chest angrily snaps at you, revealing it to be a mimic. "
                "Have your admins fix the configuration settings to defeat "
                "this menace.")

    with open("userdata/{}_{}.json".format(name, id)) as f:
        data = json.load(f)

    if "chest" not in data:
        data["chest"] = {}
        data["chest"]["key_counter"] = 0
        data["chest"]["keys"] = 0
        data["chest"]["optin"] = True
        data["chest"]["loadout"] = {}
        data["chest"]["loadout"]["head"] = "[none]" #"Fedora of Staunch Odor"
        data["chest"]["loadout"]["chest"] = "[none]" #"\"Eat. Sleep. Play Fortnite.\" T-Shirt of Purity"
        data["chest"]["loadout"]["arms"] = "[none]" #"Fingerless Gloves of Dexterity"
        data["chest"]["loadout"]["legs"] = "[none]" #"Minor Cargo Shorts of Celibacy"
        data["chest"]["loadout"]["feet"] = "[none]" #"Combat Boots of Charm Resistance"
        data["chest"]["loadout"]["weapon"] = "[none]" #"Hatsune Miku Vintage Body Pillow (quality: used)"
        data["chest"]["loadout"]["spell"] = "[none]" #"Word of Power Learned: Repel, Attractive Woman"
        data["chest"]["loadout"]["trinket"] = "[none]" #"Empowered Nintendo 3DS of Pokemon Husbandry"

    new_key = False
    if data["chest"]["key_counter"] < (int(config.key_counter_threshold) - 1):
        data["chest"]["key_counter"] += 1
    else:
        data["chest"]["key_counter"] = 0
        data["chest"]["keys"] += 1
        new_key = True

    with open("userdata/{}_{}.json".format(name, id), "w") as f:
        json.dump(data, f)

    if new_key:
        return ("{} got a key! Type !chest to use it.".format(name_full))
    else:
        return ("")


def equip(found_item, name, id):
    """Equip user with new item."""
    slot = determine_slot(found_item)
    with open("userdata/{}_{}.json".format(name, id)) as f:
        data = json.load(f)

    data["chest"]["loadout"][slot] = found_item

    with open("userdata/{}_{}.json".format(name, id), "w") as f:
        json.dump(data, f)

    return slot


def determine_slot(found_item):
    """Determine whether the item is:
    a) Armor
        - head
        - chest
        - arms
        - legs
        - feet
    b) Weapon/Misc
        - weapon
        - spell
        - trinket
    """
    found_item = found_item.lower()
    if "potion" in found_item:
        return "trinket"
    elif "word of power" in found_item or "spell tome" in found_item:
        return "spell"

    for slot in glossary:
        for item in glossary[slot]:
            if item in found_item:
                return slot

    return "trinket"


def display_loadout(name, id):
    """Return loadout string."""
    with open("userdata/{}_{}.json".format(name, id)) as f:
        data = json.load(f)

    loadout = ""

    # I do this inefficiently because I want it ordered this way.
    # This isn't really scalable, but AESTHETICS BRO
    loadout += "HEAD.......{}\n".format(data["chest"]["loadout"]["head"])
    loadout += "CHEST......{}\n".format(data["chest"]["loadout"]["chest"])
    loadout += "ARMS.......{}\n".format(data["chest"]["loadout"]["arms"])
    loadout += "LEGS.......{}\n".format(data["chest"]["loadout"]["legs"])
    loadout += "FEET.......{}\n".format(data["chest"]["loadout"]["feet"])
    loadout += "WEAPON.....{}\n".format(data["chest"]["loadout"]["weapon"])
    loadout += "SPELL......{}\n".format(data["chest"]["loadout"]["spell"])
    loadout += "TRINKET....{}".format(data["chest"]["loadout"]["trinket"])

    return ("```{}```".format(loadout))


def chest_optout(name, id):
    """Opt out of Chest."""
    with open("userdata/{}_{}.json".format(name, id)) as f:
        data = json.load(f)

    data["chest"]["optin"] = False

    with open("userdata/{}_{}.json".format(name, id), "w") as f:
        json.dump(data, f)


def chest_optin(name, id):
    """Opt in to Chest."""
    with open("userdata/{}_{}.json".format(name, id)) as f:
        data = json.load(f)

    data["chest"]["optin"] = True

    with open("userdata/{}_{}.json".format(name, id), "w") as f:
        json.dump(data, f)

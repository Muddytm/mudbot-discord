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

#dirs = os.listdir()
#with open("mudules/")


def chest(ctx):
    """Query TES_ItemsBot."""
    name = ctx.message.author.name.replace(" ", "")
    name_full = ctx.message.author.name
    id = ctx.message.author.id

    try:
        search = api.GetSearch("TES_ItemsBot")
    except twitter.error.TwitterError:
        return ("The configuration file for this plugin is empty! Bug the admins to fix it.")
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

        equip(found_item, name, id)
        return ("{} found...{}!".format(name_full, found_item))
    else:
        return ("{} has no keys to open the chest with.".format(name_full))


def chest_key(message):
    """Increment the counter, and if the counter is high enough, get a key!"""
    try:
        int(config.key_counter_threshold)
    except ValueError:
        return ("The chest angrily snaps at you, revealing it to be a mimic. "
                "Have your admins fix the configuration settings to defeat "
                "this menace.")

    with open("userdata/{}_{}.json".format(message.author.name.replace(" ", ""), message.author.id)) as f:
        data = json.load(f)

    if "chest" not in data:
        data["chest"] = {}
        data["chest"]["key_counter"] = 0
        data["chest"]["keys"] = 0
        data["chest"]["loadout"] = {}
        data["chest"]["loadout"]["head"] = "Fedora of Staunch Odor"
        data["chest"]["loadout"]["chest"] = "\"Eat. Sleep. Play Fortnite.\" T-Shirt of Purity"
        data["chest"]["loadout"]["arms"] = "Fingerless Gloves of Dexterity"
        data["chest"]["loadout"]["legs"] = "Minor Cargo Shorts of Celibacy"
        data["chest"]["loadout"]["feet"] = "Combat Boots of Charm Resistance"
        data["chest"]["loadout"]["weapon"] = "Hatsune Miku Vintage Body Pillow (quality: used)"
        data["chest"]["loadout"]["spell"] = "Word of Power Learned: Repel, Attractive Woman"
        data["chest"]["loadout"]["trinket"] = "Empowered Nintendo 3DS of Pokemon Husbandry"

    new_key = False
    if data["chest"]["key_counter"] < (int(config.key_counter_threshold) - 1):
        data["chest"]["key_counter"] += 1
    else:
        data["chest"]["key_counter"] = 0
        data["chest"]["keys"] += 1
        new_key = True

    with open("userdata/{}_{}.json".format(message.author.name.replace(" ", ""), message.author.id), "w") as f:
        json.dump(data, f)

    if new_key:
        return ("{} got a key! Type !chest to use it.".format(message.author.name))
    else:
        return ("")


def equip(found_item, name, id):
    """Equip user with new item."""
    slot = determine_slot(found_item)


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

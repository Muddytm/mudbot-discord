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


def chest(ctx):
    """Query TES_ItemsBot."""
    try:
        search = api.GetSearch("TES_ItemsBot")
    except twitter.error.TwitterError:
        return ("The configuration file for this plugin is empty! Bug the admins to fix it.")
    except Exception as e:
        return ("I AM ERROR, BEEP BOOP:\n```{}```".format(e.message))

    with open("userdata/{}_{}.json".format(ctx.message.author.name.replace(" ", ""), ctx.message.author.id)) as f:
        data = json.load(f)

    if data["chest"]["keys"] > 0:
        data["chest"]["keys"] -= 1

        item_list = []
        for tweet in search:
            item_list.append(tweet.text)

        found_item = random.choice(item_list)

        with open("userdata/{}_{}.json".format(ctx.message.author.name.replace(" ", ""), ctx.message.author.id), "w") as f:
            json.dump(data, f)

        return ("{} found...{}!".format(ctx.message.author.name, found_item))
    else:
        return ("{} has no keys to open the chest with.".format(ctx.message.author.name))


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

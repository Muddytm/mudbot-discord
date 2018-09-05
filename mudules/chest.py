"""Return an object from TES_ItemsBot. In later functionality, this will require a key."""

import os

if not os.path.isfile("configs/chest_config.py"):
    with open("configs/chest_config.py", "w") as outfile:
        outfile.write("CONSUMER_KEY = \"\"\n"
                      "CONSUMER_SECRET = \"\"\n"
                      "ACCESS_TOKEN_KEY = \"\"\n"
                      "ACCESS_TOKEN_SECRET = \"\"\n")

import configs.chest_config as config
import twitter
import random

api = twitter.Api(consumer_key=config.CONSUMER_KEY,
                  consumer_secret=config.CONSUMER_SECRET,
                  access_token_key=config.ACCESS_TOKEN_KEY,
                  access_token_secret=config.ACCESS_TOKEN_SECRET)

def chest():
    """Query TES_ItemsBot."""
    try:
        search = api.GetSearch("TES_ItemsBot")
    except twitter.error.TwitterError:
        return ("nothing. The configuration file for this plugin is empty")
    except Exception as e:
        return ("an error! Error message: {}".format(e.message))

    item_list = []
    for tweet in search:
        item_list.append(tweet.text)

    return random.choice(item_list)

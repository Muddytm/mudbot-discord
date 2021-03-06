"""Creates config files from environment variables. Part of the Travis CI process."""

import os


# Creating a normal config file with empty variables
# (we'll be using a testing config)
# NOWIMTHEPILOTOFTHISSPACESHIP = arbitrary dummy phrase from a song I like
with open("config.py", "w") as f:
    f.write("app_token = \"{}\"\n".format("NOWIMTHEPILOTOFTHISSPACESHIP"))


# For Travis and Shiny Mudbot (Mudbot test)
mudbot_token = (os.environ["mudbot_token"])
travis_token = (os.environ["travis_token"])

with open("tests/test_config.py", "w") as f:
    f.write("mudbot_app_token = \"{}\"\n"
            "travis_app_token = \"{}\"\n".format(mudbot_token, travis_token))


# For Twitter
CONSUMER_KEY = (os.environ["TWITTER_CONSUMER_KEY"])
CONSUMER_SECRET = (os.environ["TWITTER_CONSUMER_SECRET"])
ACCESS_TOKEN_KEY = (os.environ["TWITTER_ACCESS_TOKEN_KEY"])
ACCESS_TOKEN_SECRET = (os.environ["TWITTER_ACCESS_TOKEN_SECRET"])
key_counter_threshold = "5"

with open("configs/chest_config.py", "w") as f:
    f.write("CONSUMER_KEY = \"{}\"\n"
            "CONSUMER_SECRET = \"{}\"\n"
            "ACCESS_TOKEN_KEY = \"{}\"\n"
            "ACCESS_TOKEN_SECRET = \"{}\"\n"
            "key_counter_threshold = \"{}\"\n".format(CONSUMER_KEY,
                                                      CONSUMER_SECRET,
                                                      ACCESS_TOKEN_KEY,
                                                      ACCESS_TOKEN_SECRET,
                                                      key_counter_threshold))

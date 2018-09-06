import asyncio
from discord.ext import commands
import test_config as config
import discord
import time

BOT_PREFIX = "!"
TOKEN = config.travis_app_token

client = commands.Bot(command_prefix=commands.when_mentioned_or(BOT_PREFIX))


@client.event
async def on_ready():
    print ("Logged in as")
    print (client.user.name)
    print (client.user.id)
    print ("------")

    bot_channel = None
    for channel in client.get_all_channels():
        if channel.name == "bot-testing":
            bot_channel = channel

    if not bot_channel:
        print ("Channel not found. Exiting.")

    time.sleep(10)

    # TESTING STARTS HERE
    # -------------------

    # !test
    await client.send_message(bot_channel, "!test")
    time.sleep(3)

    # !chest
    await client.send_message(bot_channel, "!chest")
    for i in range(3):
        time.sleep(1)
        await client.send_message(bot_channel, "Incrementing key_counter...")
    time.sleep(3)
    await client.send_message(bot_channel, "!chest")
    time.sleep(3)

    # !scram
    await client.send_message(bot_channel, "!scram")
    time.sleep(3)

    # Testing done!
    await client.send_message(bot_channel, "Travis CI testing complete.")
    await client.logout()


client.run(TOKEN)

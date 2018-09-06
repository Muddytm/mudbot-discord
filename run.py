import asyncio
from discord.ext import commands
import config
import discord
import json
import mudules
import os
import sys

if not os.path.isdir("userdata"):
    os.makedirs("userdata")

if os.path.isfile("tests/test_config.py") and len(sys.argv) > 1 and sys.argv[1] == "test":
    import tests.test_config as testconfig
    TOKEN = testconfig.mudbot_app_token
else:
    TOKEN = config.app_token

BOT_PREFIX = "!"
client = commands.Bot(command_prefix=commands.when_mentioned_or(BOT_PREFIX))


@client.event
async def on_ready():
    print ("Logged in as")
    print (client.user.name)
    print (client.user.id)
    print ("------")


@client.event
async def on_message(message):
    """Add userdata json file and run certain functionality when a user types
    any message, anywhere.
    """
    if message.author == client.user or (message.author.bot and "Travis" not in message.author.name):
        return

    # Let's create a JSON file for this user.
    if not os.path.isfile("userdata/{}_{}.json".format(message.author.name.replace(" ", ""), message.author.id)):
        with open("userdata/{}_{}.json".format(message.author.name.replace(" ", ""), message.author.id), "w") as f:
            user_json = {"name": message.author.name, "id": message.author.id}
            json.dump(user_json, f)

    # Increment the counter, and if the counter is high enough, get a key!
    r = mudules.chest_key(message)
    if r != "":
        await client.send_message(message.channel, r)

    # This allows us to use other commands as well.
    await client.process_commands(message)


@client.command(pass_context=True)
async def test(ctx, stuff="Despacito"):
    await client.say("peep beep meme {} creep".format(stuff))
    #await client.send_message(ctx.message.channel, "Alexa play {}".format(stuff))


@client.command(pass_context=True)
async def chest(ctx, stuff=""):
    """Grant the user an item! If they have a key.

    Items taken at random from the Elder Scrolls Items Twitter."""
    await client.say(mudules.chest(ctx))


@client.command(pass_context=True)
async def loadout(ctx, stuff=""):
    """Show the user's loadout."""
    await client.say(mudules.display_loadout(ctx.message.author.name.replace(" ", ""),
                                             ctx.message.author.id))


@client.command(pass_context=True)
async def scram(ctx, stuff=""):
    """Close the bot."""
    await client.say("I'm outta here.")
    await client.logout()


client.run(TOKEN)

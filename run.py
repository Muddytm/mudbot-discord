import asyncio
from discord.ext import commands
import config
import discord
import json
import mudules
import os

BOT_PREFIX = "!"
TOKEN = config.app_token

client = commands.Bot(command_prefix=commands.when_mentioned_or(BOT_PREFIX))


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    """Add userdata json file and run certain functionality when a user types
    any message, anywhere.
    """
    #if message.content.startswith("?"):
    #    await client.send_message(message.channel, "Name: {}, ID: {}".format(message.author.name, message.author.id))

    # Let's create a JSON file for this user.
    if not os.path.isfile("userdata/{}_{}.json".format(message.author.name, message.author.id)):
        with open("userdata/{}_{}.json".format(message.author.name, message.author.id), "w") as outfile:
            user_json = {"name": message.author.name, "id": message.author.id}
            json.dump(user_json, outfile)

    # This allows us to use other commands as well.
    await client.process_commands(message)


@client.command(pass_context=True)
async def test(ctx, stuff="Despacito"):
    await client.say("peep beep meme {} creep".format(stuff))
    #await client.send_message(ctx.message.channel, "Alexa play {}".format(stuff))


@client.command(pass_context=True)
async def chest(ctx, stuff=""):
    """Grant the user an item! They will need a key, in later functionality.

    Items taken at random from the Elder Scrolls Items Twitter."""
    await client.say("You found...{}!".format(mudules.chest()))


client.run(TOKEN)

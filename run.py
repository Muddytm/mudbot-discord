import asyncio
import discord
from discord.ext import commands
import config
import discord
import json
import mudules
import os
import sys

# discord.opus.load_opus("opus")

if not os.path.isdir("userdata"):
    os.makedirs("userdata")

if os.path.isfile("tests/test_config.py") and len(sys.argv) > 1 and sys.argv[1] == "test":
    import tests.test_config as testconfig
    TOKEN = testconfig.mudbot_app_token
else:
    TOKEN = config.app_token

BOT_PREFIX = "!"
client = commands.Bot(command_prefix=commands.when_mentioned_or(BOT_PREFIX))


def clean(name):
    """Cleans name of ASCII values for storage."""
    for ch in name:
        if ord(ch) < 34 or ord(ch) > 127:
            name = name.replace(ch, "")

    return name


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
    if not os.path.isfile("userdata/{}_{}.json".format(clean(message.author.name), message.author.id)):
        with open("userdata/{}_{}.json".format(clean(message.author.name), message.author.id), "w") as f:
            user_json = {"name": clean(message.author.name), "id": message.author.id}
            json.dump(user_json, f)

    # Increment the counter, and if the counter is high enough, get a key!
    r = mudules.chest_key(message)
    if r != "":
        await client.send_message(message.channel, r)

    # This allows us to use other commands as well.
    await client.process_commands(message)


@client.command(pass_context=True)
async def test(ctx, stuff="Despacito"):
    """peep beep meme creep"""
    await client.say("peep beep {} creep".format(stuff))


@client.command(pass_context=True)
async def chest(ctx, stuff=""):
    """Grant the user an item! If they have a key."""
    await client.say(mudules.chest(ctx))


@client.command(pass_context=True)
async def loadout(ctx, stuff=""):
    """Show the user's loadout."""
    await client.say(mudules.display_loadout(clean(ctx.message.author.name),
                                             ctx.message.author.id))


@client.command(pass_context=True)
async def clap(ctx, *stuff):
    """Repeat what the user says, but with clap emojis."""
    clap_text = mudules.clap(stuff)
    if clap_text.strip():
        await client.say(clap_text)


@client.command(pass_context=True)
async def tellmeajoke(ctx):
    """Tell a joke!"""
    await client.say(mudules.telljoke(clean(ctx.message.author.name)))


# @client.command(pass_context=True)
# async def play(ctx, link=""):
#     """Play audio from a YouTube link."""
#     if not link:
#         await client.say("You gotta put in a YouTube link, friend.")
#         return
#
#     if link.startswith("https://www.youtube.com/watch?v="):
#         voice = await client.join_voice_channel(ctx.message.author.voice.voice_channel)
#         player = await voice.create_ytdl_player(link)
#         player.start()


@client.command(pass_context=True)
@commands.has_any_role("Admin", "Travis Bot")
async def scram(ctx, stuff=""):
    """Close the bot."""
    await client.say("I'm outta here.")
    await client.logout()


client.run(TOKEN)

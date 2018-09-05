import asyncio
import config
import discord
import mudules
from discord.ext import commands

BOT_PREFIX = "!"
TOKEN = config.app_token

client = commands.Bot(command_prefix=commands.when_mentioned_or(BOT_PREFIX))


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


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

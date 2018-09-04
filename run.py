import config
import discord
import json
import random
from discord.ext.commands import Bot

BOT_PREFIX = "!"
TOKEN = config.app_token

client = Bot(command_prefix=BOT_PREFIX)


@client.event
async def on_message(message):
    """This runs whenever any message is sent."""
    if message.author == client.user:
        return

    await client.send_message(message.channel, "peep beep meme creep")


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

#client.loop.create_task(do_thing())
client.run(TOKEN)

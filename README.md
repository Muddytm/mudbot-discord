# Mudbot for Discord

[![Build Status](https://travis-ci.org/Muddytm/mudbot-discord.svg?branch=master)](https://travis-ci.org/Muddytm/mudbot-discord)

Mudbot is a Discord bot used for general-purpose hootenannying. It's also easy to create plugins for, so if you're just starting to write bots but want something solid to work with, look no further! Well, look a little further. But then come back here afterwards and say "ahh, this beats the things that I found when I looked *even further*."

## Setup

Running Mudbot requires having a version of Python installed that is 3.5 or higher (and preferably lower than 3.7, though not strictly necessary), so get that done. You'll also want to download the Mudbot code itself, so use `git clone` or whatever to do so.

Once that's good and over with, run the following command line in Linux, or Powershell, or what-have-you:

`pip3 install discord.py`

The pip3 service will download the discord.py package along with its dependencies.

Next, you'll need to create a Discord app, create a bot user, and have it join your Discord server. After that, grab your app token (from the bot users page), and create a file named config.py in the same directory as run.py for the bot. You can just copy config_template.py and put the app token in the relevant place (the other keys shown are not necessary).

And at that point, running `python run.py` (or `python3 run.py` depending on what version `python` calls) should start the bot without any problems!

Unless you're using **Python 3.7**. If so, read on.

The packages that are installed (aiohttp, websockets, and the discord.py app itself) are not 100% up to date to work with Python 3.7, so some patching is required lest you crash.

So, you'll want to head over to the python37_patches directory (in the Mudbot repo, wherever you have it copied to), edit the patch_config.py to list your packages location file (where aiohttp, websockets, and discord.py reside) and run the following:

`python patch.py`

Your bot should now work with Python 3.7! Well done.

## Usage

Right now there are small amount of functions available:

- `!test`: spits out a testing message.
- `!chest`: attempts to unlock a chest for the user, granting them a stupid item from the TES\_ItemsBot Twitter page. A Twitter app must be made for this functionality to work, and the relevant tokens and keys listed in configs/chest\_config.py. Also requires a "key" to unlock the chest, acquired by sending messages in the server.
- `!loadout`: displays gear gained from unlocking chests.
- `!clap`: takes a phrase, inserts clap emojis, and spits it back out.
- `!tellmeajoke`: tells a joke.
- `!scram`: logs out (ending the process).

## FUTUUUUUUUURE

- Add more functions! (on-going)
- Better documentation! (on-going)
- Create guide explaining Discord functions, and how to add one to this bot.
- Make a neat logo?
- Use Coveralls to get code coverage data.

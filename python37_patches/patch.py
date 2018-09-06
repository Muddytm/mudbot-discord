import aiohttp_patch
import discordpy_patch
import websockets_patch
import patch_config

dir = patch_config.dir
print ("Preparing to patch packages to be python 3.7 compatible.")

print ("Patching aiohttp...")
aiohttp_patch.patch(dir)
print ("Complete.")

print ("Patching discord.py...")
discordpy_patch.patch(dir)
print ("Complete.")

print ("Patching websockets...")
websockets_patch.patch(dir)
print ("Complete.")

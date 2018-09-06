"""Patches the aiohttp package. Part of the Travis CI running process."""

compat_loc = "/home/travis/virtualenv/python3.7-dev/lib/python3.7/site-packages/aiohttp/{}"

with open(compat_loc.format("helpers.py")) as fout:
    with open(compat_loc.format("helpers_bk.py"), "w") as fin:
        for line in fout:
            line = line.replace("ensure_future = asyncio.async", "ensure_future = getattr(asyncio, \"async\")")
            fin.write(line)

with open(compat_loc.format("helpers_bk.py")) as fout:
    with open(compat_loc.format("helpers.py"), "w") as fin:
        for line in fout:
            fin.write(line)

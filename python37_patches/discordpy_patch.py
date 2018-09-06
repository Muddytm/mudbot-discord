"""Patches the Discord.py package. Part of the Travis CI running process."""

compat_loc = "/home/travis/virtualenv/python3.7-dev/lib/python3.7/site-packages/discord/{}"

with open(compat_loc.format("compat.py")) as fout:
    with open(compat_loc.format("compat_bk.py"), "w") as fin:
        for line in fout:
            line = line.replace("create_task = asyncio.async", "create_task = getattr(asyncio, \"async\")")
            fin.write(line)

with open(compat_loc.format("compat_bk.py")) as fout:
    with open(compat_loc.format("compat.py"), "w") as fin:
        for line in fout:
            fin.write(line)

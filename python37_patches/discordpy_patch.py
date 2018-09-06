"""Patches the Discord.py package. Part of the Travis CI running process."""


def patch(dir):
    """Run patching process."""
    compat_loc = "{}discord/{}"

    with open(compat_loc.format(dir, "compat.py")) as fout:
        with open(compat_loc.format(dir, "compat_bk.py"), "w") as fin:
            for line in fout:
                line = line.replace("create_task = asyncio.async", "create_task = getattr(asyncio, \"async\")")
                fin.write(line)

    with open(compat_loc.format(dir, "compat_bk.py")) as fout:
        with open(compat_loc.format(dir, "compat.py"), "w") as fin:
            for line in fout:
                fin.write(line)

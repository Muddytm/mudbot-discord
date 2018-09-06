"""Patches the aiohttp package. Part of the Travis CI running process."""


def patch(dir):
    """Run patching process."""
    compat_loc = "{}aiohttp/{}"

    with open(compat_loc.format(dir, "helpers.py")) as fout:
        with open(compat_loc.format(dir, "helpers_bk.py"), "w") as fin:
            for line in fout:
                line = line.replace("ensure_future = asyncio.async", "ensure_future = getattr(asyncio, \"async\")")
                fin.write(line)

    with open(compat_loc.format(dir, "helpers_bk.py")) as fout:
        with open(compat_loc.format(dir, "helpers.py"), "w") as fin:
            for line in fout:
                fin.write(line)

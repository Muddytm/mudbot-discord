"""Patches the websockets package. Part of the Travis CI running process."""


def patch(dir):
    """Run patching process."""
    compat_loc = "{}websockets/{}"

    with open(compat_loc.format(dir, "compatibility.py")) as fout:
        with open(compat_loc.format(dir, "compatibility_bk.py"), "w") as fin:
            for line in fout:
                line = line.replace("asyncio_ensure_future = asyncio.async", "asyncio_ensure_future = getattr(asyncio, \"async\")")
                fin.write(line)

    with open(compat_loc.format(dir, "compatibility_bk.py")) as fout:
        with open(compat_loc.format(dir, "compatibility.py"), "w") as fin:
            for line in fout:
                fin.write(line)

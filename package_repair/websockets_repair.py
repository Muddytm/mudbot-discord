"""Repairs the websockets package. Part of the Travis CI running process."""

compat_loc = "/home/travis/virtualenv/python3.7-dev/lib/python3.7/site-packages/websockets/{}"

with open(compat_loc.format("compatibility.py")) as fout:
    with open(compat_loc.format("compatibility_bk.py"), "w") as fin:
        for line in fout:
            line = line.replace("asyncio_ensure_future = asyncio.async", "asyncio_ensure_future = getattr(asyncio, \"async\")")
            fin.write(line)

with open(compat_loc.format("compatibility_bk.py")) as fout:
    with open(compat_loc.format("compatibility.py"), "w") as fin:
        for line in fout:
            fin.write(line)

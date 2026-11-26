# copied from the old project, not sure what uses this
def fmt(x):
    return str(x).zfill(8)


def parse(x):
    return int(x.lstrip("0") or 0)

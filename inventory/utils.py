def normalize_name(name):
    return name.strip().upper() if name else name


def chunks(seq, n):
    return [seq[i:i + n] for i in range(0, len(seq), n)]

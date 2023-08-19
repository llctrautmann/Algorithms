import numpy as np


def digital_root(n):
    ls = sum([int(a) for a in str(n)])
    print(ls)
    if ls < 10:
        return ls
    else:
        return digital_root(ls)

import random


def worstsort(xs):
    """
    Sort a list by randomly reording it and seeing if it is sorted

    Best case time complexity O(n) -- yay!

    Average case: n * n!

    Worst case, um, never?

    Parameters
    ==========

    xs : list of anything

    Return
    ======

    An ordered list or the heatdeath of the universe (whichever comes first)
    """

    while not is_ordered(xs):
        random.shuffle(xs)

    return xs


def is_ordered(xs):
    if len(xs) < 2:
        return xs
    else:
        for i in range(len(xs) - 1):
            if xs[i] > xs[i + 1]:
                return False
        return True

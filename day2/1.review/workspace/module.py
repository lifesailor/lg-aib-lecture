def is_odd(x):
    """

    :param x:
    :return:
    """
    assert x > 0
    if x % 2 == 0:
        return False
    else:
        return True


def is_even(x):
    """

    :param x:
    :return:
    """
    assert x > 0
    if x % 2 == 0:
        return True
    else:
        return False

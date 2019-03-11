def is_odd(x):
    assert x > 0

    if x % 2 == 0:
        return False
    else:
        return True


def check_number(number):
    """

    :param number:
    :return:
    """
    for i in range(10):
        if str(number).count(str(i)) == 1:
            continue
        else:
            return False
    return True

check_number(1234567890)
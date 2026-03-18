def func(a, b, c=1):
    """
    Function with three parameters, one of which has a default value.
    >>> func(2, 3)
    6
    >>> func(2, 3, 4)
    25

    :param a: weight of the item
    :param b: length of the item
    :param c: height of the item, default is 1
    :return:
    """
    return a * b * c

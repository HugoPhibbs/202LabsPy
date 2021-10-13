def triangle(t):
    """
    Returns a y value for a triangle wave of period 2 for a given y value

    :param t: value as described
    :return: y value as described
    """
    if int(t) % 2 == 0:
        y = t - int(t)
    else:
        y = 2 - (t - int(t) + 1)
    return abs(y)

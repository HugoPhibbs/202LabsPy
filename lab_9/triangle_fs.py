import numpy as np


def triangle_fs(t, n):
    """
    Finds the fourier series for a triangle wave of period 2

    :param t: time values for the fs to be evaluated at
    :param n: number of terms in fs to use
    :return: vector containing the fs evaluated at time values t
    """
    period = 2
    a_0 = 1

    f_t = (a_0 / 2) * np.ones(len(t))

    a_n = np.zeros((n, 1))

    for i in range(1, n + 1):
        a_n[i - 1] = 2 * ((-1) ** i - 1) / ((i ** 2) * (np.pi ** 2))

        f_t += a_n[i - 1] * np.cos((2 * np.pi * i * t) / period)

    return f_t

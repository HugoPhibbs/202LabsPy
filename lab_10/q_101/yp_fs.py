from numpy import pi, sin


def q101_yp(t, k, n):
    """
     Function to evaluate the particular solution to L10.1

    :param t: time to evaluate at
    :param k: DE parameter
    :param n: number of fourier series terms to calculate
    :return: yp evaluated with k at t for n terms
    """
    nth_term = lambda k_, n_, t_: ((1 - (-1) ** n_) / (pi * n_ * (k_ - (pi * n_) ** 2))) * sin(pi * n_ * t_)
    y_t = nth_term(k, 1, t)
    for i in range(2, n + 1):
        y_t += nth_term(k, i, t)
    return y_t

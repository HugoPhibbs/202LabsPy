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


def q4_fs(t, n):
    """
    Evaluates the fourier series from question 4 of the lab

    :param t: time value to evaluate fourier series at
    :param n: number of terms to use
    :return: value of fs evaluated at t with n terms
    """
    nth_term = lambda _t, _n: ((1 - (-1) ** _n) / (1 / pi * _n)) * sin(pi * _n * _t)
    f_t = nth_term(_t=t, _n=1)
    for i in range(2, n + 1):
        f_t += nth_term(_t=t, _n=i)
    return f_t


def q101_de(t, w, k, n):
    """
    Evaluates the DE from question L10.1 from the lab at given time value

    :param t: time evaluate to evaluate DE at
    :param k: constant k
    :param n: number of fourier series terms to approximate RHS f(t)
    :return: the DE evaluated at t
    """
    y = w[0]
    x = w[1]
    return [
        x,
        q4_fs(t, n) - k * y
    ]

from numpy import heaviside as hs
import numpy as np
from helpers.helpers import *


def de_l81b(t, y):
    return np.array([
        hs(t, 3) + np.exp(7 - t) * hs(t, 7) - y
    ])


y0 = [0]
t_span = [0, 20]

plot_ivp(de_func=de_l81b, t_span=t_span, y0=y0, max_step=0.01, show=True)

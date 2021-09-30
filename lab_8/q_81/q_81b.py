import matplotlib.pyplot as plt
from numpy import heaviside as hs
from scipy.integrate import solve_ivp
import numpy as np


def de_l81b(t, y):
    return np.array([
        hs(t, 3) + np.exp(7 - t) * hs(t, 7) - y
    ])


y0 = [0]
t_span = np.array([
    0,
    20
])

y_soln = solve_ivp(fun = de_l81b, t_span=t_span, y0=y0, max_step = 0.01)

plt.plot(
    y_soln.t,
    y_soln.y[0]
)

plt.show()
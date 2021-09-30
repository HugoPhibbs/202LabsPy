import numpy as np
from scipy.integrate import solve_ivp
from matplotlib import pyplot as plt
from numpy import heaviside as hs

# Part a
def de_86a(t, w):
    y = w[0]
    x = w[1]
    return np.array(
        [x,
        hs(t, np.pi) - hs(t, 2 * np.pi) - 2 * x - 2 * y]
    )

y0 = 0
x0 = 1
w0 = np.array(
    [y0,
    x0]
)

t_span = np.array([0, 20])

w_soln = solve_ivp(fun=de_86a, y0=w0, t_span=t_span, max_step = 0.01)

plt.plot(
    w_soln.t,
    w_soln.y[0]
)

plt.show()
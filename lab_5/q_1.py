import math

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Part a
def non_lin_spring_de(t, w):
    x = w[0]
    y = w[1]
    F = np.array(
        [
            y,
            -x ** 5 + 6 * x ** 3 - 8 * x
        ]
    )
    return F


# Part b
n = 10
y0 = np.zeros(n)
x0 = np.linspace(-3, 3, n)
w0 = np.array([x0, y0]).transpose()

t_span = np.array([0, 50])

plt.figure(1)

for i in range(len(w0)):
    continue
    w_span = solve_ivp(non_lin_spring_de, t_span=t_span, y0=w0[i], max_step=0.01)
    plt.plot(w_span.y[0], w_span.y[1])

# Part c
# Phase picture just around -sqrt(2)
n = 20
y0 = np.zeros(n)
x0 = np.linspace(-math.sqrt(2)-0.5, -math.sqrt(2)+0.5, n)
w0 = np.array([x0, y0]).transpose()

t_span = np.array([0, 50])

plt.figure(2)

for i in range(len(w0)):
    w_span = solve_ivp(non_lin_spring_de, t_span=t_span, y0=w0[i], max_step=0.01)
    plt.plot(w_span.y[0], w_span.y[1])

plt.scatter(-math.sqrt(2), 0)

# Phase picture just around +sqrt(2)
n = 20
y0 = np.zeros(n)
x0 = np.linspace(math.sqrt(2)-0.5, math.sqrt(2)+0.5, n)
w0 = np.array([x0, y0]).transpose()

t_span = np.array([0, 50])

plt.figure(3)

for i in range(len(w0)):
    w_span = solve_ivp(non_lin_spring_de, t_span=t_span, y0=w0[i], max_step=0.01)
    plt.plot(w_span.y[0], w_span.y[1])

plt.scatter(math.sqrt(2), 0)

plt.show()

# NB the plots match a hyperbolic sadle shape.
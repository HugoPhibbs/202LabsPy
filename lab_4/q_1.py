import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def spring_de(t, w, is_soft: bool):
    """Evaluates the RHS of the spring system

    is_soft (bool) to decide if the spring is soft or not"""
    x = w[0]
    y = w[1]
    x_pr = y
    if is_soft:
        y_pr = -x + x ** 3
    else:
        y_pr = -x - x ** 3
    return np.array([x_pr, y_pr])


# Part a, use a hard spring system
plt.figure(1)

w0 = np.array(
    [
        [0.9, 0.2],
        [0.9, 0.14],
        [0.9, 0.13],
        [0.9, 0],
        [2, 0],
        [0.5, 0]
    ]
)
# Let w = (x, y) for simplicity

t_span = np.array([0, 50])

hard_spring_de = lambda t, w: spring_de(t, w, False)

for i in range(len(w0)):
    w_soln = solve_ivp(hard_spring_de, t_span=t_span, y0=w0[i], max_step=0.1)
    plt.plot(w_soln.y[0], w_soln.y[1])

# Part b repeat with a soft springs system


w0 = np.array(
    [
        [0.9, 0.2],
        [0.9, 0.1347],
        [0.9, 0.13436],
        [0.9, 0.1345],
        [0.9, 0.1],
        [0.9, 0],
        [0.5, 0]
    ]
)

soft_spring_de = lambda t, w: spring_de(t, w, True)

plt.figure(2)
w_soln = solve_ivp(soft_spring_de, t_span=t_span, y0=w0[0], max_step=0.1)
plt.plot(w_soln.y[0], w_soln.y[1])

t_span = np.array([0, 9])

plt.figure(3)
w_soln = solve_ivp(soft_spring_de, t_span=t_span, y0=w0[1], max_step=0.1)
plt.plot(w_soln.y[0], w_soln.y[1])

t_span = np.array([0, 50])

for i in range(2, len(w0)):
    plt.figure(i+2)
    w_soln = solve_ivp(soft_spring_de, t_span=t_span, y0=w0[i], max_step=0.1)
    plt.plot(w_soln.y[0], w_soln.y[1])

plt.show()

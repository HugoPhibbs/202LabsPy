import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def chem_de(t, x, k4):
    A = np.array([
        [-0.002, 0, 0, 0],
        [0.002, -0.08, 0, 0],
        [0, 0.08, -1, 0],
        [0, 0, 1, 0]
    ])
    bt = k4 * np.array(
        [0, -x[1]*(x[2]**2), x[1]*x[2]**2, 0]
    )
    return np.add(np.matmul(A, x), bt)

k4 = 1
chem_de_filled = lambda t, x: chem_de(t, x, k4)
t_span = np.array([0, 1000])
x0 = np.array(
    [500, 0, 0, 0]
)

x_soln = solve_ivp(chem_de_filled, t_span= t_span, y0 = x0, max_step = 0.1)

for i in range(len(x0)):
    plt.figure(i)
    plt.plot(x_soln.t, x_soln.y[i])

plt.figure(i+1)
plt.plot(x_soln.y[1], x_soln.y[2])
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def lotka_vol_de(t, w):
    x = w[0]
    y = w[1]
    x_pr = 0.004*x*(50-x-0.75*y)
    y_pr = 0.001*y*(100-y-3.0*x)
    return np.array([x_pr, y_pr])

w0 = np.array(
    [
        (0.9, 9.1),
        (1.1, 8.9),
        (1.3, 8.7),
        (1.5, 8.5),
        (1.7, 8.3),
        (1.9, 9.1)
    ]
)

t_span = np.array([0, 200])

for i in range(len(w0)):
    w_soln = solve_ivp(lotka_vol_de, t_span=t_span, y0=w0[i], max_step = 0.1)
    plt.plot(w_soln.y[0], w_soln.y[1])

# Adding stationairy pts
plt.scatter(0, 0, color = "black")
plt.scatter(0, 100, color = "black")
plt.scatter(50, 0, color = "black")
plt.scatter(20, 40, color = "black")


plt.show()

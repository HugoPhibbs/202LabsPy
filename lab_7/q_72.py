import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import math as m


# Using q7.2
def lt_de72(t, w):
    y = w[0]
    x = w[1]
    return np.array(
        x, x + 6 * y
    )


y0 = 1
x0 = -1
w0 = np.array([x0, y0])
#t_span = np.array([0, 10])

# w_soln = solve_ivp(lt_de72, y0=w0, t_span=t_span, max_step=0.1)

# Printing y solns, don't care about x
# plt.plot(w_soln.t, w_soln.y[0])
# plt.show()

# Using q7.7
def lt_de77(t, w):
    y = w[0]
    x = w[1]
    return np.array(
        [x,
        6 * x - 9 * y + (t ** 2) * m.exp(3 * t)]
    )

y0 = 2
x0 = 17
w0 = np.array(
    [y0,
    x0]
)
t_span = np.array([0, 10])
w_soln = solve_ivp(lt_de77, t_span=t_span, y0=w0, max_step = 0.01)
# Plot y solution only
plt.plot(w_soln.t, w_soln.y[0])
plt.show()
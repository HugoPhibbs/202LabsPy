import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from heaviside import heaviside as hs
from delta import delta

# --- Finding the solution to the de via reducing to a 1st order system --- #
def de_sys(t, w, a):
    y = w[0]
    x = w[1]
    return np.array([
        x,
        4 * delta(t=t, t0=2 * np.pi, a=a) - y
    ])


y0 = 1
x0 = 0

w0 = np.array([
    y0,
    x0
])

a_vals = np.array([
    1,
    0.5,
    0.1,
    0.01
])

plt.figure(1)
t_span = np.array([0, 20])

for a in a_vals:
    de_sys_with_a = lambda t, w: de_sys(t, w, a)
    y_soln_sys = solve_ivp(fun=de_sys_with_a, t_span=t_span, y0=w0, max_step=0.01)
    plt.plot(y_soln_sys.t, y_soln_sys.y[0])


# --- Plotting the analytical solution that I found --- #

plt.figure(2)

def y_analy(t):
    return (1 / 2) * (
            np.exp(t - 2 * np.pi) * hs(t, 2 * np.pi)
            - np.exp(2 * np.pi - t) * hs(t, 2 * np.pi)
            + np.exp(-t)
            + np.exp(t)
    )


t_vals = np.linspace(
    start=0,
    stop=20,
    num=1000
)

y_vals_analy = [0] * len(t_vals)

for i in range(len(y_vals_analy)):
    y_vals_analy[i] = y_analy(t_vals[i])

plt.plot(t_vals, y_vals_analy)

plt.show()

# The plots couldn't be more different from each other, one of them
# shows strong growth (exponential) behaviour, and the other shows
# oscillatory behaviour!, did i fuck something up?

# Can this be fixed?
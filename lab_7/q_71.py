from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np
import math as m


def lt_de(t, T):
    """ Returns T' = f(t, T)"""
    rhs = 20 * m.sin(3 * t) - 3 * T
    return rhs


t_span = [0, 10]
T0 = [30]
T_soln = solve_ivp(lt_de, t_span=t_span, y0=T0, max_step = 0.01)
plt.plot(T_soln.t, T_soln.y[0])
plt.show()

from numpy import linspace

from funcs import *
from helpers.helpers import *

# Plotting the particular solution

k = 1
n = 10

t_vals = linspace(start=-1, stop=10, num=1000)
yp = lambda t: q101_yp(t=t, k=k, n=n)
y_vals = eval_func_t(yp, t_vals)

plot_xy(x_vals=t_vals, y_vals=y_vals, show=True)

# Plotting numerical general solution
w0 = [3, 1]
de_func = lambda t, w: q101_de(t, w0, k, n)
plot_ivp(de_func=de_func, t_span=t_vals, y0=w0, show=True)

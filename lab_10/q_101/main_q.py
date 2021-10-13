from numpy import linspace

from helpers.helpers import *
from yp_fs import q101_yp

k = 1
n = 10

t_vals = linspace(start=-1, stop=10, num=1000)
yp = lambda t: q101_yp(t=t, k=k, n=n)
y_vals = eval_func_t(yp, t_vals)

plot_xy(x_vals=t_vals, y_vals=y_vals, show=True)

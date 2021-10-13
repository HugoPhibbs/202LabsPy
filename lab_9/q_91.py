import numpy as np
from triangle import triangle
from helpers.helpers import plot_xy
from triangle_fs import triangle_fs
import matplotlib.pyplot as plt

# Plotting analytical solution
t = np.linspace(start=-1, stop=5, num=600)

y_analy = [0] * len(t)

for i in range(len(t)):
    y_analy[i] = triangle(t[i])

#plot_xy(t, y_analy, True)

# Plotting fourier series solution
n_vals = [1, 5, 10, 20]
y_fs = np.zeros((len(n_vals), len(t)))

for j in range(len(n_vals)):
    n = n_vals[j]
    y_fs[j,] = triangle_fs(t, n)

plt.figure(1)
plot_xy(t, y_analy-y_fs[3], True)

plt.figure(3)
plot_xy(t, y_fs[3], True)

plt.figure(2)
for k in range(len(n_vals)):
    if k == len(n_vals)-1:
        plot_xy(t, y_fs[k], True)
    else:
        plot_xy(t, y_fs[k])


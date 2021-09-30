import numpy as np
import matplotlib.pyplot as plt
from delta import delta

t_vals = np.linspace(
    start=0,
    stop=5,
    num=500
)

a_vals = np.array([
    1, 0.2, 0.1, 0.05
])

t0 = 2

for a in a_vals:
    y_vals = [0] * len(t_vals)
    for i in range(len(y_vals)):
        y_vals[i] = delta(a=a, t=t_vals[i], t0=t0)
    plt.plot(t_vals, y_vals)

plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def earthquake_mat(n, omega0, delta):
    I_nn_x2 = 2 * np.identity(n)
    diag_1_p1 = np.diag(np.ones(n-1), +1)
    diag_1_m1 = np.diag(np.ones(n-1), -1)
    K = I_nn_x2-diag_1_p1-diag_1_m1
    K[n-1, n-1] = 1
    A = np.array([
        [np.zeros((n, n)), np.identity(n)],
        [-(omega0**2)*K, -2*delta*K]
    ])
    return A

A1 = earthquake_mat(4, 1, 0)
print(A1)

[D, P] = np.linalg.eig(A1)

print("P", P)
print("D", D)
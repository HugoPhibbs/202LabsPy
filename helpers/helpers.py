from scipy.integrate import solve_ivp
from matplotlib import pyplot as plt


def plot_ivp(de_func: callable, t_span, y0, max_step=0.01, show=False):
    """ Automates solving and plotting a IVP Differential Equation"""
    de_soln = solve_ivp(fun=de_func, t_span=t_span, y0=y0, max_step=max_step)
    plt.plot(de_soln.t, de_soln.y[0])
    if show:
        plt.show()


def plot_xy(x_vals, y_vals):
    """Plots x and y vals using matplotlib, put into function to save the imports"""
    plt.plot(x_vals, y_vals)

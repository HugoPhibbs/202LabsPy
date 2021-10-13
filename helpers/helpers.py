from matplotlib import pyplot as plt
from scipy.integrate import solve_ivp


def plot_ivp(de_func: callable, t_span, y0, max_step=0.01, show=False) -> None:
    """
     Automates solving and plotting a IVP Differential Equation

    :param de_func: Function of a de, with input for t and y vals
    :param t_span: values of t to be evaluated for the de
    :param y0: initial value of y for this de problem
    :param max_step: the max step size for approximating yi
    :param show: If the solution should be shown or not
    :return: None
    """
    de_soln = solve_ivp(fun=de_func, t_span=t_span, y0=y0, max_step=max_step)
    plot_xy(x_vals=de_soln.t, y_vals=de_soln.y[0], show=show)


def plot_xy(x_vals, y_vals, show=False) -> None:
    """
    Plots x and y vals using matplotlib, put into function to save the imports

    :param x_vals: x values
    :param y_vals: y values
    :param show: if the created plot should be shown or
    :return none
    """
    plt.plot(x_vals, y_vals)
    if show:
        plt.show()


def eval_func_t(func: callable, t_vals):
    """
    Evaluates a function at given time points

    :param func: callable function to be called
    :param t_vals: array for time points for the function to be evaluated at
    :return: array of function evaluated at each time point in t_vals
    """
    y_vals = [None] * len(t_vals)
    for i in range(len(t_vals)):
        y_vals[i] = func(t_vals[i])
    return y_vals

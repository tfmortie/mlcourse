# helper functions for PC lab 3
# Stijn Decubber
import numpy as np

def simulate_linear_data(n, eps=5):
    """Simulate n data points from a noisy linear ground truth
    Inputs
    ------
    n: number of points
    eps: standard deviation of the Gaussian noise

    Returns
    ------
    x, y: x and y coordinates of the data points
    """
    x = np.linspace(start=-1, stop=1, num=n) + np.random.normal(size=n)

    X = np.zeros((n,2))
    X[:,0] = np.ones((n,))
    X[:,1] = x

    w = [np.random.normal(), 10*np.random.normal()]
    y = np.dot(X, w) + np.random.normal(scale=eps, size=n)

    return(x,y)

import numpy as np
from scipy.integrate import solve_ivp

class Pendulum:
    """Class to represent pendulums"""

    def __init__(self, L=1, M=1, g=9.81):
        self.L = L
        self.M = M
        self.g = g

    def __call__(self, t, y):
        """Setting up ODEs"""
        theta, omega = y
        d_theta = omega
        d_omega = -(self.g/self.L)*np.sin(theta)
        return d_theta, d_omega

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

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

    def solve(self, U0, T, dt, angle = "rad"):
        """Method for solving the ODE with initial conditions"""

        if angle == "deg":
            angle = np.radians(angle)

        elif angle == "rad":
            pass

        else:
            raise TypeError


        t_ev = np.linspace(0, T, int(T/dt) + 1)
        sol = solve_ivp(self.__call__, [0, T], U0, t_eval=t_ev)
        self._t = t_ev
        self._theta = sol.y[0]
        self._omega = sol.y[1]

    @property
    def t(self):
        return self._t

    @property
    def theta(self):
        return self._theta

    @property
    def omega(self):
        return self._omega

    @property
    def x(self):
        return self.L*sin(self.theta)

    @property
    def x(self):
        return -self.L*cos(self.theta)









# if __name__ == "__main__":
#     """Run example"""
#     instance = Pendulum(2)
#     instance.solve((1,1), 1, 1)
#     a = instance.t
#     print(a)

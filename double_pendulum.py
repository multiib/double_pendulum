import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

class DoublePendulum():
    def __init__(self, L1=1, L2=1, g=9.81):
        self.L1 = L1
        self.L2 = L2
        self.g = g


    def __call__(self, t, y):
        theta1, omega1, theta2, omega2 = y

        dtheta1_dt = omega1
        dtheta2_dt = omega2

        d_th = theta2 - theta1

        domega1_dt = ((self.L1*omega1**2*np.sin(d_th)*np.cos(d_th)
                    + self.g*np.sin(theta2)*np.cos(d_th)
                    + self.L2*omega2**2*np.sin(d_th)
                    - 2*self.g*np.sin(theta1))
                    / (2*self.L1 - self.L1*np.cos(d_th)**2))

        domega2_dt = ((-self.L2*omega2**2*np.sin(d_th)*np.cos(d_th)
                    + 2*self.g*np.sin(theta1)*np.cos(d_th)
                    - 2*self.L1*omega1**2*np.sin(d_th)
                    - 2*self.g*np.sin(theta2))
                    / (2*self.L2 - self.L2*np.cos(d_th)**2))


        return dtheta1_dt, domega1_dt, dtheta2_dt, domega2_dt


    def solve(self, U0, T, dt, angle="rad"):
        """Method for solving the ODE with initial conditions"""

        self.dt = dt

        if angle == "deg":
            U0[0] = np.radians(U0[0])
            U0[2] = np.radians(U0[2])
        elif angle == "rad":
            pass

        else:
            raise TypeError

        t_ev = np.linspace(0, T, int(T/self.dt) + 1)

        sol = solve_ivp(self.__call__, [0, T], U0, t_eval=t_ev)

        self._t = t_ev
        self._theta1 = sol.y[0]
        self._omega1 = sol.y[1]
        self._theta2 = sol.y[2]
        self._omega2 = sol.y[3]

    # ODE solution arrays
    @property
    def t(self):
        return self._t

    @property
    def theta1(self):
        return self._theta1

    @property
    def omega1(self):
        return self._omega1

    @property
    def theta2(self):
        return self._theta2

    @property
    def omega2(self):
        return self._omega2

    # cartesian transformation
    @property
    def x1(self):
        return self.L1*np.sin(self.theta1)

    @property
    def y1(self):
        return -self.L1*np.cos(self.theta1)

    @property
    def x2(self):
        return self.x1 + self.L2*np.sin(self.theta2)

    @property
    def y2(self):
        return self.y1 - self.L2*np.cos(self.theta2)


if __name__ == "__main__":
    """Run example"""
    dp = DoublePendulum()
    U0 = (np.pi/2, 0, np.pi/2, 0)
    dp.solve(U0, T=100, dt=0.001)
    plt.plot(dp.x2, dp.y2)
    plt.show()

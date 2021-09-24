import scipy
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np

class ExponentialDecay:
	""" ODE class for exponential decay """


	def __init__(self, a):
		self.a = a
		if a < 0:
			raise ValueError
		else:
			pass

	def __call__(self, t, u):
		return -self.a*u

	def solve(self, U0, T, dt):
		"""Method for solving the ODE with initial conditions"""

		t_ev = np.linspace(0, T, int(T/dt) + 1) # setting up dt evaluation

		sol = solve_ivp(self.__call__, [0, T], [U0], t_eval=t_ev)
		return sol.t, sol.y[0]


if __name__ == "__main__":
	"""Run example"""

	decay_model = ExponentialDecay(2)
	t, u = decay_model.solve(1, 7, 0.001)
	plt.plot(t, u)
	plt.show()

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

		self.dt = dt

		if angle == "deg":
			U0[0] = np.radians(U0[0])

		elif angle == "rad":
			pass

		else:
			raise TypeError


		t_ev = np.linspace(0, T, int(T/self.dt) + 1)
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
		return self.L*np.sin(self.theta)

	@property
	def y(self):
		return -self.L*np.cos(self.theta)

	@property
	def P(self):
		"""Potential Energy"""
		P = self.M*self.g*(self.y + self.L)
		return P

	@property
	def K(self):
		"""Kinetic Energy"""

		v_x = np.gradient(self.x, self.dt)
		v_y = np.gradient(self.y, self.dt)

		K = (1/2)*self.M*(v_x**2 + v_y**2)
		return K

	@property
	def E(self):
		"""Total Energy"""
		return self.P + self.K



class DampenedPendulum(Pendulum):
	def __init__(self, L=1, M=1, g=9.81, B = 1):
		self.B = B
		super().__init__(L=1, M=1, g=9.81)

	def __call__(self, t, y):
		"""Setting up ODEs"""
		theta, omega = y
		d_theta = omega
		d_omega = -(self.g/self.L)*np.sin(theta) - (self.B/self.M)*omega
		return d_theta, d_omega



if __name__ == "__main__":
	"""Run example"""

	instance = Pendulum(2)
	U0=(0,1)
	instance.solve(U0, 10, 0.00001)

	plt.plot(instance.t, instance.P, label="P")
	plt.plot(instance.t, instance.K, label="K")
	plt.plot(instance.t, instance.E, label="E")
	plt.legend()

	plt.show()

	plt.plot(instance.t, instance.omega)
	plt.show()


	instance = DampenedPendulum(2)
	U0=(0,1)
	instance.solve(U0, 10, 0.00001)

	plt.plot(instance.t, instance.P, label="P")
	plt.plot(instance.t, instance.K, label="K")
	plt.plot(instance.t, instance.E, label="E")
	plt.legend()

	plt.show()

	plt.plot(instance.t, instance.omega)
	plt.show()

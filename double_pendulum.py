import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from matplotlib import animation

class DoublePendulum():
	def __init__(self, L1=1, L2=1, M1=1, M2=1, g=9.81):
		self.L1 = L1
		self.L2 = L2
		self.M1 = M1
		self.M2 = M2
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

		sol = solve_ivp(self.__call__, [0, T], U0, t_eval=t_ev, method="Radau")

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

	# energy
	@property
	def P(self):
		"""Kinetic Energy"""

		P_1 = self.M1*self.g*(self.y1+self.L1)
		P_2 = self.M2*self.g*(self.y2+  self.L1 + self.L2)
		return P_1 + P_2

	@property
	def K(self):
		"""Kinetic Energy"""

		vx1 = np.gradient(self.x1, self.dt)
		vy1 = np.gradient(self.y1, self.dt)
		vx2 = np.gradient(self.x2, self.dt)
		vy2 = np.gradient(self.y2, self.dt)

		K1 = (1/2)*self.M1*(vx1**2 + vy1**2)
		K2 = (1/2)*self.M2*(vx2**2 + vy2**2)
		return K1 + K2

	@property
	def E(self):
		"""Total energy"""
		return self.P + self.K


	def create_animation(self):
	# Create empty figure
		fig = plt.figure()

		# Configure figure
		plt.axis('equal')
		plt.axis('off')
		plt.axis((-3, 3, -3, 3))

		# Make an "empty" plot object to be updated throughout the animation
		self.pendulums, = plt.plot([], [], 'ko-', lw=2)

		# Call FuncAnimation
		self.animation = animation.FuncAnimation(fig,
												 self._next_frame,

												 frames=range(len(self.x1)),

												 repeat=None,
												 interval=1000*self.dt,
												 blit=True)



	def _next_frame(self, i):
		self.pendulums.set_data((0, self.x1[i], self.x2[i]),
								(0, self.y1[i], self.y2[i]))
		return self.pendulums,

	def show_animation(self):
		plt.show()

	def save_animation(self, filename):
		self.animation.save(filename, fps=60, bitrate=-1)

if __name__ == "__main__":
	"""Run example"""
	one_degree = 2*np.pi/360
	model = DoublePendulum()
	U0 = (np.pi, 0, np.pi-one_degree, 0)
	model.solve(U0, T=10, dt=0.01)
	model.create_animation()
#    model.show_animation()
	model.save_animation("dp_benjabor.mp4")

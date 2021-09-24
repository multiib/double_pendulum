from pendulum import *
import pytest

def test_pendulum_call():
	"""Test call method in class Pendulum"""

	instance = Pendulum(2.7)
	d_theta, d_omega = instance(1, [np.pi/6, 0.15])
	assert d_theta == 0.15
	assert d_omega == pytest.approx(-109/60)


def test_properties():
	"""Testing that the properties are working correctly"""

	instance = Pendulum(2)

	with pytest.raises(AttributeError):
		v1 = instance.t
		v2 = instance.theta
		v3 = instance.omega
	with pytest.raises(UnboundLocalError):

		type(v1) == float
		type(v1) == float
		type(v1) == float

def test_initial_conditions():
	"""Testing that our ODE return values are correct"""
	instance = Pendulum()
	instance.solve((0, 0), 10, 0.01)
	test_array = np.linspace(0, 10, int(10/0.01) + 1)

	for i in range(len(instance.t)):
		assert instance.t[i] == test_array[i]
		assert instance.theta[i] == 0
		assert instance.omega[i] == 0

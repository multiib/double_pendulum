from exp_decay import *
import pytest

def test_ExponentialDecay_a_is_positive():
	"""
	Testing that class ExponentialDecay can't take in a negative number.
	"""

	with pytest.raises(ValueError):
		negative_instance = ExponentialDecay(-1)


def test_ExponentialDecay_correct_calculation():
	"""
	Testing correct calculation in ODE
	"""
	calc_instance = ExponentialDecay(0.4)
	assert calc_instance(1, 3.2) == pytest.approx(-1.28)


dt = 0.00001
@pytest.mark.parametrize(
	"t_, out", [(1/dt + 1, 0.5413411329), (2/dt + 1, 0.0732625556), (3/dt + 1, 0.0099150087)]
)

def test_ExponentialDecay_solve(t_, out):
	"""
	Testing that the solve method is implemented correctly.
	"""

	allowed_error = 1e-03
	decay_model = ExponentialDecay(2)

	t, u = decay_model.solve(4, 5, dt)

	assert abs(u[int(t_) +1] - out) <= allowed_error

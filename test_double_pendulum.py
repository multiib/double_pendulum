from double_pendulum import *
import pytest

@pytest.mark.parametrize(
	"theta1, theta2, expected",
	[
		(  0,   0,            0),
		(  0, 0.5,  3.386187037),
		(0.5,   0, -7.678514423),
		(0.5, 0.5, -4.703164534),
	]
)
def test_domega1_dt(theta1, theta2, expected):
	"""Testing ODE is implemented correctly"""
	dp = DoublePendulum()
	t = 0
	y = (theta1, 0.25, theta2, 0.15)
	dtheta1_dt, domega1_dt, _, _ = dp(t, y)
	assert np.isclose(dtheta1_dt, 0.25)
	assert np.isclose(domega1_dt, expected)

@pytest.mark.parametrize(
	"theta1, theta2, expected",
	[
		(  0,   0,          0.0),
		(  0, 0.5, -7.704787325),
		(0.5,   0,  6.768494455),
		(0.5, 0.5,          0.0),
	],
)
def test_domega2_dt(theta1, theta2, expected):
	"""Testing ODE is implemented correctly"""
	dp = DoublePendulum()
	t = 0
	y = (theta1, 0.25, theta2, 0.15)
	_, _, dtheta2_dt, domega2_dt = dp(t, y)
	assert np.isclose(dtheta2_dt, 0.15)
	assert np.isclose(domega2_dt, expected)

@pytest.mark.parametrize(
	"prop", [
			"t", "theta1", "omega1", "theta2", "omega2",
			"x1", "y1", "x2", "y2", "P", "K", "E"
			]
)
def test_property(prop):
	"""
	Testing @property is working as expected
	by trying to set attribute.
	"""
	dp = DoublePendulum()
	dp.solve((1, 0, 1, 0), T=10, dt=0.01)

	with pytest.raises(AttributeError):
		setattr(dp,f"{prop}", 1)

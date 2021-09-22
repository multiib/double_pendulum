from pendulum import *
import pytest

def test_pendulum_call():
    """Test call method in class Pendulum"""

    instance = Pendulum(2.7)
    d_theta, d_omega = instance(1, [np.pi/6, 0.15])
    assert d_theta == 0.15
    assert d_omega == pytest.approx(-109/60)

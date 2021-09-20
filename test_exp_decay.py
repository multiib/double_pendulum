from exp_decay import *
import pytest



def test_ExponentialDecay_a_is_positive():
    """
    Testing that class ExponentialDecay can't take in a negative number.
    """

    with pytest.raises(ValueError):
        negative_instance = ExponentialDecay(-1)

def test_ExponentialDecay_correct_calculation():
    calc_instance = ExponentialDecay(0.4)
    assert calc_instance(1, 3.2) == pytest.approx(-1.28)

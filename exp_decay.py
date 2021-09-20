import scipy

class ExponentialDecay:
    """
    ODE class for exponential decay.
    """
    def __init__(self, a):
        self.a = a
        if a < 0:
            raise ValueError
        else:
            pass

    def __call__(self, t, u):
        a = self.a
        return -a*u

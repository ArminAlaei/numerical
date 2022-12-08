import numpy as np
import matplotlib.pyplot as plt
from ODESolver import *
class ODESolver:
    def __init__(self, f):
        self.f = f
    def advance(self):
        """Advance solution one time step."""
        raise NotImplementedError # implement in subclass

    def set_initial_condition(self, U0):
        self.U0 = float(U0)

    def solve(self, time_points):
        self.t = np.asarray(time_points)
        N = len(self.t)
        self.u = np.zeros(N)
        # Assume that self.t[0] corresponds to self.U0
        self.u[0] = self.U0
        # Time loop
        for n in range(N-1):
            self.n = n
            self.u[n+1] = self.advance()
        return self.u, self.t

class ExplicitMidpoint(ODESolver):
    def advance(self):
        u, f, n, t = self.u, self.f, self.n, self.t
        dt = t[n+1] - t[n]
        dt2 = dt/2.0
        k1 = f(u[n], t)
        k2 = f(u[n] + dt2*k1, t[n] + dt2)
        unew = u[n] + dt*k2
        return unew


def f(u, t):
    return np.cos(t)-t*np.sin(t)

time_points = np.linspace(0, 4*np.pi, 20)
em = ExplicitMidpoint(f)
fe = ForwardEuler(f)
fe.set_initial_condition(U0=0)
em.set_initial_condition(U0=0)


u,t = fe.solve(time_points)
ex = t*np.cos(t)
u2, t2 = em.solve(time_points)
plt.plot(t2, u2, label='Explicit Midpoint')
plt.plot(t, u, label='Forward Euler')
plt.plot(t,ex, label = 'Exact')
plt.grid()
plt.legend()
plt.show()


"""

Run example:

user$ python3 Midpoint.py

plots attached
"""

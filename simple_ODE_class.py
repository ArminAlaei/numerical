#Problem E.2. Solve a simple ODE with class-based code

import numpy as np
import matplotlib.pyplot as plt

class ForwardEuler_v1:
    def __init__(self, f, U0, T, N):
        self.f, self.U0, self.T, self.N = f, U0, T, N
        self.dt = T/float(N)
        self.u = np.zeros(self.N+1)
        self.t = np.zeros(self.N+1)

    def solve(self):
        """Compute solution for 0 <= t <= T."""
        self.u[0] = float(self.U0)
        self.t[0] = float(0)
        for n in range(self.N):
            self.n = n
            self.t[n+1] = self.t[n] + self.dt
            self.u[n+1] = self.advance()
        return self.u, self.t

    def advance(self):
        """Advance the solution one time step."""
        # Create local variables to get rid of "self." in
        # the numerical formula
        u, dt, f, n, t = self.u, self.dt, self.f, self.n, self.t
        unew = u[n] + dt*f(u[n], t[n])
        return unew

    def plot(self):
        ex = 0.1 * np.exp(t / 5)
        plt.plot(self.t,ex, label = "exact")
        plt.plot(self.t,self.u, label = "numerical")
        plt.grid()
        plt.legend()
        plt.show()

class RightHandFunction:
    def __init__(self, U0):
        self.U0 = U0
    def __call__(self, u, t): # f(u,t)
        return u/5


problem = RightHandFunction(0.1)
method = ForwardEuler_v1(problem,problem.U0,5,10)
u,t = method.solve()
method.plot()

"""

Run example:

user$ python3 simple_ODE_class.py

plots are attached 

"""

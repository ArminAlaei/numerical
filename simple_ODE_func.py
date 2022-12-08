#Problem E.1. Solve a simple ODE with function-based code

import numpy as np
import matplotlib.pyplot as plt

def ForwardEuler(f, U0, T, n):
    """Solve u’=f(u,t), u(0)=U0, with n steps until t=T."""
    t = np.zeros(n+1)
    u = np.zeros(n+1) # u[k] is the solution at time t[k]
    u[0] = U0
    t[0] = 0
    dt = T/float(n)
    for k in range(n):
        t[k+1] = t[k] + dt
        u[k+1] = u[k] + dt*f(u[k], t[k])
    return u, t

#b)
def f(u, t):
    return u/5

#c)
u, t = ForwardEuler(f, U0=0.1, T=5, n=20)

#d)
plt.plot(t,u, label = "numerical")
plt.plot(t,ex, label = "exact")
plt.legend()
plt.grid()
plt.show()

#f)

t_vals = [1,2,3,4,5]

for ts in t_vals:
    u, t = ForwardEuler(f, U0=0.1, T=ts, n=5)
    ex = 0.1*np.exp(t/5)
    plt.plot(t,u, label = "T = "+str(ts))
plt.plot(t,ex, label = "exact")
plt.legend()
plt.grid()
plt.show()


"""
Run example:

user$ python3 simple_ODE_func.py

a) We have the ODE  u-5u'=0, where u(0)=0.1

We rewrite this in the form u'=f(u,t) which becomes:

u' = u/5

Rest of the tasks are marked in the code and plots
are attached.
"""

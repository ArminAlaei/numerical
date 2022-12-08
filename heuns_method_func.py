import numpy as np
import matplotlib.pyplot as plt

#a)
T = 10
U0 = 1
N = 5

def heuns_method(f, U0, T, N):
    """Solve u’=f(u,t), u(0)=U0, with n steps until t=T."""

    t = np.zeros(N+1)
    u = np.zeros(N+1) # u[n] is the solution at time t[n]
    u[0] = U0
    t[0] = 0
    dt = T/N
    for i in range(N):
        #heuns method
        t[i + 1] = t[i] + dt
        K1 = f(u[i], t[i])
        K2 = f(u[i] + (K1*dt), t[i] + dt)
        u[i + 1] = u[i] + dt*((K1/2) + (K2/2))
    return u, t

#defining function
def f(u, t):
    return u/5


u, t = heuns_method(f, U0=U0, T=T, N=N)
#b)

#comparing the solution at one timestep
def test_heuns_against_hand_calculations():
    f = lambda u, t: u
    computed = heuns_method(f, U0=U0, T=T, N=N)
    expected =4.0
    print(computed[1][2])
    success = computed[1][2] == expected
    msg = f'computed {computed[1][2]}, expected {expected}'
    assert success, msg


#c)
N_vals = [5,6,7,8,9]
for ns in N_vals:
    dt = ns/T
    u, t =heuns_method(f, U0=U0,T=T, N=ns)
    ex = 1 * np.exp(t / 5)
    plt.plot(t,u, label = "dt = "+str(dt))
plt.plot(t,ex, label = "exact", marker = "o")
plt.legend()
plt.grid()
plt.show()


"""
Run example:

user$ python3 heuns_method_func.py

(test function passes using pytest in terminal/pycharm)

"""

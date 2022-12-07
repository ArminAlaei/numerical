#Problem 8.7. Numerical approximations of the derivative
import numpy as np
import matplotlib.pyplot as plt

class  Diff:

    def __init__(self, f,h=0.1):
        self.f = f
        self.h = float(h)


    def diff1(self):
        f, h = self.f, self.h
        return (f(x+h) - f(x))/h

    def diff2(self):
        f, h = self.f, self.h
        return (f(x+(h/2)) - f(x-(h/2)))/h #writing approximation such that we only divide by h

    def diff3(self):
        f, h = self.f, self.h
        return (-f(x + (h/6)) + 8 * f(x + h/12) - 8 * f(x - h/12) + f(x - (h/6))) / h

x = np.linspace(-1,1)

#function to be approximated
def g(x):
    return np.sin(2*np.pi*x)

exact = 2*np.pi*np.cos(2*np.pi*x)

df = Diff(g)
plt.plot(x,df.diff1(),label = "diff1")
plt.plot(x,df.diff2(),label = "diff2")
plt.plot(x,df.diff3(),label = "diff3")
plt.plot(x,exact, label = "Exact")
plt.grid()
plt.title("h = 0.1")
plt.legend()
plt.show()

"""
Run example:

user$ python3 class_diff.py
output:
Plots attached for different h values.
We see improvement of the approximation for lower h values.

"""

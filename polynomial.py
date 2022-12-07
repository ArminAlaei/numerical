# Problem 9.2. Implement Polynomials as a Class

class Quadratic:
    def __init__(self, coefficients):
        self.coeff = coefficients
    def __call__(self, x):
        self.svar=(self.coeff[2]*(x**2))+(self.coeff[1]*x)+(self.coeff[0])
        return self.svar


    def __str__(self):
        return f"{self.coeff[0]} + {self.coeff[1]}*x + {self.coeff[2]}*x^2"


class Cubic(Quadratic):

    def __call__(self,x):
        return Quadratic.__call__(self,x)+ self.coeff[3]*(x**3)
    def __str__(self):
        return Quadratic.__str__(self) + f" + {self.coeff[3]}*x^3"

    def derivative(self):
        deriv = Quadratic([self.coeff[1], 2*self.coeff[2], 3*self.coeff[3]])
        return deriv


print("a)")
a = [1,3,2]
x_1 = 1
x_2 = 2
b = Quadratic(a)
print(b)
print(b(x_1))
print(b(x_2))
print()
print("b)")
d = [1,3,2,4]
f = Cubic(d)

print(f(x_1))
print(f(x_2))

print(f.derivative())




"""
Run example:

user$ python3 polynomial.py
output:

a)
1 + 3*x + 2*x^2
6
15

b)
10
47
3 + 4*x + 12*x^2

"""

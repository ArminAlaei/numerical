#Problem 8.9. A class for coordinates

from math import *
class Coords:

    def __init__(self, x,y,z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __str__(self):
        return f"({self.x},{self.y},{self.z})"
    def __len__(self):
        return len((self.x,self.y,self.z))
    def __abs__(self):
        return sqrt(self.x**2+self.y**2+self.z**2)

    def __add__(self,other):
        x2 = self.x+other.x
        y2 =self.y+other.y
        z2 = self.z+other.z

        return Coords(x2,y2,z2)


    def __sub__(self,other):
        x_2 = self.x-other.x
        y_2 =self.y-other.y
        z_2 = self.z-other.z
        return Coords(x_2,y_2,z_2)


sqrt3 = sqrt(3)
close = Coords(1/sqrt3, 1/sqrt3, 1/sqrt3)
far = Coords(3/sqrt3, 15/sqrt3, 21/sqrt3)

print("a)")
print()
print(close)
print(far)
print()
print("b)")
print(f"The class represents coordinates in {len(close)} dimensions")
print(f"The distance from the centre to the point close is {abs(close)}")
print(f"The distance from the centre to the point far is {abs(far)}")
print()
print("c)")
further = close + far
print(f"The coordinates further are at {further}")
distance = abs(far - close)
print(f"The distance from far to close is {distance}")
centre = further - further
print(f"The coordinates at the centre are {centre}")
"""
Run example:

user$ python3 Coords.py
output:
a)

(0.5773502691896258,0.5773502691896258,0.5773502691896258)
(1.7320508075688774,8.660254037844387,12.124355652982143)

b)
The class represents coordinates in 3 dimensions
The distance from the centre to the point close is 1.0
The distance from the centre to the point far is 15.000000000000002

c)
The coordinates further are at (2.3094010767585034,9.237604307034013,12.701705922171769)
The distance from far to close is 14.142135623730953
The coordinates at the centre are (0.0,0.0,0.0)


"""

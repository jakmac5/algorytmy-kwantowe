import numpy as np
from complex import Complex
import cmath
import math




class Vector:

    def __init__(self, values = []):
        self.values = values

    def __add__(self, other):
    	temp = []
    	for j in range(len(self.values)):
    		temp.append(self.values[j] + other.values[j])
    	return Vector(temp)

    def __sub__(self, other):
    	temp = []
    	for j in range(len(self.values)):
    		temp.append(self.values[j] - other.values[j])
    	return Vector(temp)

    def skalar(self, n):
        temp = []
        for j in range(len(self.values)):
            temp.append(self.values[j] * n)
        return Vector(temp)

    def __mul__(self, other):
        temp = Complex(0, 0)
        for j in range(len(self.values)):
             temp = temp + (self.values[j] * other.values[j].sprz())
        return temp

    def norma(self):
        temp = Complex(0, 0)
        for j in range(len(self.values)):
             temp = temp + (self.values[j] * self.values[j].sprz())
        return temp**0.5

    def __repr__(self):
        return str(self.values)

a = Complex(1, 0)
b = Complex(0.707106781186, 0.707106781186) + Complex(1, 0)
vector1 = Vector([a, b])
print(vector1 * vector1)

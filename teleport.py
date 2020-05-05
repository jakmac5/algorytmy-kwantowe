from qubit import Qubit, tensordot, Hadamard, Cnot, Measure, Identity, RCnot, randomQubit, PauliX, PauliY, PauliZ, M0, M1
from complex import Complex
import numpy as np
import math

#Inicjalizacja Bramek
X = PauliX()
H = Hadamard()
CNOT = Cnot()
RCNOT = RCnot()
I = Identity()
M0 = M0()
M1 = M1()

x = Qubit(Complex(1, 0), Complex(0, 0))
y = Qubit(Complex(1, 0), Complex(0, 0))

#Splątanie

x = x * H
xy = tensordot(x, y)
xy = np.tensordot(CNOT, xy, axes=[1,0])
print("splątany = ", xy)

#Qubit do teleportowania
psi = randomQubit()
# psi = Qubit(Complex(0, 0), Complex(1, 0))
print("Qubit po stronie Alicji")
print("psi = ", psi.alpha, psi.beta)

#Pierwszy Krok
# first = np.kron(xy, psi.vector())
first = np.kron(psi.vector(), xy)
print("pierwszy = ", first)

#Drugi Krok
Cnot = np.kron(CNOT, I)
# print(Cnot)
second = np.tensordot(Cnot, first, axes=[1,0])
print("drugi = ", second)

#Trzeci Krok
H = np.kron(H, I)
H = np.kron(H, I)
# print(H)
third = np.tensordot(H, second, axes=[1,0])
print("trzeci = ", third)

#Pomiar

M01 = np.kron(M0, M1)
M010 = np.kron(M01, I)
# print(M010)

P = np.tensordot(M010, third, axes=[1,0])
print(P)

for i in range(len(P)):
    print(i," ",P[i])

alpha = P[2] * 2
beta = P[3] * 2
# print(alpha, beta)

#Qubit po teleportacji
psi = Qubit(alpha, beta)
psi = psi * X
print("Qubit po stronie Boba")
print("psi = ", psi.alpha, psi.beta)

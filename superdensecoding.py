from qubit import Qubit, tensordot, Hadamard, Cnot, Measure, Identity, RCnot, randomQubit, PauliX, PauliY, PauliZ, M0, M1
from complex import Complex
import numpy as np
import math

#Inicjalizacja Bramek
X = PauliX()
Y = PauliY()
Z = PauliZ()
H = Hadamard()
CNOT = Cnot()
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

#Pierwszy krok
print("What to code? type 00 , 01 , 10 or 11")
opcja = input()
if opcja == '00':
    II=np.kron(I,I)
    print("I and I gate: ",II)
    first = np.tensordot(II,xy,axes=[1,0])
elif opcja == '01':
    X = np.kron(X, I)
    print("Gate X and I: ",X)
    first = np.tensordot(X, xy, axes=[1,0])
elif opcja == '10':
    Z = np.kron(Z, I)
    print("Gate Z and I: ",Z)
    first = np.tensordot(Z, xy, axes=[1,0])
elif opcja == '11':
    XZ = np.tensordot(X, Z, axes=[1,0])
    XZ = np.kron(XZ, I)
    print("gate X and Z: ", XZ)
    first = np.tensordot(XZ, xy, axes=[1,0])
print("After first step: ",first)

#Drugi krok
second = np.tensordot(CNOT, first, axes=[1,0])
print("After second step: ",second)

#Trzeci krok
H = np.kron(H, I)
third = np.tensordot(H, second, axes=[1,0])
print("Last step before measure: ",third)

#Pomiar

if opcja=='00':
    M00 = np.kron(M0, M0)
    P = np.tensordot(M00, third, axes=[1,0])
    print(P)
elif opcja=='01':
    M01 = np.kron(M0, M1)
    P = np.tensordot(M01, third, axes=[1,0])
    print(P)
elif opcja=='10':
    M10 = np.kron(M1, M0)
    P = np.tensordot(M10, third, axes=[1,0])
    print(P)
elif opcja=='11':
    M11 = np.kron(M1, M1)
    P = np.tensordot(M11, third, axes=[1,0])
    print(P)

"""Este  programa calcula la tension de 3 cables que soportan una fuerza de 1800 N
Elaborado por Juan Sebastian Moreno Posada"""
import math

t1 = (5, 10, 2)
t2 = (-4, 10, 0)
t3 = (0, 10, -6)
fuerza = 1800

print("El vector del cable 1 es: ", t1)
print("El vector del cable 2 es: ", t2)
print("El vector del cable 3 es: ", t3)
print("La fuerza que sostienen es: ", fuerza , "N")

print("\n")

t1Magnitud = math.sqrt(t1[0]**2 + t1[1]**2 + t1[2]**2)
t2Magnitud = math.sqrt(t2[0]**2 + t2[1]**2 + t2[2]**2)
t3Magnitud = math.sqrt(t3[0]**2 + t3[1]**2 + t3[2]**2)
print("La magnitud del cable 1 es: ", t1Magnitud)
print("La magnitud del cable 2 es: ", t2Magnitud)
print("La magnitud del cable 3 es: ", t3Magnitud)

print("\n")

unitarioT1 = (t1[0]/t1Magnitud, t1[1]/t1Magnitud, t1[2]/t1Magnitud)
unitarioT2 = (t2[0]/t2Magnitud, t2[1]/t2Magnitud, t2[2]/t2Magnitud)
unitarioT3 = (t3[0]/t3Magnitud, t3[1]/t3Magnitud, t3[2]/t3Magnitud)
print("El vector unitario del cable 1 es: ", unitarioT1)
print("El vector unitario del cable 2 es: ", unitarioT2)
print("El vector unitario del cable 3 es: ", unitarioT3)

matrixA = [[unitarioT1[0], unitarioT2[0], unitarioT3[0]], 
[unitarioT1[1], unitarioT2[1], unitarioT3[1]], 
[unitarioT1[2], unitarioT2[2], unitarioT3[2]]]

vectorIgualdad = [0, fuerza, 0]

print("\n")
print("La matriz A es: \n", matrixA[0], "\n", matrixA[1], "\n", matrixA[2])

detA = (matrixA[0][0]*(matrixA[1][1]*matrixA[2][2]- (matrixA[1][2]*matrixA[2][1])) 
- matrixA[1][0] * (matrixA[0][1] * matrixA[2][2] - matrixA[0][2] * matrixA[2][1]) 
+ matrixA[2][0] * (matrixA[0][1] * matrixA[1][2] - matrixA[0][2] * matrixA[1][1]))
print("El determinante de A es: ", detA)

matrixAx = [[vectorIgualdad[0], unitarioT2[0], unitarioT3[0]], 
[vectorIgualdad[1], unitarioT2[1], unitarioT3[1]], 
[vectorIgualdad[2], unitarioT2[2], unitarioT3[2]]]

print("\n")

print("La matriz X es: \n", matrixAx[0], "\n", matrixAx[1], "\n", matrixAx[2], "\n ")
detAx = (matrixAx[0][0]*(matrixAx[1][1]*matrixAx[2][2]- (matrixAx[1][2]*matrixAx[2][1])) 
- matrixAx[1][0] * (matrixAx[0][1]*matrixAx[2][2] - matrixAx[0][2] * matrixAx[2][1]) 
+ matrixAx[2][0]* (matrixAx[0][1] * matrixAx[1][2] - matrixAx[0][2] * matrixAx[1][1]))
print("El determinante de X es: ", detAx)

Tension1 = detAx/detA


matrixAy = [[unitarioT1[0], vectorIgualdad[0], unitarioT3[0]], 
[unitarioT1[1], vectorIgualdad[1], unitarioT3[1]], 
[unitarioT1[2], vectorIgualdad[2], unitarioT3[2]]]

print("\n")

print("La matriz Y es: \n", matrixAy[0], "\n", matrixAy[1], "\n", matrixAy[2], "\n")
detAy = matrixAy[0][0]*(matrixAy[1][1]*matrixAy[2][2]- (matrixAy[1][2]*matrixAy[2][1])) - matrixAy[1][0] * (matrixAy[0][1]*matrixAy[2][2] - matrixAy[0][2] * matrixAy[2][1]) + matrixAy[2][0]* (matrixAx[0][1] * matrixAy[1][2] - matrixAy[0][2] * matrixAy[1][1])
print("El determinante de Y es: ", detAy)
Tension2 = detAy/detA


matrixAz = [[unitarioT1[0], unitarioT2[0], vectorIgualdad[0]], 
[unitarioT1[1], unitarioT2[1], vectorIgualdad[1]], 
[unitarioT1[2], unitarioT2[2], vectorIgualdad[2]]]

print("\n")

print("La matriz Z es: \n", matrixAz[0], "\n", matrixAz[1], "\n", matrixAz[2], "\n")
detAz = (matrixAz[0][0]*(matrixAz[1][1]*matrixAz[2][2]- (matrixAz[1][2]*matrixAz[2][1])) 
- matrixAz[1][0] * (matrixAz[0][1]*matrixAz[2][2] - matrixAz[0][2] * matrixAz[2][1]) 
+ matrixAz[2][0]* (matrixAz[0][1] * matrixAz[1][2] - matrixAz[0][2] * matrixAz[1][1]))
print("El determinante de Z es: ", detAz)
Tension3 = detAz/detA

print("\n")

print("Por lo tanto... \n")
print("La tension del cable 1 es: ", Tension1, "N")
print("La tension del cable 2 es: ", Tension2, "N")
print("La tension del cable 3 es: ", Tension3, "N")
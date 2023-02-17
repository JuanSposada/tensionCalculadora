"""-este programa  calcula la resultante de 3 vectores en R2
Elaborado por Juan Sebastian Moreno Posada"""
import math
#declaracion de variables
"Vector A"
magnitudA = 800
anguloA = math.radians(20)
"Vector B"
magnitudB = 120
anguloB = math.radians(120)
"Vector C"
magnitudC = 225
anguloC = math.radians(210)
#Calculo de las componentes de los vectores
Ax = (math.cos(anguloA)*magnitudA)
Bx = (math.cos(anguloB)*magnitudB)
Cx = (math.cos(anguloC)*magnitudC)
Rx = Ax + Bx + Cx #resultante en x
Ay = (math.sin(anguloA)*magnitudA)
By = (math.sin(anguloB)*magnitudB)
Cy = (math.sin(anguloC)*magnitudC)
Ry = Ay + By + Cy #resultante en y
R = math.sqrt(Rx**2 + Ry**2)
anguloR = math.atan2(Ry, Rx)
print("La magnitud de la resultante es: ", round(R, 2))
print("El angulo de la resultante es: ", round(math.degrees(anguloR), 2))

"""Este programa calcula las componentes de un vector 
Elaborado por: Juan Sebastian Moreno Posada"""

import math

#Declaracion de variables
maginitud = 100
angulo = math.radians(35)

print("La magnitud del vector es: ", maginitud)
print("El angulo del vector es: ", math.degrees(angulo))

#Calculo de las componentes del vector
dx = (math.cos(angulo)*100)
dy = (math.sin(angulo)*100)


print("La componente dx es: ", round(dx, 2))
print("La componente dy es: ", round(dy, 2))

"""
Andrés Enrique Jaime de la Rosa, 763799
18/09/25
El propósito de este código es definir si un año es bisiesto
"""



# Entradas
año = int(input("Introduzca un año: "))


if año % 400 == 0:
    print(año,"sí es un año bisiesto")
elif año % 100 == 0:
    print(año,"no es un año bisiesto")
elif año % 4 == 0:
    print(año,"sí es un año bisiesto")
else:
    print(año,"no es un año bisiesto")


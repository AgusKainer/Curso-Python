"""
TIPO DE DATOS NUMERICOS:
    int (enteros) son los numero enteros.
    float (flotante) son los numeros decimales
    complex (complejo) son los numero enteros e imaginarios
    NOSE PUEDE PASAR UN NUMERO COMPLEJO A NUMERO ENTERO. SIMPLE NO
    range (rango) es una funcion con dos parametros, inicio, fin
    random: es una biblioteca de numeros aleatorios
"""
#TYPE NOS DICE QUE TIPO DE DATOS ES

#INTEGER
numero_entero = 1
# print(type(numero_entero))

# #FLOAT
numero_decimal = 7.56
# print(type(numero_decimal))

# #COMPLEX 
numero_complejo = 5 + 5j
# print(type(numero_complejo))
#RANGE 
range = range(1,10)

#CONVERSION DE NUMEROS
entero_decimal = float(numero_entero)

decimal_entero = int(numero_decimal)

complejo_entero = complex(numero_entero)
complejo_decimal = complex(numero_decimal)

import random

aleatorio = random.randrange(1,10)
#inicion,fin,cada cuanto se saltea
aleatorio_par = random.randrange(2,11,2)

 
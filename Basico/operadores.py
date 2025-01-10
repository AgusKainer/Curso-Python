# Operadores: nos ayudan a realizar operaciones con variabkes y valores

# Aritmeticos +, -, *, /, %, //, **

a = 10
b = 2
suma = a + b
resta = a - b
multi = a * b
division = a / b
divisionEntera = a // b
resto = a % b
exponente = a**b

# asignacion
# si colocamos un operador aritmetico al igual, va hacer la asignacion y la operacion aritmetica

x = 10
x += 3
x -= 3
x /= 3
x *= 3

# Operadores logicos
num1 = 5
num2 = 6

igualdad = num1 == num2
destinto = num1 != num2
mayor = num1 > num2  # mayor o igual >=
menor = num1 < num2  # menor o igual <=

# operadoresAND, OR, NOT
# AND: AMBAS O TODAS LAS CONDICIONES DAN TRUE
# OR: UNA DE LAS CONDICIONES DA TRUE
# NOT: OBVIAMENTE FALSE
edad = 17
tramite = edad >= 18 and edad <= 65
semaforo = "rojo"
cruzar = semaforo == "verde" or semaforo == "amarillo"
verdad = True
mentira = not verdad

# operador de identidad IS, IS NOT

nombre = "agus"
profe = "agus"

mismo = nombre is profe
diferente = nombre is not profe


# OPERADORES DE PERTENCIA IN, NOT IN

palabra = "mundo"
texto1 = "hola mundo"

pertenece = palabra in texto1
noPertenece = palabra not in texto1

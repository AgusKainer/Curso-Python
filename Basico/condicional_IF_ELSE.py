# IF, ELSE, ELIF: nos ayuda a tomar deceisiones, dependiendo la condicion

a = 5
b = 6
c = 8
if a > b:
    print("es mayor a")
elif c > b:
    print("es mayor c")
else:
    print("b es mayo que todos")

edad = 20

if edad >= 18 and edad <= 40:
    print("puede ingresar")
else:
    if edad < 18:
        print("No puede ingresar")
    else:
        print("solo mayores de edad")

# condiciona de una linea o mas fachero,
print("b es mayor que a") if b > a else print("a es mayor que b")

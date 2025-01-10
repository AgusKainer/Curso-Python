# Una de las estructuras mas usadas en la progrmacion. Almacena tdo tipo de datos.

frutas = ["banana", "manzana", "pera"]

# PARA INGRESAR A CADA INDICE
indice = frutas[0]
partesLista = frutas[1:3]  # se modifica depéndendo lo que se necesita
# LONGITUD
longitud = len(frutas)

# MODIFICAR DATOS DE LA LISTA

tecnologias = ["python", "java", "panda", "flask"]
frontend = ["react", "angular", "vuejs"]

# tecnologias[3] = "pandita"  # cambiar un valor
# tecnologias.insert(2, "flask")  # insertar un valor e cierta posicion
# tecnologias.append("tensor")  # agrega valor al final
# tecnologias.extend(frontend)  # agrega otra una lista a otra lista
# tecnologias.remove("vuejs")  # elimina ese valor
# tecnologias.pop()  # elimina el ultimo elemento
# del tecnologias[5]  # eiimina pasando el indice
# tecnologias.clear()  # deja vacia la lista


# recorrer una lista

for i in range(len(tecnologias)):
    # imprime el indice y valor
    print(f"{i}. {tecnologias[i]}")

# ordenar listas
numeros = [5, 9, 3, 7, 2, 91, 965, 216, 21]
numeros.sort()
numeros.reverse()
tecnologias.sort()
print(tecnologias)

# copiar una lista
meses = ["enero", "febrero", "marzo"]
copia = meses.copy()

unirList = meses + copia

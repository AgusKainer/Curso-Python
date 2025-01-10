"""
TIPOS DE DATOS QUE EXISTEN:
    str (string): son los caracteres, se pueden usar comillas simple, doble, triple y triple simple.
    int (enteros) son los numero enteros.
    float (flotante) son los numeros decimales
    complex (complejo) son los numero enteros e imaginarios
    list (listas) un almacen de datos. Pueden almacenar cualquier datos, sring, number, obj, todo
    tuple (tuplas) es un array lista, pero es inmutable, va con parentesis ()
    range (rango) es una funcion con dos parametros, inicio, fin
    dic (diccionario) similar a una lista,array. Pero con clave-valor, va con llaves {}. similar a un objeto, es como un json, todo va con comillas, tanto la clave como el valor(dependiendo del valor de cada clave no?)
    set: es otro tipo de array, pero con la diferencia de que no puede tener valores repetidos, va con llaves {}
    frozenSet: es un set, combinado con tupla, no se puede modificar, sigue manteniendo el tema de no tener valores repetidos ({})
    bol (booleano) verdadero o falso
    !LO UNICO QUE NO SE MODIFICA ES LA TUPLA, EL RESTO TODO SE MODIFICA¡
"""
# STRING
comillaSimple = 'simple'
comillaDoble = "doble"
comillaTriple = """triple"""
comillasSimpleTriple = '''triple simple'''

#INTEGER
numero_entero = 1

#FLOAT
numero_decimal = 7,56

#COMPLEX 
numero_complejo = 5 + 5j

#LIST
lista = [1,8,86,7,4]

#TUPLE
tupla = ("a","b","c")

#RANGE 
range = range(1,10)

#DIC
dic = {"saludo":"hola", "hora": 15.26}

#SET
set = {1,1,9,6,5,9}

#FROZENSET
frozenSet = frozenset({4,2,8,9,4,4,9})

#BOL
booleanoVerdadero = True
booleanoFalse = False
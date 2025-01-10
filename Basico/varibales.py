#Una varibla es un contenedor de datos. guardacualquier tipo de datos.

x = 4 #ya es una variable.
text = "hola"

print(x)
print(text)

#NOMBRES QUE SE PUEDE COLOCAR COMO VARIABLE
mivariable = "texto"
_mivariable = 'simple'
MiOtraVariable = """
triple
"""

print(mivariable)
print(_mivariable)
print(MiOtraVariable)

#No puede iniciar con un numero la variable
# 5variable = "no imprime, da error"

# mientras que no se ocupe un numero para iniciar una variable se puede usar, caracter, simbolo, numero.
varbviale2 = 4
#CaseSensitive
MiVariable = 5
miVariable =6
#No se puede usar palabras reservadas.
#and = 5
#MANERAS DE ESCRIBIR VARIABLE
camelCase = "s"
PascalCase = 2
snake_case =54

#SE PUEDE ASINAR EN UNA MISMA LINEA VARIOS VALORES. TAMBIEN ASIGNAR UN VALOR A VARIAS VARIBLES
x,c,v =7,8,9
a=s=d = "gola"
#EN ESTE CASO CADA VARIABLE OCUPA UN DATO DE LA LISTA
frutas = ["hola", "chau","buenas"]

q,w,e = frutas

#CONCATENACION, SE USA + O , CUALQUIERA DE ELLAS SIRVE. PERO ESO SE APLICA CON STRING, CON NUMERO SE SUMAN
txt = "curso"
txt2 = "de"
txt3 = "python"
# print(txt,txt2,txt3)
# print(txt3 + txt2 + txt)
num1 = 2
num2 = 3
num3 =6
# print(txt,num1) para concatenar string con number, se usa , sino, da error

#VARIABLE GLOBAL Y SCOPE(SIRVE PARA UNA FUNCION ESPECIFICA)
"""
DIRECTAMENTE LA VARIABLE DEL SCOPE NO ME DEJA USAR FUERA DE LA FUNCION
POR MAS QUE CAMBIEMOS EL VALOR DE LA VARIABLE GLOBAL, SIEMPRE TENDRA EL VALOR ORIGINAL.
PARA QUE LA VARIABLE DEL SCOPE SEA GLOBAL SE USA LA PALABRA RESERVADA GLOBAL ANTES DE LA VARIABLE

"""
variableGlobal = "alcance global"

def funcion():
    global variableScope 
    variableScope= "estara en la funcion nomas"
    variableGlobal = "cambiamos su valor"
    print(variableGlobal)
    print(variableScope)

funcion()
print(variableGlobal)
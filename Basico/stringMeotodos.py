"""
str (string): son los caracteres, se pueden usar comillas simple, doble, triple y triple simple.
"""
texto ="curso de python, para alguien"

# STRING
comillaSimple = 'simple'
comillaDoble = "doble"
comillaTriple = """triple"""
comillasSimpleTriple = '''triple simple'''

#METODOS
caracter = texto[2]
print(caracter) #selecciona un caracter
#len (length) longitud
amplitud = len(texto)
#in: para saber si esta dentro, distingue entre mayuscula y minuscula
print("python" in texto)
#slice (cortar) separa o crota un string, toma esa parte del string, comienzo fin, esos son los parametros
print(texto[5:9])
#Modificaciones del texto
text = "texto para modificar"
mayusculas = text.upper()
minusculas = text.lower()
texto_sin_espacios = text.strip() # del principio y final del texto, no entre medio del string
reemplazo = text.replace("modificar","actualizar")
separar_texto = text.split(",")

#Concatenar
a="hola"
b = "mundo"
c= a+b #a + " " + b

#F-String (template string) Combinar variables con variables
num = 5
txt =f"soy el numero {num}"
print(txt)

# Barra invertida \ es para poner comillas dentro deun string, porque si no se rompe

escape = "mi pais favorito es \"Brasil\" pero soy de argentina"

# MAS USADOS
texto_a_modificar = "como esta muchacho"
capitalizacion =texto_a_modificar.capitalize()
esta_comenzando = texto_a_modificar.startswith("mi")
esata_finalizando = texto_a_modificar.endswith("muchacho")
titulo = texto_a_modificar.title()
contador = texto_a_modificar.count("e") 
encontrar = texto_a_modificar.find("esta")

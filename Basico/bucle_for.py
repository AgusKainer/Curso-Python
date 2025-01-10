# estructura que se repite mientras la condicion sea verdadero

lenguajes = ["python", "java", "c++", "c#", "c"]
x = 1
texto = "hola de nuevo"

for tecnologia in lenguajes:
    if tecnologia == "java":
        continue
    print(f"{x}. {tecnologia}")
    x += 1

for letra in texto:
    print(letra)

for x in range(5):
    print(x)

for i in range(2, 4):
    print(i)

for w in range(2, 13, 2):
    print(w)

letras = ["a", "b", "c"]
pares = [2, 4, 6, 8, 10]


for l in letras:
    for q in pares:
        print(l, q)

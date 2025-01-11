print("hola")


class Robot:
    # contructor
    # self se refiere a la instancia
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    # Metodos accion del objeto
    def saludo(self):
        print("Hola, mi nombre es", self.nombre)

    def hacer_truco(self):
        if self.tipo == "Humanoide":
            print("Haciendo un backflip")
        else:
            print("No puedo hacer trucos")


robotin = Robot("Robotin", "Humanoide")
tostadora = Robot("Tostadora", "Electrico")


print(robotin.nombre)
print(robotin.tipo)

robotin.saludo()
tostadora.saludo()

robotin.hacer_truco()
tostadora.hacer_truco()

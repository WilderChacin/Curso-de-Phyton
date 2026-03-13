class estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre 
        self.edad = edad
    def presentarse(self):
        print(f"{self.nombre} Me presento amigos")
    def hablar(self):
        print(f"{self.nombre} Esta Farmeando aura")


class matematicas(estudiante):
    def _init_(self, nombre, edad, nivel):
        super().__init__(nombre,edad)
        self.nivel = nivel
    def mostrar_nivel(self):
        print(f"Tengo tremendo nivel{self.nivel}")

class literatura(estudiante):
    def _init_(self, nombre, edad, genero_favorito):
        super().__init__(nombre,edad)
        self.genero_favorito = genero_favorito
    def mostrar_genero(self):
        print(f"La ciencia ficcion es lo mejor!{self.genero_favorito}")

class fifica(estudiante):
    def __init__(self, nombre, edad, campo_estudio):
        super().__init__(nombre, edad)
        self.campo_estudio = campo_estudio
    def mostrar_campo(self):
            print(f"Mi campo de estudio es la Astrofisica{self.campo_estudio} ")

mortal = estudiante("Wilder", "Chacin", 18)
print(f"Nombre:{mortal.nombre},apellido:{mortal.apellido},Edad:{mortal.edad}")
mortal.presentarse()
mortal.hablar()
mortal.mostrar_nivel()
mortal.mostrar_genero()
mortal.mostar_campo()

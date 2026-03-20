class Dispositivo:
    cantidad_total_registrada = 0

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False
        
        Dispositivo.cantidad_total_registrada += 1

    def cambiar_estado(self):
        if self.encendido:
            self.encendido = False
        else:
            self.encendido = True

class Telefono(Dispositivo):
    def __init__(self, marca, modelo):
        
        super().__init__(marca, modelo)
        self.aplicaciones = []

    def instalar_app(self, nombre_app):
        self.aplicaciones.append(nombre_app)

def mostrar_telefonos_encendidos(lista_telefonos):
    print(" Teléfonos Encendidos ")
    for t in lista_telefonos:
        if t.encendido:
            print(f"Marca: {t.marca} Modelo: {t.modelo}")


t1 = Telefono("Samsung", "S23")
t2 = Telefono("iPhone", "15")
t3 = Telefono("Xiaomi", "Redmi note 10 PRO")

t1.cambiar_estado()  
t3.cambiar_estado()

mostrar_telefonos_encendidos([t1, t2, t3])
print(f"Total dispositivos: {Dispositivo.cantidad_total_registrada}")


print("\n##############################################\n")


class Jugador:
    puntuacion_base = 100

    def __init__(self, nombre_usuario):
        self.nombre_usuario = nombre_usuario
        self.puntos_actuales = Jugador.puntuacion_base

    def ganar_puntos(self, cantidad):
        self.puntos_actuales += cantidad

class JugadorVIP(Jugador):
    def __init__(self, nombre_usuario, multiplicador):
        super().__init__(nombre_usuario)
        self.multiplicador = multiplicador

    def ganar_puntos_vip(self, cantidad):
        
        puntos_bono = cantidad * self.multiplicador
        self.puntos_actuales += puntos_bono

def filtrar_mejores_jugadores(lista_jugadores, puntaje_minimo):
    mejores = []
    for j in lista_jugadores:
        if j.puntos_actuales >= puntaje_minimo:
            mejores.append(j.nombre_usuario)
    return mejores


j1 = Jugador("Kazuto")
j2 = JugadorVIP("Rex_VIP", 2)

j1.ganar_puntos(90)     
j2.ganar_puntos_vip(50)   

ranking = filtrar_mejores_jugadores([j1, j2], 180)
print(f"Jugadores que superan el mínimo: {ranking}")


print("\n########################################################\n")


class Vehiculo:
    costo_por_litro = 1.5  

    def __init__(self, matricula, combustible_litros):
        self.matricula = matricula
        self.combustible_litros = combustible_litros
        self.en_ruta = True

    def viajar(self, kilometros):
        consumo = kilometros / 10
        if self.combustible_litros >= consumo:
            self.combustible_litros -= consumo
            print(f"Vehículo {self.matricula} viajó {kilometros}km.")
        else:
            self.combustible_litros = 0
            self.en_ruta = False
            print(f"¡Alerta! {self.matricula} se quedó sin gasolina.")

class Camion(Vehiculo):
    def __init__(self, matricula, combustible_litros, cargas):
        super().__init__(matricula, combustible_litros)
        self.cargas_entregadas = cargas  

    def entregar_carga(self):
        if len(self.cargas_entregadas) > 0:
            carga = self.cargas_entregadas.pop() 
            print(f"Carga '{carga}' entregada por el camión {self.matricula}.")
        else:
            print(f"El camión {self.matricula} no tiene más cargas.")

def simular_jornada(lista_vehiculos, distancias_a_recorrer):
    
    for vehiculo, distancia in zip(lista_vehiculos, distancias_a_recorrer):
        vehiculo.viajar(distancia)
        
        
        if isinstance(vehiculo, Camion) and vehiculo.en_ruta:
            vehiculo.entregar_carga()


v1 = Vehiculo("ABC-123", 5)      
c1 = Camion("TRUCK-99", 20, ["Comida", "Ropa", "Juguetes"])

flota = [v1, c1]
rutas = [60, 30] 

simular_jornada(flota, rutas)
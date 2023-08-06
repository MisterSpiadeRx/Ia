import random

# Definición de la clase Entidad
class Entidad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mover_arriba(self):
        self.y += 1

    def mover_abajo(self):
        self.y -= 1

    def mover_izquierda(self):
        self.x -= 1

    def mover_derecha(self):
        self.x += 1

# Función para calcular la distancia entre dos entidades
def calcular_distancia(entidad1, entidad2):
    return abs(entidad1.x - entidad2.x) + abs(entidad1.y - entidad2.y)

# Función para aprender a evitar colisiones
def aprendizaje_social(entidades):
    for entidad in entidades:
        # Calcular la distancia a las otras entidades
        distancias = [calcular_distancia(entidad, otra_entidad) for otra_entidad in entidades if otra_entidad != entidad]

        # Encontrar la entidad más cercana
        distancia_minima = min(distancias)

        # Si está demasiado cerca de otra entidad, elegir una dirección aleatoria para moverse
        if distancia_minima < 2:
            opciones = [entidad.mover_arriba, entidad.mover_abajo, entidad.mover_izquierda, entidad.mover_derecha]
            direccion = random.choice(opciones)
            direccion()

# Crear un conjunto de entidades
entidades = [Entidad(random.randint(-10, 10), random.randint(-10, 10)) for _ in range(5)]

# Simular el comportamiento de las entidades durante 10 pasos de tiempo
for paso in range(10):
    print(f"Paso de tiempo {paso+1}:")
    for entidad in entidades:
        print(f"Entidad en ({entidad.x}, {entidad.y})")
    aprendizaje_social(entidades)
    print("-----")

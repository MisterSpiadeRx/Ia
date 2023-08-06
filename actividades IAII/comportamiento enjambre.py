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

# Función para aprender a seguir al líder y mantenerse en formación
def aprendizaje_social(entidades):
    lider = entidades[0]
    seguidores = entidades[1:]

    for seguidor in seguidores:
        # Calcular la distancia al líder
        distancia_lider = calcular_distancia(lider, seguidor)

        # Si el seguidor está lejos del líder, seguirlo
        if distancia_lider > 1:
            if seguidor.x < lider.x:
                seguidor.mover_derecha()
            elif seguidor.x > lider.x:
                seguidor.mover_izquierda()

            if seguidor.y < lider.y:
                seguidor.mover_arriba()
            elif seguidor.y > lider.y:
                seguidor.mover_abajo()

# Crear un enjambre de entidades
lider = Entidad(random.randint(-10, 10), random.randint(-10, 10))
seguidores = [Entidad(random.randint(-10, 10), random.randint(-10, 10)) for _ in range(5)]
entidades = [lider] + seguidores

# Simular el comportamiento del enjambre durante 10 pasos de tiempo
for paso in range(10):
    print(f"Paso de tiempo {paso+1}:")
    for entidad in entidades:
        print(f"Entidad en ({entidad.x}, {entidad.y})")
    aprendizaje_social(entidades)
    print("-----")

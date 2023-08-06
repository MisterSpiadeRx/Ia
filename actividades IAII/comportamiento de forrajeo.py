import random
import math

# Tamaño del área de forrajeo
area_size = 50

# Número de entidades (agentes)
num_entities = 10

# Número de pasos de tiempo para la simulación
num_steps = 100

# Radio de comunicación para compartir información sobre alimentos
communication_radius = 10

# Representación de la ubicación de alimentos en el área
food_locations = [(random.randint(0, area_size), random.randint(0, area_size)) for _ in range(5)]

# Definición de la clase Entidad
class Entidad:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.food_found = []

    def mover(self):
        # Movimiento aleatorio en una dirección
        angle = random.uniform(0, 2 * math.pi)
        distance = random.uniform(0, 3)
        new_x = self.x + distance * math.cos(angle)
        new_y = self.y + distance * math.sin(angle)

        # Limitar el movimiento dentro del área de forrajeo
        self.x = min(max(new_x, 0), area_size)
        self.y = min(max(new_y, 0), area_size)

    def compartir_informacion(self, other_entities):
        for other_entity in other_entities:
            distance = math.sqrt((self.x - other_entity.x) ** 2 + (self.y - other_entity.y) ** 2)
            if distance <= communication_radius:
                for food in other_entity.food_found:
                    if food not in self.food_found:
                        self.food_found.append(food)

# Crear un conjunto de entidades (agentes)
entidades = [Entidad(random.randint(0, area_size), random.randint(0, area_size)) for _ in range(num_entities)]

# Simular el comportamiento de forrajeo durante varios pasos de tiempo
for step in range(num_steps):
    print(f"Paso de tiempo {step+1}:")
    for entidad in entidades:
        entidad.mover()
        print(f"Entidad en ({entidad.x}, {entidad.y}): Alimentos encontrados {entidad.food_found}")

    # Compartir información sobre alimentos encontrados
    for entidad in entidades:
        other_entities = [other_entidad for other_entidad in entidades if other_entidad != entidad]
        entidad.compartir_informacion(other_entities)

    print("-----")

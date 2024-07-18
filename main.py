import numpy as np
from itertools import combinations

# Matriz de tiempos de viaje
tiempos = np.array([
    [0, 35, 20, 40, 30, 60],
    [35, 0, 45, 35, 20, 70],
    [20, 45, 0, 15, 55, 20],
    [40, 35, 15, 0, 65, 35],
    [30, 20, 55, 65, 0, 40],
    [60, 70, 20, 35, 40, 0]
])

# Crear la matriz binaria
distancia_maxima = 30
matriz_binaria = (tiempos <= distancia_maxima).astype(int)

# Función para verificar si un conjunto de estaciones cubre todas las ciudades
def cubre_todas(ciudades, estaciones, matriz_binaria):
    cubiertas = set()
    for estacion in estaciones:
        cubiertas.update(set(np.where(matriz_binaria[estacion] == 1)[0]))
    return cubiertas == set(ciudades)

# Encontrar el número mínimo de estaciones
def encontrar_min_estaciones(matriz_binaria):
    ciudades = range(len(matriz_binaria))
    for r in range(1, len(ciudades) + 1):
        for combinacion in combinations(ciudades, r):
            if cubre_todas(ciudades, combinacion, matriz_binaria):
                return combinacion

# Calcular las estaciones necesarias
estaciones_necesarias = encontrar_min_estaciones(matriz_binaria)
print(f'Número mínimo de estaciones necesarias: {len(estaciones_necesarias)}')
print(f'Estaciones ubicadas en las ciudades: {estaciones_necesarias}')
import random
import time
from ordenamiento import selection_sort
from busqueda import busqueda_secuencial_ordenada

# Crear una lista de 1000 números aleatorios entre 1 y 5000
lista = random.sample(range(1, 5001), 1000)
objetivo = lista[500]  # Elegimos un elemento que sabemos está en la lista

# Ordenamos la lista con Selection Sort
inicio_ordenamiento = time.time()
lista_ordenada = selection_sort(lista.copy())
fin_ordenamiento = time.time()

# Aplicamos búsqueda secuencial optimizada
inicio_busqueda = time.time()
posicion = busqueda_secuencial_ordenada(lista_ordenada, objetivo)
fin_busqueda = time.time()

# Resultados
print(f"Elemento buscado: {objetivo}")
print(f"Posición encontrada: {posicion}")
print(f"Tiempo de ordenamiento: {fin_ordenamiento - inicio_ordenamiento:.6f} segundos")
print(f"Tiempo de búsqueda: {fin_busqueda - inicio_busqueda:.6f} segundos")

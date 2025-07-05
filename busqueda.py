def busqueda_secuencial_ordenada(arr, objetivo):
    for i in range(len(arr)):
        if arr[i] == objetivo:
            return i  # Se encontró el elemento en la posición i
        elif arr[i] > objetivo:
            break  # No es necesario seguir, porque los datos están ordenados
    return -1  # No se encontró el elemento

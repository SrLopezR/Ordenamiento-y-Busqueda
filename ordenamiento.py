def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i  # Suponemos que el actual es el mínimo
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j  # Encontramos un nuevo mínimo
        # Intercambiamos el valor mínimo encontrado con el valor en la posición i
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def arreglo(arr, n):
    if n == 0:
        return 0
    return arr[n - 1] + arreglo(arr, n - 1)

numeros = [4, 2 , 10, 5 , 12]  
resultado = arreglo(numeros, len(numeros))
print(f"Suma de la lista: {resultado}")
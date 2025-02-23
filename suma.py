def arreglo(arr, n):
    if n == 0:
        return 0
    return arr[n - 1] + arreglo(arr, n - 1)

numeros = [17, 29 , 9, 34 , 15]  
resultado = arreglo(numeros, len(numeros))
print(f"Suma de la lista: {resultado}")
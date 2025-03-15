def multiplicar():
    a = int(input("Ingresa el primer número: "))  
    b = int(input("Ingresa el segundo número: "))  
    resultado = 0
    for i in range(b):
        resultado = resultado + a
    print("El resultado de la multiplicación es:", resultado)


multiplicar()
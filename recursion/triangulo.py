def triangulo_numeros():
    n = int(input("Ingresa un número para el triángulo: ")) 
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ") 
        print()  

triangulo_numeros()
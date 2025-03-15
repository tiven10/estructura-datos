def dividir(a, b)->float:
    if b == 0:
        return "Error: división por cero"
    cociente = 0
    while a >= b:
        a = a-b
        cociente =cociente+ 1
    return cociente + a / b

print("Ingresa el dividendo: ")
a = int(input())
print("Ingresa el divisor: ")
b = int(input())

print("El cociente es:",round(dividir(a,b),3))
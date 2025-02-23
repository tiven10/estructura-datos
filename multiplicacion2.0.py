def multiplicacion(a, b):
    if b == 0:
        return 0
    elif b == 1:
        return a
    else:
        return a + multiplicacion(a, b - 1)

print(multiplicacion(8, 12))  
print(multiplicacion(9, 5))
print(multiplicacion(12, 8))
print(multiplicacion(6, 7))
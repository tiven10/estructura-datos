def balanceo_correcto(expresion):
    pares = {')': '(', '}': '{', ']': '['}
    pila = []
    
    for i, simbolo in enumerate(expresion):
        if simbolo in '({[':
            pila.append((simbolo, i))
        elif simbolo in ')}]':
            if not pila or pila[-1][0] != pares[simbolo]:
                return f"Error en la posición {i}: '{simbolo}' no está balanceado."
            pila.pop()
    
    if pila:
        simbolo, pos = pila[-1]
        return f"Error en la posición {pos}: '{simbolo}' no tiene cierre."
    
    return "Expresión correctamente balanceada."


print("Verificador de balanceo de símbolos")
print("Este programa verifica el balanceo de los siguientes símbolos: (), {}, []")
print("Por favor, ingresa una expresión para evaluar:\n")

expresion = input("Expresión: ")
resultado = balanceo_correcto(expresion)

print("\nResultado de la evaluación:")
print(resultado)
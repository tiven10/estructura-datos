class NodoPila:
    def __init__(self, valor, siguiente=None):  
        self.valor = valor
        self.siguiente = siguiente

class PilaNodos:
    def __init__(self):  
        self.cima = None

    def push(self, valor):
        nuevo = NodoPila(valor)
        nuevo.siguiente = self.cima
        self.cima = nuevo

    def pop(self):
        if self.cima is None:
            return None
        valor = self.cima.valor
        self.cima = self.cima.siguiente
        return valor

    def top(self):
        if self.cima is None:
            return None
        return self.cima.valor

    def vacia(self):
        return self.cima is None

def verificar_balanceo(expresion):
    pila = PilaNodos()
    for simbolo in expresion:
        if simbolo in "({[":
            pila.push(simbolo)
        elif simbolo == ')':
            tope = pila.pop()
            if tope != '(':
                return False
        elif simbolo == '}':
            tope = pila.pop()
            if tope != '{':
                return False
        elif simbolo == ']':
            tope = pila.pop()
            if tope != '[':
                return False
    return pila.vacia()


expresiones = ["{[()()]}", "[(])", "{(a+b) * [c/d]}", "[{()}]", "{(a+b]}"]
for expr in expresiones:
    if verificar_balanceo(expr):
        print(expr + ": Balanceado")
    else:
        print(expr + ": No balanceado")
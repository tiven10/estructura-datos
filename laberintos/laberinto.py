class Nodo:
    def __init__(self, posicion, anterior=None):  
        self.posicion = posicion  # Tupla (x, y)
        self.anterior = anterior  # Nodo anterior en el camino


class Pila:
    def __init__(self): 
        self.elementos = []

    def apilar(self, nodo):
        self.elementos.append(nodo)

    def desapilar(self):
        return self.elementos.pop() if not self.esta_vacia() else None

    def esta_vacia(self):
        return len(self.elementos) == 0


class Laberinto:
    def __init__(self, laberinto):  
        self.laberinto = laberinto
        self.filas = len(laberinto)
        self.columnas = len(laberinto[0])
        self.inicio = self.encontrar_inicio()
        self.pila = Pila()

    def encontrar_inicio(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.laberinto[i][j] == 'S':
                    return (i, j)
        return None

    def es_valido(self, x, y):
        return 0 <= x < self.filas and 0 <= y < self.columnas and self.laberinto[x][y] in ('O', 'E')

    def imprimir_camino(self, nodo):
        camino = []
        while nodo:
            camino.append(nodo.posicion)
            nodo = nodo.anterior
        camino.reverse()
        print("Camino recorrido:", camino)

    def resolver(self):
        if not self.inicio:
            print("No se encontró el punto de inicio.")
            return False

        self.pila.apilar(Nodo(self.inicio))
        movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while not self.pila.esta_vacia():
            nodo_actual = self.pila.desapilar()
            x, y = nodo_actual.posicion

            if self.laberinto[x][y] == 'E':
                print("¡Salida encontrada!")
                self.imprimir_camino(nodo_actual)
                return True

            if self.laberinto[x][y] != 'S':
                self.laberinto[x][y] = 'V'  

            for dx, dy in movimientos:
                nx, ny = x + dx, y + dy
                if self.es_valido(nx, ny):
                    self.pila.apilar(Nodo((nx, ny), nodo_actual))

        print("No hay salida en el laberinto.")
        return False


# Prueba
laberinto_matriz = [
    ['S', 'O', 'X', 'X', 'O'],
    ['X', 'O', 'O', 'X', 'O'],
    ['X', 'X', 'O', 'O', 'X'],
    ['O', 'O', 'X', 'O', 'E'],
    ['X', 'O', 'O', 'O', 'X'],
]

laberinto = Laberinto(laberinto_matriz)
laberinto.resolver()

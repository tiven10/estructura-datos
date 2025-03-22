class Laberinto:
    def __init__(self, laberinto):
        self.laberinto = laberinto
        self.filas = len(laberinto)
        self.columnas = len(laberinto[0])
        self.movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]  
        self.inicio, self.salida = self.encontrar_inicio_salida()
    
    def encontrar_inicio_salida(self):
        inicio, salida = None, None
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.laberinto[i][j] == 'S':
                    inicio = (i, j)
                elif self.laberinto[i][j] == 'E':
                    salida = (i, j)
        return inicio, salida
    
    def resolver(self):
        if not self.inicio or not self.salida:
            return None
        
        pila = [(self.inicio, [self.inicio])]
        visitados = set()
        
        while pila:
            (x, y), camino = pila.pop()
            
            if (x, y) == self.salida:
                return camino
            
            if (x, y) in visitados:
                continue
            visitados.add((x, y))
            
            for dx, dy in self.movimientos:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.filas and 0 <= ny < self.columnas and self.laberinto[nx][ny] != 'X':
                    pila.append(((nx, ny), camino + [(nx, ny)]))
        
        return None  
    
laberinto = [
    ['S', 'O', 'X', 'X', 'O'],
    ['X', 'O', 'O', 'X', 'O'],
    ['X', 'X', 'O', 'O', 'X'],
    ['O', 'O', 'X', 'O', 'E'],
    ['X', 'O', 'O', 'O', 'X']
]

solver = Laberinto(laberinto)
solucion = solver.resolver()
print("Camino encontrado:", solucion)

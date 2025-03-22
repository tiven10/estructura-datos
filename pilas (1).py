class Pila:
    def __init__(self, max_size=8):
        self.pila = []
        self.max_size = max_size
    
    def pila_vacia(self):
        return len(self.pila) == 0
    
    def pila_llena(self):
        return len(self.pila) >= self.max_size
    
    def poner(self, dato):
        if self.pila_llena():
            print("Desbordamiento - Pila llena")
        else:
            self.pila.append(dato)
            print(f"Elemento {dato} agregado a la pila")
    
    def quitar(self):
        if self.pila_vacia():
            print("Subdesbordamiento - Pila vacía")
        else:
            dato = self.pila.pop()
            print(f"Elemento {dato} removido de la pila")
    
    def mostrar_elementos(self):
        if self.pila_vacia():
            print("La pila está vacía")
        else:
            print("La pila tiene los siguientes elementos actualmente:")
            for i, dato in enumerate(reversed(self.pila), start=1):
                print(f"Posición {i}: {dato}")


def menu():
    pila = Pila()
    while True:
        print("\nSeleccione qué quiere hacer con la estructura pila:")
        print("1 = Saber si la pila está vacía")
        print("2 = Saber si la pila está llena")
        print("3 = Colocar un elemento en la pila")
        print("4 = Quitar un elemento de la pila")
        print("5 = Mostrar los elementos actuales de la pila")
        print("Cualquier otro número = Salir")
        
        try:
            seleccion = int(input("Ingrese su opción: "))
        except ValueError:
            print("Entrada no válida. Intente de nuevo.")
            continue

        if seleccion == 1:
            print("La pila está vacía" if pila.pila_vacia() else "La pila no está vacía")
        elif seleccion == 2:
            print("La pila está llena" if pila.pila_llena() else "La pila no está llena")
        elif seleccion == 3:
            try:
                dato = int(input("Coloque dato NUMÉRICO a insertar: "))
                pila.poner(dato)
            except ValueError:
                print("Entrada no válida. Debe ser un número entero.")
        elif seleccion == 4:
            pila.quitar()
        elif seleccion == 5:
            pila.mostrar_elementos()
        else:
            print("Hasta luego")
            break

if __name__ == "__main__":
    menu()

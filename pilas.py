class NodoPila:
    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

class PilaNodos:
    def __init__(self, capacidad_maxima=8):
        self.cima = None
        self.tamano = 0
        self.capacidad_maxima = capacidad_maxima

    def push(self, valor):
        if self.tamano >= self.capacidad_maxima:
            print(" Desbordamiento: La pila ya tiene 8 elementos.")
        else:
            nuevo = NodoPila(valor)
            nuevo.siguiente = self.cima
            self.cima = nuevo
            self.tamano += 1
            print(f" Elemento '{valor}' insertado en la pila.")

    def pop(self):
        if self.cima is None:
            print(" Subdesbordamiento: La pila está vacía.")
            return None
        valor = self.cima.valor
        self.cima = self.cima.siguiente
        self.tamano -= 1
        print(f" Elemento eliminado: {valor}")
        return valor

    def top(self):
        if self.cima is None:
            print(" La pila está vacía.")
            return None
        print(f" Elemento superior: {self.cima.valor}")
        return self.cima.valor

    def vacia(self):
        if self.cima is None:
            print(" La pila está vacía.")
            return True
        else:
            print(" La pila NO está vacía.")
            return False

    def mostrar_tamano(self):
        print(f"Elementos en la pila: {self.tamano} / {self.capacidad_maxima}")


pila = PilaNodos()

while True:
    print("\nSeleccione qué quiere hacer con la estructura pila:")
    print("1. Insertar elemento (push)")
    print("2. Eliminar elemento (pop)")
    print("3. Ver elemento superior (top)")
    print("4. Verificar si la pila está vacía")
    print("5. Ver cuántos elementos hay en la pila")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        elemento = input("Ingrese el elemento a agregar: ")
        pila.push(elemento)
    elif opcion == "2":
        pila.pop()
    elif opcion == "3":
        pila.top()
    elif opcion == "4":
        pila.vacia()
    elif opcion == "5":
        pila.mostrar_tamano()
    elif opcion == "6":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    Menu()
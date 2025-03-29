from typing import Optional

class Animal:
    def __init__(self, nombre: str, edad: int, tipo: str) -> None:
        self.nombre = nombre  
        self.edad = edad
        self.tipo = tipo
        self.siguiente = None  

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Tipo: {self.tipo}"

class ListaEnlazada:
    def __init__(self) -> None:
        self.cabeza= None

    def agregar(self, nombre: str, edad: int, tipo: str) -> None:
        if self.existe_animal(nombre, tipo):
            print(f"El animal {nombre} de tipo {tipo} ya está registrado.")
            return

        nuevo_animal = Animal(nombre, edad, tipo)

        if self.cabeza is None:
            self.cabeza = nuevo_animal
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente is not None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_animal

    def existe_animal(self, nombre: str, tipo: str) -> bool:
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            if nodo_actual.nombre == nombre and nodo_actual.tipo == tipo:
                return True
            nodo_actual = nodo_actual.siguiente
        return False

    def mostrar_iterativo(self) -> None:
        if self.cabeza is None:
            print(" No hay animales registrados.")
            return

        print("\n Lista de animales (Iterativo):")
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            print(nodo_actual)
            nodo_actual = nodo_actual.siguiente

    def mostrar_recursivo(self, nodo: Optional[Animal] = None) -> None:
        if nodo is None:  
            nodo = self.cabeza
            if nodo is None:
                print(" No hay animales registrados.")
                return
            print("\n Lista de animales (Recursivo):")

        print(nodo)
        if nodo.siguiente is not None:
            self.mostrar_recursivo(nodo.siguiente)  


lista_animales = ListaEnlazada()
lista_animales.agregar("Águila", 5, "Ave")
lista_animales.agregar("Pantera", 7, "Felino")
lista_animales.agregar("Vaca", 4, "Mamífero")
lista_animales.agregar("Águila", 5, "Ave")  


lista_animales.mostrar_iterativo()
lista_animales.mostrar_recursivo()
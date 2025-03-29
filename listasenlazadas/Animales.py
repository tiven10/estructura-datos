from typing import Optional

class Animal:
    def __init__(self, nombre: str, edad: int, tipo: str) -> None:
        """ Constructor de la clase Animal """
        self.nombre = nombre  
        self.edad = edad
        self.tipo = tipo
        self.siguiente = None  

    def __str__(self) -> str:
        """ Representación en cadena del animal """
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Tipo: {self.tipo}"

class ListaEnlazada:
    def __init__(self) -> None:
        """ Constructor de la lista enlazada """
        self.cabeza= None

    def agregar(self, nombre: str, edad: int, tipo: str) -> None:
        """ Agrega un nuevo animal a la lista, evitando duplicados """
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
        """ Verifica si un animal ya está en la lista """
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            if nodo_actual.nombre == nombre and nodo_actual.tipo == tipo:
                return True
            nodo_actual = nodo_actual.siguiente
        return False

    def mostrar_iterativo(self) -> None:
        """ Muestra la lista de animales de forma iterativa """
        if self.cabeza is None:
            print(" No hay animales registrados.")
            return

        print("\n Lista de animales (Iterativo):")
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            print(nodo_actual)
            nodo_actual = nodo_actual.siguiente

    def mostrar_recursivo(self, nodo: Optional[Animal] = None) -> None:
        """ Muestra la lista de animales de forma recursiva """
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
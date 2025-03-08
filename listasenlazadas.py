from typing import Optional

class Node:
    def __init__(self, numero : int)-> None:
        self.dato = numero
        self.next: Optional["Node"] = None

class ListaEnlazada:
    def __init__(self) -> None:
        self.cabeza: Optional["Node"] = None

    def agregar(self, numero: int) -> None:
        nodo: Node = Node(numero)
        if self.cabeza is None:
            self.cabeza = nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.next:
                nodo_actual = nodo_actual.next
            nodo_actual.next = nodo

lista = ListaEnlazada()
lista.agregar(5)
lista.agregar(10)
lista.agregar(15)
lista.agregar(20)
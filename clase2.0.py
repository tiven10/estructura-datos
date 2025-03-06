class Persona:

    nombre: str
    edad: int
    genero: str

    def __init__(self,nombre:str,edad:int,genero:str)-> None:
        self.nombre= nombre
        self.edad= edad
        self.genero= genero

    def __str__(self)->str:
        return f"Nombre: {self.nombre},  Edad: {self.edad},  Género: {self.genero}"
    
    def presentarse(self) -> None:
        print(f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y soy {self.genero}")

class CuentaBancaria:

    titular: Persona
    saldo: float
    numero_cuenta: str

    def __init__(self,titular: Persona, saldo:float, numero_cuenta:str)-> None:
        self.titular= titular
        self.saldo= saldo
        self.numero_cuenta= numero_cuenta

    def __str__(self)->str:
        return f"Titular: {self.titular},  Saldo: {self.saldo},  Numero de cuenta: {self.numero_cuenta}"
    
    
    def depositar(self, cantidad: float) -> None:
        self.saldo += cantidad


    def retirar(self, cantidad: float) -> None:
        if cantidad > self.saldo:
            print("Excede el saldo disponible")
        else:
            self.saldo -= cantidad


    def consultarsaldo (self) -> float:
        return self.saldo
    
class Rectangulo:

    base: float
    altura: float

    def __init__(self, base: float, altura: float):
        self.base= base
        self.altura= altura

    def __str__(self)->str:
        return f"Base: {self.base},  Altura: {self.altura}"
    
    def calcular_area (self) -> float:
        return self.base * self.altura
    
    def calcular_perimetro (self) -> float:
        return 2*(self.base + self.altura)
    
class Circulo:

    radio: float

    def __init__(self, radio: float)-> None:
        self.radio= radio

    def __str__(self)->str:
        return f"Radio: {self.radio}"
    
    def calcular_area (self) -> float:
        return 3.1416 * self.radio ** 2
    
    def calcular_circunferencia (self)-> float:
        return 2 * 3.1416 * self.radio
    
class Libro:

    Titulo: str
    autor: str
    genero: str
    año_publicacion: int

    def __init__(self,titulo: str, autor:str, genero: str, año_publicacion: int) -> None:
        self.Titulo= titulo
        self.autor= autor
        self.genero= genero
        self.año_publicacion= año_publicacion

    def __str__(self)->str:
        return f"Titulo: {self.Titulo}, Autor: {self.autor}, Genero: {self.genero}, Año_publicacion: {self.año_publicacion}"
    
    
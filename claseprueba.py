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
    
    def mostrar_detalles(self) -> None:
         print(self)  


class Cancion:

    titulo: str
    artista: str
    album: str
    duracion: float

    def __init__(self, titulo:str, artista: str, album: str, duracion: float):
        self.titulo= titulo
        self.artista= artista
        self.album= album
        self.duracion= duracion

    def __str__(self)->str:
        return f"Titulo: {self.titulo}, Artista: {self.artista}, Album: {self.album}, Duracion: {self.duracion}"
    
    def reproducir(self) -> str:
        return f"Reproduciendo: {self.titulo}"
    
class Producto:

    nombre: str
    precio: float
    cantidad_disponible: int

    def __init__(self, nombre: str, precio: float, cantidad_disponible: int):
        self.nombre= nombre
        self.precio= precio
        self.cantidad_disponible= cantidad_disponible

    def __str__(self)->str:
        return f"Nombre: {self.nombre}, Precio: {self.precio}, Cantidad_disponible: {self.cantidad_disponible} "
    
    def calcularTotal(self, cantidad: int) -> float:
        return self.precio * cantidad
    

class Estudiante:

    nombre: str
    edad: int
    curso: str
    calificaciones: list


    def __init__(self, nombre: str, edad: int, curso: str, calificaciones: list):
        self.nombre= nombre
        self.edad= edad
        self.curso= curso
        self.calificaciones= calificaciones

    def __str__(self)->str:
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Curso: {self.curso}, Calificaciones: {self.calificaciones}"
    
    def agregar_calificacion(self, calificacion: float) -> None:
         self.calificaciones.append(calificacion)

    def calcular_promedio(self) -> float:
        if not self.calificaciones:
            return 0.0
        return sum(self.calificaciones) / len(self.calificaciones)
    
    def esta_aprobado(self, nota_minima: float = 60.0) -> bool:
        return self.calcular_promedio() >= nota_minima
    

persona1 = Persona('Juan', 25, 'Masculino')
print(persona1)
persona1.presentarse()

titular = Persona('Maria', 30, 'Femenino')
cuentabancaria1 = CuentaBancaria(titular, 25000, '43897000') 
print(cuentabancaria1)
cuentabancaria1.depositar(50.000)
cuentabancaria1.retirar(30.000)
cuentabancaria1.consultarsaldo()

rectangulo1 = Rectangulo(2.6, 7)
print(rectangulo1)
rectangulo1.calcular_area()
rectangulo1.calcular_perimetro()

circulo1 = Circulo(8.9)
print(circulo1)
circulo1.calcular_area()
circulo1.calcular_circunferencia()

libro1 = Libro('El perfume', 'Patrick Süskind', ' Novela', 1985 )
print(libro1)
libro1.mostrar_detalles()

cancion1 = Cancion('Obligao', 'Luigi 21 Plus', 'El patán', 3.31)
print(cancion1)
cancion1.reproducir()

producto1 = Producto('Gafas de descanso', 300.000, 2000)
print(producto1)
producto1.calcularTotal(5)

estudiante1 = Estudiante('steven', 20, 'ingenieria de software', [])
print(estudiante1)
estudiante1.agregar_calificacion(4)
estudiante1.agregar_calificacion(5)
estudiante1.agregar_calificacion(3.5)
estudiante1.calcular_promedio()
estudiante1.esta_aprobado()
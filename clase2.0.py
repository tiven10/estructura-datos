class Persona:
    nombre: str
    edad: int
    genero: str

    def __init__(self, nombre: str, edad: int, genero: str) -> None:
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Género: {self.genero}"
    
    def presentarse(self) -> None:
        print(f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y soy {self.genero}")

class CuentaBancaria:
    titular: Persona
    saldo: float
    numero_cuenta: str

    def __init__(self, titular: Persona, saldo: float, numero_cuenta: str) -> None:
        self.titular = titular
        self.saldo = saldo
        self.numero_cuenta = numero_cuenta

    def __str__(self) -> str:
        return f"Titular: {self.titular.nombre}, Saldo: {self.saldo}, Número de cuenta: {self.numero_cuenta}"
    
    def depositar(self, cantidad: float) -> None:
        self.saldo += cantidad
        print(f"Depósito exitoso. Nuevo saldo: {self.saldo}")

    def retirar(self, cantidad: float) -> None:
        if cantidad > self.saldo:
            print("Excede el saldo disponible")
        else:
            self.saldo -= cantidad
            print(f"Retiro exitoso. Nuevo saldo: {self.saldo}")

    def consultar_saldo(self) -> float:
        return self.saldo

class Rectangulo:
    base: float
    altura: float

    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def __str__(self) -> str:
        return f"Base: {self.base}, Altura: {self.altura}"
    
    def calcular_area(self) -> float:
        return self.base * self.altura
    
    def calcular_perimetro(self) -> float:
        return 2 * (self.base + self.altura)

class Circulo:
    radio: float

    def __init__(self, radio: float) -> None:
        self.radio = radio

    def __str__(self) -> str:
        return f"Radio: {self.radio}"
    
    def calcular_area(self) -> float:
        return 3.1416 * self.radio ** 2
    
    def calcular_circunferencia(self) -> float:
        return 2 * 3.1416 * self.radio

class Libro:
    titulo: str
    autor: str
    genero: str
    año_publicacion: int

    def __init__(self, titulo: str, autor: str, genero: str, año_publicacion: int) -> None:
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.año_publicacion = año_publicacion

    def __str__(self) -> str:
        return f"Título: {self.titulo}, Autor: {self.autor}, Género: {self.genero}, Año de publicación: {self.año_publicacion}"
    
    def mostrar_detalles(self) -> None:
        print(self)

class Cancion:
    titulo: str
    artista: str
    album: str
    duracion: float

    def __init__(self, titulo: str, artista: str, album: str, duracion: float):
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.duracion = duracion

    def __str__(self) -> str:
        return f"Título: {self.titulo}, Artista: {self.artista}, Álbum: {self.album}, Duración: {self.duracion} minutos"
    
    def reproducir(self) -> str:
        return f"Reproduciendo: {self.titulo}"

class Producto:
    nombre: str
    precio: float
    cantidad_disponible: int

    def __init__(self, nombre: str, precio: float, cantidad_disponible: int):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Precio: {self.precio}, Cantidad disponible: {self.cantidad_disponible}"
    
    def calcular_total(self, cantidad: int) -> float:
        return self.precio * cantidad

class Estudiante:
    nombre: str
    edad: int
    curso: str
    calificaciones: list

    def __init__(self, nombre: str, edad: int, curso: str, calificaciones=None):
        if calificaciones is None:
            calificaciones = []
        self.nombre = nombre
        self.edad = edad
        self.curso = curso
        self.calificaciones = calificaciones

    def __str__(self) -> str:
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

cuenta1 = CuentaBancaria(persona1, 25000, "43897000")
print(cuenta1)
cuenta1.depositar(5000)
cuenta1.retirar(10000)
print(f"Saldo actual: {cuenta1.consultar_saldo()}")

rectangulo1 = Rectangulo(5, 10)
print(f"Área del rectángulo: {rectangulo1.calcular_area()}")
print(f"Perímetro del rectángulo: {rectangulo1.calcular_perimetro()}")

circulo1 = Circulo(7)
print(f"Área del círculo: {circulo1.calcular_area()}")
print(f"Circunferencia del círculo: {circulo1.calcular_circunferencia()}")

producto1 = Producto('Gafas de descanso', 300000, 2000)
print(producto1)
print(f"Total por 2 unidades: {producto1.calcular_total(2)}")

estudiante1 = Estudiante('Steven', 20, 'Ingeniería de Software')
estudiante1.agregar_calificacion(70)
estudiante1.agregar_calificacion(80)
print(f"Promedio: {estudiante1.calcular_promedio()}")
print(f"Aprobado: {estudiante1.esta_aprobado()}")
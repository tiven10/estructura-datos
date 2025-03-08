class Empleado:
    def __init__(self, nombre: str, salario: float, departamento: str) -> None:
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento

    def __str__(self) -> str:
        return f"Empleado: {self.nombre}, Salario: {self.salario}, Departamento: {self.departamento}"

    def trabajar(self) -> None:
        print(f"{self.nombre} está trabajando en {self.departamento}.")

class Gerente(Empleado):
    def supervisar_equipo(self, equipo: list) -> None:
        print(f"{self.nombre} está supervisando a su equipo: {', '.join(equipo)}.")

class Desarrollador(Empleado):
    def escribir_codigo(self, lenguaje: str) -> None:
        print(f"{self.nombre} está programando en {lenguaje}.")

class FiguraGeometrica:
    def calcular_area(self) -> float:
        pass

class Triangulo(FiguraGeometrica):
    def __init__(self, base: float, altura: float) -> None:
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        return (self.base * self.altura) / 2

class Cuadrado(FiguraGeometrica):
    def __init__(self, lado: float) -> None:
        self.lado = lado

    def calcular_area(self) -> float:
        return self.lado ** 2

class Electrodomestico:
    def __init__(self, marca: str, modelo: str) -> None:
        self.marca = marca
        self.modelo = modelo

    def encender(self) -> None:
        print(f"El {self.marca} {self.modelo} está encendido.")

class Lavadora(Electrodomestico):
    def iniciar_ciclo_de_lavado(self) -> None:
        print(f"Iniciando ciclo de lavado en la lavadora {self.marca}.")

class Refrigerador(Electrodomestico):
    def regular_temperatura(self) -> None:
        print(f"Regulando temperatura del refrigerador {self.marca}.")

class Usuario:
    def __init__(self, nombreDeUsuario: str, contraseña: str) -> None:
        self.nombreDeUsuario = nombreDeUsuario
        self.contraseña = contraseña

    def iniciar_sesion(self, usuario: str, contraseña: str) -> bool:
        return usuario == self.nombreDeUsuario and contraseña == self.contraseña

class Administrador(Usuario):
    def gestionar_usuarios(self) -> None:
        print(f"{self.nombreDeUsuario} está gestionando usuarios.")

class Cliente(Usuario):
    def realizar_compra(self) -> None:
        print(f"{self.nombreDeUsuario} está realizando una compra.")

# Pruebas
empleado1 = Empleado("Carlos", 50000, "Ventas")
print(empleado1)
empleado1.trabajar()

gerente1 = Gerente("Ana", 70000, "TI")
print(gerente1)
gerente1.supervisar_equipo(["Luis", "Marta"])

dev1 = Desarrollador("Luis", 60000, "Desarrollo")
print(dev1)
dev1.escribir_codigo("Python")

triangulo1 = Triangulo(5, 10)
print(f"Área del triángulo: {triangulo1.calcular_area()}")

cuadrado1 = Cuadrado(4)
print(f"Área del cuadrado: {cuadrado1.calcular_area()}")

lavadora1 = Lavadora("Samsung", "X200")
lavadora1.encender()
lavadora1.iniciar_ciclo_de_lavado()

refri1 = Refrigerador("LG", "FrostCool")
refri1.encender()
refri1.regular_temperatura()

admin1 = Administrador("admin1102", "segura1542")
print(admin1.iniciar_sesion("admin1102", "segura1542"))
admin1.gestionar_usuarios()

cliente1 = Cliente("clienteXYZ", "compra2025")
print(cliente1.iniciar_sesion("clienteXYZ", "compra2025"))
cliente1.realizar_compra()
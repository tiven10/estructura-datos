class Vehiculo:

    marca: str
    combustible: str
    tipo_Vehiculo: str

    def __init__(self, marca: str, combustible: int, tipo_Vehiculo:str)-> None:
        self.marca = marca
        self.combustible = combustible
        self.tipo_Vehiculo = tipo_Vehiculo

    def __str__(self)->str:
        return f"El tipo de vehiculo es: {self.tipo_Vehiculo},  La marca del vehiculo es: {self.marca}  y El nivel de combustible es de: {self.combustible}"

    def encender(self):
        if self.combustible < 10:
            print("Advertencia debes de ir a la gasolinera")
        else:
            print("El vehiculo esta encendido")
        

    def acelerar(self):
       if self.combustible > 0:
         self.combustible -= 5
       print(f"El vehículo ha acelerado. Nivel de combustible: {self.combustible} galones.")
            
       if self.combustible < 10:
            print("Advertencia debes de ir a la gasolinera")
            
       if self.combustible == 0:
            print("Detenga la marcha.")
            return  



class Moto(Vehiculo):
    pass

class Carro(Vehiculo):
    pass


vehiculo1 = Vehiculo('audi', 5, 'carro')
print(vehiculo1)
vehiculo1.encender()
vehiculo1.acelerar()

moto1 = Moto('Yamaha', 69, 'moto')
print(moto1)
moto1.encender()
moto1.acelerar()

carro1 = Carro('mercedes', 14, 'carro')
print(carro1)
carro1.encender()
carro1.acelerar()
numeros = list()
continuar: bool= True

def agregar (numero:int)-> None:
   numeros.append(numero) 

def eliminar ()-> None:
   numeros.pop() 

while continuar:
   print("menu de operaciones")
   print("1. agregar un numero")
   print("2. eliminar el ultimo numero")
   print("3. salir")

   opcion = int(input("selecciona una opcion: "))

   if opcion == 1: 
    num = int(input("Ingresa el número que deseas agregar: "))
    agregar(num)
   elif opcion == 2:
    num = int(input("Ingresa el número que deseas eliminar: ")) 
    eliminar()

   elif opcion == 3:
    continuar = False

   print(numeros)

else:
  print("Hasta luego")
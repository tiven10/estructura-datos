temperatura = []
for n in range (0,5):
    t = int(input("Ingrese la temperatura:"))
    temperatura.append(t)

promedio = sum(temperatura)/len(temperatura)

print("La temperatura promedio es :", promedio)
if promedio < 20 :
    print("Necesita una revision")
elif 20>= promedio <=30:
    print("La temperatura esta perfecta")
else :
    print("Es necesaria una revision de los conductos de aire") 
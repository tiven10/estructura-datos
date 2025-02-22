numero = 6

def factorial (n:int)->int :
  res:int = 1
  contador = 0
  while contador < n:
    contador = contador + 1
    res = res * contador
  return res 
print(factorial(numero))
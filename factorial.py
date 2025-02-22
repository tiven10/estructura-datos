numero = 5
resultado: int

def factorial (n:int)->int :
  res:int = 1
  for i in range (1, n + 1):
      res= res * i 
  return res

print(factorial(numero))
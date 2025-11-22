#8.2 Hallar el n − esimo t´ermino de la secuencia de Fibonacci.
#serie fibonnaci      1,1,2,3,5.8
     # posiciones     0,1,2,3,4,5
def fibonnaci(n):
    a = 0
    b = 1
    c = 0
    contador = [0]
    for i in range(n-1):#porque ya tenemos el primerelemnto osea el 0
      contador.append(b)
    
      c  = a + b
      a = b
      b = c 
      
    return contador
n = int(input("ESCRIBA UN NUMERO: "))
buscar =int(input("de  que numero desea buacar su posicion: "))

resultado = fibonnaci(n)
print(resultado)
try:#codigo que puede falllar
#el try es para manejar errores es como q dice"intenta hacer esto y si va mal has esto en su lugar  

  posicion = resultado.index(buscar) 
  print(resultado)
  print(posicion)
except ValueError:#que hace si falla
 print("no esta en la serie ")
 print("emma clara lazo layme")
#programa que valide si un numero es primo
def esprimo(n): #definiendo funcion
    if n <=1: # preguntar para ver si son numeros negativos 
        return False # para poder devolver false si se cumple 
    elif n== 2: #por s n es dos ya que tambien es primo
        return True # retorna que si es primo
    else: 
        #vamos a dividir el numero n hasta n con el iterito 
        #vamos a hacer un ciclo for para que vaya desde 2 hasta el n 
        for i in range(2,n):
            if n % i == 0:
                return False # si la division es exacta no es  numero primo entonces devuekve false
        return True # si no es exacta 
#for i in range(10,101):
 #   print(i,"", esprimo(i))   # lo que hace esto es que desde el 10 hasta el 101 mostrara todos los primos con verdad y si no es false pero no es necesario en el codigo
print(esprimo(34))#en aca puedes ponercualquier numero para ver si es primo

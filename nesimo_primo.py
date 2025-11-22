#el enesimo es la posicion (n) de una lista de numeros digamos nos piden hallar del 7 :
#estamos en serie de primos seria: 2,3,5,7,11,13,17,19,23,31 ..etce
#                       posiciones 1,2,3,4,5, 6 , 7,8 ,9 ,10               
def enesimo_primo(posicion):
    primos = []
    n = 2
    
    while len(primos) < posicion: #cuanta la cantidad de digitos y las compara 
        es_primo = True     
        for i in range(2, n): #verificar si es primo o mo
            if n % i == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(n)
        n = n + 1
    
    return primos[-1]    # retorna el valor

def binario_base(posicion): 
    binario = []
    n = posicion
    
    while n > 0:
        binario.append(str(n % 2))#lo vuelve str y lo guarda en binario
        n = n // 2
    
    if not binario:
        return "0"
    
    binario.reverse()
    return ''.join(binario) #convierte la lista rn algo normal 
def sumar(posicion):
     return (posicion*(posicion+1))/2 #formula de sumatoria 
    
    
posicion = int(input("Escriba un numero: "))
resultado = enesimo_primo(posicion)  #llama la funcion emesimo_primo
print(f"es: {resultado}")
resultado2 = binario_base(resultado) #llama a la funcion binario_base 
print(f"su numero es: {resultado2}")
resultado3 =sumar(posicion)# llama a la funcion
print(f"la suma de 1 hasta n es {resultado3}")
print("emma clara lazo layme")

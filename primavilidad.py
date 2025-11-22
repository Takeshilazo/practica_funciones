def primavilidad(numero):
    if numero < 2:
        return "no primo"
    c = 0
    for i in range (2,numero):#desde dos porque es primo 
        if numero % i == 0:
            c +=1
        
    if c == 2:
       return 1
    else:
       return 0
numero = int(input("escriba un numero: "))
resultado = primavilidad(numero)
print(f"resultado {resultado}")
print("EMMA CLARA LAZO LAYME")
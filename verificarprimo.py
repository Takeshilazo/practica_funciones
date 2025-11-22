def primo(p):
 c = 0
 for i in range(1,p+1):
        if p % i == 0:
            c += 1
        
 if c == 2: 
     return True
 else:
    return False
p = int(input("escriba un numero: "))
resultado = primo(p)#llamar a la funcion
if resultado :#cuando es TRUE entra
   print("es primo")
else:#cuando es false entra
   print("no es primo") 
   print("emma clara lazo layme")
# ejemplo p = 12
#for  ira de 1 hasta 12 por el p+1 sino iria hasta el 11
# if 1 % 12 == 0 ? si c = 1 ; 2 % 12 ==0;  si contador c = 2 ; 3 % 12 == 0 : si c = 3
# se entra a if c == 2: ? NO ,se entra en false 
#cuando llamemos a la funcion en el if lo q hara es preguntar el resultado es true o false 
# como era false imprimira MO ES `PRIMO`

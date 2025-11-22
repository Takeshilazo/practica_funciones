#ejemplo  7 | 4 
#         1 | 1  no tiene divisores comunes entonces son primos amigos 
def primosfriend(p , a):
    if p % 2 == 1 and a % 2 == 0:
        return True
    else:
        return False
p =int(input("escriba un numero: "))
a = int(input("escriba otro numero: "))
resultado = primosfriend(p,a)
if resultado:
    print("PRIMOS FRIEND")
else:
    print("PRIMOSENEMIGOS")
print("emma clara lazo layme")
    
#hallar el n_esimo termino de la serie fibonnaci
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55..
# 1, 2, 3, 4, 5, 6, 7, 8, 9,  10,  11,
n = int(input("escriba un numero: "))
b = 1
c = 0
a = 0 
serie = [ ]
for i in range (1,n+1):
    serie.append(c)
    a = b
    b = b + c 
    c = a 
nueva=serie[n-1] 
print(f"En la posición {n} está el: {nueva}")
#ejemplo 
#digamos colocamos 1 
#entonces el appennd almanece el valor de c que es 0 c = 0 y estara dentro de serie luego 
#0 = 1
#1 = 1+0 
#c = 1 pero aqui va imprimir en la 2da iteracion ahora solo guarda el 0 
#nueva=serie[1-1] da igual a cero eso es lo que va imprimir y asi con todos 

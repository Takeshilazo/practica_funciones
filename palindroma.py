#comprobar si na palabra o frase ews palindromo ejemplo : anna di damos la vuelta se lle igual es es palindormo que se lee igua lde rderecha a ixquierda 
#tener en cuenta que no se tiene en cuenta los espacios ni mayusculas ni minusculas ni tildes
def espalindromo(palabra):
 palabra = palabra.lower() #la funcion lower convierte las mayusculas en minusculas a la palabra 
 palabra = palabra.replace(" ", "") #la funcion (replace) quita los espacios que halla 
 palabra = palabra.replace("à","a")#para quitar las tildes de las palabras
 palabra = palabra.replace("è","e")
 palabra = palabra.replace("ì","i")
 palabra = palabra.replace("ò","o")
 palabra = palabra.replace("ù","u")
 #ahora ver si es palindromo o no
 #lo que hara el rograma es ver si la primero palabra es igual a la ultima 
 #eso lo veremos viendo con posiciones 
 a=0
 b=len(palabra)-1#con esto tednremsoel primer y ultimo indice de la palabra 
 for i in range (0, len(palabra)): #ira en la posicion cero que es (a) de la pabra 
   # vamos a comparar si el indicede la primera palanra es igual a el ultimo indice de la palabra 
   if palabra[a] == palabra[b]: #aca estamos verificando los indices de la primero y uiltimo indice ,si se cumple hara
     a +=1 #para que verifique si es 
     b -=1 #para que vaya de a otro es decir al segundo
   else: 
     return False # por si no es palindormo en si no cumpli la condicion 
 return True # si es palindromo nos devolvera verdad
 
palabra = input("ingrese una palabra o frase: ")
if espalindromo(palabra):
  print("es palindromo")
else:
  print("no es palindromo")
  
print("emma clara lazo layme")

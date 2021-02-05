fichero = open("archivo2.txt","r") # creacion y lectura
linea = fichero.readlines() # guarda en una lista
fichero.close()

contador = 0
A = int(input("Dame un numero de lineas: "))

for i in range(A):
    print(linea[i])
    for i in linea[i].rsplit():
        contador+=int(i)
    
print(f"El resultado de la suma total es {contador}")   
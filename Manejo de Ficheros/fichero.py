from io import open

fichero = open("archivo.txt","w") # creacion y lectura
fichero.write("Esto es el metodo append")
fichero.close
print(fichero)

'''
linea = fichero.readlines() # guarda en una lista
fichero.close()
print(linea[1])
'''

'''
linea = fichero.readlines() # guarda en una lista
fichero.close()
print(linea)
'''
'''
texto = fichero.read()#leer lo que tiene el texto
fichero.close()
print(texto)
'''

'''
texto = "Hola mundo\n Estudio Python"
fichero.write(texto)#Manipulacion
'''
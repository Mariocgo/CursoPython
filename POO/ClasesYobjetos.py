'''
#clases y objetos
class Gelatina:#inializamos el molde
    def __init__(self, sabor, color,tamaño):
      self.sabor = sabor
      self.color = color
      self.tamaño = tamaño

    def imprimir(self):
        print("La gelatina es de "+self.sabor)
        print("La gelatina se ve de "+self.color)
        print("La gelatina es "+self.tamaño)

gel1 = Gelatina("Roja","Frutilla","Grande")
gel2 = Gelatina("azul","piña","mediano")
gel3 = Gelatina("verde","coco","chico")
gel4 = Gelatina("amarilla","chocolate","Grande")

gel1.imprimir()
gel2.imprimir()
gel3.imprimir()
gel4.imprimir()
'''
class Persona:
    def __init__(self, nombre, edad,sexo):
      self.nombre = nombre
      self.edad = edad
      self.sexo = sexo
      
    def datosPersonales(self):
        print("El nombre de la persona es: "+self.nombre)
        print("La edad de la Persona es "+self.edad)
        print("El sexo de la persona es "+self.sexo)

miPersona = Persona("Mario","21","HOMBRE")
miPersona2 = Persona("Maka","22","Mujer")
miPersona3 = Persona("German","10","Hombre")

miPersona.datosPersonales()
miPersona2.datosPersonales()
miPersona3.datosPersonales()

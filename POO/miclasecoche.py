class Coche():
    def __init__(self):
      self.marca = "Audi"
      self.color = "Rojo"
      self.ruedas = 4
      self.enmarcha = False
    
    def arrancar(self,arrancamos):
        self.enmarcha=arrancamos
        if(self.enmarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta apagado"
        
    def __str__(self):
        return "Este auto esta en marca {}, de color {}, tiene {} ruedas".format(self.marca,self.color,self.ruedas)

miCoche=Coche()
print(miCoche.arrancar(False))
print(str(miCoche))
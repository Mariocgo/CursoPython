c = "python"
print(len(c) < 8 or c[0] == "f")

print("sistemas de becas 2021")

kilometros = int(input("A cuantos kilometros vives de la escuela?: "))
hermanos = int(input("Cuantos hermanos tines en la escuela?"))
ingreso = int(input("de cuanto es el ingreso de la casa?: "))

if kilometros < 10 and hermanos < 2 or ingreso > 20000:
    print("tienes derecho a beca")
else:
      print("no tienes derecho a la becacion")
edad = int(input("cual es tu edad?"))
ingreso = int(input("cual es tu ingreso?"))

if edad > 16 and ingreso >= 1000:
    print("tienes que tributar")
else:
    print("No puedes tributar")
passo = str(input("Crear contraseña: "))
print("Guardando...")
pass2 = str(input("Ingrese la contraseña: "))

while passo != pass2:
    print("Contraña incorrecta")
    pass2 = str(input("Dame la contraseña de nuevo: "))
else:
    print("Acceso autorizado")
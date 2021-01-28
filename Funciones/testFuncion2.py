def validacion(correo):
    if "@" in correo:
        print("Correo valido")
        return correo
    else:
        print("Correo invalido")

a = str(input("Ingrese su correo electronico: "))
validacion(a)
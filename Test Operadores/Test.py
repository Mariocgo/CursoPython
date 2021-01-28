NumUno = int(input("Dame un numero"))
NumDos = int(input("Dame otro numero"))

if NumUno == NumDos:
    print("Son iguales")
elif(NumUno != NumDos):
    print("Son diferentes")
elif(NumUno > NumDos):
    print("Primero mayor al segundo")
elif(NumUno < NumDos):
    print("Segundo mayor que el primero")
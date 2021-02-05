def suma(num1,num2):
    return num1+num2

def resta(num1,num2):
    return num1-num2

def multi(num1,num2):
    return num1*num2

def divi(num1,num2):
    try:
        
        return num1/num2
    except ZeroDivisionError:
        print ("No se puede divir entre 0")
        
    return "Operacion no valida"

op1 = int(input("Introduce el primer valor: "))
op2 = int(input("Introduce el segundo valor: "))

operacion = input("Introduce la operacion a realizar (suma, resta, multi, dividir)")

if operacion == "suma":
    print(suma(op1,op2))
    
elif operacion == "resta":
    print(resta(op1,op2))    

elif operacion == "multi":
    print(multi(op1,op2))    

elif operacion == "dividir":
    print(divi(op1,op2))    
    
else:
    print("Error algo esta MAL")
    
print("Ejecutando")

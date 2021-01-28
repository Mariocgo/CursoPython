def infinito(**args):
    m = 0
    for i in args:
        m+=1
        print(m,"--",i,"-->",args[i])
        
infinito(a = "Hola",b = "Pizza")
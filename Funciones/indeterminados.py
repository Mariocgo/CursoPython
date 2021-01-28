'''
def infinito(*args):
    for args in args:
        print(args)
    
    
infinito("Hola", 20,10.0, [1,2,3])
'''
def infinito(**kwargs):
    for kwarg in kwargs:
        print(kwarg,"--->",kwargs[kwarg])

infinito(a = "Hola", b = 20, c = ["Maria", "Pedro", "Jose"])
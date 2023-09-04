def funcion_a(funcion_b): 
    def funcion_c():
        print("Antes del saludo")
        funcion_b()
        print("Despues del saludo")
    return funcion_c
    
@funcion_a    
def saludar():
    print("Hola desde mi decorador")
saludar()
def funcion_a(funcion_b):
    def funcion_c():
        print("Antes del cálculo")
        funcion_b()
        print("Despues del cálculo")
    return funcion_c

@funcion_a
def saludar():
    print("Hola saludos")

saludar()
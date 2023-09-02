def funcion_a(funcion_b):

    def funcion_c(*args, **kwargs):
        print("Antes de la ejecución")
        resultado = funcion_b(*args,**kwargs)
        print("Despues de la ejecucion")

        return resultado
    return funcion_c


@funcion_a
def saludar():
    print("hola")

@funcion_a
def suma(a,b):
    return a+b
print(suma(100,200))

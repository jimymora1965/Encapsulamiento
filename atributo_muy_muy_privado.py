#para la clase muy muy privada se debe crear un metodo para acceder a sus parametros....
#el atributo muy privado lleva doble guion: self.__variable.......

print("Ejemplo 1:")
class Atributo_Muy_Privado:
    def __init__(self):
        self.__variable_privada = "Valor del atributo privado"
    def acceder_variable_privada(self):
        print("El atributo privado es:\n", self.__variable_privada)

objeto = Atributo_Muy_Privado()
objeto.acceder_variable_privada()

print()
#Ejemplo 2:
print("Ejemplo 2:")
class Carro:
    def __init__(self):
        self.__valor = "Es costoso" 
        
    def imprimirValor(self):
        print("Precio: \n", self.__valor)
        
        
carro1 = Carro()
carro1.imprimirValor()
class Auto:
    def __init__(self, modelo, año):
        self._m = modelo
        self._a = año

    def get_modelo(self):
        return self._m
    
    def get_año(self):
        return self._a 
    
    def set_modelo(self,new_modelo):
        self._m = new_modelo

    def set_año(self, new_año):
        self._a = new_año

#creamos el objeto  y  lo llamamos con sus caracteristicas
vehiculo = Auto("Aveo", 2009)

modelo = vehiculo.get_modelo()
año = vehiculo.get_año()
print("El modelo es: " , modelo, "Del año: ", año)

#modificamoslos valores con set
vehiculo.set_modelo("Cruz")
vehiculo.set_año(2023)
modelo = vehiculo.get_modelo()
año = vehiculo.get_año()
print(modelo,año)


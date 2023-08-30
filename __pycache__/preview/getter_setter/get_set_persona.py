class Persona:
    def __init__(self,nombre,edad):
        self._n = nombre
        self._e = edad
        
    def get_nombre(self):
        return self._n
        
    def get_edad(self):
       return self._e
        
    def set_nombre(self,new_nombre):
        self._n = new_nombre
    
    def set_edad(self,new_edad):
        self._e = new_edad
        
        
estudiante = Persona("jimy",58)
nombre = estudiante.get_nombre()
edad = estudiante.get_edad()
print(nombre,edad)
estudiante.set_nombre("Christian")
estudiante.set_edad(27)
nombre = estudiante.get_nombre()
edad = estudiante.get_edad()
print(nombre,edad)


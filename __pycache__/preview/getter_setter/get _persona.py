print("Ejemplo 1: ")
print("get con return")
class Persona:
    def __init__(self,nombre,edad):
        self.n = nombre 
        self.e = edad 
        
    def get_nombre(self):
        return self.n
    
    def get_edad(self):
        return self.e
    
estudiante = Persona("jimy",58)
nombre = estudiante.get_nombre()
edad  = estudiante.get_edad()
print(f"{nombre} tiene {edad}años")

print()

print("Ejemplo 2:")
print("El get con print y no con return:")

class Estudiante:
    def __init__(self,nombre,edad):
        self.n = nombre 
        self.e = edad 
        
    def get_nombre(self):
        print(self.n) 
    
    def get_edad(self):
        print(self.e) 
    
estudiante = Estudiante("jimy",60)
estudiante.get_nombre()
estudiante.get_edad()

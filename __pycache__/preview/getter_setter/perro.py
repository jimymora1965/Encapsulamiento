class Animal:
    def __init__(self, raza,origen):
        self._r = raza
        self._o = origen
    
    def get_raza(self):
        return self._r 

    def get_origen(self):
        return self._o 


    def set_raza(self,new_raza):
        self._r = new_raza
    
    def set_origen(self, new_origen):
        self._o = new_origen
        
perro1 = Animal("Oddie","Mexico")
raza = perro1.get_raza()
origen = perro1.get_origen()

print(raza,origen)
    
perro1.set_raza("Pastor Aleman")
perro1.set_origen("Aleman.")
raza = perro1.get_raza()
origen = perro1.get_origen()
print(f"El {raza} es de origen {origen}")
    
  
    

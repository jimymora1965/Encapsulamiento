class Animales():
    def __init__(self, raza, origen):
        self._r = raza
        self._o = origen

    def get_raza(self):
        return self._r
    
    def get_origen(self):
        return self._o
    
    def set_raza(self, new_raza):
        self._r= new_raza

    def set_origen(self, new_origen):
        self._o = new_origen


perro = Animales("Chihuahua","Mexico")

raza = perro.get_raza()
origen= perro.get_origen()
print(raza, origen)

perro.set_raza("Pastor Aleman")
perro.set_origen("Alemania")
raza = perro.get_raza()
origen = perro.get_origen()
print(raza,origen)

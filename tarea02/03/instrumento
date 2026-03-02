class Instrumento:

    def __init__(self, nombre: str, material: str, tipo: str):
        self.nombre = nombre          
        self._material = material     
        self._tipo = tipo            

    def get_material(self) -> str:
        return self._material
    def set_material(self, material: str):
        self._material = material
    def get_tipo(self) -> str:
        return self._tipo
    def set_tipo(self, tipo: str):
        self._tipo = tipo
    def toString(self) -> str:
        return f"Instrumento [nombre={self.nombre}, material={self._material}, tipo={self._tipo}]"

instrumento1 = Instrumento("Guitarra", "Madera", "Cuerda")
instrumento2 = Instrumento("Flauta", "Metal", "Aire")

print(instrumento1.toString())
print(instrumento2.toString())
instrumento1.set_material("Caoba")
print("Nuevo material de la guitarra:", instrumento1.get_material())
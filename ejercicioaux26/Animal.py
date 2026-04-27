class Animal:
    def __init__(self, nombre, edad, nombre_dueno):
        self.nombre = nombre
        self.edad = edad
        self.nombre_dueno = nombre_dueno

class Perro(Animal):
    def __init__(self, nombre, edad, nombre_dueno, requiere_bosal, ladra_fuerte):
        super().__init__(nombre, edad, nombre_dueno)
        self.requiere_bosal = requiere_bosal
        self.ladra_fuerte = ladra_fuerte

    def __str__(self):
        return f"Perro: {self.nombre}, Edad: {self.edad}, Dueño: {self.nombre_dueno}"

class Gato(Animal):
    def __init__(self, nombre, edad, nombre_dueno, caza_ratones, toma_leche):
        super().__init__(nombre, edad, nombre_dueno)
        self.caza_ratones = caza_ratones
        self.toma_leche = toma_leche

    def __str__(self):
        return f"Gato: {self.nombre}, Edad: {self.edad}, Dueño: {self.nombre_dueno}"
    
class CentroVeterinario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.perros = []
        self.gatos = []

    def agregar_perro(self, perro):
        if len(self.perros) < 100:
            self.perros.append(perro)

    def agregar_gato(self, gato):
        if len(self.gatos) < 100:
            self.gatos.append(gato)
    
    def ordenar_perros(self):
        self.perros.sort(key=lambda p: (p.edad, p.nombre_dueno, p.nombre))

    def ordenar_gatos(self):
        self.gatos.sort(key=lambda g: (
            not g.toma_leche,   
            -g.edad, 
            g.nombre  
        ))

    def contar_animales_por_dueno(self):
        conteo = {}

        for p in self.perros:
            conteo[p.nombre_dueno] = conteo.get(p.nombre_dueno, 0) + 1

        for g in self.gatos:
            conteo[g.nombre_dueno] = conteo.get(g.nombre_dueno, 0) + 1

        for dueno, cantidad in conteo.items():
            if cantidad > 1:
                print(f"{dueno} tiene {cantidad} animales")

cv1 = CentroVeterinario("Veterinaria Norte")

cv1.agregar_perro(Perro("Firulais", 5, "Juan", True, True))
cv1.agregar_perro(Perro("Max", 3, "Ana", False, True))

cv1.agregar_gato(Gato("Michi", 2, "Juan", True, True))
cv1.agregar_gato(Gato("Luna", 4, "Carlos", False, False))


cv2 = CentroVeterinario("Veterinaria Sur")

cv2.agregar_perro(Perro("Rocky", 4, "Luis", True, False))
cv2.agregar_perro(Perro("Toby", 2, "Luis", False, True))

cv2.agregar_gato(Gato("Nina", 3, "Sofia", True, True))
cv2.agregar_gato(Gato("Pelusa", 5, "Sofia", False, True))

cv1.ordenar_perros()
cv1.ordenar_gatos()


print("\nPerros ordenados:")
for p in cv1.perros:
    print(p)

print("\nGatos ordenados:")
for g in cv1.gatos:
    print(g)

print("\nDueños con más de un animal:")
cv1.contar_animales_por_dueno()
cv2.contar_animales_por_dueno()
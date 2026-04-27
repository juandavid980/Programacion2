class Libro:
    def __init__(self, nombre, autor, anio):
        self.nombre = nombre
        self.autor = autor
        self.anio = anio

    def __str__(self):
        return f"{self.nombre} - {self.autor} ({self.anio})"

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []  

    def agregar_libro(self, libro):
        if len(self.libros) < 100:
            self.libros.append(libro)
        else:
            print("Biblioteca llena")

    def buscar_libro(self, nombre):
        for libro in self.libros:
            if libro.nombre.lower() == nombre.lower():
                return libro
        return None

    def cantidad_libros(self):
        return len(self.libros)

    def mostrar_libros(self):
        print(f"\nBiblioteca: {self.nombre}")
        for libro in self.libros:
            print(libro)


            
libro1 = Libro("Cien años de soledad", "Gabriel Garcia Marquez", 1967)
libro2 = Libro("1984", "George Orwell", 1949)
libro3 = Libro("Don Quijote", "Miguel de Cervantes", 1605)
libro4 = Libro("El Principito", "Antoine de Saint-Exupéry", 1943)

b1 = Biblioteca("Biblioteca Central")
b2 = Biblioteca("Biblioteca Escolar")

b1.agregar_libro(libro1)
b1.agregar_libro(libro2)

b2.agregar_libro(libro3)
b2.agregar_libro(libro4)

b1.mostrar_libros()
b2.mostrar_libros()

nombre_buscar = "1984"
resultado = b1.buscar_libro(nombre_buscar)

if resultado:
    print(f"\nLibro encontrado en {b1.nombre}: {resultado}")
else:
    print("\nLibro no encontrado en Biblioteca 1")

if b1.cantidad_libros() > b2.cantidad_libros():
    print(f"\nLa biblioteca con más libros es: {b1.nombre}")
elif b2.cantidad_libros() > b1.cantidad_libros():
    print(f"\nLa biblioteca con más libros es: {b2.nombre}")
else:
    print("\nAmbas bibliotecas tienen la misma cantidad de libros:")
    print(b1.nombre)
    print(b2.nombre)
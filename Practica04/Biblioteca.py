class Pagina:
    def __init__(self, numero, contenido):
        self.numero = numero
        self.contenido = contenido

    def mostrarPagina(self):
        print(f"Página {self.numero}: {self.contenido}")

class Libro:
    def __init__(self, titulo, isbn, contenidos_paginas):
        self.titulo = titulo
        self.isbn = isbn
        self.paginas = []
        for i in range(len(contenidos_paginas)):
            pagina = Pagina(i + 1, contenidos_paginas[i])
            self.paginas.append(pagina)

    def leer(self):
        print(f"\nLibro: {self.titulo}")

        for pagina in self.paginas:
            pagina.mostrarPagina()

class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def mostrarInfo(self):
        print(" AUTOR ")
        print(f"Nombre: {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")

class Estudiante:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def mostrarInfo(self):
        print("ESTUDIANTE")
        print(f"Código: {self.codigo}")
        print(f"Nombre: {self.nombre}")

class Prestamo:
    def __init__(self, estudiante, libro):

        self.fecha_prestamo = 1
        self.fecha_devolucion = 8
        self.estudiante = estudiante
        self.libro = libro

    def mostrarInfo(self):
        print(" PRÉSTAMO ")
        print(f"Estudiante: {self.estudiante.nombre}")
        print(f"Libro: {self.libro.titulo}")
        print(f"Fecha préstamo: Día {self.fecha_prestamo}")
        print(f"Fecha devolución: Día {self.fecha_devolucion}")

class Horario:
    def __init__(self, dias_apertura, hora_apertura, hora_cierre):
        self.dias_apertura = dias_apertura
        self.hora_apertura = hora_apertura
        self.hora_cierre = hora_cierre

    def mostrarHorario(self):
        print("HORARIO")
        print(f"Días: {self.dias_apertura}")
        print(f"Apertura: {self.hora_apertura}")
        print(f"Cierre: {self.hora_cierre}")

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
        self.autores = []
        self.prestamos = []
        self.horario = Horario(
            "Lunes a Viernes",
            "08:00",
            "20:00"
        )
    def agregarLibro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado.")

    def agregarAutor(self, autor):
        self.autores.append(autor)
        print(f"Autor '{autor.nombre}' registrado.")

    def prestarLibro(self, estudiante, libro):
        if libro in self.libros:
            prestamo = Prestamo(estudiante, libro)
            self.prestamos.append(prestamo)
            print(f"Libro '{libro.titulo}' prestado a {estudiante.nombre}")
        else:
            print("El libro no existe en la biblioteca")

    def mostrarEstado(self):
        print(f"BIBLIOTECA: {self.nombre}")
        self.horario.mostrarHorario()
        print("LIBROS DISPONIBLES ")

        for libro in self.libros:
            print(f"- {libro.titulo}")

        print(" AUTORES REGISTRADOS ")

        for autor in self.autores:
            print(f"- {autor.nombre}")

        print("PRÉSTAMOS ACTIVOS ")

        for prestamo in self.prestamos:
            prestamo.mostrarInfo()

    def cerrarBiblioteca(self):

        print("\nLa biblioteca está cerrando...")

        self.prestamos.clear()

        print("Todos los préstamos fueron eliminados")


biblioteca = Biblioteca("Biblioteca UMSA")

autor1 = Autor("Gabriel García Márquez", "Colombiano")
autor2 = Autor("Mario Vargas Llosa", "Peruano")

biblioteca.agregarAutor(autor1)
biblioteca.agregarAutor(autor2)

libro1 = Libro(
    "Cien años de soledad",
    "ISBN-001",
    [
        "Muchos años después frente al pelotón...",
        "El coronel recordó aquella tarde..."
    ]
)

libro2 = Libro(
    "La ciudad y los perros",
    "ISBN-002",
    [
        "Primera página del libro",
        "Segunda página del libro"
    ]
)

biblioteca.agregarLibro(libro1)
biblioteca.agregarLibro(libro2)

estudiante1 = Estudiante("2025001", "Juan Pérez")

biblioteca.prestarLibro(estudiante1, libro1)
biblioteca.mostrarEstado()
libro1.leer()

biblioteca.cerrarBiblioteca()
biblioteca.mostrarEstado()
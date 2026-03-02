class Anime:

    def __init__(self, nombre: str, genero: str, numero_episodios: int):
        self.nombre = nombre
        self.genero = genero
        self._numero_episodios = numero_episodios
        self._episodios = [None] * numero_episodios 

    def agregar_episodio(self, posicion: int, titulo: str):
        if 0 <= posicion < self._numero_episodios:
            self._episodios[posicion] = titulo
        else:
            print("Posición inválida")

    def mostrar_info(self):
        print("Nombre:", self.nombre)
        print("Género:", self.genero)
        print("Número de episodios:", self._numero_episodios)
        print("Lista de episodios:")

        for i, episodio in enumerate(self._episodios):
            if episodio is not None:
                print(f"{i+1}. {episodio}")

anime1 = Anime("Naruto", "Shonen", 3)
anime2 = Anime("Attack on Titan", "Acción", 2)

anime1.agregar_episodio(0, "Episodio 1")
anime1.agregar_episodio(1, "Episodio 2")

anime2.agregar_episodio(0, "Episodio 1")

anime1.mostrar_info()
print("")
anime2.mostrar_info()
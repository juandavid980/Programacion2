import math
class Estadistica:
    def __init__(self, n):
        self.__n = n

    def promedio(self):
        return sum(self.__n) / len(self.__n)

    def desviacion(self):
        media = self.promedio()
        suma = 0
        for x in self.__n:
            suma =suma + (x - media) ** 2
        return math.sqrt(suma / len(self.__n))


n = [ 1.9, 2.5, 3.7, 2, 1, 6, 3, 4, 5, 2]
estad = Estadistica(n)

print("El promedio es", estad.promedio())
print("La desviación estándar es", estad.desviacion())
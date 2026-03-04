import math

def promedio(n):
    return sum(n) / len(n)

def desviacion(n):
    media = promedio(n)
    suma = 0
    for x in n:
        suma =suma+ (x - media)*(x - media)
    return math.sqrt(suma / len(n))

n = [ 1.9, 2.5, 3.7, 2, 1, 6, 3, 4, 5, 2]
print("El promedio es", promedio(n))
print("La desviación estándar es", desviacion(n))
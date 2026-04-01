import math
from multimethod import multimethod 
class AlgebraVectorial:

    @multimethod
    def __init__(self):
        self.ax=0
        self.ay=0
        self.bx=0
        self.by=0

    @multimethod
    def __init__(self, ax:float, ay:float, bx:float, by:float):
        self.ax=ax
        self.ay=ay
        self.bx=bx
        self.by=by

    @multimethod
    def Perpendicular(self):
        suma = math.sqrt((self.ax+self.bx)**2 + (self.ay+self.by)**2)
        resta = math.sqrt((self.ax-self.bx)**2 + (self.ay-self.by)**2)
        return suma == resta

    @multimethod
    def Perpendicular(self, ax:float, ay:float, bx:float, by:float):
        ab = math.sqrt((ax-bx)**2 + (ay-by)**2)
        ba = math.sqrt((bx-ax)**2 + (by-ay)**2)
        return ab == ba

    @multimethod
    def Perpendicular(self, tipo:str):
        if tipo == "producto":
            return (self.ax*self.bx + self.ay*self.by) == 0

    @multimethod
    def Perpendicular(self, tipo:str, dummy:int):
        if tipo == "pitagoras":
            izq = (self.ax+self.bx)**2 + (self.ay+self.by)**2
            der = (self.ax**2 + self.ay**2) + (self.bx**2 + self.by**2)
            return izq == der


    @multimethod
    def Paralelo(self):
        if self.bx != 0:
            r = self.ax / self.bx
            return self.ay == r*self.by
        return False

    @multimethod
    def Paralelo(self, tipo:str):
        if tipo == "cruz":
            return (self.ax*self.by - self.ay*self.bx) == 0

    def proyeccion(self):
        prod = self.ax*self.bx + self.ay*self.by
        norma = self.bx**2 + self.by**2
        px = (prod/norma)*self.bx
        py = (prod/norma)*self.by
        return (px,py)
    
    def componente(self):
        prod = self.ax*self.bx + self.ay*self.by
        norma = math.sqrt(self.bx**2 + self.by**2)
        return prod/norma

v = AlgebraVectorial(3.0, 4.0, -4.0, 3.0)

print("Perpendicular (|a+b|=|a-b|):", v.Perpendicular())
print("Perpendicular (producto punto):", v.Perpendicular("producto"))
print("Perpendicular (Pitágoras):", v.Perpendicular("pitagoras", 1))

print("Paralelo (razón):", v.Paralelo())
print("Paralelo (producto cruz):", v.Paralelo("cruz"))

print("Proyección de a sobre b:", v.proyeccion())
print("Componente de a en b:", v.componente())
    
    
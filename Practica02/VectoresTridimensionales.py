import math
from multimethod import multimethod
class VectoresTri:
    @multimethod
    def __init__(self):
        self.ax = 0
        self.ay = 0
        self.az = 0
    
    @multimethod
    def __init__(self, ax, ay, az):
        self.ax = ax
        self.ay = ay
        self.az = az

    def SumaVectores(self, bx, by, bz):
        return (self.ax + bx, self.ay + by, self.az + bz)
    
    def MultEsc(self, r):
        return (r * self.ax, r * self.ay, r * self.az)
    
    def Longitud(self):
        return math.sqrt(self.ax**2 + self.ay**2 + self.az**2)


    def Normal(self):
        l = self.Longitud()
        return (self.ax/l, self.ay/l, self.az/l)

    def ProdEsc(self, bx, by, bz):
        return (self.ax * bx + self.ay * by + self.az * bz) 

    def ProdVec(self, bx, by, bz):
        return (
            self.ay*bz - self.az*by,
            self.az*bx - self.ax*bz,
            self.ax*by - self.ay*bx
        )
    
v = VectoresTri(2, 3, 4)

print("Vector a:", (v.ax, v.ay, v.az))

print("Suma con b=(1,2,3):", v.SumaVectores(1, 2, 3))

print("Multiplicación escalar r=2:", v.MultEsc(2))

print("Longitud de a:", v.Longitud())

print("Vector normal de a:", v.Normal())

print("Producto escalar con b=(1,2,3):", v.ProdEsc(1, 2, 3))

print("Producto vectorial con b=(1,2,3):", v.ProdVec(1, 2, 3))
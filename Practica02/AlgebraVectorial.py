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
    def __init__(self, ax:int,ay:int,bx:int,by:int):
        self.ax=ax
        self.ay=ay
        self.bx=bx
        self.by=by

    @multimethod
    def Perpendicular(self ):
        return (self.ax*self.bx+self.ay+self.by)==0
    
    @multimethod
    def Perpndicular(self,ax:int,ay:int,bx:int,by:int ):
        return (ax*bx+ay+by)==0
    
    @multimethod
    def Paralelo(self):
        return (self.ax*self.by-self.ay*self.bx)==0
    
    @multimethod
    def Paralelo(self,ax:int,ay:int,bx:int,by:int):
        return (ax*by-ay*bx)==0
    
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

    
    
import math
from multimethod import multimethod
class PoligonoRegular:
    
    @multimethod
    def __init__(self):
        self.__n=3
        self.__lado=1
        self.__x=0
        self.__y=0
    @multimethod
    
    
    def __init__(self,n:int,lado:float):
        self.__n=n
        self.__lado=lado
        self.__x=0
        self.__y=0
    
    
    @multimethod
    def __init__(self,n:int,lado:float,x:float,y:float):
        self.__n=n
        self.__lado=lado
        self.__x=x
        self.__y=y


    def getPerimetro(self):
        return self.__n* self.__lado
    

    def getArea(self):
        return (self.__n * self.__lado **2)/(4*math.tan(math.pi/self.__n))
    
p1=PoligonoRegular()
p2=PoligonoRegular(6,4.0)
p3=PoligonoRegular(10,4.0,5.6,7.8)

print("Poligono 1")
print("Area del poligono 1 ", p1.getArea())
print("Perimetro del poligono 1 ", p1.getPerimetro())

print("Poligono 2")
print("Area del poligono 2 ", p2.getArea())
print("Perimetro del poligono 3 ", p2.getPerimetro())

print("Poligono 3")
print("Area del poligono 2 ", p3.getArea())
print("Perimetro del poligono 2 ", p3.getPerimetro())
    

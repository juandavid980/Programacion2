import math
from multimethod import multimethod
class MiPunto:
    
    @multimethod
    def __init__(self):
        self.__x=0
        self.__y=0
    
    @multimethod
    def __init__(self, x:float,y:float):
        self.__x=x
        self.__y=y

    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    @multimethod
    def distancia(self,p):
        return math.sqrt((p.getX()-self.__x)**2+(p.getY()-self.__y)**2)
    
    @multimethod
    def distancia(self,x:float,y:float):
        return math.sqrt((x-self.__x)**2+(y-self.__y)**2)

p1=MiPunto()
p2=MiPunto(10.0,30.5)

print("distancia de p1 a p2", p1.distancia(p2))
print("distancia de p1 a 5,6", p1.distancia(5.0,6.0))


import math
from multimethod import multimethod
class VectoresTri:
    @multimethod
    def __init__(self,):
        self.ax=0
        self.ay=0
        self.az=0
    
    @multimethod
    def __init__(self,ax:int,ay:int,az:int):
        self.ax=ax
        self.ay=ay
        self.az=az


    def SumaVectores(self,bx,by,bz):
        return(self.ax+bx,self.ay+by,self.az,+bz)
    
    def MultEsc(self, e):
        return (self.ax*e+self.ay*e+self.az*e)
    
    def Lonigitud(self):
        return math.sqrt(self.ax**2+self.ay**2+self.az**2)

    def Normal(self):
        l=self.Lonigitud()
        return (self.ax/l,self.ay/l,self.az/l)

    def ProdEsc(self,bx,by,bz):
        return (self.ax*bx+self.ay*by+self.az*bz) 

    def ProdVec(self,bx,by,bz):
        return (self.ay*bz-self.az*by,self.az*bx-self.ax*bz,self.ax*by-self.ay*bx)
           
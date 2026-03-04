class EcuacionLineal:
    def __init__(self,a,b,c,d,e,f):
            self.__a=a
            self.__b=b
            self.__c=c
            self.__d=d
            self.__e=e
            self.__f=f
    def tieneSolucion(self):
          if(self.__a*self.__d-self.__b*self.__c != 0):
                return True
          else: 
               return False
    def getX(self):
        if(self.tieneSolucion()):
                return (self.__e*self.__d-self.__b*self.__f) / (self.__a*self.__d-self.__b*self.__c)
    def getY(self):
        if(self.tieneSolucion()):
                return (self.__a*self.__f-self.__e*self.__c) / (self.__a*self.__d-self.__b*self.__c) 

class Main():
    ec= EcuacionLineal(9.0,4.0,3.0,-5.0,-6.0,-21.0)
    if(ec.tieneSolucion()):
        print("x= ",ec.getX())
        print("y= ",ec.getY())
    else:
        print("La ecuacion no tiene solucion")


    ec2=EcuacionLineal(1.0,2.0,2.0,4.0,4.0,5.0)    
    if(ec2.tieneSolucion()):
        print("x= ",ec2.getX())
        print("y= ",ec2.getY())
    else:
        print("La ecuacion no tiene solucion")
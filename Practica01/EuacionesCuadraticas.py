import math
class EcuacionesLineal:
    def __init__(self,a,b,c):
        self.__a=a
        self.__b=b
        self.__c=c
   
   
    def getDiscriminante(self):
        if(self.__b*self.__b-4*self.__a*self.__c == 0):
            return 0
        if(self.__b*self.__b-4*self.__a*self.__c > 0):
            return 1
        if (self.__b*self.__b-4*self.__a*self.__c < 0):
            return -1
   
   
    def getRaiz1(self):
        return (-self.__b + math.sqrt(self.__b*self.__b-4*self.__a*self.__c )) / (2*self.__a)
   
   
    def getRaiz2(self):
        return (-self.__b - math.sqrt(self.__b*self.__b-4*self.__a*self.__c )) / (2*self.__a)

class Main():
    ec=EcuacionesLineal(1,3,1)
    ec1=EcuacionesLineal(1,2,1)
    ec2=EcuacionesLineal(1,2,3)
    
    if(ec.getDiscriminante() == 0):
        print("La ecuacion tiene una raiz ", ec.getRaiz1())
    if(ec.getDiscriminante() == 1):
        print("La ecuacion tiene dos raices ", ec.getRaiz1() , " y ", ec.getRaiz2())
    if(ec.getDiscriminante() == -1):
        print("La ecuacion no tiene raices reales ")
    


    if(ec1.getDiscriminante() == 0):
        print("La ecuacion tiene una raiz ", ec1.getRaiz1())
    if(ec1.getDiscriminante() == 1):
        print("La ecuacion tiene dos raices ", ec1.getRaiz1() , " y ", ec1.getRaiz2())
    if(ec1.getDiscriminante() == -1):
        print("La ecuacion no tiene raices reales ")


    if(ec2.getDiscriminante() == 0):
        print("La ecuacion tiene una raiz ", ec2.getRaiz1())
    if(ec2.getDiscriminante() == 1):
        print("La ecuacion tiene dos raices ", ec2.getRaiz1() , " y ", ec2.getRaiz2())
    if(ec2.getDiscriminante() == -1):
        print("La ecuacion no tiene raices reales ")
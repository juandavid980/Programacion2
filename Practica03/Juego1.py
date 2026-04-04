import random
class Juego:
    def __init__(self,numeroDeVidas,record):
        self.numeroDeVidas=numeroDeVidas
        self.record=record 

    def reiniciaPartida(self):
        self.vidasActuales=self.numeroDeVidas

    def actualizaRecord(self):
        if self.vidasActuales > self.record:
            self.record = self.vidasActuales
            print("nuevo record:", self.record)
    def quitaVida(self):
        self.vidasActuales-=1
        print("te quedan", self.vidasActuales, " vidas ")
        if self.vidasActuales>0:
            return True 
        else:
            print("game over")
            return False
class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas):
        super().__init__(numeroDeVidas,0)
        self.numeroAAdivinar=numeroDeVidas
        self.record=0
    def juega (self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0,10)
        print("adivina el numero del 1 al 10 ")
        while True:
            n=int(input("ingresa un numero"))
            if n==self.numeroAAdivinar :
                print("ganaste")
                self.actualizaRecord()
                break 
            else:
                if self.quitaVida():
                    if n>self.numeroAAdivinar:
                        print("el numero a adivinar es menor")
                    else:
                        print ("el numero a adivinar es mayor")
                else:
                    print("el numero a advinar era",self.numeroAAdivinar)
                    break 
if __name__ == "__main__":
    juego=JuegoAdivinaNumero(3)
    juego.juega()


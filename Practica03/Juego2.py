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
    def validaNumero(self, n):
        return 0 <= n <= 10
    def juega (self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0,10)
        print("adivina el numero del 1 al 10 ")
        while True:
            n=int(input("ingresa un numero"))
            if not self.validaNumero(n):
                print("Número inválido (debe estar entre 0 y 10)")
                continue
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

class JuegoAdivinaPar(JuegoAdivinaNumero):
    def validaNumero(self, n):
        if 0 <= n <= 10:
            if n % 2 == 0:
                return True
            else:
                print("el número debe ser par")
                return False
        return False
    
class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def validaNumero(self, n):
        if 0 <= n <= 10:
            if n % 2 != 0:
                return True
            else:
                print("el número debe ser  impar")
                return False
        return False
if __name__ == "__main__":
    juego1 = JuegoAdivinaNumero(3)
    juego2 = JuegoAdivinaPar(3)
    juego3 = JuegoAdivinaImpar(3)

    juego1.juega()
    juego2.juega()
    juego3.juega()


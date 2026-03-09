class Bus:
    def __init__(self,cap):
        self.cap=cap
        self.pasajeros=0
        self.pasaje=1.50
        


    def sub_P(self, cant):
        if self.pasajeros + cant <=self.cap:
            self.pasajeros += cant
            print ("acaban de subir " , cant)
        else:
            print("no hay suficientes asientos")
    
    def c_pasaje(self):
        p=self.pasajeros*self.pasaje
        print("total cobrado " , p , "Bs")
    
    def asientos_d(self):
        a=self.cap - self.pasajeros
        print("asientos disponibles " , a)

bus=Bus(35)

bus.sub_P(15)
bus.c_pasaje()
bus.asientos_d()

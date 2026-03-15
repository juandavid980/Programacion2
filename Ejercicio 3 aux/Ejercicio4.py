from multimethod import multimethod
class Videojuego:

    @multimethod
    def __init__(self):
        self.nombre="sin nombre"
        self.plataforma="sin nombre"
        self.jugadores=0
    @multimethod
    def __init__(self,nombre:str,plataforma:str):
        self.nombre=nombre
        self.plataforma=plataforma
        self.jugadores=0

    @multimethod
    def __init__(self,nombre:str,plataforma:str,jugadores:int):
        self.nombre=nombre
        self.plataforma=plataforma
        self.jugadores=jugadores

    @multimethod
    def AgregarJugadores(self):
        self.jugadores +=1

    @multimethod
    def AgregarJugadores(self,n:int):
        self.jugadores += n

v1=Videojuego("Minecraft","Computadora")
v2=Videojuego("Free Fire","Celular",4)
v2.AgregarJugadores(4)
print(v1.nombre,v1.plataforma,v1.jugadores)
print(v2.nombre,v2.plataforma,v2.jugadores)

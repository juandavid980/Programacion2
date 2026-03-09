class Minecraft:
    def __init__(self):
        self.jugadores=[]
        self.diamantes=[]
        self.max=10
    
    def ag_jugador(self, nombre, diamantes):
        if len(self.jugadores) < self.max:
            self.jugadores.append(nombre)
            self.diamantes.append(diamantes)
            print("nuevo jugador del server: " , nombre)
        else: 
            print ("el server esta lleno ")
        
    def stacks(self):
        for i in range (len (self.jugadores)):
            st=self.diamantes[i]//64
            print(self.jugadores[i], "tiene" , st ,"stacks de diamantes ")

    def jug_mas_d(self):
        max_d=max(self.diamantes)
        i=self.diamantes.index(max_d)
        print("jugador con mas diamantes", self.jugadores[i])


    def total_d(self):
        t=sum(self.diamantes)
        print("totak de diamonds en el server ", t)    



server=Minecraft()

server.ag_jugador("juanchi", 128)
server.ag_jugador("marco", 78)
server.ag_jugador("alexander", 98)

server.stacks()
server.jug_mas_d()
server.total_d()

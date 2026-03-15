from multimethod import multimethod
class Aula:

    def __init__(self,NombredeAula,piso,notas):
        self.NombredeAula=NombredeAula 
        self.piso=piso 
        self.notas=notas
    @multimethod
    def mostrar(self):
        print("nombre del aula", self.NombredeAula)
        print("piso",self.piso)
        print ("notas")
        for e in self.notas:
            print(e[0],"  ",e[1])

    @multimethod
    def mostrar(self,calificacion:str):
        print("calificacion de los estudiantes")
        for e in self.notas:
            if e[1]>=51:
                cal="aprobado"
            else:
                cal="reprobado"

            print(e[0], e[1] , cal )

matriz=[
    ["juan", 67],
    ["luis", 45],
    ["marco",25]
]
a1=Aula("promo24",1,matriz)
a1.mostrar()
a1.mostrar("calificaciones")
class NPC:  # Base, Pai, Super
    def __init__(self, nome, time, forca, municao) -> None:
        self.nome = nome
        self.time = time
        self.forca = forca
        self.municao = municao
        self.vivo = True
        self.energia = 100

    def info(self) -> None:
        print("Nome: "+str(self.nome))
        print("Time: "+str(self.time))
        print("Força: "+str(self.forca))
        print("Munição: "+str(self.municao))
        print("Vivo: "+("Sim" if self.vivo else "Não"))
        print("Energia: "+str(self.energia))
        print("-------------------------------------")


class Soldado(NPC):
    def __init__(self, nome, time) -> None:
        self.forca = 200
        self.municao = 200
        super().__init__(nome, time,self.forca, self.municao)


class Guarda(NPC):
    def __init__(self, nome, time) -> None: 
        self.forca = 100
        self.municao = 120
        super().__init__(nome, time,self.forca, self.municao)


class Elite(NPC):
    def __init__(self, nome, time) -> None:
        self.forca = 900
        self.municao = 300
        super().__init__(nome, time, self.forca, self.municao)

s1=Guarda("Cavalo", 1)
s2=Soldado("Minhoca", 1)
s3=Elite("Picapau", 1) 
s4=Guarda("Picachu", 2)
s5=Soldado("Curintia", 2)
s6=Elite("Salazar", 2)

s1.info()
s2.info()
s3.info()
s4.info()
s5.info()
s6.info()



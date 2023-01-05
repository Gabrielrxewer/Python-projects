class Carro:
    velMax = 0
    ligado = False
    cor = ""
    def __init__(self,v,l,c):
     self.velMax=v
     self.ligado=l
     self.cor=c
    def mostrar(self):
        estado = "Sim" if self.ligado else "Não"
        print("Velocidade Maxima: "+ str(self.velMax))
        print("Cor: "+self.cor) 
        print("Ligado: "+estado)
        print("-------------------------")
    def ligar(self):
        self.ligado=True
    def desligar(self):
        self.ligado=False
    def andar (self):
        if(self.ligado):
            print("Andando")
        else:
            print("Carro desligado")    

c1 = Carro(200, False, "Preto")
c2 = Carro(250, False, "Branco")
c3 = Carro(350, False, "Vermelho")

c1.ligar()
c3.ligar()

c1.andar()
c2.andar()

c1.mostrar()
c2.mostrar()
c3.mostrar()




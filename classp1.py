class Carro:
    velMax = 0
    ligado = False
    cor = ""


c1 = Carro()
c2 = Carro()
c3 = Carro()

c1.velMax = 200
c1.cor = "Preto"
c1.ligado = False

estado = "Sim" if c1.ligado else "Não"

print("Velocidade Máxima: "+str(c1.velMax))
print("Cor: " + str(c1.cor))
print("Ligado: "+str(estado))

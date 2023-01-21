def probabilidade_evento(evento_favoravel, evento_total):
    probabilidade = evento_favoravel / evento_total
    print("A probabilidade de ocorrência do evento é de  {:.2f}".format(
        probabilidade*100))


evento_favoravel = int(input("Insira o número de eventos favoráveis: "))
evento_total = int(input("Insira o número total de eventos: "))
probabilidade_evento(evento_favoravel, evento_total)

n1 = 19
n2 = 23


def somar(*num):
    r = 0
    for n in num:
        r += n
    print("A Soma é igual a: "+str(r))


somar(n1, n2)


def textos(*txt):
    for t in txt:
        print(t)


textos("Cavalo", "Sapo", "Montanha", "Savana")


def carros(c="Golf"):
    print("Modelo:" + c)


carros()

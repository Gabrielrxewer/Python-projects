import os
import random

jogarNovamente = True
jogadas = 0
quemJoga = 1
maxJogadas = 9
vit = False
velha = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


def imagem():
    global velha
    global jogadas
    i = 0
    f = 3
    a = 0
    os.system("cls")
    print("    0   1   2")
    while i < f:
        print(str(a)+":  " + velha[a][0] + " | " +
              velha[a][1] + " | " + velha[a][2])
        print("   ------------")
        a += 1
        i += 1
    print("Jogadas: "+str(jogadas))


def jogadaPlayer():
    global jogadas
    global quemJoga
    global x
    if quemJoga == 2 and jogadas < maxJogadas:
        x = int(input("Linha..: "))
        y = int(input("Coluna.: "))
        velha[x][y] = "X"
        quemJoga = 1
        jogadas += 1
    try:
        while velha[x][y] != "X":
            x = int(input("Linha..: "))
            y = int(input("Coluna.: "))
            velha[x][y] = "X"
            quemJoga = 1
            jogadas += 1
    except:
        print("Linha ou coluna inválida")


def jogada():
    global jogadas
    global quemJoga
    global x
    if quemJoga == 1 and jogadas < maxJogadas:
        x = random.randrange(0, 3)
        y = random.randrange(0, 3)
        while velha[x][y] != " ":
            x = random.randrange(0, 3)
            y = random.randrange(0, 3)
        velha[x][y] = "O"
        quemJoga = 2
        jogadas += 1


def empate():
    if jogadas == maxJogadas:
        print("Empate")
    else:
        jogada()
        jogadaPlayer()


def vitoria():
    global velha
    vitoria = "n"
    simbolos = ["X", "O"]
    for s in simbolos:
        vitoria = "n"
        # Verificação de Linha
        il = ic = 0
        while il < 3:
            soma = 0
            ic = 0
            while ic < 3:
                if (velha[il][ic] == s):
                    soma += 1
                ic += 1
            if (soma == 3):
                vitoria = s
                break
            il += 1
        if (vitoria != "n"):
            break
        # Verificação de Coluna
        il = ic = 0
        while ic < 3:
            soma = 0
            il = 0
            while il < 3:
                if (velha[il][ic] == s):
                    soma += 1
                il += 1
            if (soma == 3):
                vitoria = s
                break
            ic += 1
        if (vitoria != "n"):
            break
        # Verificação de Diagonais
        soma = 0
        idiagl = 0
        idiagc = 2
        while idiagc < 3:
            if (velha[idiagl][idiagc] == s):
                soma += 1
            idiagl += 1
            idiagl -= 1
        if (soma == 3):
            vitoria = s
            break
    return vitoria


while True:
    imagem()
    empate()
    vitoria()

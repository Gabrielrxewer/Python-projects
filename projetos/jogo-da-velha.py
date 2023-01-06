import os
import random

jogarNovamente = True
jogadas = 0
quemJoga = 2
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
    if quemJoga == 2 and jogadas < maxJogadas:
        x = int(input("Linha..: "))
        y = int(input("Coluna.: "))
    try:
        while velha[x][y] != " ":
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
    if quemJoga == 2 and jogadas < maxJogadas:
        x = int(input("Linha..: "))
        y = int(input("Coluna.: "))
    try:
        while velha[x][y] != " ":
            x = int(input("Linha..: "))
            y = int(input("Coluna.: "))
        velha[x][y] = "X"
        quemJoga = 1
        jogadas += 1
    except:
        print("Linha ou coluna inválida")

def empate():
    if jogadas == maxJogadas:
        print("Empate")
    else:
        jogada()

while True:
    imagem()
    empate()


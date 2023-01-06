import os
import random

jogarNovamente=True
jogadas=0
quemJoga=2
maxJogadas=9
vit=False
velha=[
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def imagem2():
    velha
    jogadas
    i=0
    f=3
    a=0
    os.system("cls")
    print("    0   1   2")
    while i<f:
        print(str(a)+":  " + velha[a][0] + " | " + velha[a][1] + " | " + velha[a][2])
        print("   ------------")
        a+=1
        i+=1
    print("Jogadas: "+str(jogadas))
imagem2()

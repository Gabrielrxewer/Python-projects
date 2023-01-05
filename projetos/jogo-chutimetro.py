import random
import os

os.system('cls')

print("Pensei em um número, tente adivinhar!")
num = random.randrange(0, 10)
num2 = int(input("Digite o número: "))
tent = 1
os.system('cls')
print("Tentativas: "+str(tent))


while int(num2) != num:
    if num2 < num:
        print("Você errou, o número é maior, tente novamente")
        num2 = int(input("Adivinhe o número: "))
        os.system('cls')
    elif num2 > num:
        print("Você errou, o número é menor, tente novamente")
        num2 = int(input("Adivinhe o número: "))
        os.system('cls')
    tent += 1
    print("Tentativas: "+str(tent))

if num2 == num:
    os.system('cls')
    print("Você acertou, parabéns!")
    print("Você precisou de "+str(tent)+" Tentativas!")

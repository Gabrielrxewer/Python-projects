import os
os.system('cls')

carros = ["HRV", "Golf", "Argo", "Onix", "Focus"]
i = 0
tam = len(carros)
while i < tam:
    print(carros[i])
    i += 1
    if (i >= 5):
        break
print("\n Fim do Looping \n")

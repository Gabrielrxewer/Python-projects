# Pergunta a idade da mãe
idade_mae = int(input("Qual é a idade da sua mãe? "))

# Calcula a idade média em que as mulheres engravidam pela primeira vez
idade_media_gravidez = 25

# Pergunta a preferência musical
preferencia_musical = input("Entre eletrônica, rock e sertanejo, qual você escolheria? ")

# Verifica a preferência musical e ajusta a idade em conformidade
if preferencia_musical == "eletrônica":
    ajuste_idade_preferencia = -0.01
elif preferencia_musical == "rock":
    ajuste_idade_preferencia = 0.01
else:
    ajuste_idade_preferencia = 0.05

# Pergunta a altura da pessoa
altura = float(input("Quanto você tem de altura? "))

# Verifica a altura e ajusta a idade em conformidade
if altura > 1.8:
    ajuste_idade_altura = -0.01
else:
    ajuste_idade_altura = 0.01

# Calcula a idade final estimada
idade_estimada = idade_mae - idade_media_gravidez + (ajuste_idade_preferencia * idade_mae) + (ajuste_idade_altura * idade_mae)

# Imprime a idade estimada
print("A sua idade estimada é de", round(idade_estimada), "anos.")

carros = ["Hylux", "Golf", "Argo", "Focus"]
carros.append("Fit")
carros.append("Fusion")
carros.append("Fusca")

carros.remove("Hylux")

carros.pop()

carros2 = list(carros)

carros.clear()

print(str(len(carros)) + " carros na lista")
print(carros)

print(str(len(carros2)) + " carros na lista")
print(carros2)

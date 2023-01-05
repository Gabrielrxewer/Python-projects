carro = {
    "Fabricante": "Honda",
    "Modelo": "HRV",
    "Ano": "2016",
    "Cor": "Prata"
}
carro["Cambio"] = "Automático"
carro.pop("Cambio")  # del carro["Cambio"]
fab = carro["Fabricante"]
print(carro)
print(fab)

if "Modelo" in carro:
    print("Sim, modelo e uma chave \n")

for c, v in carro.items():
    print(c + ": " + v)

carros = {
    "Carro1": {
        "Fabricante": "Honda",
        "Modelo": "HRV"
    },
    "Carro2": {
        "Fabricante": "Volkswagem",
        "Modelo": "Golf"
    },
    "Carro3": {
        "Fabricante": "Ford",
        "Modelo": "Focus"
    }
}
print(carros["Carro1"]["Fabricante"])

Carro4 = {
    "Fabricante": "Honda",
    "Modelo": "HRV"
}
Carro5 = {
    "Fabricante": "Volkswagem",
    "Modelo": "Golf"
}
Carro6 = {
    "Fabricante": "Ford",
    "Modelo": "Focus"
}

carros1 = {
    "C1": Carro4,
    "C2": Carro5,
    "C3": Carro6
}

print(carros1["C3"]["Modelo"])

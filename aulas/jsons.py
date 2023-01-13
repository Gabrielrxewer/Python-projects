import json

carros_json = '{"marca":"honda","modelo":"HRV","cor":"prata"}'


carros=json.loads(carros_json)

for x in carros.values():
    print(x)

for x in carros.items():
    print(x)

for x in carros:
    print(x)

animais={
    "peso":"15Kg",
    "tamanho":"30Cm",
    "especie":"Reptil"
}

animais_json=json.dumps(animais)

print(str(animais_json))
import json

carros_dictionary = {
    "marca": "honda",
    "modelo": "HRV",
    "cor": "prata"
}
# dictionary -> objeto json

carros_list = ["honda", "volswagem", "ford", "fiat", "chevrolet"]

# list -> array json

carros_tupla = ("honda", "volswagem", "ford", "fiat", "chevrolet")

# tupla -> array json

carros_j = json.dumps(carros_dictionary, indent=4,
                      separators=(": ", "="), sort_keys=True)
print(carros_j)

ga_j='{"nome":"Gabriel"}'
ga = json.loads(ga_j)
print(ga)

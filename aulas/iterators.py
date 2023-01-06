carros=["HRV","Polo","Jetta","Cruze","Fusion"]

itCarros=iter(carros)

while itCarros:
    try:
        print(next(itCarros))
    except:
        print("Fim da lista")
        break
import re #RegEX

texto="Curso de Python - Gabriel Roewer Pilger está estudando Python"

pesq=input("Procurar: ")
res=re.findall(pesq, texto)
qtde=len(res)

print(res)
print("Qtde: "+ str(qtde))

for t in res:
    print(t)
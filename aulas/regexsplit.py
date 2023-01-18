import re #RegEx

texto="Cursando curso de python na CFB Cursos Gabriel"

res=re.split("d", texto)
print(res)

for f in res:
    print(f)
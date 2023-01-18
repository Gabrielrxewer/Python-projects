import re #RegEx

texto="Cursando curso de python na CFB Cursos Gabriel"

pesq=input("Pesquisar: ")
res=re.search(pesq, texto)

if(res != None):
    pi=res.start()
    pf=res.end()
    tam=pf-pi
    print(res)
    print("A palavra começa na posição: "+str(res.start()))
    print("A palavra termina na posição: "+str(res.end()))
    print("A palavra tem: "+str(tam)+" letras!")
else:
    print("Não encontrado")
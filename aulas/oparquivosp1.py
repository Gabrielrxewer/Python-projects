nada="teste.txt"
f=open("C:/projetos/python/aulas/"+nada,"at")

#r - read - Leitura
#a - append - Anexar
#w - write - Escrita
#x - create - Criar
#t - text - Texto
#b - binary - Binário

txt=input("Digite algo: ")
f.write(txt+"\n")

f.close()
import re
nada="teste.txt"
f=open("C:/projetos/python/aulas/"+nada,"rt")

#for i in f:
#    print(i)

#print(f.readline())

res=re.sub("\s","-",f.readline())
f.close()

f=open("C:/projetos/python/aulas/"+nada,"wt")
f.write(res)
f.close()

print(res)
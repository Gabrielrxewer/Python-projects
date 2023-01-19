import re 
import os

nome="teste2.txt"
caminho="C:/projetos/python/aulas/"

if os.path.exists(caminho+nome):
    print("O arquivo já foi criado")
else:    
    f=open(caminho+nome,"x")
    print("O arquivo foi criado")
    f.close()

if os.path.exists(caminho+nome):
    os.remove(caminho+nome)
    print("O arquivo foi excluído")
else:
    print("O arquivo não existe")

import sqlite3
import os
from sqlite3 import Error

os.system('cls')

def conexaoBanco():
    caminho = "C:/projetos/python/database/agenda.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con


vcon = conexaoBanco()

def select(conexao, sql):
        c = conexao.cursor()
        c.execute(sql)
        resultado=c.fetchall()
        return resultado
vsql="SELECT * FROM tb_contatos"
select(vcon, vsql)
res=select(vcon, vsql)
print(res)
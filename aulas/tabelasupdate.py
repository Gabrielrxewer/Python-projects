import sqlite3
import os
from sqlite3 import Error

os.system('cls')

# Conexão


def conexaoBanco():
    caminho = "C:/projetos/python/database/agenda.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con


vcon = conexaoBanco()

# Inserir

#nome = input("Digite seu nome: ")
#tel = input("Digite seu telefone: ")
#email = input("Digite seu email: ")

#vsql = "INSERT INTO tb_contatos (T_NOMECONTATO,T_TELEFONECONTATO,T_EMAILCONTATO)   VALUES('" + \
#    nome+"','"+tel+"','"+email+"')"


def inserir(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Informações inseridas!")
    except Error as ex:
        print(ex)

# inserir(vcon, vsql)


# Deletar

def deletar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Informações deletadas!")
    except Error as ex:
        print(ex)


vsql = "DELETE FROM tb_contatos WHERE N_IDCONTATO=8"

# deletar(vcon, vsql)

# Update


def update(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Informações Atualizadas!")
    except Error as ex:
        print(ex)

d=input("Digite um novo nome: ")
vsql = "UPDATE tb_contatos SET T_NOMECONTATO='"+d+"' WHERE N_IDCONTATO=5"

update(vcon, vsql)
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

nome = input("Digite seu nome: ")
tel = input("Digite seu telefone: ")
email = input("Digite seu email: ")

vsql = "INSERT INTO tb_contatos (T_NOMECONTATO,T_TELEFONECONTATO,T_EMAILCONTATO)   VALUES('" + \
    nome+"','"+tel+"','"+email+"')"


def inserir(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Informações inseridas!")
    except Error as ex:
        print(ex)


inserir(vcon, vsql)

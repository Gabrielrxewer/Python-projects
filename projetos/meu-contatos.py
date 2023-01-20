import os
import sqlite3
from sqlite3 import Error


def conexaoBanco():
    caminho = "C:/projetos/python/database/contatos.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con


vcon = conexaoBanco()


def menu():
    print("Bem vindo ao Menu")
    print("Opção 1")
    print("Opção 2")
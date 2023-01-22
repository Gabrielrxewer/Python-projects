import sqlite3
from tkinter import *
import pygame

# Criação da base de dados e tabela
conn = sqlite3.connect('music.db')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE musicas (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                arquivo TEXT NOT NULL);""")
conn.commit()

# Inicializando pygame e tkinter
root = Tk()
pygame.init()

# Função para adicionar músicas à base de dados


def adicionar_musica():
    nome = nome_entrada.get()
    arquivo = arquivo_entrada.get()
    cursor.execute("""INSERT INTO musicas (nome, arquivo)
                VALUES (?,?)""", (nome, arquivo))
    conn.commit()

# Função para reproduzir música selecionada


def reproduzir_musica():
    musica = listbox.get(ACTIVE)
    cursor.execute("SELECT arquivo FROM musicas WHERE nome=?", (musica,))
    arquivo = cursor.fetchone()[0]
    pygame.mixer.music.load(arquivo)
    pygame.mixer.music.play()


# Criação da interface gráfica
nome_label = Label(root, text="Nome da música:")
nome_label.pack()
nome_entrada = Entry(root)
nome_entrada.pack()
arquivo_label = Label(root, text="Caminho do arquivo:")
arquivo_label.pack()
arquivo_entrada = Entry(root)
arquivo_entrada.pack()
adicionar_button = Button(
    root, text="Adicionar música", command=adicionar_musica)
adicionar_button.pack()
listbox = Listbox(root)
listbox.pack()
reproduzir_button = Button(root, text="Reproduzir", command=reproduzir_musica)
reproduzir_button.pack()

root.mainloop()

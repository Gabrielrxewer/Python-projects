import sqlite3
from tkinter import *

root = Tk()
root.title("SQLite3 Database App")

# Conecta ao banco
connection = sqlite3.connect('C:/projetos/python/database/words.db')
cursor = connection.cursor()

# Cria a tabela caso ela não exista
cursor.execute('''CREATE TABLE IF NOT EXISTS words (word TEXT)''')

# Função para inserir a palavra
def insert_word():
    word = word_entry.get()
    cursor.execute(f"INSERT INTO words (word) VALUES ('{word}')")
    connection.commit()
    word_entry.delete(0, END)

# Cria uma label para por a palavra
word_label = Label(root, text="Word:")
word_entry = Entry(root)
word_label.grid(row=0, column=0)
word_entry.grid(row=0, column=1)

# Cria um botão para enviar a palavra ao banco
insert_button = Button(root, text="Submit", command=insert_word)
insert_button.grid(row=1, column=1)

root.mainloop()
import os
import sqlite3
from sqlite3 import Error
import tkinter as tk

conn = sqlite3.connect("C:/projetos/python/enova/database/os.db", timeout=10)

#Armazena a O.S no banco de dados

def save_data():
    cod_os = entry1.get()
    desc_os = entry2.get()
    orig_os = entry3.get()
    resp_os = entry4.get()
    tipo_os = entry5.get()
    equip_os = entry6.get()
    setor_os = entry7.get()
    infos_os = entry8.get()

    with sqlite3.connect("C:/projetos/python/enova/database/os.db") as conn:
        c = conn.cursor()

        c.execute("INSERT INTO tb_OS (COD_OS, DESC_OS, ORIG_OS, RESP_OS, TIPO_OS, EQUIP_OS, SETOR_OS, INFOS_OS) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                  (cod_os, desc_os, orig_os, resp_os, tipo_os, equip_os, setor_os, infos_os))

    print("Informações inseridas!")

#Cria o Menu de cadastro
root = tk.Tk()
root.title("Cadastro de O.S")

label1 = tk.Label(root, text="Código da O.S")
label1.grid(row=0, column=0, padx=10, pady=10)

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)

label2 = tk.Label(root, text="Descrição da O.S")
label2.grid(row=1, column=0, padx=10, pady=10)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)

label3 = tk.Label(root, text="Origem O.S")
label3.grid(row=2, column=0, padx=10, pady=10)

entry3 = tk.Entry(root)
entry3.grid(row=2, column=1, padx=10, pady=10)

label4 = tk.Label(root, text="Responsável pela O.S")
label4.grid(row=3, column=0, padx=10, pady=10)

entry4 = tk.Entry(root)
entry4.grid(row=3, column=1, padx=10, pady=10)

label5 = tk.Label(root, text="Tipo da O.S")
label5.grid(row=4, column=0, padx=10, pady=10)

entry5 = tk.Entry(root)
entry5.grid(row=4, column=1, padx=10, pady=10)

label6 = tk.Label(root, text="Equipamento")
label6.grid(row=5, column=0, padx=10, pady=10)

entry6 = tk.Entry(root)
entry6.grid(row=5, column=1, padx=10, pady=10)

label7 = tk.Label(root, text="Setor")
label7.grid(row=6, column=0, padx=10, pady=10)

entry7 = tk.Entry(root)
entry7.grid(row=6, column=1, padx=10, pady=10)

label8 = tk.Label(root, text="Informações")
label8.grid(row=7, column=0, padx=10, pady=10)

entry8 = tk.Entry(root)
entry8.grid(row=7, column=1, padx=10, pady=10)

save_button = tk.Button(root, text="Gerar O.S", command=save_data)
save_button.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()

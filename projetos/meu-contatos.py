import sqlite3

# Cria ou conecta ao banco de dados
conn = sqlite3.connect('contacts.db')

# Cria o cursor
cursor = conn.cursor()

# Cria a tabela de contatos (caso ela ainda não exista)
cursor.execute("""CREATE TABLE IF NOT EXISTS contatos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                email TEXT,
                telefone TEXT
                )""")


def menu():
    print("1 - Cadastrar novo usuário")
    print("2 - Deletar usuário")
    print("3 - Buscar usuário")
    print("4 - Editar usuário")
    print("5 - Sair")
    opcao = input("Escolha uma opção: ")
    return opcao


def cadastrar_usuario():
    nome = input("Insira o nome: ")
    email = input("Insira o e-mail: ")
    telefone = input("Insira o telefone: ")
    cursor.execute(
        "INSERT INTO contatos (nome, email, telefone) VALUES (?,?,?)", (nome, email, telefone))
    conn.commit()
    print("Usuário cadastrado com sucesso!")


def deletar_usuario():
    nome = input("Insira o nome do usuário a ser deletado: ")
    cursor.execute("DELETE FROM contatos WHERE nome = ?", (nome,))
    conn.commit()
    print("Usuário deletado com sucesso!")


def buscar_usuario():
    nome = input("Insira o nome do usuário a ser buscado: ")
    cursor.execute("SELECT * FROM contatos WHERE nome = ?", (nome,))
    usuario = cursor.fetchone()
    if usuario:
        print("Nome: " + usuario[1])
        print("E-mail: " + usuario[2])
        print("Telefone: " + usuario[3])
    else:
        print("Usuário não encontrado.")


def editar_usuario():
    nome = input("Insira o nome do usuário a ser editado: ")
    cursor.execute("SELECT * FROM contatos WHERE nome = ?", (nome,))
    usuario = cursor.fetchone()
    if usuario:
        novo_nome = input("Insira o novo nome: ")
        novo_email = input("Insira o novo e-mail: ")
        novo_telefone = input("Insira o novo telefone: ")
        cursor.execute("UPDATE contatos SET nome = ?, email = ?, telefone = ? WHERE nome = ?",
                       (novo_nome, novo_email, novo_telefone, nome))
        conn.commit()
        print

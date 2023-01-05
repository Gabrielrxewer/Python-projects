import os
carros = list()


def carrinho(nome_carro='Escreva um nome válido>'):
    print(nome_carro)


def inteiro(txt):
    while True:
        try:
            potência_carro = int(input(txt))
        except (ValueError, TypeError):
            print('Digite uma potência válida')
            continue
        except KeyboardInterrupt:
            print('Digite uma potência válida')
            return 0
        else:
            return potência_carro


def cadastro(opção='Digite apenas uma opção do Menu>'):
    print(opção)


class Carro:
    nome = ''
    potência = 0
    velMax = 0
    ligado = False

    def __init__(self, nome, potência):
        self.nome = nome
        self.potência = potência
        self.velMax = int(potência)*2
        self.ligado = False

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def info(self):
        print('\nNome.......: ' + self.nome)
        print('Potência...: ' + str(self.potência))
        print('Vel.Maxima.: ' + str(self.velMax))
        print('Ligado.....: ' + ('Sim' if self.ligado == True else 'Não'))


def menu():
    print('\n')
    os.system("cls") or None
    print('-' * 43)
    print("Menu das opções")
    print('-' * 43)
    print('1 - Novo carro')
    print('2 - Informações do carro')
    print('3 - Excluir carro')
    print('4 - Ligar carro')
    print('5 - Desligar carro')
    print('6 - Listar carro')
    print('7 - Sair')
    print(
        'Quantidade de carros:' + str(len(carros)))
    print('-' * 43)

    while True:
        opção = input(">> Digite uma opção: ")
        if opção not in '1234567':
            cadastro(opção='Digite apenas as opções do menu>')
        else:
            break
    return opção


def Novo_Carro():
    print('\n')
    os.system("cls") or None
    print('=' * 43)
    print("=-=-=- Opção 1 -=-=-=")
    print('=' * 43)
    while True:
        nome_carro = input(">> Nome do carro: ")
        if nome_carro.isnumeric() or nome_carro.strip() == '' or len(nome_carro) < 2:
            carrinho(nome_carro='<Digite um nome válido')
        else:
            break
    potência_carro = inteiro(">> Potência do carro: ")
    car = Carro(nome_carro, potência_carro)
    carros.append(car)
    print('=' * 43)
    print("Novo carro adicionado!")
    print('=' * 43)
    os.system('pause')


def Informações():
    print('\n')
    os.system("cls") or None
    print('=' * 43)
    print("-=-=-= Opção 2 -=-=-=")
    print('=' * 43)
    nome_carro = input(' Informe o número do carro para ver as informações: ')
    try:
        carros[int(nome_carro)].info()
    except:
        print('=' * 43)
        print("O carro não existe na lista")
        print('=' * 43)
    os.system('pause')


def excluirCarro():
    print('\n')
    os.system("cls") or None
    print('=' * 43)
    print("-=-=-= Opção 3 -=-=-=")
    print('=' * 43)
    nome_carro = input('Informe o número do carro que deseja excluir')
    try:
        del carros[int(nome_carro)]
        print('=' * 43)
        print("Carro excluído!")
        print('=' * 43)
    except:
        print('=' * 43)
        print("O carro não existe na lista")
        print('=' * 43)
    os.system('pause')


def ligarCarro():
    print('\n')
    os.system("cls") or None
    print('=' * 43)
    print("----- Opção 4 -----")
    print('=' * 43)
    nome_carro = input(' Informe o ID do carro que deseja ligar: ')
    try:
        carros[int(nome_carro)].ligar()
        print('=' * 43)
        print("Carro ligado!")
        print('=' * 43)
    except:
        print('=' * 43)
        print("ID Não encontrado na lista!")
        print('=' * 43)
    os.system('pause')


def desligarCarro():
    print('\n')
    os.system("cls") or None
    print('=' * 43)
    print("-=-=-= Opção 5 -=-=-=")
    print('=' * 43)
    nome_carro = input(' Informe o ID do carro que deseja desligar ')
    try:
        carros[int(nome_carro)].desligar()
        print('=' * 43)
        print("Carro desligado!")
        print('=' * 43)
    except:
        print('=' * 43)
        print("ID Não encontrado na lista!")
        print('=' * 43)
    os.system('pause')


def listarCarros():
    print('\n')
    os.system("cls") or None
    print('=' * 43)
    print("-=-=-= Opção 6 -=-=-=")
    print('=' * 43)
    posição = 0
    for um, dois in enumerate(carros):
        print(um+1)
        print(str() + " - " + dois.nome)
        print('-' * 43)
        posição += 1
    os.system('pause')


retorno = menu()
while retorno < '7':

    if retorno == '1':
        Novo_Carro()

    elif retorno == '2':
        Informações()

    elif retorno == '3':
        excluirCarro()

    elif retorno == '4':
        ligarCarro()

    elif retorno == '5':
        desligarCarro()

    elif retorno == '6':
        listarCarros()
    retorno = menu()

os.system("cls") or None
print("------ Processo Finalizado ------")
print("------ Boa semana! ------")

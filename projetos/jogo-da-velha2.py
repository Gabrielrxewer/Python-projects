board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def play_game():
    display_board()

    while True:
        handle_turn("X")
        display_board()
        if check_for_winner("X"):
            print("X venceu!")
            break
        elif check_for_tie():
            print("Empate!")
            break

        handle_turn("O")
        display_board()
        if check_for_winner("O"):
            print("O venceu!")
            break
        elif check_for_tie():
            print("Empate!")
            break

def handle_turn(player):
    print(player + "'s vez.")
    position = input("Escolha uma posição de 1-9: ")
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Escolha uma posição válida de 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("Essa posição já está ocupada. Escolha outra.")

    board[position] = player

def check_for_winner(player):
    if (board[0] == player and board[1] == player and board[2] == player) or \
       (board[3] == player and board[4] == player and board[5] == player) or \
       (board[6] == player and board[7] == player and board[8] == player) or \
       (board[0] == player and board[3] == player and board[6] == player) or \
       (board[1] == player and board[4] == player and board[7] == player) or \
       (board[2] == player and board[5] == player and board[8] == player) or \
       (board[0] == player and board[4] == player and board[8] == player) or \
       (board[2] == player and board[4] == player and board[6] == player):
        return True
    else:
        return False

def check_for_tie():
    if "-" not in board:
        return True
    else:
        return False

play_game()

# Jogo da velha com AI

# Função pra printar o layout
def print_board(board):
    for row in board:
        print(" ".join(row))

# Função que chega o empate
def check_draw(board):
    for row in board:
        for col in row:
            if col == "-":
                return False
    return True

# Função para checar o vencedor
def check_win(board, player):
    # Checa as linhas
    for row in board:
        if row.count(player) == 3:
            return True
    # Checa as colunas
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    # Checa as diagonais
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

# Função para gerar os movimentos da AI
def get_ai_move(board, ai_player):
    # Checa quando a AI pode ganhar com um movimento
    for row in range(3):
        for col in range(3):
            if board[row][col] == "-":
                board[row][col] = ai_player
                if check_win(board, ai_player):
                    return (row, col)
                board[row][col] = "-"
    # Checa quando o adversário pode ganhar com um movimento
    opponent = "X" if ai_player == "O" else "O"
    for row in range(3):
        for col in range(3):
            if board[row][col] == "-":
                board[row][col] = opponent
                if check_win(board, opponent):
                    return (row, col)
                board[row][col] = "-"
    # Tenta jogar no centro
    if board[1][1] == "-":
        return (1, 1)
    # Tenta jogar no canto
    for row in [0, 2]:
        for col in [0, 2]:
            if board[row][col] == "-":
                return (row, col)
    # Joga em outro espaço disponível
    for row in range(3):
        for col in range(3):
            if board[row][col] == "-":
                return (row, col)

# Inicializa o layout
board = [["-" for _ in range(3)] for _ in range(3)]

# Inicializa os players
ai_player = "O"
human_player = "X"

# inicializa quem tá na vez
current_player = human_player

# Looping do jogo
while True:
    if current_player == human_player:
        # faz o layout
        print_board(board)
        print("Enter row and column (e.g. 0 2)):")
        row, col = map(int, input().split())
        if row >= 0 and row < 3 and col >= 0 and col < 3 and board[row][col] == "-":
            board[row][col] = human_player
            if check_win(board, human_player):
                print_board(board)
                print("You win!")
                break
            if check_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            current_player = ai_player
        else:
            print("Invalid move, try again.")
    else:
        print("AI's turn:")
        row, col = get_ai_move(board, ai_player)
        board[row][col] = ai_player
        if check_win(board, ai_player):
            print_board(board)
            print("AI wins!")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        current_player = human_player

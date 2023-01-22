# Tic-Tac-Toe game with AI

# Function to print the game board
def print_board(board):
    for row in board:
        print(" ".join(row))

# Function to check if the game is a draw
def check_draw(board):
    for row in board:
        for col in row:
            if col == "-":
                return False
    return True

# Function to check if a player has won
def check_win(board, player):
    # Check rows
    for row in board:
        if row.count(player) == 3:
            return True
    # Check columns
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

# Function to get the AI's move
def get_ai_move(board, ai_player):
    # Check if AI can win in one move
    for row in range(3):
        for col in range(3):
            if board[row][col] == "-":
                board[row][col] = ai_player
                if check_win(board, ai_player):
                    return (row, col)
                board[row][col] = "-"
    # Check if opponent can win in one move
    opponent = "X" if ai_player == "O" else "O"
    for row in range(3):
        for col in range(3):
            if board[row][col] == "-":
                board[row][col] = opponent
                if check_win(board, opponent):
                    return (row, col)
                board[row][col] = "-"
    # Try to play in the center
    if board[1][1] == "-":
        return (1, 1)
    # Try to play in a corner
    for row in [0, 2]:
        for col in [0, 2]:
            if board[row][col] == "-":
                return (row, col)
    # Play in any remaining space
    for row in range(3):
        for col in range(3):
            if board[row][col] == "-":
                return (row, col)

# Initialize the game board
board = [["-" for _ in range(3)] for _ in range(3)]

# Initialize the players
ai_player = "O"
human_player = "X"

# Initialize the current player
current_player = human_player

# Game loop
while True:
    if current_player == human_player:
        # Print the game board
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

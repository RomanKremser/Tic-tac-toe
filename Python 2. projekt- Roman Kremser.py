# projekt_2.py: druhý projekt do Engeto Online Python Akademie
# author: Ŕoman Kremser
# email: rkremser@seznam.cz
# discord: chimera #+9734



# Tic Tac Toe

# Initialize the board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    print("+---+---+---+")
    print("| {} | {} | {} |".format(board[0], board[1], board[2]))
    print("+---+---+---+")
    print("| {} | {} | {} |".format(board[3], board[4], board[5]))
    print("+---+---+---+")
    print("| {} | {} | {} |".format(board[6], board[7], board[8]))
    print("+---+---+---+")

# Function to check for a win
def check_win(player):
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical
        [0, 4, 8], [2, 4, 6]              # diagonal
    ]
    for pattern in win_patterns:
        if all(board[i] == player for i in pattern):
            return True
    return False

# Function to play the game
def play_game():
    print("Welcome to Tic Tac Toe")
    print("============================================")
    print("GAME RULES:")
    print("Each player can place one mark (or stone)")
    print("per turn on the 3x3 grid. The WINNER is")
    print("who succeeds in placing three of their")
    print("marks in a:")
    print("* horizontal,")
    print("* vertical or")
    print("* diagonal row")
    print("============================================")
    print("Let's start the game")
    print("--------------------------------------------")
    print_board()

    current_player = 'X'
    while True:
        move = int(input("Player {} | Please enter your move number: ".format(current_player)))
        if board[move - 1] != ' ':
            print("Invalid move. Try again.")
            continue
        board[move - 1] = current_player
        print("============================================")
        print_board()
        if check_win(current_player):
            print("============================================")
            print("Congratulations, the player {} WON!".format(current_player))
            print("============================================")
            break
        if ' ' not in board:
            print("============================================")
            print("It's a tie!")
            print("============================================")
            break
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
play_game()

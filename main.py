def print_board(board):
    for row in board:
        print(" | ".join(row))


def get_user_input(player):
    while True:
        try:
            index = int(input(f"Enter the index to place {player} (0-8): "))
            if 0 <= index <= 8:
                return index
            else:
                print("Invalid input. Enter a value between 0 and 8")
        except ValueError:
            print("Invalid input. Enter an integer value between 0 and 8")


def is_game_over(board, player):
    for row in range(3): 
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True
        
    for col in range(3): 
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
        
    if board[0][0] == board[1][1] == board[2][2] == player:
            return True
    
    if board[0][2] == board[1][1] == board[2][0] == player:
            return True
    
    return False
            

if __name__ == "__main__":
    board = [[" " for col in range(3)] for row in range(3)]

    player = "X"
    game_over = False

    while not game_over:
        print_board(board)

        index = get_user_input(player)
        row, col = divmod(index, 3)

        if board[row][col] == " ":
            board[row][col] = player

            game_over = is_game_over(board, player)
            
            if game_over:
                print(f"Player {player} won")
            else:
                if player == "X":
                    player = "O"
                else: 
                    player = "X"
                
        else:
            print("Alreay taken position")

    print_board(board)
        

        
        
        

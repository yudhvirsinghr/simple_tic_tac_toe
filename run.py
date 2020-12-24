import random

# functions
def make_board(board):
    """
    makes 3x3 tic tac toe board on terminal
    Input:
        board(list(int)): list of 9 integers
    Returns:
        prints 3x3 box"""
    print(100 * '\n')
    print('Welcome to terminal TIC TAC TOE')
    print('================================================================================\n')
    print(f'  {board[6]}  |  {board[7]}  |  {board[8]} ')
    print(f'----------------')
    print(f'  {board[3]}  |  {board[4]}  |  {board[5]} ')
    print(f'----------------')
    print(f'  {board[0]}  |  {board[1]}  |  {board[2]} ')
    print('================================================================================\n')

def make_markers():
    """
    Returns:
        (Player1 marker, Player2 marker)"""
    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input("Choose your marker 'X' or 'O':\t").upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_marker(board, marker, pos):
    """
    place the marker 'X' or 'O' on the board
    Input:
        board(list(int)): list of 9 integers
        marker(str): 'X' or 'O'
        pos(int): position to place marker
    Returns:
        board(list(int)): updated board"""
    board[pos - 1] = marker
    return board

def check_result(board, marker):
    """
    Checks if player won
    Input:
        board(list(int)): list of 9 integers
        marker(str): 'X' or 'O'
    Returns:
        Bool: if player one"""
    return (board[0] == board[4] == board[8] == marker) or \
            (board[0] == board[1] == board[2] == marker) or \
            (board[3] == board[4] == board[5] == marker) or \
            (board[6] == board[7] == board[8] == marker) or \
            (board[2] == board[4] == board[6] == marker) or \
            (board[0] == board[3] == board[6] == marker) or \
            (board[1] == board[4] == board[7] == marker) or \
            (board[2] == board[5] == board[8] == marker)

def pick_player():
    """
    picks player to go first
    Returns:
        Str: Player 1 or Player 2"""
    
    number = random.randint(0, 1)

    if number == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def valid_move(board, position):
    """
    checks the position on the board if its empty
    Input:
        board(list(int)): list of 9 integers
        position(int): position to check if its available
    Returns:
        Bool: if the move is possible"""
    return board[position] == ' '

def full_board(board):
    """
    Check if the board is full
    Input:
        board(list(int)): list of 9 integers
    Returns:
        Bool: if the board is full"""
    return ' ' not in board

def input_position(board):
    """
    pick a postion on the board to input your marker
    Input:
        board(list(int)): list of 9 integers"""
    pos = 0
    while pos not in list(range(1, 10)) or not valid_move(board, pos):
        pos = int(input(f'Enter the index to put your marker[1-9]:\t'))
    return pos 

def play_again():
    """
    asks user if they want to play again
    Returns:
        Bool: if the player wants to play again"""
    return input("Do you want to play again 'Yes' | 'No'\t").lower().startswith('y')
    

def play_game():
    """TIC TAC TOE GAME"""

    # keep on playing until player don't want to play
    while True:
        # make empty TIC TAC TOE BOARD
        board = list(map(lambda x: ' ', range(9)))
        # assign markers to players
        player1, player2 = make_markers()
        # decide randomly who goes first
        turn = pick_player()
        print(f'{turn} will go first')

        # ask user if they want to play the game
        play_game = input("Play game 'Yes' | 'No'\t")

        if play_game.lower().startswith('y'):
            game = True
        else:
            game = False

        # keep on playing if user wants to play
        while game:
            if turn == 'Player 1':

                # print the board on terminal
                make_board(board)
                # player 1 picks the position to place their marker
                position = input_position(board)
                # place the marker on the board
                board = place_marker(board, player1, position)

                # check if player 1 won
                if check_result(board, player1):
                    make_board(board)
                    print('Player 1 won')
                    game = False
                # check if board is full
                else:
                    if full_board(board):
                        make_board(board)
                        print("It's a Draw !")
                        break
                    # if none of above, its player 2 turn
                    else:
                        turn = 'Player 2'

            else:

                # print the board on terminal
                make_board(board)
                # player 2 picks the positin to place their marker
                position = input_position(board)
                # place the marker on the board
                board = place_marker(board, player2, position)

                # check if player 2 won
                if check_result(board, player2):
                    make_board(board)
                    print('Player 2 won')
                    game = False
                # check if board is full
                else:
                    if full_board(board):
                        make_board(board)
                        print("It's a Draw !")
                        break
                    # if none of the above, its player 1 turn
                    else:
                        turn = 'Player 1'

        # if user wants to stop playing
        if not play_again():
            break

# TIC TAC TOE
play_game()

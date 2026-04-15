from random import randrange



board = [[1,2,3],[4,'x',6],[7,8,9]]

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print(board)
    


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    user_move = int(input("Enter a number between 1 and 9: "))
    if user_move > 10 or user_move < 0:
        print("wrong Value")

    if user_move == 1:
        board [0][0] = "o"
        print(board)
    if user_move == 2:
        board [0][1] = "o"
        print(board)
    if user_move == 3:
        board [0][2] = "o"
        print(board)
    if user_move == 4:
        board [1][0] = "o"
        print(board)
    if user_move == 6:
        board [1][2] = "o"
        print(board)
    if user_move == 7:
        board [3][0] = "o"
        print(board)
    if user_move == 8:
        board [3][1] = "o"
        print(board)
    if user_move == 9:
        board [3][2] = "o"
        print(board)


# def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.


# def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game

def draw_move(board):
    # The function draws the computer's move and updates the board.
    c_value = randrange(8)
    if c_value == 1:
        board [0][0] = "x"
        print(board)
    if c_value == 2:
        board [0][1] = "x"
        print(board)
    if c_value == 3:
        board [0][2] = "x"
        print(board)
    if c_value == 4:
        board [1][0] = "x"
        print(board)
    if c_value == 6:
        board [1][2] = "x"
        print(board)
    if c_value == 7:
        board [3][0] = "x"
        print(board)
    if c_value == 8:
        board [3][1] = "x"
        print(board)
    if c_value == 9:
        board [3][2] = "x"
        print(board)



display_board(board)
enter_move(board)
draw_move(board)
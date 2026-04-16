from random import randrange



board = [[1,2,3],[4,'x',6],[7,8,9]]
loop_on = True

def comp_mv(board):
    comp_move = 2

    if comp_move == 2:
        board[0][1] = "X"
        print(board)



def usr_mv(board):
    user_move = int(input("Enter a number between 1 and 9: "))

    if user_move == 1:
        board[0][0] = "O"
        print(board)


def winner(n):
    if n == 2:
        return 0

def check_space():
    pass



while loop_on:
    usr_mv(board)
    comp_mv(board)
    winner(1)
    
    if winner(1) == 0:
        break


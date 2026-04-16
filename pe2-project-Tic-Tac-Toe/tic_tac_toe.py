from random import randrange



board = [
    [1,2,3],
    [4,'X',6],
    [7,8,9]
    ]
loop_on = True

def comp_mv(board):
    comp_move = int(input("Enter computer move: "))

    if comp_move == 2:
        board[0][1] = "X"
        print("\n")

        for row in board:
            for item in row:
                print("|",item, end=" | ")
            print()
    
    if comp_move == 8:
        board[2][1] = "X"
        print("\n")

        for row in board:
            for item in row:
                print("|",item, end=" | ")
            print()
    




def usr_mv(board):
    user_move = int(input("Enter a number between 1 and 9: "))

    
    if user_move == 1:
        board[0][0] = "O"
        for row in board:
            for item in row:
                print("|",item, end=" | ")
            print()

    if user_move == 4:
        board[1][0] = "O"
        for row in board:
            for item in row:
                print("|",item, end=" | ")
            print()


def winner():
    if board[0][1] == board[1][1] == board[2][1]:
        print("The computer won")
        return 0
    

def check_space():
    pass



while loop_on:
    usr_mv(board)
    comp_mv(board)
    winner()

    x = winner()
    print(x)
    
    if winner() == 0:
        break


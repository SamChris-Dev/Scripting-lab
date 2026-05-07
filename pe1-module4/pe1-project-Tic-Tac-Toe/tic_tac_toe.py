from random import randrange



board = [
    [1,2,3],
    [4,'X',6],
    [7,8,9]
    ]

loop_on = True

used_spot_comp = []
used_spot_user = []

def comp_mv(board):
    global used_spot_comp
    comp_move = int(input("Enter computer move: "))
    used_spot_comp.append(comp_move)

    if comp_move == 2:
        board[0][1] = "X"

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
    global used_spot_user
    user_move = int(input("Enter a number between 1 and 9: "))
    used_spot_user.append(user_move)

    
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
    global loop_on
    if board[0][1] == board[1][1] == board[2][1]:
        print("The computer won")
        loop_on = False
    

def check_space():
    global used_spot_comp
    global used_spot_user

    used_spot = used_spot_user.append(used_spot_comp)

    print("used space is ", used_spot)







while loop_on:
    usr_mv(board)
    print()
    comp_mv(board)
    print()
    winner()
    check_space()


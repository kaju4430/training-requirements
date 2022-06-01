def ttt():
    board = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
    player = "X"
    move_count = 0
    row = None
    column = None
    result = False

    while(True):

        print("Player " + player + ", make your move : ")

        try:
            row = int(input("Enter Row : "))
            column = int(input("Enter Column : "))
        except:
            print("Enter a number between 0 & 2")
            continue

        if row <= 2 and column <= 2:
            if board[row][column] == "X" or board[row][column] == "O":
                print("Position taken. Try again")
                continue            
            board[row][column] = player
            move_count += 1
            print(board)

        else:
            print("Invalid position. Try again.")
            continue

        if move_count >= 5:
            result = check_winner(board, player)
            if result:
                print("Player", player, "has won!")
                quit()

        if move_count == 9:
            print("Draw!")
            quit()

        if player == "X":
            player = "O"
        else:
            player = "X"

def check_winner(board, player):
    c1 = []
    c2 = []
    c3 = []
    d1 = []
    d2 = []

    for i, j, k in board:
        if i == j == k == player:
            print("Player " + player + " wins!")
            quit()

        c1.append(i)
        c2.append(j)
        c3.append(k)

        if len(d1) == 0:
            d1.append(i)
        elif len(d1) == 1:
            d1.append(j)
        else:
            d1.append(k)

        if len(d2) == 0:
            d2.append(k)
        elif len(d2) == 1:
            d2.append(j)
        else:
            d2.append(i)

    if c1[0] == c1[1] == c1[2] == player:
        return 1
    elif c2[0] == c2[1] == c2[2] == player:
        return 1
    elif c3[0] == c3[1] == c3[2] == player:
        return 1
    elif d1[0] == d1[1] == d1[2] == player:
        return 1
    elif d2[0] == d2[1] == d2[2] == player:
        return 1
        

if __name__ == "__main__":
    ttt()
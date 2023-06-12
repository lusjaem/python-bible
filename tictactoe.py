#creating empty board as a list

board = [" " for i in range(9)]

#print board using the indexes from the list

def print_board():
    row1 = "|{}|{}|{}|".format(board[0],board[1],board[2])
    row2 = "|{}|{}|{}|".format(board[3],board[4],board[5])
    row3 = "|{}|{}|{}|".format(board[6], board[7], board[8])
    
    print()
    print(row1)
    print(row2)
    print(row3)
    print()
    
# Player move function

def player_move(symbol):

    if symbol == "X":
        number = 1
    elif symbol == "O":
        number = 2
        
    print("Your turn Player {}.".format(number))
   
    choice = int(input("Enter your move (1-9) on num keyboard: "))
    if board[choice - 1] == " ":
        board[choice - 1] = symbol
    else:
        print()
        print("That space is taken.") 
        
# checking victory

def is_victory(symbol):
    if (board[0]==symbol and board[1]==symbol and board[2]==symbol) or\
    (board[3]==symbol and board[4]==symbol and board[5]==symbol) or\
    (board[6]==symbol and board[7]==symbol and board[8]==symbol) or\
    (board[0]==symbol and board[3]==symbol and board[8]==symbol) or\
    (board[1]==symbol and board[4]==symbol and board[7]==symbol) or\
    (board[2]==symbol and board[5]==symbol and board[8]==symbol) or\
    (board[0]==symbol and board[4]==symbol and board[8]==symbol) or\
    (board[2]==symbol and board[4]==symbol and board[6]==symbol):
        return True
    else:
        return False

# checking full space

def is_full():
    if " " not in board:
        return True
    else:
        return False

#game loop

while True:
    print_board()
    player_move("X")
    print_board()
    if is_victory("X"):
        print("X wins! Congratulations!")
        break
    elif is_full():
        print("The board is full!")
        break

    player_move("O")
    if is_victory("O"):
        print_board()
        print("O wins! Congratulations!")
        break
    elif is_full():
        print("The board is full!")
        break
    

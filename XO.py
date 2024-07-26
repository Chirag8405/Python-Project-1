rom IPython.display import clear_output
board = [" "]*10

def display(board):
    clear_output()
    print(board[0]+" | "+board[1]+" | "+board[2])
    print("- - - - - ")
    print(board[3]+" | "+board[4]+" | "+board[5])
    print("- - - - - ")
    print(board[6]+" | "+board[7]+" | "+board[8])

def XO():
    choice_1 = " "
    choice_2 = " "
    while True:
        choice_1= input("Player 1, Do you Want X or O?: ").upper()
        if choice_1 == "X":
            choice_2 = "O"
            print("Player 1 has chosen X!")
            print("Player 2 has chosen O!")
            return choice_1, choice_2
        elif choice_1 == "O":
            choice_2 = "X"
            print("Player 1 has chosen O!")
            print("Player 2 has chosen X!")
            return choice_1, choice_2
        else:
            print("Enter valid Option! Please Choose X or O!")
       
def update(board, choice, index, counter):
    if space_check(board, index - 1):
        board[index - 1] = choice[counter % 2]
        display(board)
        return counter + 1
    else:
        print("This space is already occupied!")
        return counter
       
def space_check(board, index):
    return board[index] == " "

def full_board_check(board):
    return " " not in board[0:9]

def win(board, choice):    
    if((board[0]==board[1]==board[2]==choice[0]) or #horizontal
        (board[3]==board[4]==board[5]==choice[0]) or #horizontal
        (board[6]==board[7]==board[8]==choice[0]) or #horizontal
        (board[0]==board[3]==board[6]==choice[0]) or #vertical
        (board[1]==board[4]==board[7]==choice[0]) or #vertical
        (board[2]==board[5]==board[8]==choice[0]) or #vertical
        (board[0]==board[4]==board[8]==choice[0]) or #diagonal
        (board[2]==board[4]==board[6]==choice[0])): #diagonal
        print("Player 1 has won the Game!")
        return True
    elif ((board[0]==board[1]==board[2]==choice[1]) or #horizontal
        (board[3]==board[4]==board[5]==choice[1]) or #horizontal
        (board[6]==board[7]==board[8]==choice[1]) or #horizontal
        (board[0]==board[3]==board[6]==choice[1]) or #vertical
        (board[1]==board[4]==board[7]==choice[1]) or #vertical
        (board[2]==board[5]==board[8]==choice[1]) or #vertical
        (board[0]==board[4]==board[8]==choice[1]) or #diagonal
        (board[2]==board[4]==board[6]==choice[1])): #diagonal
        print("Player 2 has won the Game!")
        return True
    elif full_board_check(board):
        print("It's a Tie!")
        return True
    return False
        
def nxt_index(board,counter):
    while True:
        player = "Player 1" if counter % 2 == 0 else "Player 2"
        while True:
            try:
                index = int(input("{}, Enter Position (1-9): ".format(player)))  
            except:
                print("Please Enter an Integer!")
                continue
            else:
                if index in range(1, 10) and space_check(board, index-1):
                    return index
                elif index not in range(1,10):
                    print("Enter Valid Position!")
                else:
                    print("Position already taken! Please try again!")
                    break
              
def replay():
    answer = input("Play Again?: Enter Yes or No! ").capitalize()
    return answer  == "Yes"

print("Welcome to Tic Tac Toe!")
while True:
    board = [" "]*10
    choice_1, choice_2 = XO()
    display(board)
    counter = 0
    while True:
        index = nxt_index(board, counter)
        counter = update(board, (choice_1, choice_2), index, counter)
        if full_board_check(board):
            print("It's a Tie!")
            break
        if win(board, (choice_1, choice_2)):
            break
    if not replay():
        break

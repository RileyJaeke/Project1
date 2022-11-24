import random
playerWins = 0
botWins = 0
player = 'O'
computer = 'X'
board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}


test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def restore_list():
    global new_list
    new_list = test_list


def list_choice(new_list):
    random_num = random.choice(new_list)
    new_list.remove(random_num)
    return int(random_num)

def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print("-+-+-")
    print(board[4] + '|' + board[5] + '|' + board[6])
    print("-+-+-")
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('\n')


playing = True
complete = False
turn = 0
prev_turn = -1

def check_turn(turn):
    if turn % 2 == 0: return 'O'
    else: return 'X'


def check_win(board):
    #Handle horizontal cases
    if (board[1] == board[2] == board[3] != ' ') \
        or (board[4] == board[5] == board[6] != ' ') \
        or (board[7] == board[8] == board[9] != ' '):
        return True
    #Handle vertical cases
    elif (board[1] == board[4] == board[7] != ' ') \
        or (board[2] == board[5] == board[8] != ' ') \
        or (board[3] == board[6] == board[9] != ' '):
        return True
    #Diagonal cases
    elif (board[1] == board[5] == board[9] != ' ') \
        or (board[3] == board[5] == board[7] != ' '):
        return True

    else: return False

def check_draw():
    if board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' \
        and board[6] != ' ' and board[7] != ' ' and board[8] != ' ' and board[9] != ' ':
        return True
    return False

def emptySpace(position):
    if board[position] == ' ':
        return True
    return False
def insertLetter(letter, position):
    global botWins
    global playerWins
    if emptySpace(position):
        board[position] = letter
        printBoard(board)
        if check_draw():
            print("Draw!")
        if check_win(board):
            print('')
            if letter == computer:
                print("Bot wins!")
                botWins =+ 1
                return
            elif letter == player:
                print('Player wins!')
                playerWins += 1
                return
        return
    else:
        print("Invalid position")
        position = int(input("Enter a new position: "))
        insertLetter(letter, position)
        return
def playerMove():
    position = int(input("Enter a position for 'O': "))
    if position in new_list:
        new_list.remove(position)
    insertLetter(player, position)
    return
def computerMove():
    print('Computer Move\n')
    position = list_choice(new_list)
    insertLetter(computer, position)
    return

def main():
    global board
    exit = 'y'
    while playerWins < 2 or botWins < 2 and (exit != 'n' and exit == 'y'):
        playerMove()
        if check_win(board) or check_draw():
            restore_list()
            board = {1: ' ', 2: ' ', 3: ' ',
                     4: ' ', 5: ' ', 6: ' ',
                     7: ' ', 8: ' ', 9: ' '}
            exit = input('Enter "y" to continue or "n" to quit: ')
            exit.lower().strip()
            while exit != 'y' and exit != 'n':
                exit = input('Make sure you enter a "y" or "n": ')
                exit.lower().strip()
        computerMove()
        if check_win(board) or check_draw():
            restore_list()
            board = {1: ' ', 2: ' ', 3: ' ',
                     4: ' ', 5: ' ', 6: ' ',
                     7: ' ', 8: ' ', 9: ' '}
            exit = input('Enter "y" to continue or "n" to quit: ')
            exit.lower().strip()
            while exit != 'y' and exit != 'n':
                exit = input('Make sure you enter a "y" or "n": ')
                exit.lower().strip()


if __name__ == '__main__':
    printBoard(board)
    main()

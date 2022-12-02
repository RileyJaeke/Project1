import random
playerWins = 0
botWins = 0
player = 'O'
computer = 'X'
board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}


new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


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


turn = 0

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
                botWins += 1
                printBoard(board)
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
    global new_list
    global playerWins
    global botWins
    playerWins = 0
    botWins = 0
    board = {1: ' ', 2: ' ', 3: ' ',
             4: ' ', 5: ' ', 6: ' ',
             7: ' ', 8: ' ', 9: ' '}
    cease = 'y'
    printBoard(board)
    new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while playerWins < 2 or botWins < 2 and (cease != 'n' and cease == 'y'):
        print(new_list)
        playerMove()
        if playerWins == 2:
            break
        if botWins == 2:
            break
        if check_win(board) or check_draw():
            board = {1: ' ', 2: ' ', 3: ' ',
                     4: ' ', 5: ' ', 6: ' ',
                     7: ' ', 8: ' ', 9: ' '}
            new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            cease = input('Enter "y" to continue or "n" to quit: ')
            cease.lower().strip()
            while cease != 'y' and cease != 'n':
                cease = input('Make sure you enter a "y" or "n": ')
                cease.lower().strip()
            if cease == 'n':
                break
        computerMove()
        if playerWins == 2:
            break
        if botWins == 2:
            break
        if check_win(board) or check_draw():
            board = {1: ' ', 2: ' ', 3: ' ',
                     4: ' ', 5: ' ', 6: ' ',
                     7: ' ', 8: ' ', 9: ' '}
            new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            cease = input('Enter "y" to continue or "n" to quit: ')
            cease.lower().strip()
            while cease != 'y' and cease != 'n':
                cease = input('Make sure you enter a "y" or "n": ')
                cease.lower().strip()
            if cease == 'n':
                break
            printBoard(board)
    if playerWins == 2:
        playAgain = input('\nThe Player has won the series\nWant to play again? (y/n): ')
        playAgain.lower().strip()
        while playAgain != 'y' and playAgain != 'n':
            playAgain = input('Enter y or n: ')
            playAgain.lower().strip()
        if playAgain == 'y':
            main()
    if botWins == 2:
        playAgain = input('\nThe Computer has won the series\nWant to play again? (y/n): ')
        playAgain.lower().strip()
        while playAgain != 'y' and playAgain != 'n':
            playAgain = input('Enter y or n: ')
            playAgain.lower().strip()
        if playAgain == 'y':
            main()


if __name__ == '__main__':
    main()

from board import Board

def validate_game_conditions(row_count: int, col_count: int, x: int) -> bool:
    '''
    Validates whether the user-entered values of row_count, col_count and x are valid or not
    The conditions are sort of arbitrary.
    '''
    if 1 <= row_count <= 10 and 1 <= col_count <= 10 and 1 <= x <= min(row_count, col_count):
        return True
    return False

def main():
    print('Welcome to Connect x!\n')
    print('This is a 2 player game with each player taking turns, much like Connect 4. See rules: https://en.wikipedia.org/wiki/Connect_Four#Gameplay')
    print('Except the user has the option to choose the board dimensions and x (lower case)')
    print('x is the number of discs of the same type that need to be together for a player to win')
    print('In this terminal based game, Player 1 uses the disc X (upper case) and Player 2 uses the disc O')
    print('Please enter board dimensions and x. Classic values are: Rows = 6, Columns = 7 and x = 4\n')

    row_count, col_count, x = 6, 7, 4
    while True:
        try:
            row_count = int(input('Enter No. of Rows (From 1 to 10, inclusive): '))
            col_count = int(input('Enter No. of Columns (From 1 to 10, inclusive): '))
            x = int(input('Enter x (At least 1 and at most equal to the smaller dimension of the board): '))
            if validate_game_conditions(row_count, col_count, x):
                break
            else:
                print('Please enter valid values')
        except ValueError:
            print('Please enter valid values')
    b = Board(row_count, col_count, x)
    b.printBoard()
    while True:
        print(f"Player {b.currPlayer + 1}'s turn. Choose a column to put your disc ({b.discs[b.currPlayer]}): ", end='')
        try:
            c = int(input()) - 1
        except ValueError:
            print('Please enter a valid integer')
            continue
        is_disc_added = b.add_disc(c)
        if is_disc_added:
            b.printBoard()

        if b.game_over:
            print('Game Over. Result is: ' + b.result)
            yn = ''
            while True:
                yn = input('Start a new game? (y/n): ')
                if yn.lower() == 'y' or yn.lower() == 'n':
                    break
                print('Please enter a valid value. ')
            if yn.lower() == 'n':
                print('Exiting...')
                break
            b.clearBoard()
            b.printBoard()



if __name__ == '__main__':
    main()
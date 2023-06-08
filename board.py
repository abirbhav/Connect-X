class Board:
    discs = ('X', 'O')
    def __init__(self, row_count, col_count, x) -> None:
        self.row_count = row_count
        self.col_count = col_count
        self.x = x
        self.clearBoard()
    
    def clearBoard(self):
        '''Initializes or clears board and all the attributes'''
        self.grid = [[' '] * self.col_count for _ in range(self.row_count)]
        self.disc_index_map = {}
        for col in range(self.col_count):
            self.disc_index_map[col] = self.row_count-1
        self.currPlayer = 0
        self.game_over = False
        self.result = ''
        self.discs_added = 0

    def printBoard(self):
        '''Prints the board on the terminal'''
        print('\nBoard: \n')
        for i in range(self.col_count):
            print('   ' + str(i + 1), end=' ')
        print()
        for i in range(self.row_count):
            for j in range(self.col_count):
                print('_____',end='')
            print()
            for j in range(self.col_count):
                print('| ' + self.grid[i][j], end='  ')
            print('|')
        for j in range(self.col_count):
            print('_____',end='')
        print()
        for i in range(3):
            print('|', end='')
            for j in range(5*self.col_count - 1):
                print(' ', end='')
            print('|')
        print()

    def add_disc(self, col: int) -> bool:
        '''
        Adds a disc to the specified column.
        Returns a boolean specifying whether disc was successfully added or not
        '''
        if self.game_over:
            print("Can't enter disc. Game over. Result is: " + self.result)
            return False
        if not self.i_and_j_in_bounds(0, col):
            print("Please enter a valid column")
            return False
        row = self.disc_index_map[col]
        if row == -1:
            print('This column is full. Please choose a different column')
            return False
        self.grid[row][col] = self.discs[self.currPlayer]
        self.disc_index_map[col] = self.disc_index_map[col] - 1 if row > 0 else -1
        self.discs_added+=1
        self.checkForResult(row, col)
        self.currPlayer = abs(self.currPlayer  -1)
        return True
    
    def i_and_j_in_bounds(self, i: int, j: int) -> bool:
        '''Checks to see if index (i, j) is inside bounds of grid'''
        if i >= 0 and i < self.row_count and j >= 0 and j < self.col_count:
            return True
        return False

    
    def checkForResult(self, row: int, col: int) -> None:
        '''
        Checks if there has been a result or not.
        ie checks if there have been x (4 in the classic case) discs in a line or if the board is full.
        Populates the attributes result and game_over
        '''
        def generic_check(i_init: int, j_init: int, i_inc: int, j_inc: int) -> bool:
            '''
            Helper function 
            '''
            curr = self.grid[row][col]
            i, j = i_init, j_init
            in_a_row = 0
            loop = 0
            while loop < 2 * self.x + 1:
                if not self.i_and_j_in_bounds(i, j) or self.grid[i][j] != curr:
                    in_a_row = 0
                else:
                    in_a_row+=1
                    if in_a_row >= self.x:
                        self.result = 'Player ' + str(self.currPlayer + 1) + ' won. They got ' + str(self.x) + ' discs in a line!'
                        self.game_over = True
                        return True
                i+=i_inc
                j+=j_inc
                loop+=1
            return False
        
        # Check if there are x discs together
        # This check is done before checking for a full board in case the last move
        # of the game is also a winning move
        # Check up-down, left-right, diagonals
        is_x_together = (generic_check(row - self.x + 1, col, 1, 0)
                or generic_check(row, col - self.x + 1, 0, 1)
                or generic_check(row - self.x + 1, col - self.x + 1, 1, 1)
                or generic_check(row - self.x + 1, col + self.x - 1, 1, -1))
        
        if not is_x_together and self.discs_added == self.row_count * self.col_count:
            self.result = 'Game tied. Board Full.'
            self.game_over = True
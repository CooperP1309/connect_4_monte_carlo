
class Grid:
    game_grid = [[0 for _ in range(7)] for _ in range(6)]

    def __init__(self):
        print("Game grid initialized...", end='\n\n')
        self.print_grid()
    
    def print_grid(self):
        for _ in range(29):         # printing of horizontal border
            print("-",end='')
        print()
        
        for i in range(5,-1,-1):
            for y in range(7):
                print("|", end=' ') # printing of vertical borders
                print(Grid.get_player_token(self.game_grid[i][y]),end=' ')
            print("|")
        
            for _ in range(29):     # printing of horizontal borders
                print("-",end='')
            print()
        
    @staticmethod
    def get_player_token(number):   # given the value of a cell in the grid,
        if number == 0:             # return the corresponding player's character symbol
            return ' '
        elif number == 1:
            return 'X'
        elif number == 2:   
            return 'O'
        


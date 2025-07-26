import random

class Gamerules:

    @staticmethod
    def process_move(grid, move_str, player):

        if Gamerules.validate_move(grid, move_str) == False:
            return False                # validate move before attempting to apply it
        
        if Gamerules.apply_move(grid, move_str, player) == False:
            return False                # update move to board

        return True
    
    @staticmethod
    def validate_move(grid, move_str):  # move verification
        try:                            # 1. determine if a valid number
            move = int(move_str)
        except ValueError:
            print("Input is not a number")
            return False
    
        if move > 7 or move < 1:        # 2. verify input is within range
            print("Input is not a real column")
            return False
            
        move -= 1
              
        if grid[5][move] == 0:          # 3. verify column is not full     
            return True
         
        print("Selected column is full")        

        return False
    
    @staticmethod
    def apply_move(grid, move_str, player):
        move = int(move_str)            # convert string into int
        move -=1
        
        for i in range(6):              # iterate from the bottm of the col up
            if grid[i][move] == 0:
                grid[i][move] = player  # set the lowest 0 as a player token
                return True
        
        print("failed to apply move")
        return False
    
    @staticmethod
    def apply_rnd_move(grid, player):
        move = random.randint(0,6)
        
        for i in range(6):              # iterate from the bottm of the col up
            if grid[i][move] == 0:
                grid[i][move] = player  # set the lowest 0 as a player token
                return True

        return False
    
    @staticmethod
    def check_win(grid):
        
        for i in range(6):                      # iterate through whole grid        
            for y in range(7):
                if grid[i][y] != 0:             # for each player move on the grid...  
    
                   if(y < 4):                   # (don't bother if past 4th col)  
                        # horizontal check
                        for z in range(4):
                            if grid[i][y+z] != grid[i][y]:
                                break           # if count doesn't make it to 4, no win, carry on
                            if z == 3:
                                return grid[i][y]
                            
                        # diag up check
                        if (i < 3):             # (don't bother if above 3rd row)
                            for z in range(4):
                                if grid[i+z][y+z] != grid[i][y]:
                                    break
                                if z == 3:
                                    return grid[i][y]
                                
                        # diag down check
                        if (i > 2):             # (don't bother if below 4th row)
                            for z in range(4):
                                if grid[i-z][y+z] != grid[i][y]:
                                    break
                                if z == 3:
                                    return grid[i][y]
                   
                   # vertical check
                   #    - only need to check upwards from lowest 3 rows. This is
                   #      the order that the grid is traversed in
                   if(i < 3):                   # (don't bother if above 3rd row) 
                    for z in range(4):
                        if grid[i+z][y] != grid[i][y]:
                            break
                        if z == 3:
                            return grid[i][y]
                        
        return 0                                # case for no winner
    
    @staticmethod
    def check_grid_full(grid):
        for i in range(6):
            for y in range(7):
                if grid[i][y] == 0:             # if there exists an empty cell
                    return False                # False: grid is not full
                
        return True                             # else, no empty cells = True. It is full
        
                   
                                
                            
                        
                            
                    
   
    

        

   
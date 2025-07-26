import gamerules
import grid
import monte

'''
connect_four_monte_carlo.py     By Cooper Peek

Can you beat Monte in connect four?

Classes explained:
    - Grid: Contains the grid/game board data structure and methods for representing the grid
    - Gamerules: Contains methods such as check_win, apply_move, verify_move and so on
    - Monte: This class contains the basis of the Monte algorithm itself

'''

game = grid.Grid()           # create a new game grid instance
rule = gamerules.Gamerules   # game rule handler
monte = monte.Monte
winner = 0                   # tracks the game status
player = 1                   # traks the player turn

while (winner == 0):
    
    if player == 2:
         print("Monte is thinking...") 
         move = monte.generate_move(game.game_grid)
         move = str(move)
         rule.process_move(game.game_grid, move, player)
    else:
        print("Player ", game.get_player_token(player), ", make your move", end="\n\n")
        move_str = input()       # prompting of and player input

        if rule.process_move(game.game_grid, move_str, player) == False:
            continue             # if invalid input (returned false), 'continue' prevents
                                 # player turn from switching, allowing to try again.             
    game.print_grid()
    
    player = 3 - player          # switch which player's turn it is

    winner = rule.check_win(game.game_grid)     # checking for win after each turn
    
print("player ", game.get_player_token(winner), " wins the game!")




    #game.game_grid[3][5]=2 # game_grid[row][col]
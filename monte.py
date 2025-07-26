import copy
from queue import PriorityQueue
import gamerules
import node

class Monte: 

    # IMPORTANT NOTE FOR FUTURE ME!!!!!
    # MODIFY THIS CLASS SUCH THAT THE "rule = gamerules.Gamerules" object
    # IS DEFINED ONCE AND FOR ALL METHODS. CURRENTLY IS REDEFINED IN NEAR EVERY METHOD

    # ALSO WHEN SIMULATION DATA IS STORED INTO NODE, FIGURE OUT HOW TO MAKE THAT ONE LINE

    @staticmethod
    def generate_move(grid):
        rule = gamerules.Gamerules
        moves = list()                                  # moves list will hold all possible moves with score data

        for i in range(7):          
            if grid[5][i] == 0:                         # iterate through all POSSIBLE moves
                temp_grid = copy.deepcopy(grid)  
                rule.apply_move(temp_grid, i+1, 2)      # deep copy board and apply current possible move

                if rule.check_win(temp_grid) == 2:      # check for immediate win before wasting resources
                    return i+1
                else:
                    score = Monte.simulate(temp_grid)   # else, begin simulations
                    move = node.Node(utility = score, col = i+1)   # store simulation data into a node
                    #move.utility = score
                    #move.col = i+1
                    moves.insert(0, move)               # process new node against other nodes
                    
        moves.sort(reverse=True)                        # finally, sort the list in descending order
                                                        
        if moves:                                       # if moves is not empty...
            return moves[0].col                         # return the move with the best utility score   

    @staticmethod
    def simulate(grid):
        iterations = 300
        score = 0.0
        player = 1                                          # arrange for opposing player to make next move        

        for i in range(iterations):                         # for each simulation
            temp_grid = copy.deepcopy(grid)                 # make a new board
            score += Monte.expand_game(temp_grid, player)   # begin recursive expansion
        
        return (score / iterations)                         # return the average score of all simulations

            
    @staticmethod
    def expand_game(grid, player):
        rule = gamerules.Gamerules  
        winner = rule.check_win(grid)                       # get the current game status

        if winner == 2:                                     # case for Monte winning
            return 1.0
        
        if winner == 1:                                     # case for opposing player winning
            return -1.0
        
        if winner == 0 and rule.check_grid_full(grid):      # if there's no winner and the board is full...
            return 0.0                                      # case for draw
     
        move_completed = False
        while not move_completed:                           # apply a valid random move
            move_completed = rule.apply_rnd_move(grid, player)
        
        player = 3 - player                                 # switch player turn
    
        return Monte.expand_game(grid, player)
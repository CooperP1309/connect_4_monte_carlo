from dataclasses import dataclass

@dataclass(order=True)    # '@dataclasses' tag enables class preferences for storing data duuuuuh
class Node:                 # !SUPER IMPORTANT c++ TO python TIP!
    utility: float          # in this case the 'order=True' attribute means that the FIRST variable listed
    col: int                # in the class (The utility in this case) will be compared amongst the first
                            # variables other nodes. 

# That is, by having utility as the first variable, putting many of these Node objects into a sortedlist
# will result in them being compared. This emulates the "Cell struct" from previous assignments:
#
#   cell(int xx, int yy, double uu) :x(xx), y(yy), utility(uu) {} 
                                                                  
#	bool operator<(const cell& c) const {                         
#		return utility < c.utility;
#   }
#
# where the operator function was responsible for sorting cells based on utility in a priority queue

# EXTRA NOTE!! The initializer list constructor is not necessary in python due to the '@dataclasses' tag.
# This automatically creates a '__init__()' constructor that handles this
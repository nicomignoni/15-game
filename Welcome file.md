# 15-game
A simple minimax-tree based solver for the 15-game. It supports the 3x3 and the 4x4 version of the game.  
## Description
The main algorithm uses a minimax search tree to find the winninp position. In the 3x3 version, due to the small size of the state space, the solution can be reached using brute force in a reasonable time. In the 4x4 euristics are required. I used the straighfoward Manhattan Distance function to measure the total distance of each tile from its correct position. The leaf nodes with the minimum total distance are chosen to be further explored. Given that the majority of the permutation of $[1,2,...,n]$ doesn't result in a solvable initial state for the general $n^2-1$-game, the winning position gets shuffled a given number of time in order to find a solvable initial state. The more the shuffling, the harder it is to find the solution. The variable `shuffle = 80` is the default. You can also play by yourself using the keyboard.

## Commands
Run the file `gui.py` to start the game. Here's a list of the commands:

 - **Spacebar**: start the AI solver,
 - **W,A,S,D**: manually move the tiles on the table,
 - **3**: initiate the 3x3 table
 - **4**: initiate the 4x4 table
> **Note**: You can  switch from 3x3 to 4x4 or viceversa at any time, though not while the program is solving the puzzle automatically, for the latter will most likely crash.


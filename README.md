---


---

<h1 id="game">15-game</h1>
<p>A simple minimax-tree based solver for the 15-game. It supports the 3x3 and the 4x4 version of the game.</p>
<h2 id="description">Description</h2>
<p>The main algorithm uses a minimax search tree to find the winning position. In the 3x3 version, due to the small size of the state space, the solution can be reached using brute force in a reasonable time. In the 4x4 euristics are required. I used the straightforward <strong>Manhattan Distance</strong> function to measure the total distance of each tile from its correct position. The leaf nodes with the minimum sum of the  distances are chosen to be further explored. Given that the majority of the permutations of [1,2,…,n] don’t result in a solvable initial state, the winning position gets shuffled a given number of time in order to find a solvable initial state. The more the shuffling, the harder it is to find the solution. The variable <code>shuffle = 80</code> is the default. You can also play by yourself using the keyboard.</p>
<h2 id="commands">Commands</h2>
<p>Run the file <code>gui.py</code> to start the game. Here’s a list of the commands:</p>
<ul>
<li><strong>Spacebar</strong>: start the AI solver,</li>
<li><strong>W,A,S,D</strong>: manually move the tiles on the table,</li>
<li><strong>3</strong>: initiate the 3x3 table</li>
<li><strong>4</strong>: initiate the 4x4 table</li>
</ul>
<blockquote>
<p><strong>Note</strong>: You can  switch from 3x3 to 4x4 or viceversa at any time, though not while the program is solving the puzzle automatically, for the latter will most likely crash.</p>
</blockquote>


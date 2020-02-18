<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Welcome file</title>
  <link rel="stylesheet" href="https://stackedit.io/style.css" />
</head>

<body class="stackedit">
  <div class="stackedit__html"><h1 id="game">15-game</h1>
<p>A simple minimax-tree based solver for the 15-game. It supports the 3x3 and the 4x4 version of the game.</p>
<h2 id="description">Description</h2>
<p>The main algorithm uses a minimax search tree to find the winninp position. In the 3x3 version, due to the small size of the state space, the solution can be reached using brute force in a reasonable time. In the 4x4 euristics are required. I used the straighfoward Manhattan Distance function to measure the total distance of each tile from its correct position. The leaf nodes with the minimum total distance are chosen to be further explored. Given that the majority of the permutation of <span class="katex--inline"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo stretchy="false">[</mo><mn>1</mn><mo separator="true">,</mo><mn>2</mn><mo separator="true">,</mo><mi mathvariant="normal">.</mi><mi mathvariant="normal">.</mi><mi mathvariant="normal">.</mi><mo separator="true">,</mo><mi>n</mi><mo stretchy="false">]</mo></mrow><annotation encoding="application/x-tex">[1,2,...,n]</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 1em; vertical-align: -0.25em;"></span><span class="mopen">[</span><span class="mord">1</span><span class="mpunct">,</span><span class="mspace" style="margin-right: 0.166667em;"></span><span class="mord">2</span><span class="mpunct">,</span><span class="mspace" style="margin-right: 0.166667em;"></span><span class="mord">.</span><span class="mord">.</span><span class="mord">.</span><span class="mpunct">,</span><span class="mspace" style="margin-right: 0.166667em;"></span><span class="mord mathdefault">n</span><span class="mclose">]</span></span></span></span></span> doesn’t result in a solvable initial state for the general <span class="katex--inline"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>n</mi><mn>2</mn></msup><mo>−</mo><mn>1</mn></mrow><annotation encoding="application/x-tex">n^2-1</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.897438em; vertical-align: -0.08333em;"></span><span class="mord"><span class="mord mathdefault">n</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height: 0.814108em;"><span class="" style="top: -3.063em; margin-right: 0.05em;"><span class="pstrut" style="height: 2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span><span class="mspace" style="margin-right: 0.222222em;"></span><span class="mbin">−</span><span class="mspace" style="margin-right: 0.222222em;"></span></span><span class="base"><span class="strut" style="height: 0.64444em; vertical-align: 0em;"></span><span class="mord">1</span></span></span></span></span>-game, the winning position gets shuffled a given number of time in order to find a solvable initial state. The more the shuffling, the harder it is to find the solution. The variable <code>shuffle = 80</code> is the default. You can also play by yourself using the keyboard.</p>
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
</div>
</body>

</html>

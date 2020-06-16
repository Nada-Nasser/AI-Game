# Add Numbers Game

Artificial intelligence project implemented Using Alpha-beta Algorithm. 
Modified Add the Numbers is a fun logic based game in which you control a box with a numerical value on it.
You can move left, right, up, down but whatever value is on the box that you replace effects your value. Some
will be positive, and some will be negative. A positive will add to your value, but a negative will subtract.
The aim of the game is to get the highest score, given maximum number of movements and minimal score could
be achieved.

### Prerequisites

* You need to have any Python IDE , for example [Spyder IDE](https://www.spyder-ide.org/)   

### Installing

* 1- Make sure all files in the same folder.
* 2- Run GUI_Game.py file to run the game using any python IDE.

## Running the tests

* 1- Run GUI_Game.py file to run the game
* 2- Enter Minimum level goal and maximum number of moves. 
* 3- press submit button.
* 4- wait until it's available to press start button (it may take long time due to the high complexity of alpha-beta algorithm, it also depends on the number of movements you entered)(for ex.: 10 moves may take 20 min or more to be able to start the game)
* 5- press start to see the game board 
* 6- press next to navigate between game states.

### Test Cases

You Can see many test cases [Here](https://github.com/Nada-Nasser/AI-Game/blob/master/Documentation/Documentation.pdf) .

### NOTES
* The implemented game running as the Max-player plays his turn optimally using alpha-beta algorithm, and Min-Player play randomly
* If you want to Make the Min-Player plays his trun optimally too, you can change the boolean in line 17 at [rand_vs_ai_agent.py](https://github.com/Nada-Nasser/AI-Game/blob/master/SourceCode/rand_vs_ai_agent.py) file to be false.
```python
   random_min = False
```
 

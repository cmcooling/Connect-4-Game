![Tests](https://github.com/coolernato/Connect-4-Game/workflows/Tests/badge.svg)

# Connect-4-Game

## Introduction

This repository contains code which is used to run a game of Connect 4. The strategies employed by players may be specified in functions which can then be passed as arguments to the function which runs the game. A few sample strategies have been included.

### Connect 4

Connect 4 is a two-player game where players take turns adding tokens to a grid with 7 columns and 6 rows. Tokens fall to the lowest unoccupied space in the column they are added to. A player wins the game as soon as four of their tokens form a horizontal, vertical or diagonal line.

![Connect 4 Box Art](https://github.com/coolernato/Connect-4-Game/blob/master/readme_resources/connect4_box.jpg?raw=true)

In the following examples, ```x``` went first and won the game.

Horizontal victory:

```
|               |
|               |
|               |
|               |
|               |
| x x x x o o o |
|---------------|
```

Vertical victory:

```
|               |
|               |
| x             |
| x o           |
| x o           |
| x o           |
|---------------|
```

Diagonal victory:

```
|               |
|               |
|         x     |
|       x o     |
|   o x o x     |
|   x o x o     |
|---------------|
```

In the version of the game we will be playing, the first player will be randomly selected.

## Writing a Strategy

To write a strategy, first download the content of this repository:
* look for the green button with "code" or "download" at the top right of the main repository page,
* click on the "local" tab of the dropdown menu,
* download the content as a compressed file to a location of your choosing on your computer by clicking "Download ZIP",
* unpack the zip file.

Open the file ```student_interface.ipynb```. The first cell in this Jupyter Notebook contains the skeleton of a function. Complete this function to define your strategy. By running the second cell, you can play against your strategy to tet how it performs. Running the third cell will assess your strategy (see the assessment section below).

### Details on Strategies

A strategy should be a function which takes two arguments. The first is the current board state and the second is the number of the player the strategy will be taking moves on behalf of (this value will be 1 or 2). The function should consider the board state and then return a value between 0 and 6 relating to the index of the column the strategy has selected for its next move.

The board state is a list of lists. Each of the inner lists contains all the entries in a given column, with the index of the value representing the bottom position in the column being 0 and the index of the value representing the top position in the column being 5. In the outer list, the left-most column has an index of 0 and the right-most column has an index of 6. The indexes of the positions on the board are thus as follows:

```
[0][5] [1][5] [2][5] [3][5] [4][5] [5][5] [6][5] 
[0][4] [1][4] [2][4] [3][4] [4][4] [5][4] [6][4] 
[0][3] [1][3] [2][3] [3][3] [4][3] [5][3] [6][3] 
[0][2] [1][2] [2][2] [3][2] [4][2] [5][2] [6][2] 
[0][1] [1][1] [2][1] [3][1] [4][1] [5][1] [6][1] 
[0][0] [1][0] [2][0] [3][0] [4][0] [5][0] [6][0] 
```

For instance, if the argument holding the state of the board has the variable name ```board```, the value representing the state of the bottom-right position could be found by writing ```board[6][0]``` and the the top-middle value could be found by writing ```board[3][5]```. For each location, the value will be 0 if no player has placed a piece there, 1 if player 1 has, and 2 if player 2 has.

For instance, after both players have taken two moves, the values of the variable of ```board``` may be:

```
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
1 0 0 0 0 0 0
2 0 0 2 0 1 0
```

In this case, ```board[0][1]``` and ```board[5][0]``` are both ```1```, while ```board [0][0]``` and ```board[3][0]``` are both ```2```. ```board[i][j]``` is zero for all other values of ```i``` and ```j```.

Make sure to return a single integer between 0 and 6 to indicate which column you want to make your move in.

### Forfeiting the Game

Other than losing the game normally, a strategy can forfeit a game in the following cases:

* Returning a non-integer value
* Returning an integer value which is less than 0 or greater than 6
* Returning an integer relating to a column which is full
* Taking more than 1 second to return a value
* Raising an exception when asked for a move

## Playing Against Your Strategy

In the file ```student_interface.ipynb``` you can play against your strategy by running the second code cell. When it's your turn, you will need to enter a value between 0 and 6 to indicate which column you're choosing to place your token into. Note that, every time you update your strategy, you will need to re-run the first code cell to update the version of the function ```my_strategy``` in use.


## Assessment

If you're using this resource as part of the I-Explore course, the final strategy you submit via Blackboard will be assessed. This will be done by pitting your strategy against a strategy which always picks a random move from a random non-full column. 1000 games will be played, with the player moving first determined randomly for each game. Your strategy will forfeit a game in the cases outlined in the section above. It will be tracked how many games end in a victory for you, a draw, a loss to the opponent without your strategy raising an exception, and the number of times your strategy forfeits by raising an exception. The final mark you receive will be calculated as follows:

$$ M_{\\%} = \left(0.25\left(1 - \frac{n_f}{1000}\right) + 0.75\left(\frac{n_{w} + \frac{n_{d}}{2}}{1000}\right)^{3}\right) \times 100\\% $$

where $M_{\\%}$ is your final mark in %, $n_{f}$ is the number of times your strategy forfeits a game, $n_{w}$ is the number of games your strategy wins a a game, and $n_{d}$ is the number of times your strategy draws. Some example marks include:

* Your strategy forfeits every game: 0%
* Your strategy loses every game without forfeiting: 50%
* Your strategy wins half the games and loses half the games without forfeiting: 62.5%
* Your strategy wins every game: 100%

The figure below shows some sample mars you could receive for different numbers of wins, draws and forfeits.

![Sample Marks](https://github.com/coolernato/Connect-4-Game/blob/master/readme_resources/marks_example.png?raw=true)

If you would like to test your strategy against the assessment, run the final code cell in the ```student_interface.ipynb``` Jupyter notebook. You can also observe your strategy play a single match against the opponent you will face in the assessment by running the third code cell in that notebook. 

## Submission

When submitting your final strategy, rename this notebook to "FIRSTNAME_SURNAME.ipynb" and submit this notebook only. We expect you to spend 3-5 hours on this assignment. The first cell in the notebook you submit must contain the entirety of your strategy. It may contain multiple functions if you wish. You may import and use any modules from the standard library (e.g. the ```math``` module). You may not use any modules that require separate installation (e.g. ```numpy```, ```pandas```, etc). The assessment submission may be found in the Blackboard module under the section "Assessment Submission".

Your strategy will be played against the strategies developed by other students in the in-person session. If you would prefer your strategy to be anonymous, please note this in a comment at the top of the code cell containing your strategy and provide a pseudonym you would like the strategy to compete under. This will allow you to see how your strategy performs, but others will not know it's your strategy.

## Tips

There are a number of ways you could go about writing this code. If you're stuck, consider the following:

* How can I prevent my code going in a column which is full?
* If an available move will win me the game, how can I detect it and select that column?
* If an available move will win my opponent the game, how can I detect it and select that column to block their winning move?
* How can I detect when going in a particular column will allow my opponent to gon in the same column and make a winning move?
* If there are no opportunities or threats of an immediate victories, how can I best progress toward a victory state, or hinder my opponent?

Particularly if you're new to programming, don't worry about making your solution perfect. Focus on code which is going to be simple to implement but have a high impact on the performance of your strategy.

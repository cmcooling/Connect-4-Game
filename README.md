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

## Running a Game

The easiest way to run a game is by running the ```game_master.py``` file. This is currently set up to pit two of the sample strategies against each other. The output of the game should be visible in the terminal used to run the code. The output will include a turn by turn output of the game-state of the board and will announce a winner.

To play manually against a strategy, change game_master.py to:
```
run_game("Left", "Manual", methodical.fill_left_right, manual.manual, move_duration=1, max_move_time=100)
```
This asks you to input a move yourself as an integer and press enter. ```max_move_time=100``` gives you a bit more time to move!

## Writing a Strategy

To write a strategy, first donwload the content of this repository:
* look for the green button with "code" or "download" at the top right of the main repository page
* download the content as a compressed file
* then unpack it

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

Make sure to return a single integer between 0 and 6 to indicate which column you want to make your move in.

### Forfeiting the Game

Other than losing the game normally, a strategy can forfeit a game in the following cases:

* Returning a non-integer value
* Returning an integer value which is less than 0 or greater than 6
* Returning an integer relating to a column which is full
* Taking more than 1 second to return a value
* Raising an exception when asked for a move

## Assessment

If you're using this resource as part of the I-Explore course, the final strategy you submit via Blackboard will be assessed. This will be done by pitting your strategy against a strategy which always picks a random move from a random non-full column. 1000 games will be played, with the player moving first determined randomly for each game. Your strategy will forfeit a game if it choses a column which is full, or takes more than 1s to make a move. It will be tracked how many games end in a victory for you, a draw, a loss to the opponent without your strategy raising an exception, and the number of times your strategy forfeits by raising an exception. The final mark you receive will be calculated as follows:

$$ M_{\\%} = \left(\frac{1 - \frac{n_f}{1000} + \left(\frac{n_{w} + \frac{n_{d}}{2}}{1000}\right)^{2}}{2}\right) \times 100\\% $$

where $M_{\\%}$ is your final mark in %, $n_{f}$ is the number of times your strategy forfeits a game, $n_{w}$ is the number of games your strategy wins a a game, and $n_{d}$ is the number of times your strategy draws. Some example marks include:

* Your strategy forfeits every game: 0%
* Your strategy loses every game without forfeiting: 50%
* Your strategy wins half the games and loses half the games without forfeiting: 62.5%
* Your strategy wins every game: 100%

If you would like to test your strategy against the assessment, run the third code cell in the ```student_interface.ipynb``` Jupyter notebook. When submitting your final strategy, rename this notebook to "FIRSTNAME_SURNAME.ipynb" and submit this notebook only.

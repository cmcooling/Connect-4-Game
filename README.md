# Connect-4-Game

## Introduction

This repository contains code which is used to run a game of Connect 4. The strategies employed by players may be specified in functions which can then be passed as arguments to the function which runs the game. A few sample strategies have been included.

### Connect 4

Connect 4 is a two-player game where players take turns adding tokens to a grid with 7 columns and six rows. Tokens fall to the lowest unoccupied space in the column they are added to. A player wins the game as soon as four of their tokens form a horizontal, vertical or diagonal line.

![Connect 4 Box Art](https://github.com/coolernato/Connect-4-Game/blob/master/readme_resources/connect4_box.jpg?raw=true)

In the following examples, ```x``` went first and won the game.

Horizontal victory:

```





x x x x o o o
```

Vertical victory:

```


x
x o
x o
x o
```

Diaognal victory:

```


        x
      x o
    x o x
  x o x o
```

In the version of the game we will be playing, the first player will be randomly selected.

## Running a Game

The easiest way to run a game is by running the ```game_master.py``` file. This is currently set up to pit two of the sample strategies against each other. The output of the game should be visible in the terminal used to run the code. The output will include a turn by turn output of the game-state of the board and will announce a winner.

## Writing a Strategy

To write a strategy, a new ```.py``` file must be added to the ```strategies``` directory. This should contain a function used to calculate the next move to be taken given the current board state. As an example, look at ```random_strategies.py``` which contains a single function or ```methodical.py``` which contains two strategies.

### Details on Strategies

A strategy should be a function which takes two arguments. The first is the current board state and the second is the number of the player the strategy will be taking moves on behalf of (this value will be 1 or 2). The function should consider the board state and then return a value between 0 and 6 relating to the index of the column the strategy has selected for its next move.

The board state is a lsit of lists. Each of the inner lists contains all the entries in a given column, with the index of the value representing the bottom position in the column being 0 and the index of the value representing the top position in the column being 5. In the outer list, the left-most column has an index of 0 and the right-most column has an index of 6. The indicies of the positions on the board are thus as follows:

```
[0][5] [1][5] [2][5] [3][5] [4][5] [5][5] [6][5] 
[0][4] [1][4] [2][4] [3][4] [4][4] [5][4] [6][4] 
[0][3] [1][3] [2][3] [3][3] [4][3] [5][3] [6][3] 
[0][2] [1][2] [2][2] [3][2] [4][2] [5][2] [6][2] 
[0][1] [1][1] [2][1] [3][1] [4][1] [5][1] [6][1] 
[0][0] [1][0] [2][0] [3][0] [4][0] [5][0] [6][0] 
```

For instance, if the argument holding the state of the board has the variable name ```board```, the value representing the state of the bottom-right position could be found by writing ```board[6][0]``` and the the top-middle value could be found by writing ```board[3][5]```. For each location, the value will be 0 if no player has placed a piece there, 1 if player 1 has, and 2 if player 2 has.

### Forfeiting the Game

Other than losing the game normally, a strategy can forfeit a game in the following cases:

* Returning a non-integer value
* Returning an integer value which is less than 0 or greater than 6
* Returning an integer relating to a column which is full
* Taking more than 1s to return a value

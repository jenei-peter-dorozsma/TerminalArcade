# Terminal Arcade
<p align="center">
    <img atl="Terminal Arcade Logo" src="images/logo_150x150.png" width="150" height="150">
</p>

![Terminal Arcade Logo](images/logo_150x150.png)

<p align="center"><i>
It's time to drop a coin.<br />
It's time to light the lights.<br />
It's time to play the games<br />
in the terminal tonight!<br />
</i></p>

## About the project
The best way to learn a new programming language, once you're familiar with the basics, is to find a project and start developing a program. I have selected small single-player games for the terminal. Please check them out, enjoy them, learn from them, and, more importantly, make suggestions to help me become a better developer.

## Getting started
### Prerequisites
* **Python:** Version 3.x
* Terminal / Command line prompt
* **Optimal terminal size:** 100 x 45
* **Tested on:** MacOs

### Start game
1. Download project
2. Enter to folder that contains `main.py`
3. Run `python3 main.py`

## Usage
### Main screen
<img src="/images/mainscreen_dark.png" width="300">
<img src="/images/mainscreen_light.png" width="300">

On the main screen you can choose from the following options:
- `1` - Start a new *Minesweeper* game
- `2` - Start a new *Yahtzee* game
- `3` - Start a new *Tic Tac Toe* game
- `4` - Start a new *Rock Paper Scissors* game
- `Q` - Exit from *Terminal Arcade*

### Games
#### Minesweeper
<img src="/images/minesweeper_dark.png" width="300">
<img src="/images/minesweeper_light.png" width="300">

Minesweeper game. The goal of the game is to find all the mines on the field without stepping on them. You can also mark the mines with flags.

Before you start looking for mines you can select on how big minefield you would like to play on. Available options are:
- `s` - Small sized minefield: 10x10 fields
- `m` - Medium sized minefield: 20x20 fields
- `l` - Large sized minefield: 30x30 fields

Once you've selected the size of the minefield, you can select the difficuly. Avaliable options are:
- `e` - Easy mode: 10% of the fields are mines
- `m` - Medium mode: 20% of the fields are mines
- `h` - Hard mode: 30% of the fields are mines

When the minefiled appears you can start looking for mines and marking them. The available commands are:
- `column,row` - Open one field by specifying the column and row numbers
- `column,row,f` - Put on or remove flag from a field by specifying the column and row numbers
- `q` - Exit game and go back to main screen

#### Yahtzee
<img src="/images/yahtzee_dark.png" width="300">
<img src="/images/yahtzee_light.png" width="300">

Yahtzee game, also known as Poker Dice. Each turn you throw with five dice. You can lock and unlock any dice and reroll the remaining ones twice in a turn. Close your turn by assigning the dice set to a combination. Different dice result set means different values at specific combination.  

The combinations you need to collect:
- `1s` - Collect as many 1 dice faces as possible. The value equals the summary of the 1s.
- `2s` - Collect as many 2 dice faces as possible. The value equals the summary of the 2s.
- `3s` - Collect as many 3 dice faces as possible. The value equals the summary of the 3s.
- `4s` - Collect as many 4 dice faces as possible. The value equals the summary of the 4s.
- `5s` - Collect as many 5 dice faces as possible. The value equals the summary of the 5s.
- `6s` - Collect as many 6 dice faces as possible. The value equals the summary of the 6s.
- `One pair` - Collect two dice faces of the same kind. The value equals the summary of the highest pair in the thrown set.
- `Two pairs` - Collect two pairs. The value equals the summary of the two pairs.
- `Three of a kind` - Collect three dice face of the same kind. The value equals the summary of the three equal dice face.
- `Four of a kind` - Collect four dice face of the same kind. The value equals the summary of the four equal dice face.
- `Full house` - Collect one pair and one three of a kind comination. The value equals the summary of all the dice.
- `Small strait` - Collect a four item long strait. The value equals the highest small strait in the thrown set.
- `Large strait` - Collect a five item long strait. The value equals the summary of all the dice.
- `Five of a kind` - Collect five dice face of the same kind. The value equals the summary of all the dice.
- `Joker` - Any combination could fit here. The value equals the summary of all the dice.

If the thrown dice set does not meet the requirements of the combination it counts as 0 points.
During the game the following commands are available:
- `r` - Throw with all five dice
- `rr` - Reroll the unlocked dice
- `a-e` - Lock or unlock any of the five dice
- `1-15` - Save the thrown set a combination
- `q` - Exit game and go back to main screen

#### Tic Tac Toe
<img src="/images/tictactoe_dark.png" width="300">
<img src="/images/tictactoe_light.png" width="300">

Tic Tac Toe game. You play against the computer. You take turns marking the spaces in a three-by-three grid with X or O. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner.  
During the game the following commands are available:
- `1-9` - Place your mark on any of the empty fields
- `q` - Exit game and go back to main screen

#### Rock Paper Scissors
<img src="/images/rockpaperscissors_dark.png" width="300">
<img src="/images/rockpaperscissors_light.png" width="300">

Rock Paper Scissors game. You play against the computer. You take one of the following hand signs:
- `r` - Rock
- `p` - Paper
- `s` - Scissors

Each turn the stronest hand wins one point. The winnig rules are:
- Rock breaks the Scissors!
- Paper covers the Rock!
- Scissors cut the Paper!

You can also use the `q` command to exit game and go back to main screen.

## Roadmap
- [ ] Hangman
- [ ] Letter drop
- [ ] Battlefield
- [ ] Campsite
- [ ] ConnectFour
- [ ] BlackJack
- [ ] Snake
- [ ] Invaders

## License
Licensed under the Apache License, Version 2.0 (the "License"); you may not use this software except in compliance with the License.

## Contact
Peter Jenei - jenei.peter.dorozsma@gmail.com  
Project Link: https://github.com/jenei-peter-dorozsma/TerminalArcade
''' Terminal Arcade: single player games for terminal '''
# Copyright 2023 Peter Jenei

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from Games.Assets.terminalColors import TColor
from Games import minefield, yahtzee, tictactoe, rockPaperScissors

DESIGN = {
    'Logo': [
        'R    ┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬      E',
        'R  ┬─┴─┬─┴───┴───┴───┴───┴───┴───┴───┴───┴─┬─┴─┬─┴─┬─┴─┬    E',
        'R┬─┴─┬─┘  EG─┬─ ┌── ┌─┐ ┌┐┌┐ |      ┌─┐ |  ER┌─┴─┬─┴─┬─┴─┬─┴    E',
        'R┴─┬─┴─┐  EG │  ├─  ├─┘ │└┘│ │ │\ │ ├─┤ │  ER└─┬─┴─┬─┴─┬─┴─┬    E',
        'R┬─┴─┬─┴─┐EG │  └── │ \ │  │ │ │ \│ │ │ └──ER  └─┬─┴─┬─┴─┬─┴    E',
        'R┴─┬─┴─┬─┴─┬───┬───┬───┬───┬───┬───┬───┬───┬─┴─┬─┴─┬─┴      E',
        'R  ┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴───┴───┴───┴───┴───┴───┴─┬─┴─┬      E',
        'R  ┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┐EG ┌─┐ ┌─┐ ┌── ┌─┐ ┌─  ┌──ER └─┬─┴─┬    E',
        'R┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┘EG ├─┤ ├─┘ │   ├─┤ │ │ ├─ ER ┌─┴─┬─┴    E',
        'R┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┐EG │ │ │ \ └── │ │ └─  └──ER └─┬─┴─┬    E',
        'R┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬───┬───┬───┬───┬───┬───┬─┴─┬─┴─┬  E',
        'R└─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬E',
        'R  ┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴E'
    ],

    'GameList': [
        f'{TColor.OKBLUE}1{TColor.ENDC} - Minesweeper',
        f'{TColor.OKBLUE}2{TColor.ENDC} - Yahtzee',
        f'{TColor.OKBLUE}3{TColor.ENDC} - Tic Tac Toe',
        f'{TColor.OKBLUE}4{TColor.ENDC} - Rock Paper Scissors',
        f'{TColor.OKBLUE}Q{TColor.ENDC} - Quit to terminal'
    ]
}

def print_main_screen(message=''):
    '''
    Display and handle main screen for Terminal Arcade
    '''
    os.system('clear')

    for row in range(0, len(DESIGN['Logo'])):
        logo_row=DESIGN['Logo'][row]
        logo_row = logo_row.replace('R', TColor.FAIL)
        logo_row = logo_row.replace('G', TColor.OKGREEN)
        logo_row = logo_row.replace('E', TColor.ENDC)
        print(logo_row)

    print('')
    for i in DESIGN['GameList']:
        print(''.center(21, ' '), end='')
        print(i)

    print(f'\n{message}')
    message=''
    command=input("Which game would you like to play?")

    if command == '1':
        game=minefield.Minesweeper()
        # game.admin_mode=True
        game.new_game()
    elif command == '2':
        game = yahtzee.Yahtzee()
        game.new_game()
    elif command == '3':
        game = tictactoe.TicTacToe()
        game.new_game()
    elif command == '4':
        game = rockPaperScissors.RockPaperScissors()
        game.new_game()
    elif command.lower() == 'q':
        return
    else:
        message=TColor.FAIL+'There is no such parameter'+TColor.ENDC

    print_main_screen(message)

if __name__ == "__main__":
    print_main_screen()
    print(f'{TColor.OKGREEN}Thank you for playing! Have a nice day!{TColor.ENDC}')

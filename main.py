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
import Games.Assets.terminalColors as TC
from Games import minefield, yahtzee, tictactoe, rockPaperScissors

DESIGN = {
    'Logo': [
        '#F    ┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬      #E',
        '#F  ┬─┴─┬─┴───┴───┴───┴───┴───┴───┴───┴───┴─┬─┴─┬─┴─┬─┴─┬    #E',
        '#F┬─┴─┬─┘  #E#G─┬─ ┌── ┌─┐ ┌┐┌┐ |      ┌─┐ |  #E#F┌─┴─┬─┴─┬─┴─┬─┴    #E',
        '#F┴─┬─┴─┐  #E#G │  ├─  ├─┘ │└┘│ │ │\ │ ├─┤ │  #E#F└─┬─┴─┬─┴─┬─┴─┬    #E',
        '#F┬─┴─┬─┴─┐#E#G │  └── │ \ │  │ │ │ \│ │ │ └──#E#F  └─┬─┴─┬─┴─┬─┴    #E',
        '#F┴─┬─┴─┬─┴─┬───┬───┬───┬───┬───┬───┬───┬───┬─┴─┬─┴─┬─┴      #E',
        '#F  ┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴───┴───┴───┴───┴───┴───┴─┬─┴─┬      #E',
        '#F  ┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┐#E#G ┌─┐ ┌─┐ ┌── ┌─┐ ┌─  ┌──#E#F └─┬─┴─┬    #E',
        '#F┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┘#E#G ├─┤ ├─┘ │   ├─┤ │ │ ├─ #E#F ┌─┴─┬─┴    #E',
        '#F┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┐#E#G │ │ │ \ └── │ │ └─  └──#E#F └─┬─┴─┬    #E',
        '#F┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬───┬───┬───┬───┬───┬───┬─┴─┬─┴─┬  #E',
        '#F└─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬#E',
        '#F  ┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴#E'
    ],

    'Logo-extended': [
        '                     ┌─────────────┐                         ',
        '        #  ┬┬       ┌┴─────────────┴┐                        ',
        ' ┬┬  ┌──┴──┴┴─┐     │  ┌┐ ┌┐ ┌┐ ┌┐  │               #        ',
        ' ┴┴──┴──┐ ┌─┐ │   # │  └┘ └┘ └┘ └┘  │┌────┐ ┬┬ # ┌──┴──┐     ',
        '  ┌┐ ┌┐ │ └─┘┌┴───┴─┴──┬┐ ┌┐ ┌┐ ┌┐  ││ # ┌┴─┴┴─┴─┴─┐   │     ',
        '  └┘ └┘ │ ┌─┐│ ┌─┐ ┌─┐ ├┘ └┘ └┘ ├┴──┴┴─┴─┴┐┌─┐ ┌─┐ │   │     ',
        '  ┌┐ ┌┐ ┼┬└─┘│ └─┘ └─┘ ├┐ ┌┐ ┌┐ │ ┌┬──────┴┴─┴─┴─┤ │   │     ',
        '  └┘┌┴┴─┴┴───┴──┬┐ ┌─┐ ├┘ └┘ └┘ │ ││ ┌─┐ ┌─┐ ┌─┐ │ │  ┌┴──── ',
        '  ┌┐│ ┌──┐ ┌──┐ ├┘ └─┘ ├┐ ┌┐ ┌┐ │ └┤ └─┘ └─┘ └─┘ │ │  │  ┌─┐ ',
        '  └┘│ └──┘ └──┘ ├┐ ┌─┐ ├┘ └┘ └┘ │ ┌┤ ┌─┐ ┌─┐ ┌─┐ │ │  │  └─┘ ',
        '    │ ┌──┐ ┌──┐ ├┘ └─┘ ├┐ ┌┐ ┌┐ │ ││ └─┘ └─┘ └─┘ │ │  │  ┌─┐ ',
        '    │ └──┘ └──┘ │      ├┘ └┘ └┘ │ └┤ ┌─┐ ┌─┐ ┌─┐ │ │  │  └─┘ ',
        '#F┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬#E',
        '#F┴─┬─┴─┬─┴───┴───┴───┴───┴───┴───┴───┴───┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴#E',
        '#F┬─┴─┬─┘  #E#G─┬─ ┌── ┌─┐ ┌┐┌┐ |      ┌─┐ |  #E#F┌─┴─┬─┴─┬─┴─┬─┴─┬─┴  #E',
        '#F┴─┬─┴─┐  #E#G │  ├─  ├─┘ │└┘│ │ │\ │ ├─┤ │  #E#F└─┬─┴─┬─┴─┬─┴─┬─┴    #E',
        '#F┬─┴─┬─┴─┐#E#G │  └── │ \ │  │ │ │ \│ │ │ └──#E#F  └─┬─┴─┬─┴─┬─┴─┬    #E',
        '#F┴─┬─┴─┬─┴─┬───┬───┬───┬───┬───┬───┬───┬───┬─┴─┬─┴─┬─┴─┬─┴    #E',
        '#F  ┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴───┴───┴───┴───┴───┴───┴─┬─┴─┬─┴─┬    #E',
        '#F  ┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┐ #E#G┌─┐ ┌─┐ ┌── ┌─┐ ┌─  ┌──#E#F └─┬─┴─┬─┴    #E',
        '#F┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┘ #E#G├─┤ ├─┘ │   ├─┤ │ │ ├─ #E#F ┌─┴─┬─┴      #E',
        '#F┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┐ #E#G│ │ │ \ └── │ │ └─  └──#E#F └─┬─┴─┬      #E',
        '#F┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬───┬───┬───┬───┬───┬───┬─┴─┬─┴─┬    #E',
        '#F└─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬  #E',
        '#F  ┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴  #E',
    ],

    'GameList': [
        f'#B1#E - Minesweeper',
        f'#B2#E - Yahtzee',
        f'#B3#E - Tic Tac Toe',
        f'#B4#E - Rock Paper Scissors',
        f'#BQ#E - Quit to terminal'
    ]
}

def print_main_screen(message=''):
    '''
    Display and handle main screen for Terminal Arcade
    '''
    os.system('clear')

    for row in range(0, len(DESIGN['Logo-extended'])):
        logo_row=DESIGN['Logo-extended'][row]
        logo_row=TC.colorize(logo_row)
        print(logo_row)

    print('')
    for i in DESIGN['GameList']:
        print(''.center(21, ' '), end='')
        print(TC.colorize(i))

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
        message=TC.colorize('#FThere is no such parameter#E')

    print_main_screen(message)

if __name__ == "__main__":
    print_main_screen()
    print(TC.colorize('#GThank you for playing! Have a nice day!#E'))

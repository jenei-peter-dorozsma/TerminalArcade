'''Terminal Arcade: small single player games for terminal'''
import os
import random
from Games.Assets.terminalColors import TColor
from Games import minefield, yahtzee, tictactoe, rockPaperScissors
import Games.Assets.handArt as ha


TERMINAL_ARCDADE = TColor.HEADER + 'T' + TColor.ENDC
TERMINAL_ARCDADE +=  TColor.OKBLUE + 'E' + TColor.ENDC
TERMINAL_ARCDADE +=  TColor.OKCYAN + 'R' + TColor.ENDC
TERMINAL_ARCDADE +=  TColor.OKGREEN + 'M' + TColor.ENDC
TERMINAL_ARCDADE +=  TColor.WARNING + 'I' + TColor.ENDC
TERMINAL_ARCDADE +=  TColor.FAIL + 'N' + TColor.ENDC
TERMINAL_ARCDADE +=  TColor.HEADER + 'A' + TColor.ENDC
TERMINAL_ARCDADE +=  TColor.OKBLUE + 'L ' + TColor.ENDC
TERMINAL_ARCDADE +=  TColor.OKCYAN + 'A' + TColor.ENDC
TERMINAL_ARCDADE +=  TColor.OKGREEN + 'R' + TColor.ENDC
TERMINAL_ARCDADE +=  TColor.WARNING + 'C' + TColor.ENDC
TERMINAL_ARCDADE +=  TColor.FAIL + 'A' + TColor.ENDC
TERMINAL_ARCDADE +=  TColor.HEADER + 'D' + TColor.ENDC
TERMINAL_ARCDADE +=  TColor.OKBLUE + 'E' + TColor.ENDC

DESIGN = {
    'Logo': [
        '                      ',
        ' ╔══════════════════╗ ',
        ' ║  Welcome         ║ ',
        ' ║        to the    ║ ',
        f' ║ {TERMINAL_ARCDADE}! ║ ',
        ' ╚══════════════════╝ ',
        '                      '
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
    hand_signs = ('Rock', 'Paper', 'Scissors', 'Metal', 'Pinky', 'Yes', 'Shaka')
    lefty = random.choice(hand_signs)
    left_art = ha.HAND_ART[lefty]
    righty = random.choice(hand_signs)
    right_art = ha.HAND_ART[righty]

    for row in range(0, ha.HAND_HEIGHT):
        left_art_row=left_art[row]
        logo_row=DESIGN['Logo'][row]
        right_art_row=right_art[row]
        right_art_row=ha.reverse_art_line(right_art_row)
        print(f'{TColor.OKBLUE}{left_art_row}{TColor.ENDC}', end='')
        print(logo_row, end='')
        print(f'{TColor.FAIL}{right_art_row}{TColor.ENDC}')

    # print(left_art)
    # print(right_art)

    for i in DESIGN['GameList']:
        print(''.center(21, ' '), end='')
        print(i)

    print(f'\n{message}')
    message=''
    command=input("Which game would you like to play?")

    if command == '1':
        game=minefield.Minesweeper()
        # game.admin_mode=True
        game.new_game('s', 'e')
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

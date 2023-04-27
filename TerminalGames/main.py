import os
from Games.Assets.terminalColors import TColor
from Games import minefield, yahtzee, tictactoe, rockPaperScissors

def print_main_screen(message=''):
    os.system('clear')
    intro = ' Welcome to the '
    intro +=  TColor.HEADER + 'T' + TColor.ENDC
    intro +=  TColor.OKBLUE + 'E' + TColor.ENDC
    intro +=  TColor.OKCYAN + 'R' + TColor.ENDC
    intro +=  TColor.OKGREEN + 'M' + TColor.ENDC
    intro +=  TColor.WARNING + 'I' + TColor.ENDC
    intro +=  TColor.FAIL + 'N' + TColor.ENDC
    intro +=  TColor.HEADER + 'A' + TColor.ENDC
    intro +=  TColor.OKBLUE + 'L ' + TColor.ENDC
    intro +=  TColor.OKCYAN + 'A' + TColor.ENDC
    intro +=  TColor.OKGREEN + 'R' + TColor.ENDC
    intro +=  TColor.WARNING + 'C' + TColor.ENDC
    intro +=  TColor.FAIL + 'A' + TColor.ENDC
    intro +=  TColor.HEADER + 'D' + TColor.ENDC
    intro +=  TColor.OKBLUE + 'E' + TColor.ENDC
    intro +=  '!!! '

    print(intro.center(60, '='))
    print('')
    print(f'   {TColor.OKBLUE}1{TColor.ENDC} - Minesweeper')
    print(f'   {TColor.OKBLUE}2{TColor.ENDC} - Yahtzee')
    print(f'   {TColor.OKBLUE}3{TColor.ENDC} - Tic Tac Toe')
    print(f'   {TColor.OKBLUE}4{TColor.ENDC} - Rock Paper Scissors')
    print(f'   {TColor.OKBLUE}Q{TColor.ENDC} - Quit to terminal')
    print('')

    print(message)
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
        return 0
    else:
        message=TColor.FAIL+'There is no such parameter'+TColor.ENDC

    print_main_screen(message)

if __name__ == "__main__":
    print_main_screen()
    print('Thank you for playing! Have a nice day!')

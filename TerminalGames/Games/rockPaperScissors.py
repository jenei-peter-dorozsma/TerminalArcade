import random
import os
from Games.Assets.terminalColors import TColor
import Games.Assets.handArt as ha

class RockPaperScissors:
    OPTIONS = {
        'r': {
            'value' : 1,
            'art': 'Rock'
        },
        'p': {
            'value' : 2,
            'art': 'Paper'
        },
        's': {
            'value' : 3,
            'art': 'Scissors'
        }
    }

    OPTION_MESSAGES = {
        'rs': f'{TColor.OKBLUE}Rock{TColor.ENDC} breaks the {TColor.FAIL}Scissors{TColor.ENDC}!',
        'pr': f'{TColor.OKBLUE}Paper{TColor.ENDC} covers the {TColor.FAIL}Rock{TColor.ENDC}!',
        'sp': f'{TColor.OKBLUE}Scissors{TColor.ENDC} cut the {TColor.FAIL}Paper{TColor.ENDC}!',
        'sr': f'{TColor.FAIL}Rock{TColor.ENDC} breaks the {TColor.OKBLUE}Scissors{TColor.ENDC}!',
        'rp': f'{TColor.FAIL}Paper{TColor.ENDC} covers the {TColor.OKBLUE}Rock{TColor.ENDC}!',
        'ps': f'{TColor.FAIL}Scissors{TColor.ENDC} cut the {TColor.OKBLUE}Paper{TColor.ENDC}!'
    }

    def __init__(self):
        self.msg=''
        self.player_score=0
        self.player_take=''
        self.computer_score=0
        self.computer_take=''

    def new_game(self):
        self.msg=''
        self.player_score=0
        self.player_take=''
        self.computer_score=0
        self.computer_take=''
        self.print_screen()

    def print_screen(self):
        '''Print gamescreen to terminal'''
        os.system('clear')
        self.print_score_board()
        self.user_consol()

    def reverse_art(self, art):
        art=art[::-1]
        art = art.replace(')', '#')
        art = art.replace('(', ')')
        art = art.replace('#', '(')
        art = art.replace('/', '#')
        art = art.replace('\\', '/')
        art = art.replace('#', '\\')

        return art

    def print_score_board(self):
        print(' Status '.center(60, '-'))
        print(' Player score '.center(30, ' '), end='')
        print(' Computer score '.center(30, ' '))
        print(f'{TColor.OKBLUE}{self.player_score}{TColor.ENDC}'.center(40, ' '), end='')
        print(f'{TColor.FAIL}{self.computer_score}{TColor.ENDC}'.center(40, ' '))
        if self.player_take!='' and self.computer_take!='':
            for row in range(0, ha.HAND_HEIGHT):
                player_art_row=ha.HAND_ART[self.OPTIONS[self.player_take]['art']][row]
                computer_art_row=ha.HAND_ART[self.OPTIONS[self.computer_take]['art']][row]
                computer_art_row=self.reverse_art(computer_art_row)
                print(f'{TColor.OKBLUE}{player_art_row}{TColor.ENDC}'.center(35, ' '), end='')
                print(f'{TColor.FAIL}{computer_art_row}{TColor.ENDC}'.center(35, ' '))
            print('')

        self.player_take=''
        self.computer_take=''

    def user_consol(self):
        print(' User consol '.center(60, '-'))

        print(self.msg)
        command=input('\nWhat do you choose (r-Rock, p-Paper, s-scissors)?')
        self.msg=''

        if command == 'q':
            exit(0)
        elif command.lower() in ('r', 'rock'):
            self.answer_step('r')
        elif command.lower() in ('p', 'paper'):
            self.answer_step('p')
        elif command.lower() in ('s', 'scissors'):
            self.answer_step('s')
        else:
            self.msg=TColor.FAIL+'There is no such parameter'+TColor.ENDC
        
        self.print_screen()

    def answer_step(self, player_take):
        self.player_take=player_take
        self.computer_take=random.choice(['r', 'p', 's'])

        self.update_points()

    def update_points(self):
        result=self.OPTIONS[self.player_take]['value']-self.OPTIONS[self.computer_take]['value']
        if result==0:
            self.msg='It is a TIE. Noone gets point.'
        elif result in (1, -2):
            self.player_score += 1
            self.msg=self.OPTION_MESSAGES[self.player_take+self.computer_take]
            self.msg+=' Player gets a point'
        else:
            self.computer_score += 1
            self.msg=self.OPTION_MESSAGES[self.player_take+self.computer_take]
            self.msg+=' Computer gets a point.'

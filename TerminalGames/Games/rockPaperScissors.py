'''Terminal based Rock-Paper-Scissors game'''
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
import random
from Games.Assets.terminalColors import TColor
import Games.Assets.handArt as ha

class RockPaperScissors:
    '''Rock Paper Scissors game implementation with TUI'''

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
        '''Start a new game'''
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

    def print_score_board(self):
        '''Print actual status and latest round to the screen'''
        print(' Status '.center(60, '-'))
        print(' Player score '.center(30, ' '), end='')
        print(' Computer score '.center(30, ' '))
        print(f'{TColor.OKBLUE}{self.player_score}{TColor.ENDC}'.center(40, ' '), end='')
        print(f'{TColor.FAIL}{self.computer_score}{TColor.ENDC}'.center(40, ' '))
        if self.player_take!='' and self.computer_take!='':
            for row in range(0, ha.HAND_HEIGHT):
                player_art_row=ha.HAND_ART[self.OPTIONS[self.player_take]['art']][row]
                computer_art_row=ha.HAND_ART[self.OPTIONS[self.computer_take]['art']][row]
                computer_art_row=ha.reverse_art_line(computer_art_row)
                print(f'{TColor.OKBLUE}{player_art_row}{TColor.ENDC}'.center(35, ' '), end='')
                print(f'{TColor.FAIL}{computer_art_row}{TColor.ENDC}'.center(35, ' '))
            print('')

        self.player_take=''
        self.computer_take=''

    def user_consol(self):
        '''Print user consol and handle user inputs'''
        print(' User consol '.center(60, '-'))

        print(self.msg)
        command=input('\nWhat do you choose (r-Rock, p-Paper, s-Scissors, q-End game)?')
        self.msg=''

        if command.lower() == 'q':
            return
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
        '''Select a random hand as an aswer step'''
        self.player_take=player_take
        self.computer_take=random.choice(['r', 'p', 's'])

        self.update_points()

    def update_points(self):
        '''Analyze the relation of the selected hands and update the points based on the result'''
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

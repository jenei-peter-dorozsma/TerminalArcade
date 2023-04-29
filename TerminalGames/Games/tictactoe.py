'''Terminal based Tic Tac Toe game'''
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

class TicTacToe:
    '''Tic Tac Toe game implementation with TUI'''
    EMPTY_FIELD = ' '
    MARK_X = f'{TColor.OKBLUE}x{TColor.ENDC}'
    MARK_O = f'{TColor.FAIL}o{TColor.ENDC}'
    SEPARATOR_LINE = '═══╬═══╬═══'
    VERTICAL_PIPE = '║'

    def __init__(self):
        self.msg=''
        self.gameboard = [self.EMPTY_FIELD for x in range(9) ]
        self.player_mark=self.MARK_X
        self.computer_mark=self.MARK_O
        self.end_of_game = False

    def new_game(self):
        '''Start a new game'''
        self.msg=''
        self.gameboard = [self.EMPTY_FIELD for x in range(9) ]
        self.player_mark=self.MARK_X
        self.computer_mark=self.MARK_O
        self.end_of_game=False
        self.print_screen()

    def print_screen(self):
        '''Print gamescreen to terminal'''
        os.system('clear')
        self.print_board(self.gameboard)
        self.user_consol()

    def print_board(self, board):
        '''Print a board on the screen'''
        for i in range(3):
            for j in range(3):
                print(f' {board[i*3+j]} ', end='')
                if j<2:
                    print(self.VERTICAL_PIPE, end='')
            if i<2:
                print('\n'+self.SEPARATOR_LINE)
        print('')

    def user_consol(self):
        '''Print user consol and handle user inputs'''
        print(' Help '.center(60, '-'))
        self.print_board(range(1,10))
        print(' User consol '.center(60, '-'))

        print(self.msg)
        if self.end_of_game:
            command=input('\nWould you like to play new game?')
        else:
            command=input('\nWhere would you like place a mark (1-9)?')
        self.msg=''

        try:
            if self.end_of_game and command in ('y', 'yes'):
                self.new_game()
            elif self.end_of_game and command in ('n', 'no'):
                return
            elif command ==  'q':
                return
            elif 0 < int(command) < 10:
                if self.gameboard[int(command)-1] != self.EMPTY_FIELD:
                    self.msg='This field is already taken, select another one!'
                else:
                    self.place_a_mark(int(command)-1, self.player_mark)
                    if not self.end_of_game:
                        self.answer_step()
            else:
                self.msg='Number must be between 1-9!'
        except ValueError:
            self.msg=TColor.FAIL+'There is no such parameter'+TColor.ENDC

        self.print_screen()

    def place_a_mark(self, place, mark):
        '''Place a mark on the board'''
        self.gameboard[place]=mark
        self.check_end_of_game(place)

    def check_end_of_game(self, last_step):
        '''Check if there is any possible step or one of players has won already'''
        paths=self.get_all_path()
        paths = [path for path in paths if last_step in path]
        for path in paths:
            line_items=set()
            for i in path:
                line_items.add(self.gameboard[i])

            if len(line_items)==1:
                self.end_of_game=True
                if self.gameboard[last_step]==self.player_mark:
                    self.msg='Player won this game!'
                else:
                    self.msg='Computer won this game!'
                break

        if self.gameboard.count(self.EMPTY_FIELD)==0:
            self.end_of_game=True
            self.msg='There are no possible moves. It is a TIE!'

    def check_row_sum(self, i, check_value):
        '''Check and compare summary of a row values
        - Empty fields count as 0
        - Computer marks count as 1
        - Player marks count as -1'''
        check_sum = 0
        possible_answer = ''
        for j in range(3):
            if self.gameboard[i*3 + j]==self.computer_mark:
                check_sum +=1
            elif self.gameboard[i*3 + j]==self.player_mark:
                check_sum -=1
            else:
                possible_answer = i*3 + j

        if check_sum == check_value:
            return possible_answer
        else:
            return -1

    def check_column_sum(self, i, check_value):
        '''Check and compare summary of a column values
        - Empty fields count as 0
        - Computer marks count as 1
        - Player marks count as -1'''
        check_sum = 0
        possible_answer = ''
        for j in range(3):
            if self.gameboard[j*3 + i]==self.computer_mark:
                check_sum +=1
            elif self.gameboard[j*3 + i]==self.player_mark:
                check_sum -=1
            else:
                possible_answer = j*3 + i

        if check_sum == check_value:
            return possible_answer
        else:
            return -1

    def check_diagonal_sum(self, checkvalue):
        '''Check and compare summary of diagonal values
        - Empty fields count as 0
        - Computer marks count as 1
        - Player marks count as -1'''
        check_sum_main_diagonal = 0
        possible_answer_main_diagonal = ''
        check_sum_antidiagonal = 0
        possible_answer_antidiagonal = ''
        for i in range(3):
            if self.gameboard[i*3 + i]==self.computer_mark:
                check_sum_main_diagonal +=1
            elif self.gameboard[i*3 + i]==self.player_mark:
                check_sum_main_diagonal -=1
            else:
                possible_answer_main_diagonal = i*3 + i

            if self.gameboard[i*3 + 2 - i]==self.computer_mark:
                check_sum_antidiagonal +=1
            elif self.gameboard[i*3 + 2 - i]==self.player_mark:
                check_sum_antidiagonal -=1
            else:
                possible_answer_antidiagonal = i*3 + 2 - i

        if check_sum_main_diagonal==checkvalue:
            return possible_answer_main_diagonal

        if check_sum_antidiagonal==checkvalue:
            return possible_answer_antidiagonal

        return -1

    def get_winning_step(self):
        '''Check if there is a winning position'''
        for i in range(3):
            possible_answer_row = self.check_row_sum(i, 2)
            if possible_answer_row!=-1:
                return possible_answer_row

            possible_answer_col = self.check_column_sum(i, 2)
            if possible_answer_col!=-1:
                return possible_answer_col

        possible_answer_diagonal=self.check_diagonal_sum(2)
        if possible_answer_diagonal!=-1:
            return possible_answer_diagonal

        return -1

    def get_blocking_step(self):
        '''Check if there is a winning position for the opponent'''
        for i in range(3):
            possible_answer_row = self.check_row_sum(i, -2)
            if possible_answer_row!=-1:
                return possible_answer_row

            possible_answer_col = self.check_column_sum(i, -2)
            if possible_answer_col!=-1:
                return possible_answer_col

        possible_answer_diagonal=self.check_diagonal_sum(-2)
        if possible_answer_diagonal!=-1:
            return possible_answer_diagonal

        return -1

    def get_all_path(self):
        '''Return all possible indexes for possible wins of the game'''
        rows = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        cols = [[0, 3, 6], [1, 4, 7], [2, 5, 8]]
        diags = [[0, 4, 8], [2, 4, 6]]
        paths = rows + cols + diags

        return paths

    def get_possible_winning_paths(self, player_mark):
        '''Return remaining possible winning paths that does not
        contaion opponents mark'''
        paths = self.get_all_path()

        for key, value in enumerate(self.gameboard):
            if value!=player_mark and value!=self.EMPTY_FIELD:
                paths = [path for path in paths if key not in path]

        return paths

    def get_possible_forking_paths(self, player_mark):
        '''Return the remaining possible winning paths, 
        that already contains the players mark'''
        paths = self.get_possible_winning_paths(player_mark)
        possible_paths = []

        for path in paths:
            for i in path:
                if self.gameboard[i]==player_mark:
                    possible_paths.append(path)
                    break

        return possible_paths

    def get_forking_step(self):
        '''Check if there is position that provides 
        two possible way to win'''
        possible_paths=self.get_possible_forking_paths(self.computer_mark)
        for key, value in enumerate(self.gameboard):
            if value==self.EMPTY_FIELD:
                count = sum(1 for path in possible_paths if key in path)
                if count > 1:
                    return key
        return -1

    def get_block_fork_step(self):
        '''Check if there is position that provides 
        two possible way to win for the opponent'''
        possible_paths=self.get_possible_forking_paths(self.player_mark)

        for key, value in enumerate(self.gameboard):
            if value==self.EMPTY_FIELD:
                count = sum(1 for path in possible_paths if key in path)
                if count > 1:
                    return key
        return -1

    def get_center_step(self):
        '''Check if the center field is empty'''
        if self.gameboard[4] == self.EMPTY_FIELD:
            return 4
        else:
            return -1

    def get_opposite_corner_step(self):
        '''Check if only one of the corners is taken by the opponent
        and get the index of the opposite corner'''
        corners = (0, 2, 6, 8)
        corner_dictionary = {0:8, 2:6, 6:2, 8:0}
        possible_corner_answer = -1
        corner_sum=0
        for i in corners:
            if self.gameboard[i]==self.player_mark:
                corner_sum -=1
                possible_corner_answer=i
            elif self.gameboard[i]==self.computer_mark:
                return -1

        if corner_sum==-1:
            return corner_dictionary[possible_corner_answer]

        return -1

    def get_random_corner_step(self):
        '''Get random empty corner field'''
        possible_corners=[]
        corners = (0, 2, 6, 8)
        for i in corners:
            if self.gameboard[i]==self.EMPTY_FIELD:
                possible_corners.append(i)

        if len(possible_corners) > 0:
            return random.choice(possible_corners)

        return -1

    def get_random_side_step(self):
        '''Get random side field'''
        possible_sides=[]
        sides = (1, 3, 5, 7)
        for i in sides:
            if self.gameboard[i]==self.EMPTY_FIELD:
                possible_sides.append(i)

        if len(possible_sides) > 0:
            return random.choice(possible_sides)

        return -1

    def get_strategy(self, strategy):
        '''Strategy steps by Newell, A., & Simon, H. A. (1972).'''
        strategy_suggested_step=-1

        match strategy:
            case 0:
                strategy_suggested_step=self.get_winning_step()
            case 1:
                strategy_suggested_step=self.get_blocking_step()
            case 2:
                strategy_suggested_step=self.get_forking_step()
            case 3:
                strategy_suggested_step=self.get_block_fork_step()
            case 4:
                strategy_suggested_step=self.get_center_step()
            case 5:
                strategy_suggested_step=self.get_opposite_corner_step()
            case 6:
                strategy_suggested_step=self.get_random_corner_step()
            case 7:
                strategy_suggested_step=self.get_random_side_step()
            case _:
                strategy_suggested_step=-1

        return strategy_suggested_step

    def answer_step(self):
        '''Check the strategy options one by one and select the first available'''
        for i in range(8):
            next_step = self.get_strategy(i)
            if next_step != -1:
                self.place_a_mark(next_step, self.computer_mark)
                break

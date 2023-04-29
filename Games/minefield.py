'''Terminal based Minesweeper game'''
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

class Minesweeper():
    '''Classic Minesweeper game implementation with TUI'''

    class Field():
        '''Field of mines that needs to be explored'''
        class Cell():
            '''Cell object on the minefiled, thats value can be covered and/or flagged'''
            def __init__(self, value, covered=True, flagged=False):
                self.value=value
                self.covered=covered
                self.flagged=flagged

            def cheat_display(self):
                '''Alternative __str__ function to display all the fields with admin rights'''
                if self.value=='*':
                    return TColor.FAIL + self.value + TColor.ENDC
                return self.value

            def __str__(self):
                cell_display=''
                if self.flagged:
                    cell_display = TColor.BOLD + 'F' + TColor.ENDC
                elif self.covered:
                    cell_display = '?'
                elif self.value=='*':
                    cell_display = TColor.FAIL + self.value + TColor.ENDC
                elif self.value==0:
                    cell_display = '.'
                elif self.value==1:
                    cell_display = TColor.OKBLUE + str(self.value) + TColor.ENDC
                elif self.value==2:
                    cell_display = TColor.OKGREEN + str(self.value) + TColor.ENDC
                elif self.value==3:
                    cell_display = TColor.OKCYAN + str(self.value) + TColor.ENDC
                else:
                    cell_display = TColor.WARNING + str(self.value) + TColor.ENDC
                return cell_display

            def switch_flag(self):
                '''Swith flag value on and off'''
                self.flagged = not self.flagged

        def __init__(self, field_width, field_height, num_of_mines):
            self.field_width=field_width
            self.field_height=field_height
            self.num_of_mines=num_of_mines
            self.mfield=[]
            self.generate_mfield()
            self.show_full_map=False

        def __str__(self):
            field_display=''
            for i in range(0, self.field_height):
                if i==0:
                    header1 = '    '
                    header2 = '    '
                    for j in range(0, self.field_width):
                        if j<10:
                            space_for_cols=' '
                        else:
                            space_for_cols=''
                        header1 += space_for_cols + str(j+1) + ' '
                        header2 += '---'
                    field_display += header1+'\n'+header2+'\n'

                if i<9:
                    space_for_rows=' '
                else:
                    space_for_rows=''

                field_display += f'{space_for_rows}{i+1} | '

                for j in range(0, self.field_width):
                    if self.show_full_map:
                        field_display += ' ' + str(self.mfield[i*self.field_width+j].cheat_display()) + ' '
                    else:
                        field_display += ' ' + str(self.mfield[i*self.field_width+j]) + ' '

                field_display += '\n'

            return field_display

        def generate_mfield(self):
            '''Generate the minefiled based on size and number of mines'''
            all_fields = self.field_height*self.field_width
            safe_fields = all_fields-self.num_of_mines
            raw_mfield = random.sample([0, '*'], counts=[safe_fields, self.num_of_mines], k=all_fields)
            self.mfield = list(map(lambda x: self.Cell(x), raw_mfield))

        def first_step_on_the_field(self, x, y):
            '''Make sure, that player will not blow up at first dig'''
            mine_cell_index= x + self.field_width * y
            if self.mfield[mine_cell_index].value=='*':
                safe_cell_list=[]
                for key, cell in enumerate(self.mfield):
                    if cell.value==0:
                        safe_cell_list.append(key)

                safe_cell_index=random.choice(safe_cell_list)

                self.mfield[safe_cell_index].value='*'
                self.mfield[mine_cell_index].value=0

            self.register_minefield()

        def register_minefield(self):
            '''Register the mines on the minefield'''
            for i in range(0, self.field_height):
                for j in range(0, self.field_width):
                    if self.mfield[i*self.field_width+j].value=='*':
                        self.register_mine(j, i)

        def register_mine(self, x,y):
            '''Update minefield cells around the mines'''
            for i in range(-1, 2):
                for j in range(-1, 2):
                    vector_index = ((y+i)*self.field_width)+(x+j)
                    if (-1<(x+j)<self.field_width and
                            -1<(y+i)<self.field_height and
                            self.mfield[vector_index].value!='*'):
                        self.mfield[vector_index].value = self.mfield[vector_index].value + 1

        def is_valid_cell(self, axis_x, axis_y):
            '''Check if the coordinates are within the minefield'''
            return -1<axis_x<self.field_width and -1<axis_y<self.field_height

        def get_cell(self, axis_x, axis_y):
            '''Get a cell by two dimensional address'''
            return self.mfield[axis_x + axis_y * self.field_width]

        def is_end_of_game(self):
            '''Check if the game is over already'''
            is_end_of_game=True
            for i in self.mfield:
                if i.covered and i.value != '*':
                    is_end_of_game=False
                    break

            return is_end_of_game

        def full_map_display(self):
            '''Display the whole map uncovered in admin mode and at the end of game'''
            self.show_full_map=True
            full_map = str(self)
            self.show_full_map=False
            return full_map

    def __init__(self):
        self.end_of_game = False
        self.chain = set()
        self.msg=''
        self.admin_mode=False
        self.game_board= ''
        self.first_guess=True

    def new_game(self, size='s', difficulty='e'):
        '''
        Start a preconfigured game, 
        the size of the field can be "S" (for small), "M" (for medium) or "L" (for large)
        the difficulty can be: "E" (for easy), "M" (for medium), or "H" (for hard)
        '''
        width=0
        height=0
        mines=0
        error=False
        if size.lower()=='s':
            width=10
            height=10
        elif size.lower()=='m':
            width=20
            height=20
        elif size.lower()=='l':
            width=30
            height=30
        else:
            error=True

        all_fields=width*height
        if difficulty.lower()=='e':
            mines=int(all_fields*0.1)
        elif difficulty.lower()=='m':
            mines=int(all_fields*0.2)
        elif difficulty.lower()=='h':
            mines=int(all_fields*0.3)
        else:
            error=True

        if error:
            print('Wrong parameters. For more information please check documentation.')
        else:
            self.new_custom_game(width, height, mines)

    def new_custom_game(self, field_width=10, field_height=10, num_of_mines=10):
        '''Start a new game'''
        if field_height<1 or field_height>50 or field_width<1 or field_width>50:
            print('Field size must be between 1 and 50')
        elif num_of_mines >= field_width*field_height or num_of_mines<1:
            print(f'Number of mines must be between: 1 and {field_width*field_height-1}')
        else:
            self.game_board=self.Field(field_width, field_height, num_of_mines)
            self.msg=''
            self.update_screen()

    def print_help(self):
        '''Print rules of the game for the user'''
        print(' Help '.center(60, '-'))
        print(f'- type "{TColor.OKBLUE}COLUMN,ROW{TColor.ENDC}" to check a cell')
        print(f'- type "{TColor.OKBLUE}COLUMN,ROW,F{TColor.ENDC}" to flag of unflag a cell')
        print(f'- type "{TColor.OKBLUE}Q{TColor.ENDC}" exit game and return to main screen')

    def update_screen(self):
        '''Draw the field and the user consol to the terminal sceen'''
        os.system('clear')

        if self.admin_mode or self.end_of_game:
            print(self.game_board.full_map_display())
            print()

        if not self.end_of_game:
            print(self.game_board)

        self.guess_consol()

    def guess_consol(self):
        '''Display of user consol and handling of input data'''
        if not self.end_of_game:
            self.print_help()

        print(' User consol '.center(60, '-'))
        print(f'\n {TColor.WARNING}{self.msg}{TColor.ENDC}')
        self.msg=''

        if not self.end_of_game:
            guess=input('What would you like to do? ')

            if guess.lower()=='q':
                self.end_of_game = True
            else:
                try:
                    guess_coords=guess.split(',')
                    if len(guess_coords)>2 and guess_coords[2].lower()=='f':
                        self.flag(int(guess_coords[0])-1, int(guess_coords[1])-1)
                    else:
                        if self.first_guess:
                            self.game_board.first_step_on_the_field(int(guess_coords[0])-1, int(guess_coords[1])-1)
                            self.first_guess=False
                        self.dig(int(guess_coords[0])-1, int(guess_coords[1])-1)
                    self.update_screen()
                except Exception as err:
                    self.msg=err
                    self.update_screen()

    def flag(self, x, y):
        '''"Flag or unflag a cell on the minefield'''
        if self.game_board.is_valid_cell(x, y):
            if not self.game_board.get_cell(x, y).covered:
                self.msg='You can not flag a discovered cell.'
            else:
                self.game_board.get_cell(x, y).switch_flag()
        else:
            self.msg="Try to guess within the field."

    def chain_reaction(self, x, y):
        '''Chain discover neighbour cells of empty cells'''
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (self.game_board.is_valid_cell(x+j, y+i) and
                        self.game_board.get_cell(x+j, y+i).value !='*' and
                        self.game_board.get_cell(x+j, y+i).covered):
                    self.game_board.get_cell(x+j, y+i).covered=False
                    if self.game_board.get_cell(x+j, y+i).value == 0:
                        self.chain.add((x+j, y+i))
        if len(self.chain)>0:
            empty_cell=self.chain.pop()
            self.chain_reaction(empty_cell[0], empty_cell[1])

    def dig(self, x, y):
        '''"Open a cell on the minefield'''
        if self.game_board.is_valid_cell(x, y):
            if self.game_board.get_cell(x, y).value=='*':
                self.msg=TColor.FAIL+"BOOM! You stepped on a mine!"+TColor.ENDC
                self.end_of_game=True
            elif not self.game_board.get_cell(x, y).covered:
                self.msg="You already checked this cell."
            elif self.game_board.get_cell(x, y).flagged:
                self.msg="First remove the flag from the cell."
            else:
                self.game_board.get_cell(x, y).covered = False
                if self.game_board.get_cell(x, y).value == 0:
                    self.chain_reaction(x, y)
        else:
            self.msg="Try to guess within the field."

        if self.game_board.is_end_of_game():
            self.msg="You found all the mines. You WON!"
            self.end_of_game=True

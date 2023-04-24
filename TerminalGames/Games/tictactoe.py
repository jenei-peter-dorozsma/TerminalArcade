import random
import os
from Games.Assets.terminalColors import TColor

class TicTacToe:
    EMPTY_FIELD = ' '
    MARK_X = f'{TColor.OKBLUE}x{TColor.ENDC}'
    MARK_O = f'{TColor.FAIL}o{TColor.ENDC}'
    SEPARATOR_LINE = '═══╬═══╬═══'
    VERTICAL_PIPE = '║'

    def __init__(self):
        self.msg=''
        self.gameboard = [self.EMPTY_FIELD for x in range(10) ]
        self.player_mark=self.MARK_X
        self.computer_mark=self.MARK_O

    def new_game(self):
        self.print_screen()
        self.player_mark=self.MARK_X
        self.computer_mark=self.MARK_O

    def print_screen(self):
        '''Print gamescreen to terminal'''
        os.system('clear')
        self.print_board()
        self.user_consol()

    def print_board(self):
        for i in range(3):
            for j in range(3):
                print(f' {self.gameboard[i*3+j]} ', end='')
                if j<2:
                    print(self.VERTICAL_PIPE, end='')
            if i<2:
                print('\n'+self.SEPARATOR_LINE)
        print('')

    def user_consol(self):
        print(' User consol '.center(60, '-'))
        # self.print_throw()

        print(self.msg)
        command=input('\nWhere would you like place a mark (1-9)?')
        self.msg=''

        try:
            if command ==  'q':
                exit(0)
            if 0 < int(command) < 10:
                if self.gameboard[int(command)-1] != self.EMPTY_FIELD:
                    self.msg="This field is already taken, select another one!"
                else:
                    self.place_a_mark(int(command)-1, self.player_mark)
                    # self.answer_step()
            else:
                self.msg="Number must be between 1-9!"
        except ValueError:
            self.msg=TColor.FAIL+'There is no such parameter'+TColor.ENDC

        self.print_screen()

    def place_a_mark(self, place, mark):
        self.gameboard[place]=mark

    def get_winning_step(self):
        check_sum_main_diagonal = 0
        possible_answer_main_diagonal = ''
        check_sum_antidiagonal = 0
        possible_answer_antidiagonal = ''
        for i in range(3):
            check_sum_row = 0
            check_sum_col = 0
            possible_answer_row = ''
            possible_answer_col = ''
            for j in range(3):
                if self.gameboard[i*3 + j]==self.computer_mark:
                    check_sum_row +=1
                elif self.gameboard[i*3 + j]==self.player_mark:
                    check_sum_row -=1
                else:
                    possible_answer_row = i*3 + j

                if self.gameboard[j*3 + i]==self.computer_mark:
                    check_sum_col +=1
                elif self.gameboard[j*3 + i]==self.player_mark:
                    check_sum_col -=1
                else:
                    possible_answer_col = j*3 + i

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

            if check_sum_row==2:
                return possible_answer_row

            if check_sum_col==2:
                return possible_answer_col

        if check_sum_main_diagonal==2:
            return possible_answer_main_diagonal

        if check_sum_antidiagonal==2:
            return possible_answer_antidiagonal

        return -1

    def get_blocking_step(self):
        return -1

    def get_forking_step(self):
        return -1

    def get_block_fork_step(self):
        return -1

    def get_center_step(self):
        if self.gameboard[4] == self.EMPTY_FIELD:
            return 4
        else:
            return -1

    def get_oposite_corner_step(self):
        return -1

    def get_random_corner_step(self):
        return -1

    def get_random_side_step(self):
        return -1

    def get_strategy(self, strategy):
        match strategy:
            case 0:
                return self.get_winning_step()
            case 1:
                return self.get_blocking_step()
            case 2:
                return self.get_forking_step()
            case 3:
                return self.get_block_fork_step()
            case 4:
                return self.get_center_step()
            case 5:
                return self.get_oposite_corner_step()
            case 6:
                return self.get_random_corner_step()
            case 7:
                return self.get_random_side_step()
            case _:
                return 0

    def answer_step(self):
        for i in range(8):
            next_step = self.get_strategy(i)
            if next_step != -1:
                self.place_a_mark(next_step, self.computer_mark)
                break

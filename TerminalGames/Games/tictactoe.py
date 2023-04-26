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
        self.gameboard = [self.EMPTY_FIELD for x in range(9) ]
        self.player_mark=self.MARK_X
        self.computer_mark=self.MARK_O
        self.end_of_game = False

    def new_game(self):
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
        for i in range(3):
            for j in range(3):
                print(f' {board[i*3+j]} ', end='')
                if j<2:
                    print(self.VERTICAL_PIPE, end='')
            if i<2:
                print('\n'+self.SEPARATOR_LINE)
        print('')

    def user_consol(self):
        print(' Help '.center(60, '-'))
        self.print_board(range(1,10))
        # print('Gameboard:')
        # print(self.gameboard)
        # print('Empty fields:')
        # print(self.gameboard.count(self.EMPTY_FIELD))
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
                exit(0)
            elif command ==  'q':
                exit(0)
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
        self.gameboard[place]=mark
        self.check_end_of_game(place)

    def check_end_of_game(self, last_step):
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

        if check_sum_main_diagonal==2:
            return possible_answer_main_diagonal

        if check_sum_antidiagonal==2:
            return possible_answer_antidiagonal

        return -1

    def get_winning_step(self):
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
        rows = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        cols = [[0, 3, 6], [1, 4, 7], [2, 5, 8]]
        diags = [[0, 4, 8], [2, 4, 6]]
        paths = rows + cols + diags

        return paths

    def get_possible_winning_paths(self, player_mark):
        paths = self.get_all_path()

        for key, value in enumerate(self.gameboard):
            if value!=player_mark and value!=self.EMPTY_FIELD:
                paths = [path for path in paths if key not in path]

        return paths

    def get_possible_forking_paths(self, player_mark):
        paths = self.get_possible_winning_paths(player_mark)
        possible_paths = []

        for path in paths:
            for i in path:
                if self.gameboard[i]==player_mark:
                    possible_paths.append(path)
                    break

        return possible_paths

    def get_forking_step(self):
        possible_paths=self.get_possible_forking_paths(self.computer_mark)
        for key, value in enumerate(self.gameboard):
            if value==self.EMPTY_FIELD:
                count = sum(1 for path in possible_paths if key in path)
                if count > 1:
                    return key
        return -1

    def get_block_fork_step(self):
        possible_paths=self.get_possible_forking_paths(self.player_mark)

        for key, value in enumerate(self.gameboard):
            if value==self.EMPTY_FIELD:
                count = sum(1 for path in possible_paths if key in path)
                if count > 1:
                    return key
        return -1

    def get_center_step(self):
        if self.gameboard[4] == self.EMPTY_FIELD:
            return 4
        else:
            return -1

    def get_opposite_corner_step(self):
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
        possible_corners=[]
        corners = (0, 2, 6, 8)
        for i in corners:
            if self.gameboard[i]==self.EMPTY_FIELD:
                possible_corners.append(i)

        if len(possible_corners) > 0:
            return random.choice(possible_corners)

        return -1

    def get_random_side_step(self):
        possible_sides=[]
        sides = (1, 3, 5, 7)
        for i in sides:
            if self.gameboard[i]==self.EMPTY_FIELD:
                possible_sides.append(i)

        if len(possible_sides) > 0:
            return random.choice(possible_sides)

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
                return self.get_opposite_corner_step()
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

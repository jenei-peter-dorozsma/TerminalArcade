import os, random
from Games.Assets.terminalColors import TColor
import Games.Assets.diceArt as da

class Yahtzee:
    ALPHABET = ['a', 'b', 'c', 'd', 'e']

    def __init__(self):
        self.score_board={}
        self.remaining_rolls=0
        self.re_rolls=0
        self.latest_throw=[]
        self.dice_locks=[0, 0, 0, 0, 0]
        self.msg=''

    def reset_score_board(self):
        '''Reset game paramteres for next round'''
        self.score_board={
            '1s':'-',
            '2s':'-',
            '3s':'-',
            '4s':'-',
            '5s':'-',
            '6s':'-',
            'One pair':'-',
            'Two pairs':'-',
            'Three of a kind':'-',
            'Four of a kind':'-',
            'Full house':'-',
            'Small strait':'-',
            'Large strait':'-',
            'Five of a kind':'-',
            'Joker':'-'
        }
        self.remaining_rolls=15
        self.re_rolls=2
        self.latest_throw=[]
        self.dice_locks=[0, 0, 0, 0, 0]

    def print_screen(self):
        '''Print gamescreen to terminal'''
        os.system('clear')

        self.print_score_board()
        self.print_help()
        self.user_consol()

    def print_score_board(self):
        '''Print actual status of the scoreboard'''
        print(' Score board '.center(60, '-'))
        print('')

        total_score=0
        left_column=True
        item_index=0

        for slot, score in self.score_board.items():
            item_index += 1

            if left_column:
                print(f'{item_index}) {TColor.BOLD}{slot}:{TColor.ENDC} {score}'.ljust(40, ' '), end='')
                left_column=not left_column
            else:
                print(f'{item_index}) {TColor.BOLD}{slot}:{TColor.ENDC} {score}'.ljust(20, ' '))
                left_column=not left_column

            if not score=='-':
                total_score += score

        print('')
        print(' Status '.center(60, '-'))
        print(f'Turns left: {self.remaining_rolls}'.ljust(30, ' '), end='')
        print(f'Rerolls left: {self.re_rolls}'.ljust(30, ' '))
        print(f'\n{TColor.OKGREEN}{TColor.BOLD}Total score: {total_score}{TColor.ENDC}{TColor.ENDC}')

    def user_consol(self):
        '''Print user consol and handle user inputs'''
        print(' User consol '.center(60, '-'))
        self.print_throw()

        print(self.msg)
        command=input('\nWhat would you like to do?')

        try:
            if command.lower() == 'q':
                return 0
            if command.lower() == 'r':
                if not self.latest_throw == []:
                    self.msg=TColor.WARNING+'Save your throw before next turn.'+TColor.ENDC
                elif self.remaining_rolls==0:
                    self.msg=TColor.WARNING+'End of game.'+TColor.ENDC
                else:
                    self.throw_full()
            elif command.lower() == 'rr':
                if self.latest_throw == []:
                    self.msg=TColor.WARNING+'No dice on the tabe. First throw one'+TColor.ENDC
                elif self.re_rolls==0:
                    self.msg=TColor.WARNING+'You can not reroll in this turn.'+TColor.ENDC
                else:
                    self.reroll()
            elif command.lower() in self.ALPHABET:
                if self.latest_throw == []:
                    self.msg=TColor.WARNING+'No dice on the table. First throw one.'+TColor.ENDC
                elif self.re_rolls==0:
                    self.msg=TColor.WARNING+'You can not reroll in this turn.'+TColor.ENDC
                else:
                    self.lock_die(command)
            elif int(command) in range(1, 16):
                self.save_combination(int(command)-1)
            else:
                self.msg=TColor.FAIL+'There is no such parameter'+TColor.ENDC
        except ValueError:
            self.msg=TColor.FAIL+'There is no such parameter'+TColor.ENDC
        self.print_screen()

    def print_help(self):
        '''Print rules of the game for the user'''
        print(' Help '.center(60, '-'))
        print('- type R to start a new turn and roll full set of five dice')
        print('- type A-E to lock or unlock a dice')
        print('- type RR to reroll the unlocked dice')
        print('- type Q exit game and return to main screen')
        print('- type 1-15 save result as combination')

    def print_throw(self):
        '''Print faces of five dice'''
        if not self.latest_throw==[]:
            for row in range(0, da.DIE_HEIGHT):
                for index,value in enumerate(self.latest_throw):
                    if self.dice_locks[index]:
                        print(TColor.OKGREEN+da.DICE_ART[value][row]+TColor.ENDC, end='')
                    else:
                        print(da.DICE_ART[value][row], end='')
                print(da.DIE_FACE_SEPARATOR + '\n', end='')
            print(' A '.center(11, ' '), end='')
            print(' B '.center(11, ' '), end='')
            print(' C '.center(11, ' '), end='')
            print(' D '.center(11, ' '), end='')
            print(' E '.center(11, ' '), end='')
            print('')

    def throw_full(self):
        '''Throw with five dice'''
        self.remaining_rolls -= 1
        self.latest_throw = random.sample([1,2,3,4,5,6], counts=[5,5,5,5,5,5], k=5)
        self.dice_locks=[0, 0, 0, 0, 0]
        self.re_rolls=2

    def reroll(self):
        '''Reroll the unlocked dice'''
        self.re_rolls -= 1

        for key, value in enumerate(self.dice_locks):
            if value==0:
                rerolled_die=random.randint(1,6)
                self.latest_throw[key]=rerolled_die

    def save_combination(self, combination):
        '''Calculate and save combination value'''
        keys = list(self.score_board)
        if not self.score_board[keys[combination]] == '-':
            self.msg=TColor.WARNING+'You have already used this combination.'+TColor.ENDC
        else:
            combination_value=0
            if combination==0:
                combination_value=self.latest_throw.count(1)*1
            elif combination==1:
                combination_value=self.latest_throw.count(2)*2
            elif combination==2:
                combination_value=self.latest_throw.count(3)*3
            elif combination==3:
                combination_value=self.latest_throw.count(4)*4
            elif combination==4:
                combination_value=self.latest_throw.count(5)*5
            elif combination==5:
                combination_value=self.latest_throw.count(6)*6
            elif combination==6:
                for i in range(6, 1, -1):
                    if self.latest_throw.count(i) >= 2:
                        combination_value = i * 2
                        break
            elif combination==7:
                number_of_pairs = 0
                for i in range(6, 1, -1):
                    if self.latest_throw.count(i) >= 4:
                        number_of_pairs = 2
                        combination_value += i * 4
                        break
                    elif self.latest_throw.count(i) >= 2:
                        number_of_pairs += 1
                        combination_value += i * 2
                if not number_of_pairs==2:
                    combination_value=0
            elif combination==8:
                for i in range(6, 1, -1):
                    if self.latest_throw.count(i) >= 3:
                        combination_value = i * 3
                        break
            elif combination==9:
                for i in range(6, 1, -1):
                    if self.latest_throw.count(i) >= 4:
                        combination_value = i * 4
                        break
            elif combination==10:
                twos=False
                threes=False
                for i in range(6, 1, -1):
                    if self.latest_throw.count(i) == 2:
                        twos=True
                    elif self.latest_throw.count(i) == 3:
                        threes=True
                if twos and threes:
                    combination_value = sum(self.latest_throw)
            elif combination==11:
                list1=[3,4,5,6]
                list2=[2,3,4,5]
                list3=[1,2,3,4]

                if all(x in self.latest_throw for x in list1):
                    combination_value=sum(list1)
                elif all(x in self.latest_throw for x in list2):
                    combination_value=sum(list2)
                elif  all(x in self.latest_throw for x in list3):
                    combination_value=sum(list3)
            elif combination==12:
                list1=[1,2,3,4,5]
                list2=[2,3,4,5,6]
                self.latest_throw.sort()
                if self.latest_throw==list1 or self.latest_throw==list2:
                    combination_value = sum(self.latest_throw)
            elif combination==13:
                for i in range(6, 1, -1):
                    if self.latest_throw.count(i) == 5:
                        combination_value = i * 5
                        break
            elif combination==14:
                combination_value = sum(self.latest_throw)

            self.score_board[keys[combination]] = combination_value
            self.latest_throw=[]

    def lock_die(self, lock):
        '''Lock a die before reroll'''
        lock_index=self.ALPHABET.index(lock.lower())
        if self.dice_locks[lock_index]==1:
            self.dice_locks[lock_index]=0
        else:
            self.dice_locks[lock_index]=1

    def new_game(self):
        '''Start a new game'''
        self.reset_score_board()
        self.print_screen()

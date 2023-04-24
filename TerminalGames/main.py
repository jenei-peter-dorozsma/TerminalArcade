from Games import minefield, yahtzee, tictactoe

if __name__ == "__main__":
    # GAME 1
    # game=minefield.Minesweeper()
    # # game.admin_mode=True
    # game.new_game('s', 'e')

    # GAME 2
    # game = yahtzee.Yahtzee()
    # game.new_game()

    # GAME 3
    game = tictactoe.TicTacToe()
    game.new_game()
    

    # gameboard = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # for i in range(3):
    #     for j in range(3):
    #         print(f'{gameboard[i*3+j]} ', end='')
    #     print('')

    # print('')

    # for i in range(3):
    #     for j in range(3):
    #         print(f'{gameboard[j*3+i]} ', end='')
    #     print('')

    print('success')

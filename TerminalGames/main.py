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

    print('success')

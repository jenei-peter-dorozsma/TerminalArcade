from Games import minefield, yahtzee

if __name__ == "__main__":
    game = yahtzee.Yahtzee()
    game.new_game()

    # game=minefield.Minesweeper()
    # # game.admin_mode=True
    # game.new_game('s', 'e')

    print('success')

# TODO:
# - automated tests
# - github
# - create a GUI for it

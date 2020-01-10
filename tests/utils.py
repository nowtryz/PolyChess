from game import Game
from colors import BLACK, WHITE
from pieces import King


def clean_board():
    """
    Create a clean chess board whit only kings
    """
    game = Game()
    for color in [BLACK, WHITE]:
        [p.die() for p in game.board.living_pieces[color].copy() if not isinstance(p, King)]
    return game
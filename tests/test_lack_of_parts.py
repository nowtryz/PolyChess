import unittest

from colors import BLACK, WHITE
from game import Game
from pieces import King, Bishop, Knight


def clean_board():
    game = Game()
    for color in [BLACK, WHITE]:
        [p.die() for p in game.board.living_pieces[color].copy() if not isinstance(p, King)]
    return game


class TestLackOfParts(unittest.TestCase):

    def test_lack_of_parts_king_vs_king(self):
        game = clean_board()
        self.assertTrue(game.lack_of_pieces())

    def test_lack_of_parts_king_bishop_vs_king(self):
        game = clean_board()
        game.board.create(Bishop, (0, 0), WHITE)
        self.assertTrue(game.lack_of_pieces())

    def test_lack_of_parts_king_bishop_vs_king_bishop(self):
        game = clean_board()
        game.board.create(Bishop, (0, 0), WHITE)
        game.board.create(Bishop, (2, 0), BLACK)
        self.assertTrue(game.lack_of_pieces())

    def test_lack_of_parts_king_knight_vs_king(self):
        game = clean_board()
        game.board.create(Knight, (0, 0), WHITE)
        self.assertTrue(game.lack_of_pieces())


if __name__ == '__main__':
    unittest.main()

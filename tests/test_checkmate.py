import unittest

from game import Game
from colors import BLACK, WHITE
from pieces import Rook, Queen
from utils import clean_board


class TestCheckmate(unittest.TestCase):

    def test_ladder_checkmate(self):
        game = clean_board()
        game.board.create(Rook, (0, 1), WHITE)
        game.board.create(Rook, (1, 0), WHITE)
        game.display.display_board()
        game.player = BLACK
        self.assertTrue(game.is_checkmate())

    def test_kiss_of_death(self):
        game = clean_board()
        game.board.kings[WHITE].move_to((2, 2))
        game.board.kings[BLACK].move_to((0, 0))
        game.board.create(Queen, (1, 1), WHITE)
        game.display.display_board()
        game.player = BLACK
        self.assertTrue(game.is_checkmate())

    def test_shepherd_mate(self):
        game = Game()
        game.board.grid[0,1].move_to((4, 3))
        game.board.grid[1,4].move_to((3, 4))
        game.board.grid[6,4].move_to((4, 4))
        game.board.grid[7,5].move_to((4, 2))
        game.board.grid[7,3].move_to((1, 5))
        game.display.display_board()
        game.player = BLACK
        self.assertTrue(game.is_checkmate())


if __name__ == '__main__':
    unittest.main()

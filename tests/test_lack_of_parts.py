import unittest

from colors import BLACK, WHITE
from pieces import Bishop, Knight
from utils import clean_board


class TestLackOfParts(unittest.TestCase):

    def test_lack_of_parts_king_vs_king(self):
        game = clean_board()
        game.display()
        self.assertTrue(game.lack_of_pieces())

    def test_lack_of_parts_king_bishop_vs_king(self):
        game = clean_board()
        game.board.create(Bishop, (0, 0), WHITE)
        game.display()
        self.assertTrue(game.lack_of_pieces())

    def test_lack_of_parts_king_bishop_vs_king_bishop_same_color(self):
        game = clean_board()
        game.board.create(Bishop, (0, 0), WHITE)
        game.board.create(Bishop, (2, 0), BLACK)
        game.display()
        self.assertTrue(game.lack_of_pieces())

    def test_lack_of_parts_king_bishop_vs_king_bishop_diff_color(self):
        game = clean_board()
        game.board.create(Bishop, (0, 0), WHITE)
        game.board.create(Bishop, (1, 0), BLACK)
        game.display()
        self.assertFalse(game.lack_of_pieces())

    def test_lack_of_parts_king_knight_vs_king(self):
        game = clean_board()
        game.board.create(Knight, (0, 0), WHITE)
        game.display()
        self.assertTrue(game.lack_of_pieces())

    def test_lack_of_parts_other(self):
        game = clean_board()
        game.board.create(Bishop, (0, 0), WHITE)
        game.board.create(Knight, (3, 5), WHITE)
        game.display()
        self.assertFalse(game.lack_of_pieces())


if __name__ == '__main__':
    unittest.main()

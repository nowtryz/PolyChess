import numpy as np

from colors import WHITE, BLACK
from Config import DISPLAY_CONF
from pieces import Piece, Pawn, Rook, Bishop, Knight, Queen, King


class Board:
    """
    The class manage piece positions, alive pieces and dead ones.
    """

    def __init__(self):
        """
        Initialize the class

        """

        self.grid = np.empty((8, 8), dtype=Piece)
        """Matrix containing the boxes of the board and the piece for each of them"""
        self.living_pieces = {
            BLACK: [],
            WHITE: []
        }
        """A dict of living pieces, subscript with either BLACK or WHITE to get alive pieces of the specified color"""
        self.dead_pieces = {
            BLACK: [],
            WHITE: []
        }
        """A dict of dead pieces, subscript with either BLACK or WHITE to get dead pieces of the specified color"""
        self.check = None
        """The color in check, None if neither are check"""
        self.kings = {
            BLACK: None,
            WHITE: None
        }
        """A dict containing the king of each color"""
        self._place_pieces()

    def _place_pieces(self):
        """
        Place pieces to their initial position
        """

        self._place_type(Pawn, range(8), (1, 6))
        self._place_type(Rook, [0, 7])
        self._place_type(Knight, [1, 6])
        self._place_type(Bishop, [2, 5])
        self._place_type(Queen, [3])
        self._place_kings()

    def _place_type(self, piece_type, places, rows=(0, 7)):
        """
        Place a specific type of pieces to their positions
        :param piece_type: The class of the piece to place, a class that extends Piece
        :param places: a tuple or a list containing all columns where would be places pieces
        :param rows: a two value tuple (black row, white row), defaults to (0, 7) which is the th row of Rooks etc...
        """

        for i in places:
            for row, color in zip(rows, (BLACK, WHITE)):
                pos = (row, i)
                piece = piece_type(self, pos, color, DISPLAY_CONF[piece_type][color])
                self.living_pieces[color].append(piece)
                self.grid[pos] = piece

    def _place_kings(self):
        """
        Place kings for each color and fill kings property
        """

        for row, color in zip((0, 7), (BLACK, WHITE)):
            pos = (row, 4)
            king = King(self, pos, color, DISPLAY_CONF[King][color])
            self.living_pieces[color].append(king)
            self.grid[pos] = king
            self.kings[color] = king

    def piece_died(self, piece: Piece):
        """Notify the board that a piece died

        the piece is hence removed from the board and living pieces to be added to
        dead pieces list
        :param piece:
        :type piece: Piece
        """

        self.living_pieces[piece.color].remove(piece)
        self.dead_pieces[piece.color].append(piece)
        self.grid[piece.position] = None

    def move_piece(self, piece: Piece, new_position):
        """Move a piece

        If there is a piece at the selected position, it will be killed and replaced by the given piece
        :param piece: the piece to move
        :param new_position: the new position of the piece
        """

        if self.grid[new_position] is not None:
            self.grid[new_position].die()
        self.grid[piece.position] = None
        self.grid[new_position] = piece
        piece.position = new_position

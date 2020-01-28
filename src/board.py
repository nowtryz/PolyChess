from typing import Dict, List, Any

import numpy as np

from Config import get_conf
from colors import WHITE, BLACK
from pieces import Piece, Pawn, Rook, Bishop, Knight, Queen, King


class Board:
    """
    The class manage piece positions, alive pieces and dead ones.
    """

    def __init__(self, game):
        """
        Initialize the class

        """

        self.game = game
        """Game instance"""
        self.grid = np.empty((8, 8), dtype=Piece)
        """Matrix containing the boxes of the board and the piece for each of them"""
        self.living_pieces: Dict[Any, List[Piece]] = {
            BLACK: [],
            WHITE: []
        }
        """A dict of living pieces, subscript with either BLACK or WHITE to get alive pieces of the specified color"""
        self.dead_pieces: Dict[Any, List[Piece]] = {
            BLACK: [],
            WHITE: []
        }
        """A dict of dead pieces, subscript with either BLACK or WHITE to get dead pieces of the specified color"""
        self.check = None
        """The color in check, None if neither are check"""
        self.kings: Dict[Any, Piece] = {}
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
                self.create(piece_type, (row, i), color)

    def _place_kings(self):
        """
        Place kings for each color and fill kings property
        """

        for row, color in zip((0, 7), (BLACK, WHITE)):
            pos = (row, 4)
            king = King(self, pos, color, get_conf()[King][color])
            self.living_pieces[color].append(king)
            self.grid[pos] = king
            self.kings[color] = king

    def create(self, piece_type, position, color):
        """
        Creates a piece at a given position
        :param piece_type: the class of the piece to create
        :param position: the position to place the piece
        :param color: the color of the piece, either `BLACK` or `WHITE`
        :return: Return the created piece
        :rtype: The type given in parameter
        """
        piece = piece_type(self, position, color, get_conf()[piece_type][color])
        self.living_pieces[color].append(piece)
        self.grid[position] = piece
        return piece

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

    def __getitem__(self, position):
        """
        Get a piece from the grid
        :param position: the coordinates of the item on the grid
        :return: the item at the specified position
        """
        return self.grid[position]

    def __setitem__(self, position, piece):
        """
        Set the piece at the specified position of the grid
        :param position: the position on the grid
        :param piece: the piece to put instead
        """
        self.grid[position] = piece

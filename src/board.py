import numpy as np

from Config import WHITE, BLACK, DISPLAY_CONF
from pieces import Piece, Pawn, Rook, Bishop, Knight, Queen, King


class Board:
    def __init__(self):
        self.grid = np.empty((8, 8), dtype=Piece)
        self.living_pieces = {
            BLACK: [],
            WHITE: []
        }
        self.dead_pieces = {
            BLACK: [],
            WHITE: []
        }
        self._place_pieces()

    def _place_pieces(self):
        self._place_type(Pawn, range(8), (1, 6))
        self._place_type(Rook, [0, 7])
        self._place_type(Knight, [1, 6])
        self._place_type(Bishop, [2, 5])
        self._place_type(Queen, [3])
        self._place_type(King, [4])

    def _place_type(self, piece_type, places, rows=(0, 7)):
        for i in places:
            black_pos = (rows[0], i)
            black = piece_type(self, black_pos, BLACK, DISPLAY_CONF[piece_type][BLACK])
            self.living_pieces[BLACK].append(black)
            self.grid[black_pos] = black

            white_pos = (rows[1], i)
            white = piece_type(self, white_pos, WHITE, DISPLAY_CONF[piece_type][WHITE])
            self.living_pieces[WHITE].append(white)
            self.grid[white_pos] = white

    def piece_died(self, piece: Piece):
        self.living_pieces[piece.color].remove(piece)
        self.dead_pieces[piece.color].append(piece)
        self.grid[piece.position] = None

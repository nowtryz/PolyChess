from colors import WHITE, BLACK
import numpy as np


class Piece:
    """
    Abstract class implementation for pieces
    """

    def __init__(self, board, position, color, character):
        """
        Initialise the piece
        :param board: the board of the game, used to manipulate positions
        :param position: the position of the piece
        :param color: the color of the piece, either BLACK or WHITE, imported from configurations
        :param character: the character to display for this piece
        """

        self.board = board
        self.alive = True
        self.position = position
        self.color = color
        self.character = character
        self.moves = 0

    def _clear_invalid_moves(self, input_moves):
        """
        Remove positions outside the board or positions held by a piece of the same color
        :param input_moves: Positions to check
        :return: a position list without invalid positions
        :rtype: list of tuple
        """
        moves = []
        for pos in input_moves:
            if 0 <= pos[0] < 8 and 0 <= pos[1] < 8:
                target = self.board.grid[pos]
                if target is None or target.color != self.color:
                    moves.append(pos)
        return moves

    def legal_moves(self):
        """
        Get moves where the piece can play
        :return: A list of coordinates where the piece can play
        :rtype: list of tuple
        """

        raise NotImplementedError()

    def can_play_at(self, position: tuple):
        """

        Check if this piece can play at the specified position
        :param position: the position to check
        :return: True if this piece can play at the specified position, False otherwise
        :rtype: bool
        """

        return position in self.legal_moves()

    def move_to(self, position):
        """
        Move the piece to the specified position on the board

        :param position: the new position
        """

        self.board.move_piece(self, position)
        self.moves += 1

    def die(self):
        """
        Kill the current piece
        """

        self.board.piece_died(self)
        self.alive = False

    def __repr__(self):
        return self.character

    @property
    def col(self):
        return self.position[1]

    @property
    def row(self):
        return self.position[0]

    @property
    def opponent(self):
        """
        Give the color of the opponent
        :return: the color of the opponent
        """
        if self.color == WHITE:
            return BLACK
        return WHITE


class Pawn(Piece):
    """
    The pawn piece
    """

    def __init__(self, board, position, color, character):
        super().__init__(board, position, color, character)

    def legal_moves(self):
        return []


class Knight(Piece):
    """
    The knight piece
    """

    def __init__(self, board, position, color, character):
        super().__init__(board, position, color, character)

    def legal_moves(self):
        return []


class Bishop(Piece):
    """
    The bishop piece
    """

    def __init__(self, board, position, color, character):
        super().__init__(board, position, color, character)

    def legal_moves(self):
        return []


class Rook(Piece):
    """
    The rook piece
    """

    def __init__(self, board, position, color, character):
        super().__init__(board, position, color, character)

    def legal_moves(self):
        return []


class Queen(Piece):
    """
    The queen piece
    """

    def __init__(self, board, position, color, character):
        super().__init__(board, position, color, character)

    def legal_moves(self):
        return []


class King(Piece):
    """
    The king piece
    """

    def __init__(self, board, position, color, character):
        super().__init__(board, position, color, character)

    def legal_moves(self):
        moves = []
        moves += zip(range(self.row - 1, self.row + 1), [self.col - 1] * 3)
        moves += [(self.row - 1, self.col), (self.row + 1, self.col)]
        moves += zip(range(self.row - 1, self.row + 1), [self.col + 1] * 3)

        # For Castling
        if self.moves == 0 and not self.board.check:
            left_rook = self.board.grid[self.row, 0]
            right_rook = self.board.grid[self.row, 7]

            if (
                    left_rook is not None
                    and left_rook.moves == 0
                    and self.board.grid[self.row, 1] is None
                    and self.board.grid[self.row, 2] is None
                    and self.board.grid[self.row, 3] is None
                    and np.all([not piece.can_play_at((self.row, 3))
                                for piece in self.board.living_pieces[self.opponent]])
            ):
                moves.append((self.row, 2))
            if (
                    right_rook is not None
                    and right_rook.moves == 0
                    and self.board.grid[self.row, 5] is None
                    and self.board.grid[self.row, 6] is None
                    and np.all([not piece.can_play_at((self.row, 5))
                                for piece in self.board.living_pieces[self.opponent]])
            ):
                moves.append((self.row, 6))

        return self._clear_invalid_moves(moves)

    def move_to(self, position):
        """
        Overrides default `move_to` to handle castling
        :param position: the new position
        """
        # For Castling
        if self.moves == 0 and position[0] == self.row:
            if position[1] == 6:
                rook = self.board.grid[self.row, 7]
                if rook is not None and rook.moves == 0:
                    rook.move_to((self.row, 5))
            elif position[0] == 2:
                rook = self.board.grid[self.row, 0]
                if rook is not None and rook.moves == 0:
                    rook.move_to((self.row, 3))

        # King move
        super().move_to(position)

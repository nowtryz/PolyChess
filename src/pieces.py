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
        self.pinned = False
        self.moves = 0
        self.last_move = 0

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

    def all_moves(self):
        """
        Get technically all coordinates where the piece can play from its current position without removing illegal ones
        :return: A list of coordinates the piece see
        :rtype: list of tuple
        """
        
        raise NotImplementedError()

    def legal_moves(self):
        """
        Get moves where the piece can play
        :return: A list of coordinates where the piece can play
        :rtype: list of tuple
        """

        return self._clear_invalid_moves(self.all_moves())

    def can_play_at(self, position: tuple):
        """
        Check if this piece can play at the specified position
        :param position: the position to check
        :return: True if this piece can play at the specified position, False otherwise
        :rtype: bool
        """

        return position in self.legal_moves()

    def can_capture_at(self, position: tuple):
        """
        Check if this piece can capture another piece at the specified position, it sightly differ from `can_play_at`
        for Pawns
        :param position: the position to check
        :return: True if this piece can play at the specified position, False otherwise
        :rtype: bool
        """

        return self.can_play_at(position)

    def move_to(self, position):
        """
        Move the piece to the specified position on the board

        :param position: the new position
        """

        self.board.move_piece(self, position)
        self.last_move = self.board.game.turn
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


class StraightMover(Piece):
    def _clear_invalid_directional_moves(self, directions):
        moves = []
        for direction in directions:
            for pos in direction:
                if self.board.grid[pos]:
                    if self.board.grid[pos].color != self.color:
                        moves.append(pos)
                    break
                moves.append(pos)
        # Here moves are already clean, so there is no need to call Piece._clear_invalid_moves
        return moves

    def get_directions(self):
        raise NotImplementedError()

    def all_moves(self):
        return sum(self.get_directions())

    def legal_moves(self):
        return self._clear_invalid_directional_moves(self.get_directions())

    def pin_targets(self):
        """
        Explore visible targets to pin them if their are hiding a king
        """
        for direction in self.get_directions():
            pinnable = None
            for pos in direction:
                p = self.board.grid[pos]
                if p:
                    # if first or second target has the same color -> cannot pin
                    if p.color == self.color:
                        break
                    # if the first target has the opponent's color, it may be a pinnable piece
                    elif pinnable is None:
                        if isinstance(p, King):
                            break
                        else:
                            pinnable = p
                    # if the second target is a king, pin last piece
                    elif isinstance(p, King):
                        pinnable.pinned = True
                    # if the second target is not a king -> cannot pin
                    else:
                        break


class Pawn(Piece):
    """
    The pawn piece
    """

    def __init__(self, board, position, color, character):
        super().__init__(board, position, color, character)
        self.direction = 1 if self.color == BLACK else -1

    def capture_moves(self):
        moves = []
        # capture
        for pos in [(self.row + self.direction, self.col - 1), (self.row + self.direction, self.col + 1)]:
            if 0 <= pos[1] < 8:
                target = self.board.grid[pos]
                if target and target.color == self.opponent:
                    moves.append(pos)
        # "en passant"
        for pos in [(self.row, self.col - 1), (self.row, self.col + 1)]:
            if 0 <= pos[1] < 8:
                target = self.board.grid[pos]
                if target and target.color == self.opponent and target.last_move == self.board.game.turn - 1:
                    moves.append(pos)
        return moves

    def all_moves(self):
        moves = []
        # default moves
        front = (self.row + self.direction, self.col)
        if not self.board.grid[front]:
            moves.append(front)
            # first move
            if self.moves == 0 and not self.board.grid[self.row + 2 * self.direction, self.col]:
                moves.append((self.row + 2 * self.direction, self.col))
        moves += self.capture_moves()

        return moves

    def legal_moves(self):
        return self.all_moves()

    def can_capture_at(self, position: tuple):
        return position in [(self.row + self.direction, self.col - 1), (self.row + self.direction, self.col + 1)]



class Knight(Piece):
    """
    The knight piece
    """

    def all_moves(self):
        return (((self.row + 2),(self.col + 1)), #1H
                ((self.row + 1),(self.col + 2)), #2H
                ((self.row - 1),(self.col + 2)), #4H
                ((self.row - 2),(self.col + 1)), #5H
                ((self.row - 2),(self.col - 1)), #7H
                ((self.row - 1),(self.col - 2)), #8H
                ((self.row + 1),(self.col - 2)), #10H
                ((self.row + 2),(self.col - 1))  #11H              
                )


class Bishop(StraightMover):
    """
    The bishop piece
    """

    def get_directions(self):
        return (
            zip(reversed(range(0, self.row)), reversed(range(0, self.col))),  # top left
            zip(reversed(range(0, self.row)), range(self.col + 1, 8)),  # top right
            zip(range(self.row + 1, 8), range(self.col + 1, 8)),  # bottom right
            zip(range(self.row + 1, 8), reversed(range(0, self.col))),  # bottom left
        )


class Rook(StraightMover):
    """
    The rook piece
    """

    def get_directions(self):
        return (
            [(row, self.col) for row in reversed(range(0, self.row))],  # top
            [(self.row, col) for col in range(self.col + 1, 8)],  # right
            [(row, self.col) for row in range(self.row + 1, 8)],  # bottom
            [(self.row, col) for col in reversed(range(0, self.col))],  # left
        )


class Queen(StraightMover):
    """
    The queen piece
    """

    def get_directions(self):
        return (
            zip(reversed(range(0, self.row)), reversed(range(0, self.col))),  # top left
            [(row, self.col) for row in reversed(range(0, self.row))],  # top
            zip(reversed(range(0, self.row)), range(self.col + 1, 8)),  # top right
            [(self.row, col) for col in range(self.col + 1, 8)],  # right
            zip(range(self.row + 1, 8), range(self.col + 1, 8)),  # bottom right
            [(row, self.col) for row in range(self.row + 1, 8)],  # bottom
            zip(range(self.row + 1, 8), reversed(range(0, self.col))),  # bottom left
            [(self.row, col) for col in reversed(range(0, self.col))],  # left
        )


class King(Piece):
    """
    The king piece
    """

    def can_castling_short(self):
        """
        Whether or not the king can make a castling short
        :return: true if it cans, false other wise
        """
        rook = self.board.grid[self.row, 7]
        return (
            rook is not None
            and rook.moves == 0
            and self.board.grid[self.row, 5] is None
            and self.board.grid[self.row, 6] is None
            and np.all([not piece.can_capture_at((self.row, 5))
                        for piece in self.board.living_pieces[self.opponent]])
        )

    def can_castling_long(self):
        """
        Whether or not the king can make a castling long
        :return: true if it cans, false other wise
        """
        rook = self.board.grid[self.row, 0]
        return (
            rook is not None
            and rook.moves == 0
            and self.board.grid[self.row, 1] is None
            and self.board.grid[self.row, 2] is None
            and self.board.grid[self.row, 3] is None
            and np.all([not piece.can_capture_at((self.row, 3))
                        for piece in self.board.living_pieces[self.opponent]])
        )

    def all_moves(self):
        moves = []
        moves += zip(range(self.row - 1, self.row + 2), [self.col - 1] * 3)
        moves += [(self.row - 1, self.col), (self.row + 1, self.col)]
        moves += zip(range(self.row - 1, self.row + 2), [self.col + 1] * 3)

        # For Castling
        if self.moves == 0 and not self.board.check:
            if self.can_castling_long():
                moves.append((self.row, 2))
            if self.can_castling_short():
                moves.append((self.row, 6))

        return moves

    def legal_moves(self):
        return [move for move in self._clear_invalid_moves(self.all_moves()) if np.all([
            not piece.can_capture_at(move) for piece in self.board.living_pieces[self.opponent]
            if type(piece) != 'King'
        ])]

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

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

    def can_play_at(self, position):
        """
        Check if this piece can play at the specified position
        :param position: the position to check
        :return: True if this piece can play at the specified position, False otherwise
        """

        pass

    def move_to(self, position):
        """
        Move the piece to the specified position on the board
        :param position: the new position
        """

        self.board.move_piece(self, position)

    def die(self):
        """
        Kill the current piece
        """

        self.board.piece_died(self)
        self.alive = False

    def __repr__(self):
        return self.character


class Pawn(Piece):
    """
    The pawn piece
    """

    def __init__(self, board, position, color, character):
        super().__init__(board, position, color, character)


class Knight(Piece):
    """
    The knight piece
    """

    def __init__(self, board, position, color, character):
        super().__init__(board, position, color, character)


class Bishop(Piece):
    """
    The bishop piece
    """

    def __init__(self, board, position, color, character):
        super().__init__(board, position, color, character)


class Rook(Piece):
    """
    The rook piece
    """

    def __init__(self, board, position, color, character):
        super().__init__(board, position, color, character)


class Queen(Piece):
    """
    The queen piece
    """

    def __init__(self, board, position, color, character):
        super().__init__(board, position, color, character)


class King(Piece):
    """
    The king piece
    """

    def __init__(self, board, position, color, character):
        super().__init__(board, position, color, character)

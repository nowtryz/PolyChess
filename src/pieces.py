class Piece:
    def __init__(self, board, position, color, character):
        self.board = board
        self.alive = True
        self.position = position
        self.color = color
        self.character = character

    def can_play_at(self, position):
        pass

    def move_to(self, position):
        pass

    def die(self):
        self.board.piece_died(self)
        self.alive = False

    def __repr__(self):
        return self.character


class Pawn(Piece):
    def __init__(self, board, position, color, character):
        super().__init__(board, position, color, character)


class Knight(Piece):
    def __init__(self, board, position, color, character):
        super().__init__(board, position, color, character)


class Bishop(Piece):
    def __init__(self, board, position, color, character):
        super().__init__(board, position, color, character)


class Rook(Piece):
    def __init__(self, board, position, color, character):
        super().__init__(board, position, color, character)


class Queen(Piece):
    def __init__(self, board, position, color, character):
        super().__init__(board, position, color, character)


class King(Piece):
    def __init__(self, board, position, color, character):
        super().__init__(board, position, color, character)

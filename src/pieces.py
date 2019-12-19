class Piece:
    def __init__(self, position, color, character):
        self.alive = True
        self.position = position
        self.color = color
        self.character = character

    def can_play_at(self, position):
        pass

    def move_to(self, position):
        pass

    def die(self):
        pass


class Pawn(Piece):
    pass


class Knight(Piece):
    pass


class Bishop(Piece):
    pass


class Rook(Piece):
    pass


class Queen(Piece):
    pass


class King(Piece):
    pass

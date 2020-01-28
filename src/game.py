# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 11:26:56 2019

@author: szelagp
"""

from board import Board
from datetime import datetime
from colors import WHITE, BLACK
from pieces import StraightMover, King, Knight, Bishop
from display import display_board


class Game:
    def __init__(self):
        """
        Initialise the Game
        """
        self.board = Board(self)
        self.timestamp = datetime.now()
        self.player = WHITE
        self.turn = 0
        self.winner = None

    def display(self):
        display_board(self.board)

    def is_check(self, color):
        """
        Parse the board to check if a king is in check and store the color in check in the check parameter of the board
        if there is not a check the value None remain in the check parameter
        :param color: the color of the king to check
        """
        king_pos = self.board.kings[color].position

        threats = []

        for i in self.board.living_pieces[opposite_color(color)]:
            if type(i) != King:
                if i.can_capture_at(king_pos):
                    threats = threats+[i]

        return threats

    def is_checkmate(self):
        """

        """
        threats = self.is_check(self.player)
        king = self.board.kings[self.player]
        if len(threats) == 0:
            return False

        # if the king cannot move
        if len(king.legal_moves()) != 0:
            return False

        #  a partir d ici le roi ne peut plus bouger
        if len(threats) > 1:
            return True

        # pinned pieces
        for p in self.board.living_pieces[opposite_color(self.player)]:
            if isinstance(p, StraightMover):
                p.pin_targets()

        # if une piece peut se mettre sur le chemin de la menace
        if isinstance(threats[0], StraightMover):
            directions = threats[0].get_directions()
            for direction in directions:
                if king.position in direction:
                    counters = direction[:direction.index(king.position)]
                    for position in counters:
                        for piece in self.board.living_pieces[self.player]:
                            if piece.can_play_at(position):
                                return False
        return True

    def lack_of_pieces(self):
        """

        """
        lack = False
        all_living_pieces = [
                piece
                for piece in self.board.living_pieces[BLACK] + self.board.living_pieces[WHITE]
                if not isinstance(piece, King)
            ]

        # King vs King
        if len(all_living_pieces) == 0:
            lack = True

        # King vs King + (Knight | Bishop)
        elif len(all_living_pieces) == 1:
            for i in all_living_pieces:
                if type(i) == Knight or type(i) == Bishop:
                    lack = True

        # King + Bishop vs King + Bishop (bishops on the same square color)
        elif len(all_living_pieces) == 2:
            if type(all_living_pieces[0]) == type(all_living_pieces[1]) == Bishop:
                if (sum(all_living_pieces[0].position) + sum(all_living_pieces[1].position)) % 2 == 0:
                    lack = True

        if lack:
            print("\nDraw due to lack of pieces")
            return True

        return False

    def end_game(self):
        """
        Display a summary message at the end of a game
        """
        if self.winner == WHITE or self.winner == BLACK:
            print("\nThe ",self.winner," player won in ",self.turn," turns",'\nThe game lasted : ',(datetime.now()-self.timestamp))
        if self.winner == "draw":
            print("\nThe game ended in ",self.turn," turns",'\nThe game lasted : ',(datetime.now()-self.timestamp))

    def command_to_pos(self, command):
        """
        Retrieve the command input of the player and convert it to movement coordinate
        :param command: the input of the player
        """
        if command == "break":
            return None, None, "break"

        if command == "resign":
            return None, None, "resign"

        piece = target = None
        if 64 < ord(command[0]) < 73:
            piece = 8 - int(command[1]), ord(command[0])-65

        if 96 < ord(command[0]) < 105:
            piece = 8 - int(command[1]), ord(command[0])-97

        if 64 < ord(command[3]) < 73:
            target = 8 - int(command[4]), ord(command[3])-65

        if 96 < ord(command[3]) < 105:
            target = 8 - int(command[4]), ord(command[3])-97

        return piece, target, None

    def play_turn(self,color, piece, target):
        """
        Check is a movement is valid
        :param color: color of the piece to move
        :param piece: coordinate of the piece to move
        :param target: coordinate of the destination of the movement
        """

        if piece.color != self.player:
            print("You can only move your pieces !")
            return False

        if not (piece.can_play_at(target)):
            print("This move is illegal !")
            return False

        else:
            piece.move_to(target)
            return True


    def run(self):
        print("\nTo move a piece the format of the command is <letter><number><space><letter><number>")
        print("\nYou can abandon a game by typing : resign")
        while True:
            print('#----------------------------------------#')
            print(f'\n{self.player}s are playing\n')
            self.display()
            if self.lack_of_pieces():
                self.winner = "draw"
                self.end_game()
                break

            if self.is_checkmate():
                self.winner = opposite_color(self.player)
                self.end_game()
                break

            command = input('commande:')
            if command and len(command) > 4:
                coord_piece, coord_target, status = self.command_to_pos(command)
                if status == "break":
                    break
                elif status == "resign":
                    self.winner=opposite_color(self.player)
                    self.end_game()
                    break
                if coord_piece and coord_target:
                    piece = self.board.grid[coord_piece]
                    if piece:
                        if self.play_turn(piece.color, piece, coord_target):
                            for p in self.board.living_pieces[self.player]:
                                p.pinned = False
                            self.turn += 1
                            #  Unpin pieces
                            for piece in self.board.living_pieces[self.player]:
                                piece.pinned = False
                            self.player = opposite_color(self.player)

                        if self.winner is not None:
                            self.end_game()
                            break
                    else:
                        print("This square is empty !")
                else:
                    print("Invalid coordinates !")
            else:
                print("The command is invalid !")


def opposite_color(color):
    """
    Give the opposite color
    :return: the opposite color
    """
    if color == WHITE:
        return BLACK
    return WHITE


if __name__ == "__main__":
    game = Game()
    game.run()

# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 11:26:56 2019

@author: szelagp
"""
from board import Board
from datetime import datetime
from colors import WHITE, BLACK
from pieces import StraightMover
from display import Display


class Game:
    def __init__(self):
        """
        Initialise the Game
        """
        self.board = Board(self)
        self.display = Display(self.board)
        self.timestamp = datetime.now()
        self.player = WHITE
        self.turn = 0
        self.end = False

    def is_check(self, color):
        """
        Parse the board to check if a king is in check and store the color in check in the check parameter of the board
        if there is not a check the value None remain in the check parameter
        :param color: the color of the king to check
        """
        king_pos=self.board.kings[color].position

        threats=[]

        for i in self.board.living_pieces[color]:
            if type(i) != "King":
                if i.can_play_at(king_pos):
                    threats=threats+[i]

        return threats

    def is_checkmate(self, color):
        """

        """
        mate = False
        threat=self.is_check(self.player)[0]
        king=self.board.kings[color]

        if len(threat) >= 2:
            mate = True
        # if le roi peut pas bouger

        # pinned pieces

        # if une piece peut se mettre sur le chemin de la menace
        if issubclass(threat, StraightMover):
            for i in threat.get_directions():
                if i[len(i)-1] == king.position:
                    for j in i:
                        for h in self.board.living_pieces[color]:
                            if h.can_play_at(j):
                                mate = False

        return mate

    def end_game(self):
        """
        Display a summary message at the end of a game
        """
        if self.end==True and self.player==WHITE:
            return ("The BLACK player won in ",self.turn," turns",'\n the game lasted : ',(datetime.now()-self.timestamp).strftime("%H:%M:%S"))
        if self.end==True and self.player==BLACK:
            return ("The WHITE player won in ",self.turn," turns",'\n the game lasted : ',(datetime.now()-self.timestamp).strftime("%H:%M:%S"))

    def command_to_pos(self, command):
        """
        Retrieve the command input of the player and convert it to movement coordinate
        :param command: the input of the player
        """
        piece = target = None
        if 64 < ord(command[0]) < 73:
            piece = 8 - int(command[1]), ord(command[0])-65

        if 96 < ord(command[0]) < 105:
            piece = 8 - int(command[1]), ord(command[0])-97

        if 64 < ord(command[3]) < 73:
            target = 8 - int(command[4]), ord(command[3])-65

        if 96 < ord(command[3]) < 105:
            target = 8 - int(command[4]), ord(command[3])-97

        return piece, target

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

        while True:
            print(f'{self.player}s are playing')
            self.display.display_board(self.player)
            command = input('commande:')
            if command and len(command) > 4:
                coord_piece, coord_target = self.command_to_pos(command)
                if coord_piece and coord_target:
                    piece = self.board.grid[coord_piece]
                    if piece:
                        if self.play_turn(piece.color, piece, coord_target):
                            self.turn += 1
                            if self.player == WHITE:
                                self.player = BLACK
                            else:
                                self.player = WHITE

                        if self.end:
                            self.end_game()
                            break
                    else:
                        print("This square is empty !")
                else:
                    print("Invalid coordinates !")
            else:
                print("The command is invalid !")


if __name__ == "__main__":
    game = Game()
    game.run()

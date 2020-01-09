# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

"""

from Config import DISPLAY_CONF
from colors import BLACK, WHITE
from board import Board


class Display:
    """
    The class display in the sideboard the chess board
    """
    
    def __init__(self, board: Board):
        """Initialize the class"""
        
        self.board=board
        """the board of the game, used to manipulate positions"""


    def display_board(self, color):
        """
        Manage the display of the board and the list of the dead pieces for each players
        :param color: take the color of the player
        :return: the board
        """
        
        if(color == WHITE):
            self.line = reversed(range(8))
            print('\x1b[6;39;40m' + 'Black dead pieces:', end=' ')
            for l in self.board.dead_pieces[color]:
                print(l,end = ' ')
        if(color == BLACK):
            self.line = range(8)
            print('\x1b[6;39;40m' + 'White dead pieces:', end=' ')
            for l in self.board.dead_pieces[color]:
                print(l,end = ' ')
        print('\x1b[0m')
        print('\x1b[6;39;40m' + '    A   B   C   D   E   F   G   H      ' + '\x1b[0m')
        print('\x1b[6;39;40m' + '                                       ')
        self.column = range(8)
        for i in self.line:
            print('\x1b[6;39;40m' , (i+1), end='  ')
            for j in self.column:
                if self.board.grid[i,j]:
                    print(self.board.grid[i,j], end='  ') 
                else:
                    if (j!=7):
                        print(DISPLAY_CONF["Square"][WHITE], end='  ')
                    else:
                        print(DISPLAY_CONF["Square"][WHITE], end=' ')
            print('\x1b[6;39;40m' , (i+1), end='  ')
            print('\x1b[0m')
            print('\x1b[6;39;40m' + '                                       ')
        print('\x1b[6;39;40m' + '    A   B   C   D   E   F   G   H      ' + '\x1b[0m')
        if (color == WHITE):
            print('\x1b[6;39;40m' + 'White dead pieces:', end=' ')
            for l in self.board.dead_pieces[BLACK]:
                print(l,end = ' ')
        else:
            print('\x1b[6;39;40m' + 'Black dead pieces:', end=' ')
            for l in self.board.dead_pieces[WHITE]:
                print(l,end = ' ')
        print('\x1b[0m')


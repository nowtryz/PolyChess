# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

"""

from Config import get_conf
from board import Board
from colors import BLACK, WHITE


def display_board(board: Board):
    """The function that display in the sideboard the chess board
    Manage the display of the board and the list of the dead pieces for each players
    :param board: the board of the game, used to manipulate positions
    """
    print('\x1b[6;39;39m' + 'Black dead pieces:', end=' ')
    for l in board.dead_pieces[BLACK]:
        print(l, end=' ')
    print('\x1b[0m')
    print('\x1b[6;39;39m' + '    A  B  C  D  E  F  G  H     ' + '\x1b[0m')
    for i in range(8):
        print('\x1b[6;39;39m', 8-i, end='  ')
        for j in range(8):
            if board.grid[i, j]:
                print(board.grid[i, j], end='  ')
            else:
                if j != 7:
                    print(get_conf()["Square"][WHITE], end='  ')
                else:
                    print(get_conf()["Square"][WHITE], end=' ')
        print('\x1b[6;39;39m', 8-i, end='  ')
        print('\x1b[6;39;39m' + '                                       ')
    print('\x1b[6;39;39m' + '    A  B  C  D  E  F  G  H     ' + '\x1b[0m')
    print('\x1b[6;39;39m' + 'White dead pieces:', end=' ')
    for l in board.dead_pieces[WHITE]:
        print(l, end=' ')
    print('\x1b[0m')


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
    print('Black dead pieces:', end=' ')
    for l in board.dead_pieces[BLACK]:
        print(l, end=' ')
    print('')
    print('   A  B  C  D  E  F  G  H     ')
    for i in range(8):
        print(8-i, end='  ')
        for j in range(8):
            if board.grid[i, j]:
                print(board.grid[i, j], end='  ')
            else:
                print(get_conf()["Square"][WHITE], end='  ')
        print(8-i, end='  ')
        print('')
    print('   A  B  C  D  E  F  G  H     ')
    print('White dead pieces:', end=' ')
    for l in board.dead_pieces[WHITE]:
        print(l, end=' ')
    print('')


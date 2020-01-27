# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 14:26:36 2019

@author: Roshan
bp='\u265F'
br='\u265C'
bn='\u265E'
bb='\u265D'
bq='\u265B'
bk='\u265A'
wp='\u2659'
wr='\u2656'
wn='\u2658'
wb='\u2657'
wq='\u2655'
wk='\u2654'

"""

from pieces import Pawn, Rook, Knight, Bishop, Queen, King
from colors import BLACK, WHITE

DISPLAY_CONF = {
    Pawn: {
        BLACK: '\u2659',
        WHITE: '\u265F',
    },
    Rook: {
        BLACK: '\u2656',
        WHITE: '\u265C',
    },
    Knight: {
        BLACK:  '\u2658',
        WHITE: '\u265E',
    },
    Bishop: {
        BLACK: '\u2657',
        WHITE: '\u265D',
    },
    Queen: {
        BLACK: '\u2655',
        WHITE: '\u265B',
    },
    King: {
        BLACK: '\u2654',
        WHITE: '\u265A',
    },
    "Square": {
        BLACK: ".",
        WHITE: "."
    }
 }

"""    
DISPLAY_CONF = {
    Pawn: {
        BLACK: 'p',
        WHITE: 'P',
    },
    Rook: {
        BLACK: 'r',
        WHITE: 'R',
    },
    Knight: {
        BLACK:  'n',
        WHITE: 'N',
    },
    Bishop: {
        BLACK: 'b',
        WHITE: 'B',
    },
    Queen: {
        BLACK: 'q',
        WHITE: 'Q',
    },
    King: {
        BLACK: 'k',
        WHITE: 'K',
    },
    "Square": {
        BLACK: ".",
        WHITE: "."
    }
 }
"""

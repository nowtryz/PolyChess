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

from config.pieces import Pawn, Rook, Knight, Bishop, Queen, King
# ...

# colors
BLACK = (100, 100, 100)
WHITE = (255, 255, 255)

# constants for each display_conf entry
CHAR = 0
COLOR = 1


DISPLAY_CONF = {
    Pawn: {
        BLACK: '\u265F',
        WHITE: '\u2659'
    },
    Rook: {
        BLACK: '\u265C',
        WHITE: '\u2656'
    },
    Knight: {
        BLACK: '\u265E',
        WHITE:  '\u2658'
    },
    Bishop: {
        BLACK: '\u265D',
        WHITE: '\u2657'
    },
    Queen: {
        BLACK: '\u265B',
        WHITE: '\u2655'
    },
    King: {
        BLACK: '\u265A',
        WHITE: '\u2654'
    },
    "Square": {
        BLACK: " ",
        WHITE: " "
    }
 }   
    
    
    
    
    
    
    
    
    
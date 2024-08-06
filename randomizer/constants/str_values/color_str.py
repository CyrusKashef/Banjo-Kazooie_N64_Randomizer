'''
Purpose:
*
'''

###################
##### IMPORTS #####
###################

from enum import StrEnum, unique, auto

###################
##### CLASSES #####
###################

@unique
class COLORS(StrEnum):
    red = auto()
    green = auto()
    blue = auto()
    alpha = auto()
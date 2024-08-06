'''
Purpose:
*
'''

###################
##### IMPORTS #####
###################

from enum import IntEnum, unique, auto

###################
##### CLASSES #####
###################

@unique
class COLOR_BLINDNESS(IntEnum):
    trichromacy = auto()
    deuteranomaly = auto()
    deuteranopia = auto()
    protanomaly = auto()
    protanopia = auto()
    tritanomaly = auto()
    tritanopia = auto()
    monochromacy = auto()
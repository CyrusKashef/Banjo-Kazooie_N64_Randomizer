'''
Each enumerator in the class below is the value used IN GAME.
'''

###################
##### IMPORTS #####
###################

from enum import IntEnum, unique

##########################
##### LEVEL ID ENUMS #####
##########################

@unique
class FURNACE_FUN_TILE_TYPE_ENUMS(IntEnum):
    null = 0
    banjo_kazooie = 1
    picture = 2
    sound = 3
    minigame = 4
    gruntilda = 5
    skull = 6
    joker = 8
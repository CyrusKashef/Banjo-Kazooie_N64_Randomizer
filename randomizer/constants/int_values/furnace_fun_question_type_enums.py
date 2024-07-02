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
class FURNACE_FUN_QUESTION_TYPE_ENUMS(IntEnum):
    banjo_kazooie = 0
    picture = 1
    sound = 2
    gruntilda = 3
    minigame = 4
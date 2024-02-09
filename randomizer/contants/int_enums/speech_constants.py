'''
Purpose:
*
'''

###################
##### IMPORTS #####
###################

from enum import IntEnum, unique, auto

##########################
##### ASSET ID ENUMS #####
##########################

@unique
class SPEECH_CONSTANTS(IntEnum):
    generic_speech = auto()
    furnace_fun_gruntilda_question = auto()
    furnace_fun_other_question = auto()
    full_screen = auto()
    top_section = auto()
    bottom_section = auto()
    sprite = auto()
    speech = auto()
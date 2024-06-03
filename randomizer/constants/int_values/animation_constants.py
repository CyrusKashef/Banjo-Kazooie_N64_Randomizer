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
class ANIMATION_CONSTANTS(IntEnum):
    # HEADER
    header_unk0 = auto()
    header_unk2 = auto()
    element_list = auto()
    # ELEMENT
    element_unk0_0 = auto()
    element_unk0_1 = auto()
    elemment_data_count = auto()
    element_data_list = auto()
    # ELEMENT DATA
    element_data_unk0_0 = auto()
    element_data_unk0_1 = auto()
    element_data_unk0_2 = auto()
    element_data_unk2 = auto()
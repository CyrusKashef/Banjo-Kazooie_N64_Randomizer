'''
Purpose:
*
'''

###################
##### IMPORTS #####
###################

from enum import StrEnum, unique, auto

##########################
##### ASSET ID ENUMS #####
##########################

@unique
class MAP_SETUP_CONSTANTS(StrEnum):
    x_position = auto()
    y_position = auto()
    z_position = auto()
    byte_6_unk_0 = auto()
    byte_6_unk_1 = auto()
    byte_6_unk_2 = auto()
    actor_id = auto()
    marker_id = auto()
    byte_b_unk_0 = auto()
    byte_b_unk_1 = auto()
    byte_b_unk_2 = auto()
    byte_b_unk_3 = auto()
    byte_b_unk_4 = auto()
    rotation_y_axis = auto()
    byte_c_unk_1 = auto()
    byte_10_unk_0 = auto()
    byte_10_unk_1 = auto()
    byte_10_unk_2 = auto()
    byte_10_unk_3 = auto()
    byte_10_unk_4 = auto()
    byte_10_unk_5 = auto()
    byte_0_unk_0 = auto()
    byte_0_unk_1 = auto()
    byte_0_unk_2 = auto()
    byte_0_unk_3 = auto()
    byte_0_unk_4 = auto()
    byte_0_unk_5 = auto()
    byte_0_unk_6 = auto()
    byte_0_unk_7 = auto()
    byte_8_unk_0 = auto()
    byte_8_unk_1 = auto()
    byte_8_unk_2 = auto()
    byte_8_unk_3 = auto()
    byte_8_unk_4 = auto()
    byte_8_unk_5 = auto()
    byte_8_unk_6 = auto()
    byte_8_unk_7 = auto()
    camera_id_indicator = auto()
    camera_type_indicator = auto()
    camera_end_indicator = auto()
    camera_section_1_indicator = auto()
    camera_section_2_indicator = auto()
    camera_section_3_indicator = auto()
    camera_section_4_indicator = auto()
    camera_section_5_indicator = auto()
    camera_section_6_indicator = auto()
    camera_id = auto()
    camera_type = auto()
    horizontal_speed = auto()
    vertical_speed = auto()
    rotation = auto()
    acceleration = auto()
    pitch = auto()
    yaw = auto()
    roll = auto()
    camera_unk_byte = auto()
    close_distance = auto()
    far_distance = auto()
    lighting_start_indicator = auto()
    lighting_section_1_indicator = auto()
    lighting_section_2_indicator = auto()
    lighting_section_3_indicator = auto()
    lighting_section_4_indicator = auto()
    byte_f = auto()
    byte_13 = auto()
    red_value = auto()
    green_value = auto()
    blue_value = auto()
    file_end_indicator = auto()
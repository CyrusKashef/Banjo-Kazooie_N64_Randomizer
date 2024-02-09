'''
Purpose:
* Class of in-game enumerators for abilities
'''

###################
##### IMPORTS #####
###################

from enum import IntEnum, unique

#########################
##### ABILITY ENUMS #####
#########################

@unique
class ABILITY_ENUMS(IntEnum):
    beak_barge = 0x0
    beak_bomb = 0x1
    beak_buster = 0x2
    camera_control = 0x3
    claw_swipe = 0x4
    climb = 0x5
    egg_firing = 0x6
    feathery_flap = 0x7
    flap_flip = 0x8
    flight = 0x9
    high_jump = 0xA
    rat_a_tat_rap = 0xB
    roll = 0xC
    shock_jump = 0xD
    stilt_stride = 0xE
    dive = 0xF
    talon_trot = 0x10
    turbo_talon_trot = 0x11
    wonderwing = 0x12
    note_door = 0x13
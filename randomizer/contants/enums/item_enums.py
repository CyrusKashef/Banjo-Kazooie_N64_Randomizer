'''
Purpose:
*
'''

###################
##### IMPORTS #####
###################

from enum import IntEnum, unique

##########################
##### LEVEL ID ENUMS #####
##########################

@unique
class ITEM_ENUMS(IntEnum):
    hourglass_timer = 0x00
    skull_hourglass_timer = 0x01

    propeller_timer = 0x03

    xmas_tree_timer = 0x05
    hourglass = 0x06
    skull_hourglass = 0x07

    propeller = 0x09

    xmas_tree = 0x0B
    note = 0x0C
    blue_egg = 0x0D
    jiggy = 0x0E
    red_feather = 0x0F
    gold_feather = 0x10

    jinjos = 0x12
    empty_honeycomb = 0x13
    health = 0x14
    health_total = 0x15
    life = 0x16
    air = 0x17
    gold_bullions = 0x18
    orange = 0x19
    player_vile_score = 0x1A
    mr_vile_vile_score = 0x1B
    mumbo_token = 0x1C
    grumblie = 0x1D
    yumblie = 0x1E
    green_present = 0x1F
    blue_present = 0x20
    red_present = 0x21
    caterpillar = 0x22
    acorns = 0x23
    twinkly_score = 0x24
    mumbo_token_total = 0x25
    jiggy_total = 0x26
    joker_card = 0x27
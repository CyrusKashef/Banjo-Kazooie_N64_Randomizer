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
class EMPTY_HONEYCOMB_ENUMS(IntEnum):
    mumbos_mountain_alcove = 0x01
    mumbos_mountain_atop_juju = 0x02
    treasure_trove_cove_underwater = 0x03
    treasure_trove_cove_floating_crate = 0x04
    clankers_cavern_underwater_pipe = 0x05
    clankers_cavern_grated_pipe = 0x06
    bubblegloop_swamp_mumbos_skull = 0x07
    bubblegloop_swamp_tanktup = 0x08
    freezeezy_peak_wozzas_cave = 0x09
    freezeezy_peak_under_sir_slush = 0x0A
    gobis_valley_cactus = 0x0B
    gobis_valley_gobi_3 = 0x0C
    click_clock_wood_gnawty = 0x0D
    click_clock_wood_acorn_storage = 0x0E
    rusty_bucket_bay_boat_room = 0x0F
    rusty_bucket_bay_engine_room = 0x10
    mad_monster_mansion_church_rafters = 0x11
    mad_monster_mansion_floorboards = 0x12
    spiral_mountain_stump = 0x13
    spiral_mountain_waterfall = 0x14
    spiral_mountain_underwater = 0x15
    spiral_mountain_atop_tree = 0x16
    spiral_mountain_colliwobble = 0x17
    spiral_mountain_quarries = 0x18
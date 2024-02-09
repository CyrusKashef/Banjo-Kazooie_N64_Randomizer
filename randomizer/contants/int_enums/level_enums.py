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
class LEVEL_ID_ENUMS(IntEnum):
    mumbos_mountain = 0x1
    treasure_trove_cove = 0x2
    clankers_cavern = 0x3
    bubblegloop_swamp = 0x4
    freezeezy_peak = 0x5
    gruntildas_lair = 0x6
    gobis_valley = 0x7
    click_clock_wood = 0x8
    rusty_bucket_bay = 0x9
    mad_monster_mansion = 0xA
    spiral_mountain = 0xB
    final_battle = 0xC
    cutscenes = 0xD
'''
Purpose:
*
'''

###################
##### IMPORTS #####
###################

from enum import StrEnum, unique

##########################
##### LEVEL ID ENUMS #####
##########################

@unique
class LEVEL_NAME_ENUMS(StrEnum):
    mumbos_mountain = "Mumbo's Mountain"
    treasure_trove_cove = "Treasure Trove Cove"
    clankers_cavern = "Clanker's Cavern"
    bubblegloop_swamp = "Bubblegloop Swamp"
    freezeezy_peak = "Freezeezy Peak"
    gruntildas_lair = "Gruntilda's Lair"
    gobis_valley = "Gobi's Valley"
    click_clock_wood = "Click Clock Wood"
    rusty_bucket_bay = "Rusty Bucket Bay"
    mad_monster_mansion = "Mad Monster Mansion"
    spiral_mountain = "Spiral Mountain"
    final_battle = "Final Battle"
    cutscenes = "Cutscenes"
'''
Purpose:
* Class of generic enumerators for the assembly files
'''

###################
##### IMPORTS #####
###################

from enum import IntEnum, unique, auto

###############################
##### ASSEMBLY FILE ENUMS #####
###############################

@unique
class ASSEMBLY_FILE_ENUMS(IntEnum):
    c_libraries_code = auto()
    c_libraries_data = auto()
    game_engine_code = auto()
    game_engine_data = auto()
    clankers_cavern_code = auto()
    clankers_cavern_data = auto()
    mad_monster_mansion_code = auto()
    mad_monster_mansion_data = auto()
    gobis_valley_code = auto()
    gobis_valley_data = auto()
    treasure_trove_cove_code = auto()
    treasure_trove_cove_data = auto()
    mumbos_mountain_code = auto()
    mumbos_mountain_data = auto()
    bubblegloop_swamp_code = auto()
    bubblegloop_swamp_data = auto()
    rusty_bucket_bay_code = auto()
    rusty_bucket_bay_data = auto()
    freezeezy_peak_code = auto()
    freezeezy_peak_data = auto()
    spiral_mountain_code = auto()
    spiral_mountain_data = auto()
    cutscenes_code = auto()
    cutscenes_data = auto()
    gruntildas_lair_code = auto()
    gruntildas_lair_data = auto()
    final_battle_code = auto()
    final_battle_data = auto()
    click_clock_wood_code = auto()
    click_clock_wood_data = auto()
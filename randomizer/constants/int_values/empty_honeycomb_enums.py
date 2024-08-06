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
class EMPTY_HONEYCOMB_ENUMS(IntEnum):
    ###########################
    ##### MUMBOS MOUNTAIN #####
    ###########################
    mumbos_mountain_alcove = 0x01
    mumbos_mountain_atop_juju = 0x02
    ###############################
    ##### TREASURE TROVE COVE #####
    ###############################
    treasure_trove_cove_underwater = 0x03
    treasure_trove_cove_floating_crate = 0x04
    ###########################
    ##### CLANKERS CAVERN #####
    ###########################
    clankers_cavern_underwater_pipe = 0x05
    clankers_cavern_grated_pipe = 0x06
    #############################
    ##### BUBBLEGLOOP SWAMP #####
    #############################
    bubblegloop_swamp_mumbos_skull = 0x07
    bubblegloop_swamp_tanktup = 0x08
    ##########################
    ##### FREEZEEZY PEAK #####
    ##########################
    freezeezy_peak_wozzas_cave = 0x09
    freezeezy_peak_under_sir_slush = 0x0A
    ########################
    ##### GOBIS VALLEY #####
    ########################
    gobis_valley_cactus = 0x0B
    gobis_valley_gobi_3 = 0x0C
    ############################
    ##### CLICK CLOCK WOOD #####
    ############################
    click_clock_wood_gnawty = 0x0D
    click_clock_wood_acorn_storage = 0x0E
    ############################
    ##### RUSTY BUCKET BAY #####
    ############################
    rusty_bucket_bay_boat_room = 0x0F
    rusty_bucket_bay_engine_room = 0x10
    ###############################
    ##### MAD MONSTER MANSION #####
    ###############################
    mad_monster_mansion_church_rafters = 0x11
    mad_monster_mansion_floorboards = 0x12
    ###########################
    ##### SPIRAL MOUNTAIN #####
    ###########################
    spiral_mountain_stump = 0x13
    spiral_mountain_waterfall = 0x14
    spiral_mountain_underwater = 0x15
    spiral_mountain_atop_tree = 0x16
    spiral_mountain_colliwobble = 0x17
    spiral_mountain_quarries = 0x18
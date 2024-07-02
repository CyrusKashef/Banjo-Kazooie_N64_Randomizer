'''
Enumerators from the following class are arbitrary values used to make each instance unique.
'''

###################
##### IMPORTS #####
###################

from enum import IntEnum, auto

###########################
##### ITEM TYPE ENUMS #####
###########################

class ITEM_TYPE_ENUMS(IntEnum):
    ###################
    ##### GENERAL #####
    ###################
    musical_note = auto()
    blue_egg = auto()
    red_feather = auto()
    gold_feather = auto()
    extra_life = auto()
    jiggy = auto()
    empty_honeycomb = auto()
    mumbo_token = auto()
    ###########################
    ##### SPIRAL MOUNTAIN #####
    ###########################
    quarries = auto()
    ###########################
    ##### MUMBOS MOUNTAIN #####
    ###########################
    mumbos_mountain_pink_jinjo = auto()
    mumbos_mountain_blue_jinjo = auto()
    mumbos_mountain_orange_jinjo = auto()
    mumbos_mountain_yellow_jinjo = auto()
    mumbos_mountain_green_jinjo = auto()
    mumbos_mountain_witch_switch = auto()
    chimpys_orange = auto()
    mumbos_mountain_break_huts = auto()
    ###############################
    ##### TREASURE TROVE COVE #####
    ###############################
    treasure_trove_cove_pink_jinjo = auto()
    treasure_trove_cove_blue_jinjo = auto()
    treasure_trove_cove_orange_jinjo = auto()
    treasure_trove_cove_yellow_jinjo = auto()
    treasure_trove_cove_green_jinjo = auto()
    treasure_trove_cove_witch_switch = auto()
    blubbers_gold = auto()
    ###########################
    ##### CLANKERS CAVERN #####
    ###########################
    clankers_cavern_pink_jinjo = auto()
    clankers_cavern_blue_jinjo = auto()
    clankers_cavern_orange_jinjo = auto()
    clankers_cavern_yellow_jinjo = auto()
    clankers_cavern_green_jinjo = auto()
    clankers_cavern_witch_switch = auto()
    #############################
    ##### BUBBLEGLOOP SWAMP #####
    #############################
    bubblegloop_swamp_pink_jinjo = auto()
    bubblegloop_swamp_blue_jinjo = auto()
    bubblegloop_swamp_orange_jinjo = auto()
    bubblegloop_swamp_yellow_jinjo = auto()
    bubblegloop_swamp_green_jinjo = auto()
    bubblegloop_swamp_witch_switch = auto()
    croctus = auto()
    bubblegloop_swamp_break_huts = auto()
    ##########################
    ##### FREEZEEZY PEAK #####
    ##########################
    freezeezy_peak_pink_jinjo = auto()
    freezeezy_peak_blue_jinjo = auto()
    freezeezy_peak_orange_jinjo = auto()
    freezeezy_peak_yellow_jinjo = auto()
    freezeezy_peak_green_jinjo = auto()
    freezeezy_peak_witch_switch = auto()
    red_present = auto()
    blue_present = auto()
    green_present = auto()
    ########################
    ##### GOBIS VALLEY #####
    ########################
    gobis_valley_pink_jinjo = auto()
    gobis_valley_blue_jinjo = auto()
    gobis_valley_orange_jinjo = auto()
    gobis_valley_yellow_jinjo = auto()
    gobis_valley_green_jinjo = auto()
    gobis_valley_witch_switch = auto()
    ###############################
    ##### MAD MONSTER MANSION #####
    ###############################
    mad_monster_mansion_pink_jinjo = auto()
    mad_monster_mansion_blue_jinjo = auto()
    mad_monster_mansion_orange_jinjo = auto()
    mad_monster_mansion_yellow_jinjo = auto()
    mad_monster_mansion_green_jinjo = auto()
    mad_monster_mansion_witch_switch = auto()
    flower_pot = auto()
    ############################
    ##### RUSTY BUCKET BAY #####
    ############################
    rusty_bucket_bay_pink_jinjo = auto()
    rusty_bucket_bay_blue_jinjo = auto()
    rusty_bucket_bay_orange_jinjo = auto()
    rusty_bucket_bay_yellow_jinjo = auto()
    rusty_bucket_bay_green_jinjo = auto()
    rusty_bucket_bay_witch_switch = auto()
    ############################
    ##### CLICK CLOCK WOOD #####
    ############################
    click_clock_wood_pink_jinjo = auto()
    click_clock_wood_blue_jinjo = auto()
    click_clock_wood_orange_jinjo = auto()
    click_clock_wood_yellow_jinjo = auto()
    click_clock_wood_green_jinjo = auto()
    click_clock_wood_witch_switch = auto()
    nubnuts_acorn = auto()
    eyries_caterpillar = auto()
    ###########################
    ##### GRUNTILDAS LAIR #####
    ###########################
    activate_pink_cauldron_puzzles = auto()
    activate_pink_cauldron_gruntilda_head_statue = auto()
    activate_teal_cauldron_gruntilda_head_statue = auto()
    activate_teal_cauldron_rusty_bucket_bay_entrance = auto()
    activate_amber_cauldron_pipe = auto()
    activate_amber_cauldron_click_clock_wood_entrance = auto()
    activate_gold_cauldron_furnace_fun = auto()
    activate_gold_cauldron_810_note_door = auto()
    break_pink_cauldron_web = auto()
    break_teal_cauldron_web = auto()
    activate_water_level_1 = auto()
    activate_water_level_2 = auto()
    able_to_activate_water_level_3 = auto()
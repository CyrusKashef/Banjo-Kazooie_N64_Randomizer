'''
Each enumerator in the class below is the value used IN GAME.
'''

###################
##### IMPORTS #####
###################

from enum import IntEnum, unique

#############################
##### MUMBO TOKEN ENUMS #####
#############################

@unique
class MUMBO_TOKEN_ENUMS(IntEnum):
    ###########################
    ##### MUMBOS MOUNTAIN #####
    ###########################
    mumbos_mountain_conga = 0x01
    mumbos_mountain_stonehenge = 0x02
    mumbos_mountain_under_mumbos_bridge = 0x03
    mumbos_mountain_near_pink_jinjo = 0x04
    mumbos_mountain_tickers_tower = 0x05
    ###############################
    ##### TREASURE TROVE COVE #####
    ###############################
    treasure_trove_cove_inside_salty_hippo = 0x06
    treasure_trove_cove_lockup_1 = 0x07
    treasure_trove_cove_lockup_2 = 0x08
    treasure_trove_cove_salty_hippo_mast = 0x09
    treasure_trove_cove_lighthouse = 0x0A
    treasure_trove_cove_floating_box = 0x0B
    treasure_trove_cove_by_last_x = 0x0C
    treasure_trove_cove_inside_pool = 0x0D
    treasure_trove_cove_shock_spring_pad = 0x0E
    treasure_trove_cove_behind_nipper = 0x0F
    ###########################
    ##### CLANKERS CAVERN #####
    ###########################
    clankers_cavern_tail_chompa = 0x10
    clankers_cavern_above_world_exit = 0x11
    clankers_cavern_underwater_alcove = 0x12
    clankers_cavern_window = 0x13
    clankers_cavern_clankers_tooth = 0x14
    #############################
    ##### BUBBLEGLOOP SWAMP #####
    #############################
    bubblegloop_swamp_under_huts_1 = 0x15
    bubblegloop_swamp_under_huts_2 = 0x16
    bubblegloop_swamp_above_cattail = 0x17
    bubblegloop_swamp_by_yellow_jinjo = 0x18
    bubblegloop_swamp_above_huts = 0x19
    bubblegloop_swamp_behind_mumbos_skull = 0x1A
    bubblegloop_swamp_elevated_walkway = 0x1B
    bubblegloop_swamp_inside_tanktup = 0x1C
    bubblegloop_swamp_mr_vile = 0x1D
    bubblegloop_swamp_behind_mumbos_chair = 0x1E
    ##########################
    ##### FREEZEEZY PEAK #####
    ##########################
    freezeezy_peak_snowman_leg_1 = 0x1F
    freezeezy_peak_snowman_leg_2 = 0x20
    freezeezy_peak_present_stack = 0x21
    freezeezy_peak_chimney_fly_pad = 0x22
    freezeezy_peak_sir_slush_island = 0x23
    freezeezy_peak_sir_slush_present = 0x24
    freezeezy_peak_christmas_tree_base = 0x25
    freezeezy_peak_scarf_sled = 0x26
    freezeezy_peak_water_by_wozza = 0x27
    freezeezy_peak_boggys_igloo = 0x28
    ########################
    ##### GOBIS VALLEY #####
    ########################
    gobis_valley_jinxys_nose = 0x29
    gobis_valley_in_sand_by_jinxy = 0x2A
    gobis_valley_moat = 0x2B
    gobis_valley_over_maze_pyramid = 0x2C
    gobis_valley_water_temple_door = 0x2D
    gobis_valley_matching_pyramid = 0x2E
    gobis_valley_in_maze_pyramid = 0x2F
    gobis_valley_in_water_pyramid = 0x30
    gobis_valley_rubees_pyramid = 0x31
    gobis_valley_inside_jinxy = 0x32
    ###############################
    ##### MAD MONSTER MANSION #####
    ###############################
    mad_monster_mansion_by_fountain = 0x33
    mad_monster_mansion_by_tumblar_shed = 0x34
    mad_monster_mansion_church_roof = 0x35
    mad_monster_mansion_hedges_by_ramp = 0x36
    mad_monster_mansion_hedge_maze = 0x37
    mad_monster_mansion_cemetary = 0x38
    mad_monster_mansion_in_fountain_whipcrack = 0x39
    mad_monster_mansion_church_rafters = 0x3A
    mad_monster_mansion_organ_stool = 0x3B
    mad_monster_mansion_tumblar_shed_roof = 0x3C
    mad_monster_mansion_cellar_or_loggo = 0x3D
    mad_monster_mansion_dining_room = 0x3E
    mad_monster_mansion_well = 0x3F
    mad_monster_mansion_bedroom = 0x40
    mad_monster_mansion_bathroom = 0x41
    ############################
    ##### RUSTY BUCKET BAY #####
    ############################
    rusty_bucket_bay_top_of_funnel = 0x42
    rusty_bucket_bay_front_of_ship = 0x43
    rusty_bucket_bay_lifeboat = 0x44
    rusty_bucket_bay_above_tollway = 0x45
    rusty_bucket_bay_toxic_pool = 0x46
    rusty_bucket_bay_witch_switch_chompa = 0x47
    rusty_bucket_bay_chompa_container = 0x48
    rusty_bucket_bay_seaman_grublin_container = 0x49
    rusty_bucket_bay_crew_cabin = 0x4A
    rusty_bucket_bay_navigation_room = 0x4B
    rusty_bucket_bay_kitchen_oven = 0x4C
    rusty_bucket_bay_engine_room_left = 0x4D
    rusty_bucket_bay_engine_room_right = 0x4E
    rusty_bucket_bay_engine_room_middle = 0x4F
    rusty_bucket_bay_boom_box_pipe = 0x50
    ###########################
    ##### GRUNTILDAS LAIR #####
    ###########################
    gruntildas_lair_behind_pink_cauldron = 0x51
    gruntildas_lair_by_ccw_puzzle = 0x52
    gruntildas_lair_near_pipe_amber_cauldron = 0x53
    gruntildas_lair_above_cc_entrance = 0x54
    gruntildas_lair_behind_gv_sarcophagus = 0x55
    gruntildas_lair_advent_calendar = 0x56
    gruntildas_lair_in_crypt = 0x57
    gruntildas_lair_above_640_note_door = 0x58
    gruntildas_lair_rbb_entrance_underwater = 0x59
    gruntildas_lair_mmm_puzzle = 0x5A
    ############################
    ##### CLICK CLOCK WOOD #####
    ############################
    click_clock_wood_spring_house = 0x5B
    click_clock_wood_spring_low_branch = 0x5C
    # 0x5D Skipped
    click_clock_wood_spring_brambles_or_eyrie = 0x5E
    click_clock_wood_spring_garden_snare = 0x5F
    click_clock_wood_spring_entrance = 0x60
    click_clock_wood_spring_hive = 0x61
    click_clock_wood_spring_nabnuts = 0x62
    click_clock_wood_summer_eyrie = 0x63
    click_clock_wood_summer_garden_corner = 0x64
    click_clock_wood_summer_bramble_snare = 0x65
    click_clock_wood_summer_low_branch = 0x66
    click_clock_wood_summer_gnawtys = 0x67
    click_clock_wood_summer_leaf_jumps = 0x68
    click_clock_wood_summer_in_mumbos = 0x69
    click_clock_wood_autumn_leaf_jumps = 0x6A
    click_clock_wood_autumn_entrance = 0x6B
    click_clock_wood_autumn_top = 0x6C
    click_clock_wood_autumn_by_house = 0x6D
    click_clock_wood_autumn_low_branch = 0x6E
    click_clock_wood_winter_flower = 0x6F
    click_clock_wood_winter_river_fly_pad = 0x70
    click_clock_wood_winter_hive = 0x71
    click_clock_wood_winter_nabnut = 0x72
    click_clock_wood_winter_sir_slush = 0x73
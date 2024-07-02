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
    mm_conga = 0x01
    mm_stonehenge = 0x02
    mm_under_mumbos_bridge = 0x03
    mm_near_pink_jinjo = 0x04
    mm_tickers_tower = 0x05
    ###############################
    ##### TREASURE TROVE COVE #####
    ###############################
    ttc_inside_salty_hippo = 0x06
    ttc_lockup_1 = 0x07
    ttc_lockup_2 = 0x08
    ttc_salty_hippo_mast = 0x09
    ttc_lighthouse = 0x0A
    ttc_floating_box = 0x0B
    ttc_by_last_x = 0x0C
    ttc_inside_pool = 0x0D
    ttc_shock_spring_pad = 0x0E
    ttc_behind_nipper = 0x0F
    ###########################
    ##### CLANKERS CAVERN #####
    ###########################
    cc_tail_chompa = 0x10
    cc_above_world_exit = 0x11
    cc_underwater_alcove = 0x12
    cc_window = 0x13
    cc_clankers_tooth = 0x14
    #############################
    ##### BUBBLEGLOOP SWAMP #####
    #############################
    bgs_under_huts_1 = 0x15
    bgs_under_huts_2 = 0x16
    bgs_above_cattail = 0x17
    bgs_by_yellow_jinjo = 0x18
    bgs_above_huts = 0x19
    bgs_behind_mumbos_skull = 0x1A
    bgs_elevated_walkway = 0x1B
    bgs_inside_tanktup = 0x1C
    bgs_mr_vile = 0x1D
    bgs_behind_mumbos_chair = 0x1E
    ##########################
    ##### FREEZEEZY PEAK #####
    ##########################
    fp_snowman_leg_1 = 0x1F
    fp_snowman_leg_2 = 0x20
    fp_present_stack = 0x21
    fp_chimney_fly_pad = 0x22
    fp_sir_slush_island = 0x23
    fp_sir_slush_present = 0x24
    fp_christmas_tree_base = 0x25
    fp_scarf_sled = 0x26
    fp_water_by_wozza = 0x27
    fp_boggys_igloo = 0x28
    ########################
    ##### GOBIS VALLEY #####
    ########################
    gv_jinxys_nose = 0x29
    gv_in_sand_by_jinxy = 0x2A
    gv_moat = 0x2B
    gv_over_maze_pyramid = 0x2C
    gv_water_temple_door = 0x2D
    gv_matching_pyramid = 0x2E
    gv_in_maze_pyramid = 0x2F
    gv_in_water_pyramid = 0x30
    gv_rubees_pyramid = 0x31
    gv_inside_jinxy = 0x32
    ###############################
    ##### MAD MONSTER MANSION #####
    ###############################
    mmm_by_fountain = 0x33
    mmm_by_tumblar_shed = 0x34
    mmm_church_roof = 0x35
    mmm_hedges_by_ramp = 0x36
    mmm_hedge_maze = 0x37
    mmm_cemetary = 0x38
    mmm_in_fountain_whipcrack = 0x39
    mmm_church_rafters = 0x3A
    mmm_organ_stool = 0x3B
    mmm_tumblar_shed_roof = 0x3C
    mmm_cellar_or_loggo = 0x3D
    mmm_dining_room = 0x3E
    mmm_well = 0x3F
    mmm_bedroom = 0x40
    mmm_bathroom = 0x41
    ############################
    ##### RUSTY BUCKET BAY #####
    ############################
    rbb_top_of_funnel = 0x42
    rbb_front_of_ship = 0x43
    rbb_lifeboat = 0x44
    rbb_above_tollway = 0x45
    rbb_toxic_pool = 0x46
    rbb_witch_switch_chompa = 0x47
    rbb_chompa_container = 0x48
    rbb_seaman_grublin_container = 0x49
    rbb_crew_cabin = 0x4A
    rbb_navigation_room = 0x4B
    rbb_kitchen_oven = 0x4C
    rbb_engine_room_left = 0x4D
    rbb_engine_room_right = 0x4E
    rbb_engine_room_middle = 0x4F
    rbb_boom_box_pipe = 0x50
    ###########################
    ##### GRUNTILDAS LAIR #####
    ###########################
    gl_behind_pink_cauldron = 0x51
    gl_by_ccw_puzzle = 0x52
    gl_near_pipe_amber_cauldron = 0x53
    gl_above_cc_entrance = 0x54
    gl_behind_gv_sarcophagus = 0x55
    gl_advent_calendar = 0x56
    gl_in_crypt = 0x57
    gl_above_640_note_door = 0x58
    gl_rbb_entrance_underwater = 0x59
    gl_mmm_puzzle = 0x5A
    ############################
    ##### CLICK CLOCK WOOD #####
    ############################
    ccw_spring_house = 0x5B
    ccw_spring_low_branch = 0x5C
    # 0x5D Skipped
    ccw_spring_brambles_or_eyrie = 0x5E
    ccw_spring_garden_snare = 0x5F
    ccw_spring_entrance = 0x60
    ccw_spring_hive = 0x61
    ccw_spring_nabnuts = 0x62
    ccw_summer_eyrie = 0x63
    ccw_summer_garden_corner = 0x64
    ccw_summer_bramble_snare = 0x65
    ccw_summer_low_branch = 0x66
    ccw_summer_gnawtys = 0x67
    ccw_summer_leaf_jumps = 0x68
    ccw_summer_in_mumbos = 0x69
    ccw_autumn_leaf_jumps = 0x6A
    ccw_autumn_entrance = 0x6B
    ccw_autumn_top = 0x6C
    ccw_autumn_by_house = 0x6D
    ccw_autumn_low_branch = 0x6E
    ccw_winter_flower = 0x6F
    ccw_winter_river_fly_pad = 0x70
    ccw_winter_hive = 0x71
    ccw_winter_nabnut = 0x72
    ccw_winter_sir_slush = 0x73
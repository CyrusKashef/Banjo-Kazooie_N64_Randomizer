'''
Purpose:
*
'''

###################
##### IMPORTS #####
###################

from enum import IntEnum, unique, auto

############################
##### MUSIC ZONE ENUMS #####
############################

@unique
class MUSIC_ZONE_ENUMS(IntEnum):
    # MAP_1_SM_SPIRAL_MOUNTAIN
    spiral_mountain_underwater = auto()
    spiral_mountain_default = auto()
    # MAP_8C_SM_BANJOS_HOUSE
    spiral_mountain_banjos_house_default = auto()


    # MAP_2_MM_MUMBOS_MOUNTAIN
    mumbos_mountain_conga_1 = auto()
    mumbos_mountain_conga_2 = auto()
    mumbos_mountain_juju = auto()
    mumbos_mountain_tickers_tower = auto()
    mumbos_mountain_underwater = auto()
    mumbos_mountain_default = auto()


    # MAP_7_TTC_TREASURE_TROVE_COVE
    treasure_trove_cove_underwater = auto()
    treasure_trove_cove_outside_blubbers_ship = auto()
    # MAP_A_TTC_SANDCASTLE
    treasure_trove_cove_default = auto()
    # MAP_5_TTC_BLUBBERS_SHIP
    treasure_trove_cove_inside_blubbers_ship = auto()
    treasure_trove_cove_inside_sandcastle = auto()


    # MAP_B_CC_CLANKERS_CAVERN
    clankers_cavern_underwater_general = auto()
    clankers_cavern_underwater_deep = auto()
    clankers_cavern_default = auto()
    # MAP_21_CC_WITCH_SWITCH_ROOM
    # MAP_22_CC_INSIDE_CLANKER
    # MAP_23_CC_GOLDFEATHER_ROOM
    clankers_cavern_inside_clanker = auto()


    # MAP_D_BGS_BUBBLEGLOOP_SWAMP
    bubblegloop_swamp_yellow_flibbits = auto()
    bubblegloop_swamp_default = auto()


    # MAP_27_FP_FREEZEEZY_PEAK
    freezeezy_peak_underwater = auto()
    freezeezy_peak_xmas = auto()
    freezeezy_peak_default = auto()
    # MAP_7F_FP_WOZZAS_CAVE
    freezeezy_peak_wozza_cave_underwater = auto()
    freezeezy_peak_wozza_cave_default = auto()


    # MAP_12_GV_GOBIS_VALLEY
    gobis_valley_underwater = auto()
    gobis_valley_outside_jinxy = auto()
    gobis_valley_default = auto()
    # MAP_13_GV_MEMORY_GAME
    # MAP_14_GV_SANDYBUTTS_MAZE
    # MAP_15_GV_WATER_PYRAMID
    # MAP_16_GV_RUBEES_CHAMBER
    # MAP_1A_GV_INSIDE_JINXY
    gobis_valley_inside_pyramids = auto()


    # MAP_25_MMM_WELL
    # MAP_2F_MMM_WATERDRAIN_BARREL
    mad_monster_mansion_well_drain = auto()
    # MAP_1B_MMM_MAD_MONSTER_MANSION
    mad_monster_mansion_default = auto()
    # MAP_1D_MMM_CELLAR
    mad_monster_mansion_cellar_default = auto()


    # MAP_31_RBB_RUSTY_BUCKET_BAY
    ship_bow = auto()
    rusty_bucket_bay_underwater = auto()
    rusty_bucket_bay_default = auto()
    # MAP_35_RBB_WAREHOUSE
    # MAP_36_RBB_BOATHOUSE
    # MAP_37_RBB_CONTAINER_1
    # MAP_38_RBB_CONTAINER_3
    # MAP_3E_RBB_CONTAINER_2
    rusty_bucket_bay_container_houses = auto()
    # MAP_8B_RBB_ANCHOR_ROOM
    rusty_bucket_bay_anchor_room_underwater = auto()
    rusty_bucket_bay_anchor_room_default = auto()
    # MAP_34_RBB_ENGINE_ROOM
    rusty_bucket_bay_engine_room_underwater = auto()
    rusty_bucket_bay_engine_room_default = auto()


    # MAP_40_CCW_HUB
    click_clock_wood_hub_center = auto()
    click_clock_wood_hub_spring = auto()
    click_clock_wood_hub_summer = auto()
    click_clock_wood_hub_autumn = auto()
    click_clock_wood_hub_winter = auto()
    # MAP_43_CCW_SPRING
    click_clock_wood_spring_default = auto()
    # MAP_65_CCW_SPRING_WHIPCRACK_ROOM
    click_clock_wood_spring_whipcrack = auto()
    # MAP_5E_CCW_SPRING_NABNUTS_HOUSE
    click_clock_wood_spring_nabnut = auto()
    # MAP_66_CCW_SUMMER_WHIPCRACK_ROOM
    click_clock_wood_summer_whipcrack = auto()
    # MAP_5F_CCW_SUMMER_NABNUTS_HOUSE
    click_clock_wood_summer_nabnut = auto()
    # MAP_45_CCW_AUTUMN
    click_clock_wood_autumn_underwater = auto()
    click_clock_wood_autumn_default = auto()
    # MAP_67_CCW_AUTUMN_WHIPCRACK_ROOM
    click_clock_wood_autumn_whipcrack = auto()
    # MAP_60_CCW_AUTUMN_NABNUTS_HOUSE
    click_clock_wood_autumn_nabnut = auto()
    # MAP_63_CCW_AUTUMN_NABNUTS_WATER_SUPPLY
    click_clock_wood_autumn_flooded_room = auto()
    # MAP_46_CCW_WINTER
    click_clock_wood_winter_default = auto()
    # MAP_68_CCW_WINTER_WHIPCRACK_ROOM
    click_clock_wood_winter_whipcrack = auto()
    # MAP_61_CCW_WINTER_NABNUTS_HOUSE
    click_clock_wood_winter_nabnut = auto()
    # MAP_64_CCW_WINTER_NABNUTS_WATER_SUPPLY
    click_clock_wood_winter_flooded_room = auto()


    # MAP_69_GL_MM_LOBBY
    gruntildas_lair_mumbos_mountain_entrance = auto()
    gruntildas_lair_mumbos_mountain_default = auto()
    # MAP_6A_GL_TTC_AND_CC_PUZZLE
    gruntildas_lair_cc_podium = auto()
    gruntildas_lair_ttc_podium = auto()
    gruntildas_lair_ttc_cc_puzzles_default = auto()
    # MAP_6B_GL_180_NOTE_DOOR
    gruntildas_lair_ccw_puzzle_underwater = auto()
    gruntildas_lair_ccw_puzzle_podium = auto()
    gruntildas_lair_ccw_puzzle_ttc_entrance = auto()
    gruntildas_lair_ccw_puzzle_default = auto()
    # MAP_6C_GL_RED_CAULDRON_ROOM
    gruntildas_lair_cauldron_pipe_default = auto()
    # MAP_6D_GL_TTC_LOBBY
    gruntildas_lair_ttc_entrance_default = auto()
    # MAP_70_GL_CC_LOBBY
    gruntildas_lair_clankers_cavern_underwater = auto()
    gruntildas_lair_clankers_cavern_entrance = auto()
    gruntildas_lair_clankers_cavern_default = auto()
    # MAP_6E_GL_GV_LOBBY
    gruntildas_lair_gobis_valley_entrance = auto()
    gruntildas_lair_gobis_valley_default = auto()
    # MAP_6F_GL_FP_LOBBY
    gruntildas_lair_freezeezy_peak_entrance = auto()
    gruntildas_lair_freezeezy_peak_default = auto()
    # MAP_74_GL_GV_PUZZLE
    gruntildas_lair_gobis_valley_puzzle_podium = auto()
    gruntildas_lair_gobis_valley_puzzle_default = auto()
    # MAP_75_GL_MMM_LOBBY
    # MAP_7A_GL_CRYPT
    gruntildas_lair_mad_monster_mansion_default = auto()
    # MAP_71_GL_STATUE_ROOM
    gruntildas_lair_grunty_statue_underwater = auto()
    gruntildas_lair_grunty_statue_bubblegloop_swamp_entrance = auto()
    gruntildas_lair_grunty_statue_default = auto()
    # MAP_72_GL_BGS_LOBBY
    gruntildas_lair_bubblegloop_swamp_entrance = auto()
    gruntildas_lair_bubblegloop_swamp_default = auto()
    # MAP_76_GL_640_NOTE_DOOR
    gruntildas_lair_water_room_underwater = auto()
    gruntildas_lair_water_room_default = auto()
    # MAP_77_GL_RBB_LOBBY
    gruntildas_lair_rusty_bucket_bay_underwater = auto()
    gruntildas_lair_rusty_bucket_bay_default = auto()
    # MAP_78_GL_RBB_AND_MMM_PUZZLE
    gruntildas_lair_rbb_mmm_puzzle_underwater = auto()
    gruntildas_lair_mmm_podium = auto()
    gruntildas_lair_rbb_mmm_puzzle_center_area = auto()
    gruntildas_lair_rbb_mmm_puzzle_default = auto()
    # MAP_79_GL_CCW_LOBBY
    gruntildas_lair_click_clock_wood_token_entrance = auto()
    gruntildas_lair_click_clock_wood_whipcrack_entrance = auto()
    gruntildas_lair_click_clock_wood_default = auto()
    # MAP_80_GL_FF_ENTRANCE
    gruntildas_lair_path_to_furnace_fun_door_entrance = auto()
    gruntildas_lair_path_to_furnace_fun_default = auto()

    # MAP_91_FILE_SELECT
    file_select_file_one = auto()
    file_select_file_two_three = auto()

    # MAP_3_UNUSED
    unused_1_default = auto()
    # MAP_54_UNUSED
    # MAP_55_UNUSED
    # MAP_57_UNUSED
    # MAP_58_UNUSED
    # MAP_59_UNUSED
    unused_2_default = auto()
    # MAP_56_UNUSED
    unused_3_default = auto()
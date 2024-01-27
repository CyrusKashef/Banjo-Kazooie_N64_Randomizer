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
class MAP_SETUP_ASSET_ID(IntEnum):
    spiral_mountain_main = 0x071D,
    mumbos_mountain_main = 0x071E,
    treasure_trove_cove_blubbers_ship = 0x0721,
    treasure_trove_cove_nippers_shell = 0x0722,
    treasure_trove_cove_treasure_trove_cove = 0x0723,
    treasure_trove_cove_sandcastle = 0x0726,
    clankers_cavern_main = 0x0727,
    mumbos_mountain_termite_hill = 0x0728,
    bubblegloop_swamp_main = 0x0729,
    mumbos_mountain_mumbos_skull = 0x072A,
    bubblegloop_swamp_mr_vile = 0x072C,
    bubblegloop_swamp_tip_tup_chior = 0x072D,
    gobis_valley_main = 0x072E,
    gobis_valley_matching_puzzle = 0x072F,
    gobis_valley_king_sandybutts_tomb = 0x0730,
    gobis_valley_water_pyramid = 0x0731,
    gobis_valley_rupee = 0x0732,
    gobis_valley_jinxy = 0x0736,
    mad_monster_mansion_main = 0x0737,
    mad_monster_mansion_church_main = 0x0738,
    mad_monster_mansion_cellar = 0x0739,
    cutscene_intro = 0x073A,
    cutscene_n64_logo = 0x073B,
    cutscene_beach_ending_without_100_jiggies = 0x073C,
    clankers_cavern_blowhole = 0x073D,
    clankers_cavern_mouth_belly = 0x073E,
    clankers_cavern_wonderwing = 0x073F,
    mad_monster_mansion_tumblar = 0x0740,
    mad_monster_mansion_well = 0x0741,
    mad_monster_mansion_dining_room = 0x0742,
    freezeezy_peak_main = 0x0743,
    mad_monster_mansion_egg_room = 0x0744,
    mad_monster_mansion_note_room = 0x0745,
    mad_monster_mansion_red_feather_room = 0x0746,
    mad_monster_mansion_secret_church_room = 0x0747,
    mad_monster_mansion_bathroom = 0x0748,
    mad_monster_mansion_bedroom = 0x0749,
    mad_monster_mansion_honeycomb_room = 0x074A,
    mad_monster_mansion_drainpipe = 0x074B,
    mad_monster_mansion_mumbos_hut = 0x074C,
    rusty_bucket_bay_main = 0x074D,
    rusty_bucket_bay_engine_room = 0x0750,
    rusty_bucket_bay_chump_warehouse = 0x0751,
    rusty_bucket_bay_boat_room = 0x0752,
    rusty_bucket_bay_chompa_container = 0x0753,
    rusty_bucket_bay_boom_box_container = 0x0754,
    rusty_bucket_bay_cabin_window = 0x0755,
    rusty_bucket_bay_boss_boom_box_room = 0x0756,
    rusty_bucket_bay_boom_box_pipe = 0x0757,
    rusty_bucket_bay_kitchen_pipe = 0x0758,
    rusty_bucket_bay_navigation_window = 0x0759,
    rusty_bucket_bay_seaman_grublins_container = 0x075A,
    rusty_bucket_bay_captains_window = 0x075B,
    click_clock_wood_main_hub = 0x075C,
    freezeezy_peak_igloo = 0x075D,
    click_clock_woods_spring_main = 0x075F,
    click_clock_woods_summer_main = 0x0760,
    click_clock_woods_autumn_main = 0x0761,
    click_clock_woods_winter_main = 0x0762,
    bubblegloop_swamp_mumbos_skull = 0x0763,
    freezeezy_peak_mumbos_skull = 0x0764,
    click_clock_wood_spring_mumbos_skull = 0x0766,
    click_clock_wood_summer_mumbos_skull = 0x0767,
    click_clock_wood_autumn_mumbos_skull = 0x0768,
    click_clock_wood_winter_mumbos_skull = 0x0769,
    freezeezy_peak_christmas_tree = 0x076F,
    click_clock_wood_summer_zubbas = 0x0776,
    click_clock_wood_spring_zubbas = 0x0777,
    click_clock_wood_autumn_zubbas = 0x0778,
    click_clock_wood_spring_nabnuts = 0x077A,
    click_clock_wood_summer_nabnuts = 0x077B,
    click_clock_wood_autumn_nabnuts = 0x077C,
    click_clock_wood_winter_nabnuts = 0x077D,
    click_clock_wood_winter_acorn_attic = 0x077E,
    click_clock_wood_autumn_flooded_attic = 0x077F,
    click_clock_wood_winter_flooded_attic = 0x0780,
    click_clock_wood_spring_whipcracks = 0x0781,
    click_clock_wood_summer_whipcracks = 0x0782,
    click_clock_wood_autumn_whipcracks = 0x0783,
    click_clock_wood_winter_whipcracks = 0x0784,
    gruntildas_lair_mumbos_mountain_entrance = 0x0785,
    gruntildas_lair_treasure_trove_cove_clankers_cavern_puzzles = 0x0786,
    gruntildas_lair_click_clock_wood_puzzle = 0x0787,
    gruntildas_lair_cauldron_pipe_room = 0x0788,
    gruntildas_lair_treasure_trove_cove_entrance = 0x0789,
    gruntildas_lair_gobis_valley_entrance = 0x078A,
    gruntildas_lair_freezeezy_peak_entrance = 0x078B,
    gruntildas_lair_clankers_cavern_entrance = 0x078C,
    gruntildas_lair_pointing_grunty_statue = 0x078D,
    gruntildas_lair_bubblegloop_swamp_entrance = 0x078E,
    gruntildas_lair_gobis_valley_puzzle = 0x0790,
    gruntildas_lair_mad_monster_mansion_entrance = 0x0791,
    gruntildas_lair_640_note_door = 0x0792,
    gruntildas_lair_rusty_bucket_bay_entrance = 0x0793,
    gruntildas_lair_mad_monster_mansion_rusty_bucket_bay_puzzle = 0x0794,
    gruntildas_lair_click_clock_wood_entrance = 0x0795,
    gruntildas_lair_mad_monster_mansion_crypt = 0x0796,
    cutscene_lair_hallway_then_open_door = 0x0797,
    cutscene_banjo_sleeping = 0x0798,
    cutscene_tooty_running_to_bottles = 0x0799,
    freezeezy_peak_wozzas_cave = 0x079B,
    gruntildas_lair_path_to_quiz_show = 0x079C,
    cutscene_grunty_running_out_door = 0x079D,
    cutscene_enter_gruntildas_lair_cutscene = 0x079E,
    cutscene_game_over = 0x079F,
    cutscene_outside_tower_thunder = 0x07A1,
    cutscene_gruntilda_rides_outside_her_lair = 0x07A2,
    cutscene_gruntilda_falling_towards_ground = 0x07A3,
    cutscene_gruntilda_hits_ground = 0x07A4,
    cutscene_tootys_being_captured = 0x07A5,
    # test_house = 0x07A6,
    rusty_bucket_bay_anchor_room = 0x07A7,
    spiral_mountain_banjos_house = 0x07A8,
    mad_monster_mansion_inside_loggo = 0x07A9,
    gruntildas_lair_furnace_fun = 0x07AA,
    treasure_trove_cove_sharkfood_island = 0x07AB,
    final_battle_arena = 0x07AC,
    cutscene_game_select = 0x07AD,
    gobis_valley_stop_n_swap_egg = 0x07AE,
    gruntildas_lair_final_battle_puzzle = 0x07AF,
    cutscene_mumbos_barbaque = 0x07B0,
    cutscene_beach_ending_have_100_jiggies = 0x07B1,
    cutscene_beach_about_to_show_cast_list = 0x07B2,
    cutscene_beach_after_pictures = 0x07B3,
    cutscene_klungo_cant_move_boulder_without_100_jiggies = 0x07B4,
    cutscene_klungo_cant_move_boulder_with_100_jiggies = 0x07B5,

# asset_id_path:str = "C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/Map_Setup_Asset_Ids.txt"
# with open(asset_id_path, "r") as asset_id_file:
#     asset_id_readlines:list = asset_id_file.readlines()

# new_file_str:str = ""
# for asset_id_line in asset_id_readlines:
#     asset_id_line_split:list = asset_id_line.split("|")
#     asset_id_str:str = f"0x{asset_id_line_split[1][1:-1]}"
#     asset_description_str:str = (asset_id_line_split[4][4:-1]).replace("= ", "").replace("- ", "").replace(" ", "_").replace("'", "").lower()
#     if(asset_description_str):
#         new_file_str += f"    {asset_description_str}: {asset_id_str},\n"

# new_file_path:str = "C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/Map_Setup_Asset_Ids_Print.txt"
# with open(new_file_path, "w+") as new_file:
#     new_file.write(new_file_str)
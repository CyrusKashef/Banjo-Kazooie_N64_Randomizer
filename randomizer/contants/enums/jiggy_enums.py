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
class JIGGY_ENUMS(IntEnum):
    mumbos_mountain_jinjo = 0x01
    mumbos_mountain_atop_tickers_tower = 0x02
    mumbos_mountain_mumbos_skull_eye = 0x03
    mumbos_mountain_juju = 0x04
    mumbos_mountain_huts = 0x05
    mumbos_mountain_stonehenge = 0x06
    mumbos_mountain_hill = 0x07
    mumbos_mountain_orange_pads = 0x08
    mumbos_mountain_chimp = 0x09
    mumbos_mountain_conga = 0x0A
    treasure_trove_cove_jinjo = 0x0B
    treasure_trove_cove_atop_lighthouse = 0x0C
    treasure_trove_cove_shock_jump_alcove = 0x0D # Confirm?
    treasure_trove_cove_backside_alcove = 0x0E # Confirm?
    treasure_trove_cove_pool = 0x0F
    treasure_trove_cove_sandcastle = 0x10
    treasure_trove_cove_treasure_hunt = 0x11
    treasure_trove_cove_nipper = 0x12
    treasure_trove_cove_lockup = 0x13
    treasure_trove_cove_blubber = 0x14
    clankers_cavern_jinjo = 0x15
    clankers_cavern_mutie_snippets = 0x16
    clankers_cavern_raise_clanker = 0x17
    clankers_cavern_bolt = 0x18
    clankers_cavern_tail = 0x19
    clankers_cavern_long_pipe = 0x1A
    clankers_cavern_tooth = 0x1B
    clankers_cavern_rings = 0x1C
    clankers_cavern_blowhole = 0x1D
    clankers_cavern_wonderwing = 0x1E
    bubblegloop_swamp_jinjo = 0x1F
    bubblegloop_swamp_central_button = 0x20
    bubblegloop_swamp_pink_egg = 0x21
    bubblegloop_swamp_croctus = 0x22
    bubblegloop_swamp_huts = 0x23
    bubblegloop_swamp_yellow_flibbits = 0x24
    bubblegloop_swamp_maze_button = 0x25
    bubblegloop_swamp_tanktup = 0x26
    bubblegloop_swamp_tiptup = 0x27
    bubblegloop_swamp_mr_vile = 0x28
    freezeezy_peak_jinjo = 0x29
    freezeezy_peak_save_boggy = 0x2A
    freezeezy_peak_smoke_pipe = 0x2B
    freezeezy_peak_race_boggy_bk = 0x2C
    freezeezy_peak_snowman_buttons = 0x2D
    freezeezy_peak_presents = 0x2E
    freezeezy_peak_christmas_tree = 0x2F
    freezeezy_peak_race_boggy_walrus = 0x30
    freezeezy_peak_sir_slushes = 0x31
    freezeezy_peak_wozza = 0x32
    gruntildas_lair_1st_jiggy = 0x33
    gruntildas_lair_mumbos_mountain_witch_switch = 0x34
    gruntildas_lair_clankers_cavern_witch_switch = 0x35
    gruntildas_lair_treasure_trove_cove_witch_switch = 0x36
    gruntildas_lair_bubblegloop_swamp_witch_switch = 0x37
    gruntildas_lair_freezeezy_peak_witch_switch = 0x38
    gruntildas_lair_mad_monster_mansion_witch_switch = 0x39
    gruntildas_lair_gobis_valley_witch_switch = 0x3A
    gruntildas_lair_rusty_bucket_bay_witch_switch = 0x3B
    gruntildas_lair_click_clock_wood_witch_switch = 0x3C
    gobis_valley_jinjo = 0x3D
    gobis_valley_grabba = 0x3E
    gobis_valley_jinxy = 0x3F
    gobis_valley_matching_puzzle = 0x40
    gobis_valley_king_sandybutt = 0x41
    gobis_valley_water_pyramid = 0x42
    gobis_valley_rubee = 0x43
    gobis_valley_free_gobi = 0x44
    gobis_valley_trunker = 0x45
    gobis_valley_ancient_ones = 0x46
    click_clock_wood_jinjo = 0x47
    click_clock_wood_treehouse = 0x48
    click_clock_wood_eyrie = 0x49
    click_clock_wood_nabnut = 0x4A
    click_clock_wood_gnawty = 0x4B
    click_clock_wood_zubbas = 0x4C
    click_clock_wood_flower = 0x4D
    click_clock_wood_leaf_jumps = 0x4E
    click_clock_wood_tree_top = 0x4F
    click_clock_wood_whipcrack_room = 0x50
    rusty_bucket_bay_jinjo = 0x51
    rusty_bucket_bay_chump_warehouse = 0x52
    rusty_bucket_bay_snorkel = 0x53
    rusty_bucket_bay_whistles = 0x54
    rusty_bucket_bay_atop_funnel = 0x55
    rusty_bucket_bay_boss_boom_box = 0x56
    rusty_bucket_bay_propeller = 0x57
    rusty_bucket_bay_captains_cabin = 0x58
    rusty_bucket_bay_crane_cage = 0x59
    rusty_bucket_bay_engine_room = 0x5A
    mad_monster_mansion_jinjo = 0x5B
    mad_monster_mansion_well = 0x5C
    mad_monster_mansion_napper = 0x5D
    mad_monster_mansion_cellar = 0x5E
    mad_monster_mansion_church_roof = 0x5F
    mad_monster_mansion_motzand = 0x60
    mad_monster_mansion_rain_barrel = 0x61
    mad_monster_mansion_tumblar = 0x62
    mad_monster_mansion_flower_pots = 0x63
    mad_monster_mansion_loggo = 0x64
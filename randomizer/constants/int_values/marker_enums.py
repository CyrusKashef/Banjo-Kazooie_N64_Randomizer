'''
Each enumerator in the class below is the value used IN GAME.
'''

###################
##### IMPORTS #####
###################

from enum import IntEnum, unique, auto

##########################
##### PARAMETER NAME #####
##########################

class PARAMETERS_ENUM(IntEnum):
    @classmethod
    def get_marker_name(cls, value:int):
        '''
        Pass
        '''
        parameter_name:str = cls(value).name
        return parameter_name

    marker_id = 0
    or_parameter = auto()
    claw_swipe_collisions = auto()
    roll_attack_collisions = auto()
    jump_on_them_collisions = auto()
    rat_a_tat_rap_collisions = auto()
    beak_barge_collisions = auto()
    beak_buster_collisions = auto()
    beak_bomb_collisions = auto()
    egg_firing_collisions = auto()
    wonderwing_collisions = auto()
    croc_bite_collisions = auto()
    other_contact_collisions = auto()

###########################
##### COLLISION ENUMS #####
###########################

class COLLISION_ENUMS(IntEnum):
    bk_effect = auto()
    entity_next_state = auto()
    collision_sfx = auto()
    bk_damage = auto()
    hits_to_trigger = auto()
    item_drop_slot = auto()

###########################
##### MARKER ID ENUMS #####
###########################

@unique
class MARKER_ID_ENUMS(IntEnum):
    @classmethod
    def get_marker_name(cls, value:int):
        '''
        Pass
        '''
        try:
            marker_name:str = cls(value).name
        except ValueError:
            marker_name:str = "Unknown"
        return marker_name

    #
    bigbutt_active = 0x003 # New
    ticker = 0x004
    grublin = 0x005
    mumbo = 0x006
    conga = 0x007
    #
    beta_lilbutt = 0x009 # New
    chimpy = 0x00A
    #
    orange_projectile = 0x00C
    #
    wading_boots = 0x011
    #
    snippet = 0x013
    snacker = 0x014
    #
    yum_yum = 0x015
    #
    concert_banjo_kazooie = 0x017 # New
    concert_mumbo = 0x018 # New
    yellow_jinjo_concert_5 = 0x019 # New
    yellow_jinjo_concert_6 = 0x01A # New
    concert_tooty = 0x01B # New
    nintendo_cube = 0x01C # New
    rareware_logo = 0x01D # New
    yellow_jinjo_concert_7 = 0x01E # New
    yellow_jinjo_concert_8 = 0x01F # New
    yellow_jinjo_concert_9 = 0x020 # New
    yellow_jinjo_concert_10 = 0x021 # New
    unknown_7 = 0x022 # New
    unknown_8 = 0x023 # New
    concert_lilbutt = 0x024 # New
    concert_green_frog = 0x025 # New
    concert_bigbutt = 0x026 # New
    cutscene_gruntilda_on_broomstick = 0x027
    #
    clanker_sawblade = 0x028
    #
    grille_chompa_a = 0x029 # New
    rusty_bucket_bay_whistle_1 = 0x02A # New
    rusty_bucket_bay_whistle_2 = 0x02B # New
    rusty_bucket_bay_whistle_3 = 0x02C # New
    #
    grimlet = 0x02E
    anchor_button = 0x02F
    snorkel = 0x030 # New
    boat_anchor_and_chain = 0x031 # New
    player_shadow = 0x032
    leaky = 0x033
    mad_monster_mansion_flower_pot = 0x034
    #
    orange_collectable = 0x036
    blubbers_gold = 0x037
    turbo_talon_trainers = 0x038
    mumbo_token = 0x039
    #
    scarf_sled = 0x03B
    race_slde = 0x03C
    #
    flight_pad = 0x045
    #
    napper = 0x048
    motzand = 0x049
    clankers_key = 0x04A
    clankers_screw = 0x04B
    clanker_token_tooth_external = 0x04C
    clanker_jiggy_tooth_external = 0x04D
    clanker_token_tooth_internal = 0x04E # New
    clanker_jiggy_tooth_internal = 0x04F # New
    beehive = 0x50 # New
    mumbos_mountain_mud_hut = 0x051
    jiggy = 0x052
    empty_honeycomb = 0x053
    #
    honeycomb = 0x055
    #
    shoe_sparkles_1 = 0x058 # New
    shoe_sparkles_2 = 0x059 # New
    blue_jinjo = 0x05A
    green_jinjo = 0x05B
    orange_jinjo = 0x05C
    pink_jinjo = 0x05D
    yellow_jinjo = 0x5E
    musical_note = 0x05F
    blue_egg_collectable = 0x060
    extra_life = 0x061
    red_arrow = 0x062
    red_question_mark = 0x063
    red_x = 0x064
    shrapnel = 0x065
    orange_pad = 0x066
    juju = 0x067
    jigsaw_dance = 0x068
    chump_1 = 0x069
    gloop = 0x06A
    gloop_bubble = 0x06B
    tanktup = 0x06C
    tanktup_leg = 0x06D
    pink_egg_largest = 0x06E
    yellow_jinjo_concert_11 = 0x06F # New
    banjo_kazooie_low_poly_model = 0x070 # New
    unknown_9 = 0x071 # New
    fire_sparkles = 0x072
    yellow_jinjo_concert_12 = 0x073 # New
    unknown_10 = 0x074 # New
    cutscene_buzzbomb = 0x075 # New
    concert_ant = 0x076 # New
    cutscene_bbq_mumbo = 0x077 # New
    roysten_on_grill = 0x078 # New
    tooty_dingpot_image = 0x079 # New
    dingpot_top = 0x07A # New
    gruntildas_arms = 0x07B # New
    cutscene_gruntilda = 0x07C # New
    cutscene_nibbly = 0x07D # New
    cutscene_dingpot = 0x07E # New
    green_mist = 0x07F # New
    cutscene_bottles = 0x080 # New
    cutscene_bottles_molehill = 0x081 # New
    beauty_machine_room_door = 0x082 # New
    #
    credits_tooty_1 = 0x084 # New
    gruntildas_broomstick = 0x085 # New
    gruntilda_riding_boomstick = 0x086 # New
    yellow_jinjo_concert_13 = 0x087 # New
    banjo_top_half = 0x088 # New
    banjos_bed_cutscene = 0x089 # New
    yellow_jinjo_concert_14 = 0x08A # New
    kazooie_in_backpack_stand = 0x08B # New
    banjo_house_curtains = 0x08C # New
    banjo_house_door = 0x08D # New
    yellow_jinjo_concert_15 = 0x08E # New
    yellow_jinjo_concert_16 = 0x08F # New
    kazooie_wing = 0x090 # New
    demo_jiggy_transition = 0x091 # New
    sexy_gruntilda = 0x092 # New
    ugly_tooty = 0x093 # New
    #
    chimpy_stump = 0x095
    ripper = 0x096
    boggy_2 = 0x097
    #
    teehee = 0x099
    barrel_lid = 0x09A # New
    baddie_shadow = 0x09B # New
    #
    tumblar_door = 0x09C # New
    dining_room_entrance_door = 0x09D # New
    cellar_hatch = 0x09E # New
    locked_gate_left = 0x09F # New
    locked_gate_right_1 = 0x0A0 # New
    salty_hippo_top_hatch = 0x0A1 # New
    church_door = 0x0A2 # New
    blubber = 0x0A3
    lockup_slow = 0x0A4
    nipper_invulnerable = 0x0A5
    grabba = 0x0A6
    magic_carpet_1 = 0x0A7
    king_sandybutt_sarcophagus = 0x0A8
    rubee = 0x0A9
    histup = 0x0AA
    rubees_egg_pot = 0x0AB
    slappa_shadow = 0x0AC # New
    slappa = 0x0AD
    raise_carpets_jinxy_heads = 0x0AE # New
    #
    magic_carpet_shadow = 0x0AF
    magic_carpet_2 = 0x0B0
    sir_slush_body_portion = 0x0B1
    snowball = 0x0B2
    sir_slush_just_hat = 0x0B3
    #
    red_feather_collectable = 0x0B5
    #
    tutorial_bottles = 0x0B7
    #
    bottles_molehill = 0x0B8 # New
    freezeezy_peak_snowman_button = 0x0B9
    christmas_tree = 0x0BA
    sandybutt_jinxy_heads = 0x0BB
    #
    gobi_1 = 0x0BC
    gobi_rope = 0x0BD
    gobi_rock = 0x0BE
    gobi_2 = 0x0BF
    trunker = 0x0C0
    red_flibbit = 0x0C1
    buzzbomb = 0x0C2
    gobi_3 = 0x0C3
    yellow_flibbit_control = 0x0C4
    yellow_flibbit = 0x0C5
    mr_vile_game_control = 0x0C6
    yumblie = 0x0C7
    mr_vile = 0x0C8
    flotsam = 0x0C9
    #
    secret_x_barrel_lid = 0x0D3 # New
    spring_pad = 0x0D4
    bubblegloop_swamp_mud_hut = 0x0D5
    pink_egg_large = 0x0D6
    pink_egg_medium = 0x0D7
    pink_egg_small = 0x0D8
    pink_egg_smallest = 0x0D9
    leafboat = 0x0DA
    buried_treasure = 0x0DB
    big_alligator = 0x0DC
    black_snippet = 0x0DD
    black_snippet_upside_down = 0x0DE
    #
    banjos_bed = 0x0E1 # New
    banjos_chair = 0x0E2 # New
    banjos_kitchen = 0x0E3 # New
    banjo_kazooie_game_select_1 = 0x0E4 # New
    banjo_kazooie_game_select_2 = 0x0E5 # New
    banjo_kazooie_game_select_3 = 0x0E6 # New
    #
    dining_room_exit_door = 0x0E7 # New
    #
    lighthouse_door = 0x0EA
    gobis_valley_banjo_door = 0x0EB
    gobis_valley_sun_switch = 0x0EC
    gobis_valley_sun_door = 0x0ED
    #
    gobis_valley_star_hatch = 0x0EF
    gobis_valley_kazooie_rubee_door = 0x0F0
    gobis_valley_star_switch = 0x0F1
    honeycomb_switch = 0x0F2
    gobis_valley_kazooie_target = 0x0F3
    ancient_one = 0x0F4
    bubblegloop_swamp_central_switch = 0x0F5
    lockup_medium = 0x0F6
    lockup_fast = 0x0F7
    gobis_valley_kazooie_sandybutt_door = 0x0F8
    jinxy = 0x0F9
    unknown_2 = 0x0FA
    gobis_valley_cactus = 0x0FB
    #
    croctus = 0x0FC
    bubblegloop_swamp_maze_switch = 0x0FD
    mad_monster_mansion_clock_switch = 0x0FE
    locked_gate_right_2 = 0xFF # New
    red_feather_used = 0x100 # New
    gold_feather_used = 0x101 # New
    #
    mumbos_mountain_witch_switch = 0x103
    mad_monster_mansion_witch_switch = 0x104
    treasure_trove_cove_witch_switch = 0x105
    rusty_bucket_bay_witch_switch = 0x106
    engine_room_door = 0x107 # New
    captains_room_wooden_door = 0x108 # New
    breakable_brick_wall = 0x109
    #
    treasure_trove_cove_chest_lid = 0x10D # New
    #
    raise_bgs_puzzle_grate_switch = 0x110 # New
    green_pipe_to_clankers_cavern_entrance = 0x111 # New
    blue_pipe_to_clankers_cavern_entrance = 0x112 # New
    raise_pipes_to_clankers_cavern_switch = 0x113 # New
    short_pipe_to_brentilda = 0x114 # New
    raise_pipe_to_brentilda_switch = 0x115 # New
    #
    grate_to_level_3_water_switch = 0x118
    grate_between_mmm_and_rbb_puzzles = 0x119
    grate_to_rusty_bucket_bay_puzzle = 0x11A
    water_1_level_switch = 0x11B
    water_2_level_switch = 0x11C
    water_3_level_switch = 0x11D
    ice_ball_to_cheato = 0x11E # New
    rareware_box = 0x11F # New (Latest)
    #
    glass_eye = 0x121
    #
    mansion_medium_window = 0x123 # New
    boggy_1 = 0x124
    boggy_race_red_flag_1 = 0x125 # New
    boggy_race_red_flag_2 = 0x126 # New
    nibbly = 0x127
    colliwobble_tutorial = 0x128
    bawl_tutorial = 0x129
    topper_tutorial = 0x12A
    attack_tutorial = 0x12B
    #
    click_clock_wood_winter_switch = 0x12C # New
    click_clock_wood_winter_door = 0x12D # New
    click_clock_wood_autumn_switch = 0x12E # New
    click_clock_wood_autumn_door = 0x12F # New
    click_clock_wood_summer_switch = 0x130 # New
    click_clock_wood_summer_door = 0x131 # New
    click_clock_wood_spring_switch = 0x132 # New
    click_clock_wood_spring_door = 0x133 # New
    quarrie = 0x135
    beauty_stealing_machine_1 = 0x136 # New
    klungo_1 = 0x137 # New
    credits_tooty_2 = 0x138 # New
    beauty_stealing_machine_console = 0x139 # New
    beauty_machine_force_field = 0x13A # New
    beauty_stealing_machine_2 = 0x13B # New
    lightning = 0x13C # New
    roysten_in_bowl = 0x13D # New
    cuckoo_clock = 0x13E # New
    yellow_jinjo_concert_1 = 0x13F # New
    yellow_jinjo_concert_2 = 0x140 # New
    yellow_jinjo_concert_3 = 0x141 # New
    yellow_jinjo_concert_4 = 0x142 # New
    klungo_2 = 0x143 # New
    banjo_kazooie_chilling = 0x144 # New
    transformation_mumbo = 0x145 # New
    cutscene_snacker = 0x146 # New
    yellow_jinjo_concert_17 = 0x147 # New
    unknown_11 = 0x148 # New
    bikini_girl = 0x149 # New
    cutscene_captain_blubber = 0x14A # New
    gruntildas_green_boulder = 0x14B # New
    yellow_jinjo_concert_18 = 0x14C # New
    yellow_jinjo_concert_19 = 0x14D # New
    yellow_jinjo_concert_20 = 0x14E # New
    yellow_jinjo_concert_21 = 0x14F # New
    yellow_jinjo_concert_22 = 0x150 # New
    yellow_jinjo_concert_23 = 0x151 # New
    yellow_jinjo_concert_24 = 0x152 # New
    yellow_jinjo_concert_25 = 0x153 # New
    #
    rusty_bucket_bay_empty_honeycomb_button = 0x15F # New
    #
    gobis_valley_witch_switch = 0x161
    bubblegloop_swamp_witch_switch = 0x162
    coffin_lid = 0x163
    gruntilda_floor_picture_eye_1 = 0x164 # New
    gruntilda_floor_picture_eye_2 = 0x165 # New
    clankers_cavern_witch_switch = 0x166
    sharkfood_island = 0x167
    ice_key = 0x168
    sns_egg = 0x169
    #
    snippet_upside_down = 0x16B
    nipper_vulnerable = 0x16C
    cheato_blue_eggs = 0x16D
    cheato_red_feathers = 0x16E
    cheato_gold_feathers = 0x16F
    refill_pillow_blue_eggs = 0x170
    refill_pillow_red_feathers = 0x171
    refill_pillow_gold_feathers = 0x172
    chump_2 = 0x173
    game_over_overlay = 0x174
    #
    banjo_kazooie_sign = 0x175 # New
    copyright_overlay = 0x176
    press_start_overlay = 0x177
    no_controller_overlay = 0x178
    bottles_bonus_jiggy_picture = 0x179 # New
    bottles_bonus_game_hand = 0x17A # New
    blank_picture = 0x17B # New
    the_end_sign = 0x17C # New
    iron_gate_no_lock = 0x17D
    #
    rusty_bucket_bay_toll = 0x182
    #
    rusty_bucket_bay_egg_toll_1 = 0x183
    rusty_bucket_bay_egg_toll_2 = 0x184
    rusty_bucket_bay_rear_propeller = 0x185
    green_slow_propeller_switch = 0x186 # New
    rusty_bucket_bay_thin_shaft_1 = 0x187 # New
    rusty_bucket_bay_spinning_platform_1 = 0x188 # New
    rusty_bucket_bay_spinning_platform_2 = 0x189 # New
    rusty_bucket_bay_spinning_platform_3 = 0x18A # New
    rusty_bucket_bay_small_cog = 0x18B # New
    rusty_bucket_bay_medium_cog = 0x18C # New
    rusty_bucket_bay_large_cog = 0x18D # New
    rusty_bucket_bay_thin_shaft_2 = 0x18E # New
    rusty_bucket_bay_double_shaft_1 = 0x18F # New
    rusty_bucket_bay_double_shaft_2 = 0x190 # New
    engine_room_propeller_1 = 0x191
    engine_room_propeller_2 = 0x192
    engine_room_propeller_3 = 0x193
    grey_slow_propeller_switch = 0x194 # New
    whistle_1_button = 0x195 # New
    whistle_2_button = 0x196 # New
    whistle_3_button = 0x197 # New
    rareware_flag = 0x198 # New
    #
    tiptup = 0x19A
    yellow_choir_turtle = 0x19B
    cyan_choir_turtle = 0x19C
    blue_choir_turtle = 0x19D
    red_choir_turtle = 0x19E
    pink_choir_turtle = 0x19F
    violet_choir_turtle = 0x1A0
    boss_boom_box_largest = 0x1A1
    boss_boom_box_large = 0x1A2
    boss_boom_box_medium = 0x1A3
    boss_boom_box_small = 0x1A4
    gobis_valley_egg_toll = 0x1A5 # New
    beta_vent = 0x1A6 # New
    whiplash = 0x1A7
    #
    clanker_cavern_breakable_grates = 0x1A9 # New
    rusty_bucket_bay_bell_buoy = 0x1AA # New
    row_boat = 0x1AB # New
    zubba_hive_lid = 0x1AC # New
    zubba_honey_lump = 0x1AD # New
    zubba = 0x1AE
    unknown_4 = 0x1AF # Unknown CCW/code_14B0.c
    click_clock_wood_growing_beanstalk = 0x1B0 # New
    click_clock_wood_gobi = 0x1B1
    clucker_attack_1 = 0x1B2
    eyrie_egg = 0x1B3 # New
    eyrie_baby = 0x1B4
    caterpillar = 0x1B5
    eyrie_adult_1 = 0x1B6 # New
    boom_box = 0x1B7
    nabnut_eating_acorns = 0x1B9 # New
    #
    nabnut_belly_full = 0x1BA # New
    nabnut_fall_outside = 0x1BB
    acorn_collectible = 0x1BC # New
    gnawty_swimming = 0x1BD # New
    gnawty_summer = 0x1BE # New
    gnawty_boulder = 0x1BF # New
    #
    click_clock_wood_dead_beanstalk = 0x1C2 # New
    eyrie_snore_z = 0x1C3 # New
    eyrie_adult_2 = 0x1C4 # New
    whipcrack = 0x1C5
    nabnuts_mound_of_acorns = 0x1C6 # New
    nabnuts_girlfriend = 0x1C7 # New
    nabnuts_bedsheets = 0x1C8 # New
    nabnuts_bed = 0x1C9 # New
    nabnut_winter = 0x1CA # New
    nabnut_sleeping = 0x1CB # New
    #
    king_sandybutt_maze_control = 0x1CD
    gnawty_in_den = 0x1CE
    grille_chompa_b = 0x1CF
    clucker_attack_2 = 0x1D0
    portrait_chompa_attack_1 = 0x1D1
    #
    king_sandybutt_pyramid = 0x1D4
    palm_tree = 0x1D5
    #
    bottles = 0x1DF # New
    brentilda = 0x1E0 # New
    furnace_fun_minigame = 0x1E1
    grublin_hood = 0x1E2
    #
    gold_feather_collectible = 0x1E5
    topper_non_tutorial = 0x1E6
    bawl_non_tutorial = 0x1E7
    colliwobble_non_tutorial = 0x1E8
    mumbo_cost_sign = 0x1E9
    red_gruntling = 0x1EA
    #
    black_gruntling = 0x1F1
    mansion_short_window = 0x1F2 # New
    mansion_tall_window = 0x1F3 # New
    #
    toots = 0x1F4
    #
    unknown_12 = 0x1F8 # New
    snarebear = 0x1F9
    moggy = 0x1FA
    soggy = 0x1FB
    groggy = 0x1FC
    blue_present_collectible = 0x1FD
    green_present_collectible = 0x1FE
    red_present_collectible = 0x1FF
    blue_twinkly = 0x200
    green_twinkly = 0x201
    orange_twinkly = 0x202
    red_twinkly = 0x203
    twinklies_box = 0x204 # New
    twinkly_muncher = 0x205
    christmas_tree_switch = 0x206 # New
    christmas_tree_star = 0x207 # New
    blue_present_non_collectible = 0x208
    green_present_non_collectible = 0x209
    red_present_non_collectible = 0x20A
    wozza_outside_cave = 0x20B
    wozzas_jiggy = 0x20C
    boggy_on_sled = 0x20D # New
    unknown_1 = 0x20E # New
    wozza_inside_cave = 0x20F
    glass_christmas_tree = 0x210 # New
    unknown_13 = 0x211 # New
    fiery_rock = 0x212 # New
    #
    bee_swarm = 0x217
    limbo = 0x218
    mum_mum = 0x219
    seaman_grublin = 0x21A
    #
    freezeezy_peak_house = 0x21D # New
    mumbos_skull = 0x21E # New
    mumbos_skull_frozen = 0x21F # New
    stack_of_presents = 0x220 # New
    snowy_bridge_1 = 0x221 # New
    snowy_bridge_2 = 0x222 # New
    snowy_bridge_3 = 0x223 # New
    breakable_floor_cobweb = 0x224
    breakable_wall_cobweb = 0x225
    #
    click_clock_wood_witch_switch = 0x22A
    freezeezy_peak_witch_switch = 0x22B
    freezeezy_peak_hatch_door = 0x22C # New
    rusty_bucket_bay_window_1 = 0x22D # New
    rusty_bucket_bay_window_2 = 0x22E # New
    rusty_bucket_bay_safety_boat_1 = 0x22F # New
    rusty_bucket_bay_safety_boat_2 = 0x230 # New
    #
    warp_cauldron = 0x231
    #
    click_clock_wood_podium_switch = 0x232 # New
    transformation_pad = 0x233 # New
    #
    rusty_bucket_bay_skylights = 0x235 # New
    nabnut_window_1 = 0x236 # New
    nabnut_window_2 = 0x237 # New
    nabnut_window_3 = 0x238 # New
    nabnut_window_4 = 0x239 # New
    gobis_valley_sns_chamber_door = 0x23A
    gobis_valley_sns_sarcophagus = 0x23B
    gobis_valley_sns_switch = 0x23C
    ice_key_barrier_1 = 0x23D # New
    ice_key_barrier_2 = 0x23E # New
    temporary_flight_pad_switch = 0x23F
    temporary_flight_pad = 0x240
    moving_shock_jump_pad_switch = 0x241 # New
    moving_shock_jump_pad = 0x242 # New
    nabnut_door = 0x243
    dingpot = 0x244
    christmas_tree_egg_toll = 0x245
    #
    three_purple_ice_crystals = 0x247 # New
    three_blue_ice_crystals = 0x248 # New
    three_green_ice_crystals = 0x249 # New
    one_large_blue_ice_crystal = 0x24A # New
    one_small_blue_ice_crystal = 0x24B # New
    race_rostrum = 0x24C # New
    finish_banner = 0x24D # New
    start_banner = 0x24E # New
    #
    chinker_large = 0x250
    #
    dead_snarebear = 0x251 # New
    loggo = 0x252
    scabby = 0x253
    portrait_chompa_attack_2 = 0x254
    gruntilda_portrait = 0x255
    fire_fx = 0x256
    blackeye_portrait = 0x257
    tower_portrait = 0x258
    tree_and_moon_portrait = 0x259
    teehee_portrait = 0x25A
    minions_portrait = 0x25B
    gruntilda_fireball_spell = 0x25C
    green_smoke = 0x25D # New
    gruntilda_final_boss_phase_1 = 0x25E
    chinker_small = 0x25F
    gruntilda_final_boss_invulnerable = 0x260
    final_battle_flight_pad = 0x261
    #
    click_clock_wood_whipcrack_door = 0x263
    large_door_to_final_battle = 0x264 # New
    world_entry_pad = 0x265 # New
    #
    lighthouse_a = 0x267 # New
    treasure_trove_cove_stairs_1 = 0x268 # New
    treasure_trove_cove_stairs_2 = 0x269 # New
    #
    lighthouse_b = 0x26A # New
    gnawtys_den = 0x26B # New
    gnawtys_bed = 0x26C # New
    gnawtys_shelves = 0x26D # New
    unknown_5 = 0x26E # New
    unknown_6 = 0x26F # New
    unknown_14 = 0x270 # New
    #
    stone_jinjo = 0x276
    #
    jinjo_statue_base = 0x27A
    final_battle_orange_jinjo = 0x27B
    final_battle_green_jinjo = 0x27C
    final_battle_pink_jinjo = 0x27D
    final_battle_yellow_jinjo = 0x27E
    jinjonator_statue_base = 0x27F
    #
    guntilda_homing_spell = 0x280
    gruntilda_final_boss_phase_2 = 0x281
    gruntilda_final_boss_phase_3 = 0x282
    gruntilda_final_boss_phase_4_and_5 = 0x283
    gruntilda_spell_barrier = 0x284
    jinjonator = 0x285
    boggys_igloo = 0x286
    sir_slush_hat_portion = 0x287
    gruntilda_shadow = 0x288
    freezeey_peak_house_chimney = 0x289 # New
    #
    mumbos_hand_with_picture = 0x294 # New
    blue_gruntilda = 0x295
    purple_teehee = 0x296
    giant_ripper = 0x297
    mum_mum_ball_forme = 0x298
    #
    furnace_fun_prize = 0x29A
    #
    gruntilda_trapping_rock = 0x29D
    bigbutt_knocked_down = 0x29E

############################
##### PARAMETER VALUES #####
############################

class BK_EFFECT_ENUMS(IntEnum):
    @classmethod
    def get_effect_name(cls, value:int):
        '''
        Pass
        '''
        effect_name:str = cls(value).name
        return effect_name

    no_effect_to_bk = 0b0000
    #
    damage_bk_smallest_push = 0b0001
    damage_bk_small_push = 0b0010
    damage_bk_decent_push = 0b0011
    damage_bk_large_push = 0b0100
    damage_bk_largest_push = 0b0101
    #
    bounce_bk_smallest_push = 0b0111
    bounce_bk_small_push = 0b1000
    bounce_bk_decent_push = 0b1001
    bounce_bk_large_push = 0b1010
    bounce_bk_largest_push = 0b1011

class ENTITY_NEXT_STATE_ENUM(IntEnum):
    @classmethod
    def get_state_name(cls, value:int):
        '''
        Pass
        '''
        state_name:str = cls(value).name
        return state_name

    no_next_state = 0b00
    alternate_state = 0b01
    kill_entity = 0b10

class COLLISION_SFX_ENUM(IntEnum):
    @classmethod
    def get_sfx_name(cls, value:int):
        '''
        Pass
        '''
        return cls(value).name

    sfx_0 = 0
    sfx_1 = auto()
    sfx_2 = auto()
    sfx_3 = auto()
    sfx_4 = auto()
    sfx_5 = auto()
    sfx_6 = auto()
    sfx_7 = auto()
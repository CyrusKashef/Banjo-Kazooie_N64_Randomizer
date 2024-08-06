'''
Enumerators from the following class are arbitrary values used to make each instance unique.
'''

###################
##### IMPORTS #####
###################

from enum import IntEnum, unique, auto

##########################
##### ASSET ID ENUMS #####
##########################

@unique
class SPEECH_CONSTANTS(IntEnum):
    @classmethod
    def get_constant_name(cls, value:int):
        constant_name:str = cls(value).name
        return constant_name

    empty_speech = auto()
    generic_speech = auto()
    furnace_fun_gruntilda_question = auto()
    furnace_fun_other_question = auto()
    full_screen = auto()
    top_section = auto()
    bottom_section = auto()
    sprite = auto()
    speech = auto()

@unique
class GENERAL_SPEECH_SPRITE_ENUMS(IntEnum):
    @classmethod
    def get_sprite_name(cls, value:int):
        sprite_name:str = cls(value).name
        return sprite_name

    # Special?
    vile_a_or_b_1 = 0x1
    health_tutorial_a_or_b_2 = 0x2
    boggy_cheats_a_or_b_3 = 0x3
    end_top_bottom_4 = 0x4
    transition_top_bottom_6 = 0x6
    action_7 = 0x7
    selections_8 = 0x8
    counts_9 = 0x9
    # Sprites
    banjo_80 = 0x80
    kazooie_81 = 0x81
    kazooie_82 = 0x82
    bottles_83 = 0x83
    mumbo_84 = 0x84
    chimpy_85 = 0x85
    conga_86 = 0x86
    blubber_87 = 0x87
    nipper_88 = 0x88
    clanker_89 = 0x89
    mutie_snippet_8A = 0x8A
    mr_vile_8B = 0x8B
    choir_member_8C = 0x8C
    tanktup_8D = 0x8D
    yellow_flibbit_8E = 0x8E
    trunker_8F = 0x8F
    rubee_90 = 0x90
    gobi_91 = 0x91
    grabba_92 = 0x92
    napper_93 = 0x93
    yellow_jinjo_94 = 0x94
    green_jinjo_95 = 0x95
    blue_jinjo_96 = 0x96
    pink_jinjo_97 = 0x97
    orange_jinjo_98 = 0x98
    musical_note_99 = 0x99
    mumbo_token_9A = 0x9A
    blue_egg_9B = 0x9B
    red_feather_9C = 0x9C
    gold_feather_9D = 0x9D
    orange_9E = 0x9E
    blubbers_gold_9F = 0x9F
    beehive_A0 = 0xA0
    empty_honeycomb_A1 = 0xA1
    extra_life_A2 = 0xA2
    jiggy_A3 = 0xA3
    beehive_A4 = 0xA4
    wading_boots_A5 = 0xA5
    turbo_trainers_A6 = 0xA6
    piranha_A7 = 0xA7
    ticker_A8 = 0xA8
    juju_A9 = 0xA9
    yum_yum_AA = 0xAA
    little_lockup_AB = 0xAB
    leaky_AC = 0xAC
    gloop_AD = 0xAD
    tiptup_AE = 0xAE
    snacker_AF = 0xAF
    jinxy_B0 = 0xB0
    sand_eel_B1 = 0xB1
    snorkel_B2 = 0xB2
    ancient_one_B3 = 0xB3
    croctus_B4 = 0xB4
    gruntilda_B5 = 0xB5
    tooty_B6 = 0xB6
    boggy_B7 = 0xB7
    wozza_B8 = 0xB8
    motzand_B9 = 0xB9
    tumblar_BA = 0xBA
    mum_mum_BB = 0xBB
    present_BC = 0xBC
    caterpillar_BD = 0xBD
    icy_water_BE = 0xBE
    twinklie_BF = 0xBF
    twinklie_muncher_C0 = 0xC0
    gnawty_C1 = 0xC1
    boss_boom_box_C2 = 0xC2
    zubba_C3 = 0xC3
    nabnut_C4 = 0xC4
    boggys_kids_C5 = 0xC5
    baby_eyrie_C6 = 0xC6
    baby_eyrie_C7 = 0xC7
    baby_eyrie_C8 = 0xC8
    adult_eyrie_C9 = 0xC9
    cauldron_CA = 0xCA
    brentilda_CB = 0xCB
    tooty_CC = 0xCC
    black_snippet_CD = 0xCD
    loggo_CE = 0xCE
    cheato_CF = 0xCF
    present_D0 = 0xD0
    present_D1 = 0xD1
    klungo_D2 = 0xD2
    sexy_grunty_D3 = 0xD3
    ugly_tooty_D4 = 0xD4
    banjo_D5 = 0xD5
    kazooie_D6 = 0xD6
    tooty_D7 = 0xD7
    dingpot_D8 = 0xD8
    mr_vile_D9 = 0xD9
    gruntilda_DA = 0xDA
    lockup_DB = 0xDB
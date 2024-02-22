'''
Purpose:
*
'''

###################
##### IMPORTS #####
###################

from randomizer.constants.str_values.string_constants import STRING_CONSTANTS as STR_CONST
from randomizer.constants.int_values.ability_enums import ABILITY_ENUMS

##########################
##### DICT CONSTANTS #####
##########################

class DICT_CONSTANTS:
    paddings:dict = {
        STR_CONST.asset: {
            STR_CONST.padding_byte: b"\xAA",
            STR_CONST.padding_interval: 0x08,
        },
        STR_CONST.assembly: {
            STR_CONST.padding_byte: b"\x00",
            STR_CONST.padding_interval: 0x10,
        },
    }
    assembly_pointers:dict = {
        STR_CONST.c_libraries: {
            STR_CONST.start_upper:  0x107A,
            STR_CONST.lower_offset: 0x8,
        },
        STR_CONST.game_engine: {
            STR_CONST.start_upper:  0x27FA,
            STR_CONST.lower_offset: 0x28,
        },
        STR_CONST.spiral_mountain: {
            STR_CONST.start_upper:  0x28F2,
            STR_CONST.lower_offset: 0x28,
        },
        STR_CONST.mumbos_mountain: {
            STR_CONST.start_upper:  0x287A,
            STR_CONST.lower_offset: 0x28,
        },
        STR_CONST.treasure_trove_cove: {
            STR_CONST.start_upper:  0x2872,
            STR_CONST.lower_offset: 0x28,
        },
        STR_CONST.clankers_cavern: {
            STR_CONST.start_upper:  0x280A,
            STR_CONST.lower_offset: 0x28,
        },
        STR_CONST.bubblegloop_swamp: {
            STR_CONST.start_upper:  0x2882,
            STR_CONST.lower_offset: 0x28,
        },
        STR_CONST.freezeezy_peak: {
            STR_CONST.start_upper:  0x2892,
            STR_CONST.lower_offset: 0x28,
        },
        STR_CONST.gobis_valley: {
            STR_CONST.start_upper:  0x281A,
            STR_CONST.lower_offset: 0x28,
        },
        STR_CONST.mad_monster_mansion: {
            STR_CONST.start_upper:  0x2812,
            STR_CONST.lower_offset: 0x28,
        },
        STR_CONST.rusty_bucket_bay: {
            STR_CONST.start_upper:  0x288A,
            STR_CONST.lower_offset: 0x28,
        },
        STR_CONST.click_clock_wood: {
            STR_CONST.start_upper:  0x28EA,
            STR_CONST.lower_offset: 0x28,
        },
        STR_CONST.gruntildas_lair: {
            STR_CONST.start_upper:  0x2902,
            STR_CONST.lower_offset: 0x28,
        },
        STR_CONST.cutscenes: {
            STR_CONST.start_upper:  0x28FA,
            STR_CONST.lower_offset: 0x28,
        },
        STR_CONST.final_battle: {
            STR_CONST.start_upper:  0x290A,
            STR_CONST.lower_offset: 0x28,
        },
        STR_CONST.unused_level: {
            STR_CONST.start_upper: 0x2802,
            STR_CONST.lower_offset: 0x28,
        }
    }
    gui_move_enum_dict = {
        STR_CONST.beak_barge: ABILITY_ENUMS.beak_barge,
        STR_CONST.beak_bomb: ABILITY_ENUMS.beak_bomb,
        STR_CONST.beak_buster: ABILITY_ENUMS.beak_buster,
        STR_CONST.claw_swipe: ABILITY_ENUMS.claw_swipe,
        STR_CONST.climb: ABILITY_ENUMS.climb,
        STR_CONST.egg_firing: ABILITY_ENUMS.egg_firing,
        STR_CONST.feather_flap: ABILITY_ENUMS.feathery_flap,
        STR_CONST.flap_flip: ABILITY_ENUMS.flap_flip,
        STR_CONST.flight: ABILITY_ENUMS.flight,
        STR_CONST.high_jump: ABILITY_ENUMS.high_jump,
        STR_CONST.rat_a_tap_rap: ABILITY_ENUMS.rat_a_tat_rap,
        STR_CONST.roll_attack: ABILITY_ENUMS.roll,
        STR_CONST.shock_jump: ABILITY_ENUMS.shock_jump,
        STR_CONST.stilt_stride: ABILITY_ENUMS.stilt_stride,
        STR_CONST.dive: ABILITY_ENUMS.dive,
        STR_CONST.talon_trot: ABILITY_ENUMS.talon_trot,
        STR_CONST.turbo_talon_trot: ABILITY_ENUMS.turbo_talon_trot,
        STR_CONST.wonderwing: ABILITY_ENUMS.wonderwing,
        STR_CONST.open_note_door: ABILITY_ENUMS.note_door,
    }
'''
Purpose:
*
'''

###################
##### IMPORTS #####
###################

from randomizer.constants.int_values.level_enums import LEVEL_ID_ENUMS
from randomizer.constants.int_values.jiggy_enums import JIGGY_ENUMS
from randomizer.constants.int_values.empty_honeycomb_enums import EMPTY_HONEYCOMB_ENUMS
from randomizer.constants.int_values.item_enums import ITEM_ENUMS

from randomizer.constants.str_values.string_constants import STRING_CONSTANTS as STR_CONST

###############################
##### WIN CONDITION DICTS #####
###############################

WIN_CONDITION_FUNCTION_DICT:dict = {
    STR_CONST.level_count: {
        ITEM_ENUMS.note: 0x0C0D1BCD, # itemscore_noteScores_get() # Verify?
        ITEM_ENUMS.jiggy: 0x0C0C846B, # jiggyscore_leveltotal()
        ITEM_ENUMS.empty_honeycomb: 0x0C0C84FE, # honeycombscore_get_level_total() # Verify?
    },
    STR_CONST.total_count: {
        ITEM_ENUMS.note: 0x0C0D1BBB, # itemscore_noteScores_getTotal()
        ITEM_ENUMS.jiggy: 0x0C0C848F, # jiggyscore_total()
        ITEM_ENUMS.mumbo_token: 0x0C0C8599, # mumboscore_get_total()
        ITEM_ENUMS.empty_honeycomb: 0x0C0C8527, # honeycombscore_get_total()
    },
    STR_CONST.item_enum: {
        ITEM_ENUMS.jiggy: 0x0C0C83F8, # jiggyscore_isCollected()
        ITEM_ENUMS.mumbo_token: 0x0C0C8551, # mumboscore_get()
        ITEM_ENUMS.empty_honeycomb: 0x0C0C84BF, # honeycombscore_get() # Verify?
    }
}

WIN_CONDITION_COMMANDS_DICT:dict = {
    STR_CONST.level_count: \
        lambda level_item_count_function, level_enum, count_num, branch_count: [
            level_item_count_function,
            0x24040000 + level_enum, # ADDIU 4, 0, level_enum
            0x28410000 + count_num, # SLTI 1, 2, count_num
            0x14200000 + branch_count, # BNE 3, 0, branch_count
            0x00000000,  # null
        ],
    STR_CONST.total_count: \
        lambda item_count_function, count_num, branch_count: [
            item_count_function,
            0x00000000,  # null
            0x28410000 + count_num, # SLTI 1, 2, count_num
            0x14200000 + branch_count, # BNE 3, 0, branch_count
            0x00000000,  # null
        ],
    STR_CONST.item_enum: \
        lambda item_check_function, item_enum, branch_count: [
            item_check_function,
            0x24040000 + item_enum, # ADDIU 4, 0, item_enum
            0x10400000 + branch_count, # BEQ 2 0 branch_count
            0x00000000,  # null
        ]
}

#################################
##### SAMPLE WIN CONDITIONS #####
#################################

SAMPLE_WIN_CONDITIONS_DICT:dict = {
    STR_CONST.win_condition_all_jinjos: [
        (ITEM_ENUMS.jiggy, None, JIGGY_ENUMS.mumbos_mountain_jinjo),
        (ITEM_ENUMS.jiggy, None, JIGGY_ENUMS.treasure_trove_cove_jinjo),
        (ITEM_ENUMS.jiggy, None, JIGGY_ENUMS.clankers_cavern_jinjo),
        (ITEM_ENUMS.jiggy, None, JIGGY_ENUMS.bubblegloop_swamp_jinjo),
        (ITEM_ENUMS.jiggy, None, JIGGY_ENUMS.freezeezy_peak_jinjo),
        (ITEM_ENUMS.jiggy, None, JIGGY_ENUMS.gobis_valley_jinjo),
        (ITEM_ENUMS.jiggy, None, JIGGY_ENUMS.mad_monster_mansion_jinjo),
        (ITEM_ENUMS.jiggy, None, JIGGY_ENUMS.rusty_bucket_bay_jinjo),
        (ITEM_ENUMS.jiggy, None, JIGGY_ENUMS.click_clock_wood_jinjo),
    ],
    STR_CONST.win_condition_trotless: [
        (ITEM_ENUMS.empty_honeycomb, LEVEL_ID_ENUMS.spiral_mountain, 6),
        (ITEM_ENUMS.jiggy, LEVEL_ID_ENUMS.mumbos_mountain, 10),
        (ITEM_ENUMS.note, LEVEL_ID_ENUMS.mumbos_mountain, 100),
        (ITEM_ENUMS.empty_honeycomb, LEVEL_ID_ENUMS.mumbos_mountain, 2),
        (ITEM_ENUMS.jiggy, None, JIGGY_ENUMS.gruntildas_lair_1st_jiggy),
        (ITEM_ENUMS.jiggy, None, JIGGY_ENUMS.gruntildas_lair_mumbos_mountain_witch_switch),
    ],
}
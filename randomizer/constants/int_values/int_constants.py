'''
Purpose:
*
'''

###################
##### IMPORTS #####
###################

from enum import IntEnum

#############################
##### INTEGER CONSTANTS #####
#############################

class INTEGER_CONSTANTS(IntEnum):
    asset_table_start_index = 0x5E98
    asset_table_end_index = 0x10CC8
    asset_table_offset = 0x10CD0
    asset_table_interval = 0x8
    asset_table_start_id = 0x0000
    asset_table_end_id = 0x15C6
    rom_end_index = 0x1000000
    cic = 0xA3886759
    crc1_index_start = 0x10
    crc2_index_start = 0x14
    check_rom_start_index = 0x1000
    check_rom_end_index = 0x101000
    check_rom_interval = 0x4
    wbits = -15
    end_offset = 0x4
    asm_start_address = 0xF19250
    asm_end_address = 0xFDAA30
    furnace_fun_board_start_index:int = 0xAB0
    furnace_fun_board_end_index:int = 0x168F
    furnace_fun_board_interval:int = 0x20
    sound_question_start_index:int = 0x16A4
    sound_question_end_index:int = 0x1907
    sound_question_interval:int = 0xC
    mini_game_start_index:int = 0x1908
    mini_game_end_index:int = 0x191F
    mini_game_interval:int = 0x4
    picture_question_start_index:int = 0x1920
    picture_question_end_index:int = 0x1AF7
    picture_question_interval:int = 0x4
    cauldron_start_index:int = 0x970
    cauldron_end_index:int = 0x9C0
    cauldron_interval:int = 0X8
    note_door_cost_start_index:int = 0x7CC
    note_door_cost_end_index:int = 0x7E4
    note_door_cost_interval:int = 0x2
    jigsaw_puzzle_cost_start_index:int = 0x1B48
    jigsaw_puzzle_cost_end_index:int = 0x1B74
    jigsaw_puzzle_cost_interval:int = 0x4
    jigsaw_puzzle_starting_bit_offset:int = 0x5D
    jigsaw_puzzle_alloted_bit_count:int = 0x25
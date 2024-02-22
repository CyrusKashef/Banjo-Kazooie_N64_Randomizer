'''
Purpose:
*
'''

###################
##### IMPORTS #####
###################

from randomizer.generic_bin_file_class import Generic_Bin_File_Class

from randomizer.constants.str_values.string_constants import STRING_CONSTANTS as STR_CONST
from randomizer.constants.int_values.int_constants import INTEGER_CONSTANTS as INT_CONST
from randomizer.constants.list_values.list_constants import LIST_CONSTANTS as LIST_CONST

######################################
##### GRUNTILDAS LAIR DATA CLASS #####
######################################

class GRUNTILDAS_LAIR_DATA_CLASS(Generic_Bin_File_Class):
    '''
    Pass
    '''
    def __init__(self, file_name:str):
        '''
        Constructor
        '''
        file_path:str = STR_CONST.extracted_files_dir + file_name + STR_CONST.decompressed_bin_extension
        super().__init__(file_path)
    
    #############################
    ##### NOTE DOORS VALUES #####
    #############################
    
    def read_note_door_values(self):
        '''
        Pass
        '''
        note_door_list:list = []
        for curr_index in range(
                INT_CONST.note_door_cost_start_index,
                INT_CONST.note_door_cost_end_index,
                INT_CONST.note_door_cost_interval):
            note_door_value:int = self._read_bytes_as_int(curr_index, byte_count=2)
            note_door_list.append(note_door_value)
        return note_door_list
    
    def set_note_door_values(self,
            note_door_list:list=LIST_CONST.default_note_door_list):
        '''
        Pass
        '''
        for index_count, curr_index in enumerate(range(
                INT_CONST.note_door_cost_start_index,
                INT_CONST.note_door_cost_end_index,
                INT_CONST.note_door_cost_interval)):
            note_door_value:int = note_door_list[index_count]
            if(note_door_value != None):
                self._write_bytes_from_int(curr_index, note_door_value, byte_count=2)
    
    ###############################
    ##### JIGSAW PUZZLE COSTS #####
    ###############################
    
    def read_jigsaw_puzzle_costs(self):
        '''
        Pass
        '''
        jigsaw_puzzle_list:list = []
        for curr_index in range(
                INT_CONST.jigsaw_puzzle_cost_start_index,
                INT_CONST.jigsaw_puzzle_cost_end_index,
                INT_CONST.jigsaw_puzzle_cost_interval):
            jigsaw_puzzle_cost:int = self._read_bytes_as_int(curr_index, byte_count=1)
            jigsaw_puzzle_list.append(jigsaw_puzzle_cost)
        return jigsaw_puzzle_list
    
    def set_jigsaw_puzzle_costs(self,
            jigsaw_puzzle_list:list=LIST_CONST.default_jiggy_puzzle_list):
        '''
        Pass
        '''
        total_bit_requirement:int = 0
        current_bit_offset = INT_CONST.jigsaw_puzzle_starting_bit_offset
        for index_count, curr_index in enumerate(range(
                INT_CONST.jigsaw_puzzle_cost_start_index,
                INT_CONST.jigsaw_puzzle_cost_end_index,
                INT_CONST.jigsaw_puzzle_cost_interval)):
            jigsaw_puzzle_cost:int = jigsaw_puzzle_list[index_count]
            if(jigsaw_puzzle_cost == None):
                needed_bits = self._read_bytes_as_int(curr_index + 0x1, byte_count=1)
                total_bit_requirement += needed_bits
                self._write_bytes_from_int(curr_index + 0x2, current_bit_offset, byte_count=2)
                current_bit_offset += needed_bits
            else:
                needed_bits = max(jigsaw_puzzle_cost.bit_length(), 1)
                total_bit_requirement += needed_bits
                self._write_bytes_from_int(curr_index, jigsaw_puzzle_cost, byte_count=1)
                self._write_bytes_from_int(curr_index + 0x1, needed_bits, byte_count=1)
                self._write_bytes_from_int(curr_index + 0x2, current_bit_offset, byte_count=2)
                current_bit_offset += needed_bits
        if(total_bit_requirement > INT_CONST.jigsaw_puzzle_alloted_bit_count):
            error_message:str = \
                f"ERROR: set_jigsaw_puzzle_costs: " + \
                f"Attempted to use {total_bit_requirement}/{INT_CONST.jigsaw_puzzle_alloted_bit_count} alloted bits"
            print(error_message)
            raise SystemError(error_message)
    
    ###################
    ### FURNACE FUN ###
    ###################
    # Decomp: lair/code_5ED0.c

    ### TILES
    # You read the board bottom left to top right,
    # with the first one being the first bk square,
    # then going to the first eye square,
    # then going to the extra life tile on the bottom left.
    #                             191 (Finish?)
    # ___ ___ ___ ___ ___ ___ ___ 1EF (Skull Tile)    ___ ___ ___ ___
    # 1E3 1E4 1E5 ___ ___ ___ 1E6 1E7 1E8 1E9 1EA 1EB 1EC 1ED 1EE ___
    # 1DF ___ 1E0 ___ ___ ___ 1E1 ___ ___ ___ ___ 1E2 ___ ___ ___ ___
    # ___ ___ 1D9 1DA 1DB 1DC 1DD ___ ___ ___ ___ 1DE ___ ___ ___ ___
    # ___ ___ 1D6 ___ ___ ___ 1D7 ___ ___ ___ ___ 1D8 ___ ___ ___ ___
    # ___ ___ 1CD ___ ___ ___ 1CE 1CF 1D0 1D1 1D2 1D3 1D4 1D5 ___ ___
    # 1C4 1C5 1C6 1C7 1C8 ___ ___ ___ 1C9 ___ ___ ___ ___ 1CA 1CB 1CC
    # 1C0 ___ ___ ___ 1C1 ___ ___ ___ 1C2 ___ ___ ___ ___ 1C3 ___ ___
    # 1B5 ___ ___ ___ 1B6 1B7 1B8 1B9 1BA 1BB 1BC 1BD 1BE 1BF ___ ___
    # 1AF 1B0 1B1 1B2 1B3 ___ ___ ___ ___ ___ ___ 1B4 ___ ___ ___ ___
    # 1AC ___ ___ ___ 1AD ___ ___ ___ ___ ___ ___ 1AE ___ ___ ___ ___
    # 1A1 ___ ___ ___ 1A2 1A3 1A4 1A5 1A6 1A7 1A8 1A9 1AA 1AB ___ ___
    # ___ ___ ___ ___ ___ 19E ___ ___ 19F ___ ___ ___ ___ 1A0 ___ ___
    # ___ ___ ___ ___ ___ 19B ___ ___ 19C ___ ___ ___ ___ 19D ___ ___
    # ___ 193 194 195 196 197 198 199 19A ___ ___ ___ ___ ___ ___ ___
    # ___ ___ ___ ___ ___ ___ ___ 192 ___ ___ ___ ___ ___ ___ ___ ___
    # ___ ___ ___ ___ ___ ___ ___ 0?? (BK TILE)   ___ ___ ___ ___ ___
    #                           ENTRANCE
    
    def get_furnace_fun_board_dict(self):
        '''
        Pass
        '''
        furnace_fun_board_dict:dict = {}
        for tile_count, curr_index in enumerate(range(
                INT_CONST.furnace_fun_board_start_index, 
                INT_CONST.furnace_fun_board_end_index,
                INT_CONST.furnace_fun_board_interval)):
            furnace_fun_board_dict[tile_count] = {
                STR_CONST.tile_below: self._read_bytes_as_int(curr_index, byte_count=2),
                STR_CONST.tile_left: self._read_bytes_as_int(curr_index + 0x2, byte_count=2),
                STR_CONST.tile_above: self._read_bytes_as_int(curr_index + 0x4, byte_count=2),
                STR_CONST.tile_right: self._read_bytes_as_int(curr_index + 0x6, byte_count=2),
                STR_CONST.tile_type: self._read_bytes_as_int(curr_index + 0x8, byte_count=1),
                STR_CONST.byte_9_unk: self._read_bytes_as_int(curr_index + 0x9, byte_count=1),
                STR_CONST.byte_a_unk: self._read_bytes_as_int(curr_index + 0xA, byte_count=1),
                STR_CONST.byte_b_unk: self._read_bytes_as_int(curr_index + 0xB, byte_count=1),
                STR_CONST.byte_c_unk: self._read_bytes_as_float(curr_index + 0xC),
                STR_CONST.byte_10_unk: self._read_bytes_as_int(curr_index + 0x10, byte_count=1),
                STR_CONST.byte_11_unk: self._read_bytes_as_int(curr_index + 0x11, byte_count=1),
                STR_CONST.byte_12_unk: self._read_bytes_as_int(curr_index + 0x12, byte_count=1),
                STR_CONST.byte_13_unk: self._read_bytes_as_int(curr_index + 0x13, byte_count=1),
                STR_CONST.byte_14_unk: self._read_bytes_as_int(curr_index + 0x14, byte_count=1),
                STR_CONST.byte_15_unk: self._read_bytes_as_int(curr_index + 0x15, byte_count=1),
                STR_CONST.byte_16_unk: self._read_bytes_as_int(curr_index + 0x16, byte_count=1),
                STR_CONST.byte_17_unk: self._read_bytes_as_int(curr_index + 0x17, byte_count=1),
                STR_CONST.byte_18_unk: self._read_bytes_as_int(curr_index + 0x18, byte_count=1),
                STR_CONST.byte_19_unk: self._read_bytes_as_int(curr_index + 0x19, byte_count=1),
                STR_CONST.byte_1a_unk: self._read_bytes_as_int(curr_index + 0x1A, byte_count=1),
                STR_CONST.byte_1b_unk: self._read_bytes_as_int(curr_index + 0x1B, byte_count=1),
                STR_CONST.byte_1c_unk: self._read_bytes_as_int(curr_index + 0x1C, byte_count=1),
                STR_CONST.byte_1d_unk: self._read_bytes_as_int(curr_index + 0x1D, byte_count=1),
                STR_CONST.byte_1e_unk: self._read_bytes_as_int(curr_index + 0x1E, byte_count=1),
                STR_CONST.byte_1f_unk: self._read_bytes_as_int(curr_index + 0x1F, byte_count=1),
            }
        return furnace_fun_board_dict
    
    def set_furnace_fun_board_dict(self, furnace_fun_board_dict:dict):
        '''
        Pass
        '''
        for tile_count, curr_index in enumerate(range(
                INT_CONST.furnace_fun_board_start_index, 
                INT_CONST.furnace_fun_board_end_index,
                INT_CONST.furnace_fun_board_interval)):
            tile_dict:dict = furnace_fun_board_dict[tile_count]
            self._write_bytes_from_int(curr_index, tile_dict[STR_CONST.tile_below], byte_count=2)
            self._write_bytes_from_int(curr_index + 0x2, tile_dict[STR_CONST.tile_left], byte_count=2)
            self._write_bytes_from_int(curr_index + 0x4, tile_dict[STR_CONST.tile_above], byte_count=2)
            self._write_bytes_from_int(curr_index + 0x6, tile_dict[STR_CONST.tile_right], byte_count=2)
            self._write_bytes_from_int(curr_index + 0x8, tile_dict[STR_CONST.tile_type], byte_count=2)
            self._write_bytes_from_int(curr_index + 0x9, tile_dict[STR_CONST.byte_9_unk], byte_count=2)
            self._write_bytes_from_int(curr_index + 0xA, tile_dict[STR_CONST.byte_a_unk], byte_count=2)
            self._write_bytes_from_int(curr_index + 0xB, tile_dict[STR_CONST.byte_b_unk], byte_count=2)
            self._write_bytes_from_float(curr_index + 0xC, tile_dict[STR_CONST.byte_c_unk])
            self._write_bytes_from_int(curr_index + 0x10, tile_dict[STR_CONST.byte_10_unk], byte_count=2)
            self._write_bytes_from_int(curr_index + 0x11, tile_dict[STR_CONST.byte_11_unk], byte_count=2)
            self._write_bytes_from_int(curr_index + 0x12, tile_dict[STR_CONST.byte_12_unk], byte_count=2)
            self._write_bytes_from_int(curr_index + 0x13, tile_dict[STR_CONST.byte_13_unk], byte_count=2)
            self._write_bytes_from_int(curr_index + 0x14, tile_dict[STR_CONST.byte_14_unk], byte_count=2)
            self._write_bytes_from_int(curr_index + 0x15, tile_dict[STR_CONST.byte_15_unk], byte_count=2)
            self._write_bytes_from_int(curr_index + 0x16, tile_dict[STR_CONST.byte_16_unk], byte_count=2)
            self._write_bytes_from_int(curr_index + 0x17, tile_dict[STR_CONST.byte_17_unk], byte_count=2)
            self._write_bytes_from_int(curr_index + 0x18, tile_dict[STR_CONST.byte_18_unk], byte_count=2)
            self._write_bytes_from_int(curr_index + 0x19, tile_dict[STR_CONST.byte_19_unk], byte_count=2)
            self._write_bytes_from_int(curr_index + 0x1A, tile_dict[STR_CONST.byte_1a_unk], byte_count=2)
            self._write_bytes_from_int(curr_index + 0x1B, tile_dict[STR_CONST.byte_1b_unk], byte_count=2)
            self._write_bytes_from_int(curr_index + 0x1C, tile_dict[STR_CONST.byte_1c_unk], byte_count=2)
            self._write_bytes_from_int(curr_index + 0x1D, tile_dict[STR_CONST.byte_1d_unk], byte_count=2)
            self._write_bytes_from_int(curr_index + 0x1E, tile_dict[STR_CONST.byte_1e_unk], byte_count=2)
            self._write_bytes_from_int(curr_index + 0x1F, tile_dict[STR_CONST.byte_1f_unk], byte_count=2)
    
    ### QUESTION COUNT
    # Start, Count
    # {  0x0, 100} # BK
    # { 0x64, 118} # Picture
    # { 0xDA,  51} # Sounds
    # {0x10D,  30} # Grunty
    # {0x12B,   6} # Mini Game
    
    def get_furnace_fun_question_count(self):
        '''
        Pass
        '''
        pass

    def set_furnace_fun_question_count(self):
        '''
        Pass
        '''
        pass

    ### SOUND QUESTIONS
    
    def get_sound_question_dict(self):
        '''
        Pass
        '''
        sound_question_dict:dict = {}
        for sound_count, curr_index in enumerate(range(
                INT_CONST.sound_question_start_index,
                INT_CONST.sound_question_end_index,
                INT_CONST.sound_question_interval)):
            sound_question_dict[sound_count] = {
                STR_CONST.byte_1_unk: self._read_bytes_as_int(curr_index, byte_count=1),
                # 00
                STR_CONST.sound_enum: self._read_bytes_as_int(curr_index + 0x2, byte_count=2),
                STR_CONST.byte_4_unk: self._read_bytes_as_int(curr_index + 0x4, byte_count=2),
                # 00 00
                STR_CONST.byte_8_unk: self._read_bytes_as_float(curr_index + 0x8),
            }
        return sound_question_dict
    
    def set_sound_qusetion_dict(self, sound_question_dict:dict):
        '''
        Pass
        '''
        for sound_count, curr_index in enumerate(range(
                INT_CONST.sound_question_start_index,
                INT_CONST.sound_question_end_index,
                INT_CONST.sound_question_interval)):
            question_dict:dict = sound_question_dict[sound_count]
            self._write_bytes_from_int(curr_index, question_dict[STR_CONST.byte_1_unk], byte_count=1)
            # 00
            self._write_bytes_from_int(curr_index + 0x2, question_dict[STR_CONST.sound_enum], byte_count=2)
            self._write_bytes_from_int(curr_index + 0x4, question_dict[STR_CONST.byte_4_unk], byte_count=2)
            # 00 00
            self._write_bytes_from_float(curr_index + 0x8, question_dict[STR_CONST.byte_8_unk])
    
    ### MINI GAMES

    def _get_mini_game_dict(self):
        '''
        Pass
        '''
        mini_game_dict = {}
        for question_count, curr_index in enumerate(range(
                INT_CONST.mini_game_start_index,
                INT_CONST.mini_game_end_index,
                INT_CONST.mini_game_interval)):
            mini_game_dict[question_count] = {
                STR_CONST.map_enum: self._read_bytes_as_int(curr_index, byte_count=2),
                STR_CONST.state: self._read_bytes_as_int(curr_index + 0x2, byte_count=2),
            }
    
    def _set_mini_game_dict(self, mini_game_dict:dict):
        '''
        Pass
        '''
        for question_count, curr_index in enumerate(range(
                INT_CONST.mini_game_start_index,
                INT_CONST.mini_game_end_index,
                INT_CONST.mini_game_interval)):
            question_dict:dict = mini_game_dict[question_count]
            self._write_bytes_from_int(curr_index, question_dict[STR_CONST.map_enum], byte_count=2)
            self._write_bytes_from_int(curr_index, question_dict[STR_CONST.state], byte_count=2)
    
    ### PICTURE QUESTIONS

    def _get_picture_question_dict(self):
        '''
        Pass
        '''
        picture_question_dict = {}
        for question_count, curr_index in enumerate(range(
                INT_CONST.picture_question_start_index,
                INT_CONST.picture_question_end_index,
                INT_CONST.picture_question_interval)):
            picture_question_dict[question_count] = {
                STR_CONST.map_enum: self._read_bytes_as_int(curr_index, byte_count=2),
                STR_CONST.camera_id: self._read_bytes_as_int(curr_index + 0x2, byte_count=2),
            }
        return picture_question_dict
    
    def _set_picture_question_dict(self, picture_question_dict:dict):
        '''
        Pass
        '''
        for question_count, curr_index in enumerate(range(
                INT_CONST.picture_question_start_index,
                INT_CONST.picture_question_end_index,
                INT_CONST.picture_question_interval)):
            question_dict:dict = picture_question_dict[question_count]
            self._write_bytes_from_int(curr_index, question_dict[STR_CONST.map_enum], byte_count=2)
            self._write_bytes_from_int(curr_index + 0x2, question_dict[STR_CONST.camera_id], byte_count=2)
    
    #################
    ### CAULDRONS ###
    #################
    # Decomp: lair/ch/cauldron.c#L46

    def _get_cauldron_dict(self):
        '''
        Pass
        '''
        cauldron_dict = {}
        for cauldron_count, curr_index in enumerate(range(
                INT_CONST.cauldron_start_index,
                INT_CONST.cauldron_end_index,
                INT_CONST.cauldron_interval)):
            cauldron_dict[cauldron_count] = {
                STR_CONST.map_enum: self._read_bytes_as_int(curr_index, byte_count=1),
                STR_CONST.byte_1_unk: self._read_bytes_as_int(curr_index + 0x1, byte_count=1),
                STR_CONST.entry_point: self._read_bytes_as_int(curr_index + 0x2, byte_count=1),
                STR_CONST.byte_3_unk: self._read_bytes_as_int(curr_index + 0x3, byte_count=1),
                STR_CONST.byte_4_unk: self._read_bytes_as_int(curr_index + 0x4, byte_count=1),
                STR_CONST.byte_5_unk: self._read_bytes_as_int(curr_index + 0x5, byte_count=1),
                STR_CONST.byte_6_unk: self._read_bytes_as_int(curr_index + 0x6, byte_count=2),
            }
        return cauldron_dict

    def _set_cauldron_dict(self, cauldron_dict:dict):
        '''
        Pass
        '''
        for cauldron_count, curr_index in enumerate(range(
                INT_CONST.cauldron_start_index,
                INT_CONST.cauldron_end_index,
                INT_CONST.cauldron_interval)):
            curr_dict:dict = cauldron_dict[cauldron_count]
            self._write_bytes_from_int(curr_index, curr_dict[STR_CONST.map_enum], byte_count=1)
            self._write_bytes_from_int(curr_index + 0x1, curr_dict[STR_CONST.byte_1_unk], byte_count=1)
            self._write_bytes_from_int(curr_index + 0x2, curr_dict[STR_CONST.entry_point], byte_count=1)
            self._write_bytes_from_int(curr_index + 0x3, curr_dict[STR_CONST.byte_3_unk], byte_count=1)
            self._write_bytes_from_int(curr_index + 0x4, curr_dict[STR_CONST.byte_4_unk], byte_count=1)
            self._write_bytes_from_int(curr_index + 0x5, curr_dict[STR_CONST.byte_5_unk], byte_count=1)
            self._write_bytes_from_int(curr_index + 0x6, curr_dict[STR_CONST.byte_6_unk], byte_count=2)
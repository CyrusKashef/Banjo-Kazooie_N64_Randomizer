'''
Purpose:
*
'''

###################
##### IMPORTS #####
###################

from randomizer.generic_bin_file_class import Generic_Bin_File_Class

from randomizer.contants.variables.assembly_variables import \
    EXTRACTED_FILES_DIR, DECOMPRESSED_BIN_EXTENSION

TILE_BELOW_STR:str = "Tile Below"
TILE_LEFT_STR:str = "Tile Left"
TILE_ABOVE_STR:str = "Tile Above"
TILE_RIGHT_STR:str = "Tile Right"
TILE_TYPE_STR:str = "Tile Type"
SOUND_ENUM_STR:str = "Sound Enum"
MAP_STR:str = "Map"
STATE_STR:str = "State"
CAMERA_STR:str = "Camera"
ENTRY_POINT_STR:str = "Entry Point"

UNKNOWN_1_STR:str = "Unknown 1"
UNKNOWN_2_STR:str = "Unknown 2"
UNKNOWN_3_STR:str = "Unknown 3"
UNKNOWN_4_STR:str = "Unknown 4"
UNKNOWN_5_STR:str = "Unknown 5"
UNKNOWN_6_STR:str = "Unknown 6"
UNKNOWN_8_STR:str = "Unknown 8"
UNKNOWN_9_STR:str = "Unknown 9"
UNKNOWN_A_STR:str = "Unknown A"
UNKNOWN_B_STR:str = "Unknown B"
UNKNOWN_C_STR:str = "Unknown C"
UNKNOWN_10_STR:str = "Unknown 10"
UNKNOWN_11_STR:str = "Unknown 11"
UNKNOWN_12_STR:str = "Unknown 12"
UNKNOWN_13_STR:str = "Unknown 13"
UNKNOWN_14_STR:str = "Unknown 14"
UNKNOWN_15_STR:str = "Unknown 15"
UNKNOWN_16_STR:str = "Unknown 16"
UNKNOWN_17_STR:str = "Unknown 17"
UNKNOWN_18_STR:str = "Unknown 18"
UNKNOWN_19_STR:str = "Unknown 19"
UNKNOWN_1A_STR:str = "Unknown 1A"
UNKNOWN_1B_STR:str = "Unknown 1B"
UNKNOWN_1C_STR:str = "Unknown 1C"
UNKNOWN_1D_STR:str = "Unknown 1D"
UNKNOWN_1E_STR:str = "Unknown 1E"
UNKNOWN_1F_STR:str = "Unknown 1F"

FURNACE_FUN_BOARD_START_INDEX:int = 0xAB0
FURNACE_FUN_BOARD_END_INDEX:int = 0x168F
FURNACE_FUN_BOARD_INTERVAL:int = 0x20

SOUND_QUESTION_START_INDEX:int = 0x16A4
SOUND_QUESTION_END_INDEX:int = 0x1907
SOUND_QUESTION_INTERVAL:int = 0xC

MINI_GAME_START_INDEX:int = 0x1908
MINI_GAME_END_INDEX:int = 0x191F
MINI_GAME_INTERVAL:int = 0x4

PICTURE_QUESTION_START_INDEX:int = 0x1920
PICTURE_QUESTION_END_INDEX:int = 0x1AF7
PICTURE_QUESTION_INTERVAL:int = 0x4

CAULDRON_START_INDEX:int = 0x970
CAULDRON_END_INDEX:int = 0x9C0
CAULDRON_INTERVAL:int = 0X8

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
        file_path:str = EXTRACTED_FILES_DIR + file_name + DECOMPRESSED_BIN_EXTENSION
        super().__init__(file_path)
    
    #############################
    ##### NOTE DOORS VALUES #####
    #############################
    
    def read_note_door_values(self):
        '''
        Pass
        '''
        note_door_list:list = []
        for curr_index in range(0x7CC, 0x7E4, 0x2):
            note_door_value:int = self._read_bytes_as_int(curr_index, byte_count=2)
            note_door_list.append(note_door_value)
        return note_door_list
    
    def set_note_door_values(self,
            note_door_list:list=[
                50, 180, 260, 350, 450, 640,
                765, 810, 828, 846, 864, 882]):
        '''
        Pass
        '''
        for index_count, curr_index in enumerate(range(0x7CC, 0x7E4, 0x2)):
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
        for curr_index in range(0x1B48, 0x1B74, 0x4):
            jigsaw_puzzle_cost:int = self._read_bytes_as_int(curr_index, byte_count=1)
            jigsaw_puzzle_list.append(jigsaw_puzzle_cost)
        return jigsaw_puzzle_list
    
    def set_jigsaw_puzzle_costs(self,
            jigsaw_puzzle_list:list=[
                1, 2, 5, 7, 8, 9,
                10, 12, 15, 25, 4]):
        '''
        Pass
        '''
        total_bit_requirement:int = 0
        current_bit_offset = 0x5D
        for index_count, curr_index in enumerate(range(0x1B48, 0x1B74, 0x4)):
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
        if(total_bit_requirement > 37):
            error_message:str = f"ERROR: set_jigsaw_puzzle_costs: Attempted to use {total_bit_requirement}/37 alloted bits"
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
                FURNACE_FUN_BOARD_START_INDEX, 
                FURNACE_FUN_BOARD_END_INDEX,
                FURNACE_FUN_BOARD_INTERVAL)):
            furnace_fun_board_dict[tile_count] = {
                TILE_BELOW_STR: self._read_bytes_as_int(curr_index, byte_count=2),
                TILE_LEFT_STR: self._read_bytes_as_int(curr_index + 0x2, byte_count=2),
                TILE_ABOVE_STR: self._read_bytes_as_int(curr_index + 0x4, byte_count=2),
                TILE_RIGHT_STR: self._read_bytes_as_int(curr_index + 0x6, byte_count=2),
                TILE_TYPE_STR: self._read_bytes_as_int(curr_index + 0x8, byte_count=1),
                UNKNOWN_9_STR: self._read_bytes_as_int(curr_index + 0x9, byte_count=1),
                UNKNOWN_A_STR: self._read_bytes_as_int(curr_index + 0xA, byte_count=1),
                UNKNOWN_B_STR: self._read_bytes_as_int(curr_index + 0xB, byte_count=1),
                UNKNOWN_C_STR: self._read_bytes_as_float(curr_index + 0xC),
                UNKNOWN_10_STR: self._read_bytes_as_int(curr_index + 0x10, byte_count=1),
                UNKNOWN_11_STR: self._read_bytes_as_int(curr_index + 0x11, byte_count=1),
                UNKNOWN_12_STR: self._read_bytes_as_int(curr_index + 0x12, byte_count=1),
                UNKNOWN_13_STR: self._read_bytes_as_int(curr_index + 0x13, byte_count=1),
                UNKNOWN_14_STR: self._read_bytes_as_int(curr_index + 0x14, byte_count=1),
                UNKNOWN_15_STR: self._read_bytes_as_int(curr_index + 0x15, byte_count=1),
                UNKNOWN_16_STR: self._read_bytes_as_int(curr_index + 0x16, byte_count=1),
                UNKNOWN_17_STR: self._read_bytes_as_int(curr_index + 0x17, byte_count=1),
                UNKNOWN_18_STR: self._read_bytes_as_int(curr_index + 0x18, byte_count=1),
                UNKNOWN_19_STR: self._read_bytes_as_int(curr_index + 0x19, byte_count=1),
                UNKNOWN_1A_STR: self._read_bytes_as_int(curr_index + 0x1A, byte_count=1),
                UNKNOWN_1B_STR: self._read_bytes_as_int(curr_index + 0x1B, byte_count=1),
                UNKNOWN_1C_STR: self._read_bytes_as_int(curr_index + 0x1C, byte_count=1),
                UNKNOWN_1D_STR: self._read_bytes_as_int(curr_index + 0x1D, byte_count=1),
                UNKNOWN_1E_STR: self._read_bytes_as_int(curr_index + 0x1E, byte_count=1),
                UNKNOWN_1F_STR: self._read_bytes_as_int(curr_index + 0x1F, byte_count=1),
            }
        return furnace_fun_board_dict
    
    def set_furnace_fun_board_dict(self, furnace_fun_board_dict:dict):
        '''
        Pass
        '''
        for tile_count, curr_index in enumerate(range(
                FURNACE_FUN_BOARD_START_INDEX, 
                FURNACE_FUN_BOARD_END_INDEX,
                FURNACE_FUN_BOARD_INTERVAL)):
            tile_dict:dict = furnace_fun_board_dict[tile_count]
            self._write_bytes_from_int(curr_index, tile_dict[TILE_BELOW_STR], byte_count=2)
            self._write_bytes_from_int(curr_index + 0x2, tile_dict[TILE_LEFT_STR], byte_count=2)
            self._write_bytes_from_int(curr_index + 0x4, tile_dict[TILE_ABOVE_STR], byte_count=2)
            self._write_bytes_from_int(curr_index + 0x6, tile_dict[TILE_RIGHT_STR], byte_count=2)
            self._write_bytes_from_int(curr_index + 0x8, tile_dict[TILE_TYPE_STR], byte_count=2)
            self._write_bytes_from_int(curr_index + 0x9, tile_dict[UNKNOWN_9_STR], byte_count=2)
            self._write_bytes_from_int(curr_index + 0xA, tile_dict[UNKNOWN_A_STR], byte_count=2)
            self._write_bytes_from_int(curr_index + 0xB, tile_dict[UNKNOWN_B_STR], byte_count=2)
            self._write_bytes_from_float(curr_index + 0xC, tile_dict[UNKNOWN_C_STR])
            self._write_bytes_from_int(curr_index + 0x10, tile_dict[UNKNOWN_10_STR], byte_count=2)
            self._write_bytes_from_int(curr_index + 0x11, tile_dict[UNKNOWN_11_STR], byte_count=2)
            self._write_bytes_from_int(curr_index + 0x12, tile_dict[UNKNOWN_12_STR], byte_count=2)
            self._write_bytes_from_int(curr_index + 0x13, tile_dict[UNKNOWN_13_STR], byte_count=2)
            self._write_bytes_from_int(curr_index + 0x14, tile_dict[UNKNOWN_14_STR], byte_count=2)
            self._write_bytes_from_int(curr_index + 0x15, tile_dict[UNKNOWN_15_STR], byte_count=2)
            self._write_bytes_from_int(curr_index + 0x16, tile_dict[UNKNOWN_16_STR], byte_count=2)
            self._write_bytes_from_int(curr_index + 0x17, tile_dict[UNKNOWN_17_STR], byte_count=2)
            self._write_bytes_from_int(curr_index + 0x18, tile_dict[UNKNOWN_18_STR], byte_count=2)
            self._write_bytes_from_int(curr_index + 0x19, tile_dict[UNKNOWN_19_STR], byte_count=2)
            self._write_bytes_from_int(curr_index + 0x1A, tile_dict[UNKNOWN_1A_STR], byte_count=2)
            self._write_bytes_from_int(curr_index + 0x1B, tile_dict[UNKNOWN_1B_STR], byte_count=2)
            self._write_bytes_from_int(curr_index + 0x1C, tile_dict[UNKNOWN_1C_STR], byte_count=2)
            self._write_bytes_from_int(curr_index + 0x1D, tile_dict[UNKNOWN_1D_STR], byte_count=2)
            self._write_bytes_from_int(curr_index + 0x1E, tile_dict[UNKNOWN_1E_STR], byte_count=2)
            self._write_bytes_from_int(curr_index + 0x1F, tile_dict[UNKNOWN_1F_STR], byte_count=2)
    
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
                SOUND_QUESTION_START_INDEX,
                SOUND_QUESTION_END_INDEX,
                SOUND_QUESTION_INTERVAL)):
            sound_question_dict[sound_count] = {
                UNKNOWN_1_STR: self._read_bytes_as_int(curr_index, byte_count=1),
                # 00
                SOUND_ENUM_STR: self._read_bytes_as_int(curr_index + 0x2, byte_count=2),
                UNKNOWN_4_STR: self._read_bytes_as_int(curr_index + 0x4, byte_count=2),
                # 00 00
                UNKNOWN_8_STR: self._read_bytes_as_float(curr_index + 0x8),
            }
        return sound_question_dict
    
    def set_sound_qusetion_dict(self, sound_question_dict:dict):
        '''
        Pass
        '''
        for sound_count, curr_index in enumerate(range(
                SOUND_QUESTION_START_INDEX,
                SOUND_QUESTION_END_INDEX,
                SOUND_QUESTION_INTERVAL)):
            question_dict:dict = sound_question_dict[sound_count]
            self._write_bytes_from_int(curr_index, question_dict[UNKNOWN_1_STR], byte_count=1)
            # 00
            self._write_bytes_from_int(curr_index + 0x2, question_dict[SOUND_ENUM_STR], byte_count=2)
            self._write_bytes_from_int(curr_index + 0x4, question_dict[UNKNOWN_4_STR], byte_count=2)
            # 00 00
            self._write_bytes_from_float(curr_index + 0x8, question_dict[UNKNOWN_8_STR])
    
    ### MINI GAMES

    def _get_mini_game_dict(self):
        '''
        Pass
        '''
        mini_game_dict = {}
        for question_count, curr_index in enumerate(range(
                MINI_GAME_START_INDEX,
                MINI_GAME_END_INDEX,
                MINI_GAME_INTERVAL)):
            mini_game_dict[question_count] = {
                MAP_STR: self._read_bytes_as_int(curr_index, byte_count=2),
                STATE_STR: self._read_bytes_as_int(curr_index + 0x2, byte_count=2),
            }
    
    def _set_mini_game_dict(self, mini_game_dict:dict):
        '''
        Pass
        '''
        for question_count, curr_index in enumerate(range(
                MINI_GAME_START_INDEX,
                MINI_GAME_END_INDEX,
                MINI_GAME_INTERVAL)):
            question_dict:dict = mini_game_dict[question_count]
            self._write_bytes_from_int(curr_index, question_dict[MAP_STR], byte_count=2)
            self._write_bytes_from_int(curr_index, question_dict[STATE_STR], byte_count=2)
    
    ### PICTURE QUESTIONS

    def _get_picture_question_dict(self):
        '''
        Pass
        '''
        picture_question_dict = {}
        for question_count, curr_index in enumerate(range(
                PICTURE_QUESTION_START_INDEX,
                PICTURE_QUESTION_END_INDEX,
                PICTURE_QUESTION_INTERVAL)):
            picture_question_dict[question_count] = {
                MAP_STR: self._read_bytes_as_int(curr_index, byte_count=2),
                CAMERA_STR: self._read_bytes_as_int(curr_index + 0x2, byte_count=2),
            }
    
    def _set_picture_question_dict(self, picture_question_dict:dict):
        '''
        Pass
        '''
        for question_count, curr_index in enumerate(range(
                PICTURE_QUESTION_START_INDEX,
                PICTURE_QUESTION_END_INDEX,
                PICTURE_QUESTION_INTERVAL)):
            question_dict:dict = picture_question_dict[question_count]
            self._write_bytes_from_int(curr_index, question_dict[MAP_STR], byte_count=2)
            self._write_bytes_from_int(curr_index, question_dict[CAMERA_STR], byte_count=2)
    
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
                CAULDRON_START_INDEX,
                CAULDRON_END_INDEX,
                CAULDRON_INTERVAL)):
            cauldron_dict[cauldron_count] = {
                MAP_STR: self._read_bytes_as_int(curr_index, byte_count=1),
                UNKNOWN_1_STR: self._read_bytes_as_int(curr_index + 0x1, byte_count=1),
                ENTRY_POINT_STR: self._read_bytes_as_int(curr_index + 0x2, byte_count=1),
                UNKNOWN_3_STR: self._read_bytes_as_int(curr_index + 0x3, byte_count=1),
                UNKNOWN_4_STR: self._read_bytes_as_int(curr_index + 0x4, byte_count=1),
                UNKNOWN_5_STR: self._read_bytes_as_int(curr_index + 0x5, byte_count=1),
                UNKNOWN_6_STR: self._read_bytes_as_int(curr_index + 0x6, byte_count=2),
            }
        return cauldron_dict

    def _set_cauldron_dict(self, cauldron_dict:dict):
        '''
        Pass
        '''
        for cauldron_count, curr_index in enumerate(range(
                CAULDRON_START_INDEX,
                CAULDRON_END_INDEX,
                CAULDRON_INTERVAL)):
            curr_dict:dict = cauldron_dict[cauldron_count]
            self._write_bytes_from_int(curr_index, curr_dict[MAP_STR], byte_count=1)
            self._write_bytes_from_int(curr_index, curr_dict[UNKNOWN_1_STR], byte_count=1)
            self._write_bytes_from_int(curr_index, curr_dict[ENTRY_POINT_STR], byte_count=1)
            self._write_bytes_from_int(curr_index, curr_dict[UNKNOWN_3_STR], byte_count=1)
            self._write_bytes_from_int(curr_index, curr_dict[UNKNOWN_4_STR], byte_count=1)
            self._write_bytes_from_int(curr_index, curr_dict[UNKNOWN_5_STR], byte_count=1)
            self._write_bytes_from_int(curr_index, curr_dict[UNKNOWN_6_STR], byte_count=2)
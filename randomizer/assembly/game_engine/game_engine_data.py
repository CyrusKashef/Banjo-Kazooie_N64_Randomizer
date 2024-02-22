'''
Purpose:
* Modifies data written for the game engine
'''

###################
##### IMPORTS #####
###################

from randomizer.generic_bin_file_class import Generic_Bin_File_Class

from randomizer.constants.str_values.string_constants import STRING_CONSTANTS as STR_CONST

SPRITE_STR:str = "Sprite"
SFX_LIST_STR:str = "SFX List"
SFX_ID_STR:str = "SFX Id"
UNKNOWN_2_STR:str = "Unknown 2"
UNKNOWN_3_STR:str = "Unknown 3"
UNKNOWN_4_STR:str = "Unknown 4"

ZOOMBOX_SPRITE_SFX_START_INDEX:int = 0x9130
ZOOMBOX_SPRITE_SFX_END_INDEX:int = 0xA394
ZOOMBOX_SPRITE_SFX_INTERVAL:int =0x2C

#############################
##### C LIBRARIES CLASS #####
#############################

class GAME_ENGINE_DATA_CLASS(Generic_Bin_File_Class):
    '''
    Class for modifying code written for the game engine
    '''
    def __init__(self, file_name:str):
        '''
        Constructor
        '''
        file_path:str = STR_CONST.extracted_files_dir + file_name + STR_CONST.decompressed_bin_extension
        super().__init__(file_path)
    
    ######################
    ##### PAUSE MENU #####
    ######################
        
    def adjust_menu_for_witchs_lair(self):
        '''
        Changes the positioning, ordering, and sprite of
        the pause menu when 'Exit To Witch's Lair' is added.
        '''
        # Positioning
        self._write_bytes_from_int(0x8F5C, 0x002D, byte_count=2) # "RETURN TO GAME"
        self._write_bytes_from_int(0x8F6C, 0x004C, byte_count=2) # "EXIT TO WITCH'S LAIR"
        self._write_bytes_from_int(0x8F7C, 0x006B, byte_count=2) # "VIEW TOTALS"
        self._write_bytes_from_int(0x8F8C, 0x008A, byte_count=2) # "SAVE AND QUIT"
        # Ordering
        self._write_bytes_from_int(0x8F60, 0x3DCCCCCD, byte_count=4) # "EXIT TO WITCH'S LAIR"
        self._write_bytes_from_int(0x8F70, 0x3E4CCCCD, byte_count=4) # "VIEW TOTALS"
        self._write_bytes_from_int(0x8F80, 0x3E99999A, byte_count=4) # "SAVE AND QUIT"
        # Sprite
        self._write_bytes_from_int(0x8F6E, 0x05, byte_count=1) # Give "EXIT TO WITCH'S LAIR" the Gruntilda Sprite
    
    ###################
    ##### ZOOMBOX #####
    ###################
    # core2/gc/zoombox.c
    
    def get_zoombox_sprite_sfx_dict(self):
        '''
        Pass
        '''
        zoombox_dict:dict = {}
        for curr_count, curr_index in range(
                ZOOMBOX_SPRITE_SFX_START_INDEX,
                ZOOMBOX_SPRITE_SFX_END_INDEX,
                ZOOMBOX_SPRITE_SFX_INTERVAL):
            zoombox_dict[curr_count] = {
                SPRITE_STR: self._read_bytes_as_int(curr_index, byte_count=2),
                UNKNOWN_2_STR: self._read_bytes_as_int(curr_index + 0x2, byte_count=1),
                UNKNOWN_3_STR: self._read_bytes_as_int(curr_index + 0x3, byte_count=1),
                SFX_LIST_STR: [],
            }
            curr_index += 0x4
            sfx_count:int = 0
            while(sfx_count < 5):
                zoombox_dict[curr_count][SFX_LIST_STR][sfx_count] = {
                    SFX_ID_STR: self._read_bytes_as_int(curr_index, byte_count=2),
                    UNKNOWN_2_STR: self._read_bytes_as_int(curr_index + 0x2, byte_count=2),
                    UNKNOWN_4_STR: self._read_bytes_as_float(curr_index + 0x4),
                }
                curr_index += 0x8
                sfx_count += 1
        return zoombox_dict
    
    def set_zoombox_sprite_sfx_dict(self, zoombox_dict:dict):
        '''
        Pass
        '''
        for curr_count, curr_index in range(
                ZOOMBOX_SPRITE_SFX_START_INDEX,
                ZOOMBOX_SPRITE_SFX_END_INDEX,
                ZOOMBOX_SPRITE_SFX_INTERVAL):
            zoombox_item:dict = zoombox_dict[curr_count]
            self._write_bytes_from_int(curr_index, zoombox_item[SPRITE_STR], byte_count=2)
            self._write_bytes_from_int(curr_index + 0x2, zoombox_item[UNKNOWN_2_STR], byte_count=1)
            self._write_bytes_from_int(curr_index + 0x3, zoombox_item[UNKNOWN_3_STR], byte_count=1)
            curr_count += 0x4
            sfx_count:int = 0
            while(sfx_count < 5):
                sfx_item:dict = zoombox_dict[curr_count][SFX_LIST_STR]
                self._write_bytes_from_int(curr_index, sfx_item[SFX_ID_STR], byte_count=2)
                self._write_bytes_from_int(curr_index, sfx_item[UNKNOWN_2_STR], byte_count=2)
                self._write_bytes_from_float(curr_index, sfx_item[UNKNOWN_4_STR])
                curr_count += 0x8
                sfx_count += 1
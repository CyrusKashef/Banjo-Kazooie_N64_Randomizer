'''
Purpose:
* Modifies code written for Spiral Mountain
'''

###################
##### IMPORTS #####
###################

from randomizer.generic_bin_file_class import Generic_Bin_File_Class

from randomizer.constants.str_values.string_constants import STRING_CONSTANTS as STR_CONST

from randomizer.constants.int_values.ability_enums import ABILITY_ENUMS

######################################
##### SPIRAL MOUNTAIN CODE CLASS #####
######################################

class SPIRAL_MOUNTAIN_CODE_CLASS(Generic_Bin_File_Class):
    '''
    Class for modifying code written for Spiral Mountain
    '''
    def __init__(self, file_name:str):
        '''
        Constructor
        '''
        file_path:str = STR_CONST.extracted_files_dir + file_name + STR_CONST.decompressed_bin_extension
        super().__init__(file_path)
    
    def disable_anti_tamper(self):
        '''
        Disables the anti-tampering functions for Spiral Mountain
        Thank You, Wedarobi! <3
        '''
        self._write_bytes_from_int(0x1D4, 0x1000, byte_count=2)
        self._write_bytes_from_int(0x1EC, 0x1000, byte_count=2)
        self._write_bytes_from_int(0x204, 0x1000, byte_count=2)
        self._write_bytes_from_int(0x3FA4, 0x00000000, byte_count=4)
    
    #####################
    ##### ABILITIES #####
    #####################
    
    def bottles_tutorial_items(self,
            blue_egg_count:int=0,
            red_feather_count:int=0,
            gold_feather_count:int=0,
            mumbo_token_count:int=0):
        '''
        When learning moves from the intro Bottles,
        he will give the player these number of blue eggs,
        red feathers, gold feathers, and Mumbo Tokens.
        '''
        # Allocate Memory
        # self._write_bytes_from_int(0x2A58, 0x27BDFFE8, byte_count=4)
        # self._write_bytes_from_int(0x2A5C, 0xAFBF0014, byte_count=4)
        # 0C0D1905 = item_set()
        # 0C0D18F5 = func_803463D4() = item_give()?
        # func_803463D4(ITEM_D_EGGS, blue_egg_count)
        self._write_bytes_from_int(0x2A60, 0x2404000D, byte_count=4)
        self._write_bytes_from_int(0x2A64, 0x0C0D18F5, byte_count=4)
        self._write_bytes_from_int(0x2A68, 0x2405, byte_count=2)
        self._write_bytes_from_int(0x2A6A, blue_egg_count, byte_count=2)
        # func_803463D4(ITEM_F_RED_FEATHER, red_feather_count)
        self._write_bytes_from_int(0x2A6C, 0x2404000F, byte_count=4)
        self._write_bytes_from_int(0x2A70, 0x0C0D18F5, byte_count=4)
        self._write_bytes_from_int(0x2A74, 0x2405, byte_count=2)
        self._write_bytes_from_int(0x2A76, red_feather_count, byte_count=2)
        # func_803463D4(ITEM_10_GOLD_FEATHER, gold_feather_count)
        self._write_bytes_from_int(0x2A78, 0x24040010, byte_count=4)
        self._write_bytes_from_int(0x2A7C, 0x0C0D18F5, byte_count=4)
        self._write_bytes_from_int(0x2A80, 0x2405, byte_count=2)
        self._write_bytes_from_int(0x2A82, gold_feather_count, byte_count=2)
        # func_803463D4(ITEM_1C_MUMBO_TOKEN, mumbo_token_count)
        self._write_bytes_from_int(0x2A84, 0x2404001C, byte_count=4)
        self._write_bytes_from_int(0x2A88, 0x0C0D18F5, byte_count=4)
        self._write_bytes_from_int(0x2A8C, 0x2405, byte_count=2)
        self._write_bytes_from_int(0x2A8E, mumbo_token_count, byte_count=2)
        # Nice
        self._write_bytes_from_int(0x2A90, 0x24040045, byte_count=4)
        self._write_bytes_from_int(0x2A94, 0x24040045, byte_count=4)
        self._write_bytes_from_int(0x2A98, 0x24040045, byte_count=4)
        self._write_bytes_from_int(0x2A9C, 0x24040045, byte_count=4)
        self._write_bytes_from_int(0x2AA0, 0x24040045, byte_count=4)
        self._write_bytes_from_int(0x2AA4, 0x24040045, byte_count=4)
        self._write_bytes_from_int(0x2AA8, 0x24040045, byte_count=4)
        self._write_bytes_from_int(0x2AAC, 0x24040045, byte_count=4)
        # Deallocate Memory
        # self._write_bytes_from_int(0x2AB0, 0x8FBF0014, byte_count=4)
        # self._write_bytes_from_int(0x2AB4, 0x27BD0018, byte_count=4)
        # Return Null
        # self._write_bytes_from_int(0x2AB8, 0x03E00008, byte_count=4)
        # self._write_bytes_from_int(0x2ABC, 0x00000000, byte_count=4)
        # Remove Instances Of Calling
        self._write_bytes_from_int(0x3390, 0x00000000, byte_count=4)

    def bottles_tutorial_moves(self, ability_enum_list:list):
        '''
        Replaces Intro Bottle's default moves with any
        combination of moves given in the ability_enum_list.
        '''
        # Allocate Memory
        # self._write_bytes_from_int(0x2AC0, 0x27BDFFE8, byte_count=4)
        # self._write_bytes_from_int(0x2AC4, 0xAFBF0014, byte_count=4)
        # ability_setAllUsed()
        # Works For 0x00-0x0E
        move_val:int = 0
        for ability_enum in range(0xF):
            if(ability_enum in ability_enum_list):
                move_val += (1 << ability_enum)
        self._write_bytes_from_int(0x2AC8, 0x0C0A5619, byte_count=4)
        self._write_bytes_from_int(0x2ACC, 0x2404, byte_count=2)
        self._write_bytes_from_int(0x2ACE, move_val, byte_count=2)
        # ability_unlock()
        # Needed For 0xF-0x13
        starting_index:int = 0x2AD0
        for ability_enum in range(0xF, 0x14):
            if(ability_enum in ability_enum_list):
                self._write_bytes_from_int(starting_index, 0x0C0A3CEE, byte_count=4)
                self._write_bytes_from_int(starting_index + 4, 0x2404, byte_count=2)
                self._write_bytes_from_int(starting_index + 6, ability_enum, byte_count=2)
            else:
                # Nice
                self._write_bytes_from_int(starting_index, 0x24040045, byte_count=4)
                self._write_bytes_from_int(starting_index + 4, 0x24040045, byte_count=4)
            starting_index += 0x8
        # ability_setAllUsed(-1)
        self._write_bytes_from_int(0x2AF8, 0x0C0A561C, byte_count=4)
        self._write_bytes_from_int(0x2AFC, 0x2404FFFF, byte_count=4)
        # Give Items To Player
        self._write_bytes_from_int(0x2B00, 0x0C0E2392, byte_count=4) # func_80388E48()
        self._write_bytes_from_int(0x2B04, 0x00000000, byte_count=4)
        # Nice
        self._write_bytes_from_int(0x2B08, 0x24040045, byte_count=4)
        self._write_bytes_from_int(0x2B0C, 0x24040045, byte_count=4)
        self._write_bytes_from_int(0x2B10, 0x24040045, byte_count=4)
        self._write_bytes_from_int(0x2B14, 0x24040045, byte_count=4)
        # mapSpecificFlags_set(3, 1)
        # self._write_bytes_from_int(0x2B18, 0x24040003, byte_count=4)
        # self._write_bytes_from_int(0x2B1C, 0x0C0B2B70, byte_count=4)
        # self._write_bytes_from_int(0x2B20, 0x24050001, byte_count=4)
        # Deallocate Memory
        # self._write_bytes_from_int(0x2B24, 0x8FBF0014, byte_count=4)
        # self._write_bytes_from_int(0x2B28, 0x27BD0018, byte_count=4)
        # Return Null
        # self._write_bytes_from_int(0x2B2C, 0x03E00008, byte_count=4)
        # self._write_bytes_from_int(0x2B30, 0x00000000, byte_count=4)
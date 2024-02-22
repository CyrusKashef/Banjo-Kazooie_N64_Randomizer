'''
Purpose:
* Modifies code written for Treasure Trove Cove
'''

###################
##### IMPORTS #####
###################

from randomizer.generic_bin_file_class import Generic_Bin_File_Class

from randomizer.constants.str_values.string_constants import STRING_CONSTANTS as STR_CONST

##########################################
##### TREASURE TROVE COVE CODE CLASS #####
##########################################

class TREASURE_TROVE_COVE_CODE_CLASS(Generic_Bin_File_Class):
    '''
    Class for modifying code written for Treasure Trove Cove
    '''
    def __init__(self, file_name:str):
        '''
        Constructor
        '''
        file_path:str = STR_CONST.extracted_files_dir + file_name + STR_CONST.decompressed_bin_extension
        super().__init__(file_path)
    
    def disable_anti_tamper(self):
        '''
        Disables the anti-tampering functions for Treasure Trove Cove assembly
        Thank You, Wedarobi! <3
        '''
        self._write_bytes_from_int(0x31B4, 0x00000000, byte_count=4)
    
    def patch_yum_yum_crash_fix(self):
        '''
        Fixes a vanilla bug: 
        When a yum-yum in TTC tries to eat a sprite in a cube,
        the game treats it as an actor, derefs an invalid pointer,
        and segfaults.
        Thank You, Wedarobi! <3
        '''
        # Set hook in Yum-Yum eat update function
        self._write_bytes_from_int(0xC90, 0x08096C05, byte_count=4)
'''
Purpose:
*
'''

###################
##### IMPORTS #####
###################

from randomizer.generic_bin_file_class import Generic_Bin_File_Class

from randomizer.constants.str_values.string_constants import STRING_CONSTANTS as STR_CONST

########################################
##### BUBBLEGLOOP SWAMP CODE CLASS #####
########################################

class BUBBLEGLOOP_SWAMP_CODE_CLASS(Generic_Bin_File_Class):
    '''
    Pass
    '''
    def __init__(self, file_name:str):
        '''
        Constructor
        '''
        file_path:str = STR_CONST.extracted_files_dir + file_name + STR_CONST.decompressed_bin_extension
        super().__init__(file_path)
    
    def disable_anti_tamper(self):
        '''
        Disables the anti-tampering functions for Bubblegloop Swamp assembly
        Thank You, Wedarobi! <3
        '''
        self._write_bytes_from_int(0x86C0, 0x1000, byte_count=2)
'''
Purpose:
*
'''

###################
##### IMPORTS #####
###################

from randomizer.generic_bin_file_class import Generic_Bin_File_Class

from randomizer.constants.str_values.string_constants import STRING_CONSTANTS as STR_CONST

#######################################
##### CLICK CLOCK WOOD CODE CLASS #####
#######################################

class CLICK_CLOCK_WOOD_CODE_CLASS(Generic_Bin_File_Class):
    '''
    Pass
    '''
    def __init__(self, file_name:str):
        '''
        Constructor
        '''
        file_path:str = STR_CONST.extracted_files_dir + file_name + STR_CONST.decompressed_bin_extension
        super().__init__(file_path)
    
    #####################
    ##### SNAREBEAR #####
    #####################

    def all_transformations_snarebear_collision_off(self):
        '''
        Pass
        '''
        # Checks If You Are Banjo Or Wishywashy
        self._write_bytes_from_int(0x7D64, 0x0C0A3C35, byte_count=4)
        # Set Comparison To 0 (False)
        self._write_bytes_from_int(0x7D6C, 0x24010000, byte_count=4)
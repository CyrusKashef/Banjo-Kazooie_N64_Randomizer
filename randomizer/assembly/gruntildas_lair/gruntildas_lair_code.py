'''
Purpose:
*
'''

###################
##### IMPORTS #####
###################

from randomizer.generic_bin_file_class import Generic_Bin_File_Class

from randomizer.constants.str_values.string_constants import STRING_CONSTANTS as STR_CONST

######################################
##### GRUNTILDAS LAIR CODE CLASS #####
######################################

class GRUNTILDAS_LAIR_CODE_CLASS(Generic_Bin_File_Class):
    '''
    Pass
    '''
    def __init__(self, file_name:str):
        '''
        Constructor
        '''
        file_path:str = STR_CONST.extracted_files_dir + file_name + STR_CONST.decompressed_bin_extension
        super().__init__(file_path)
    
    ######################
    ##### NOTE DOORS #####
    ######################

    def note_door_item_requirement(self, mips_hex:int=0x0C0D1BBB):
        '''
        Pass
        '''
        # 0x0C0D1BBB -> itemscore_noteScores_getTotal()
        # 0x0C0C8527 -> honeycombscore_get_total()
        # 0x0C0C848F -> jiggyscore_total()
        # 0x0C0C8599 -> mumboscore_get_total()
        self._write_bytes_from_int(0x1504, mips_hex, byte_count=4)
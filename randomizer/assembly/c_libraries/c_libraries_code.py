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

##################################
##### C LIBRARIES CODE CLASS #####
##################################

class C_LIBRARIES_CODE_CLASS(Generic_Bin_File_Class):
    '''
    Pass
    '''
    def __init__(self, file_name:str):
        '''
        Constructor
        '''
        file_path:str = EXTRACTED_FILES_DIR + file_name + DECOMPRESSED_BIN_EXTENSION
        super().__init__(file_path)
    
    def disable_anti_tamper(self):
        '''
        Disables the anti-tampering functions for C Libraries assembly
        Thank You, Wedarobi! <3
        '''
        self._write_bytes_from_int(0x10A1C, 0x00000000, byte_count=4)
        self._write_bytes_from_int(0x10A30, 0x1000, byte_count=2)
    
    def patch_yum_yum_crash_fix(self):
        '''
        Fixes a vanilla bug: 
        When a yumyum in TTC tries to eat a sprite in a cube,
        the game treats it as an actor, derefs an invalid pointer,
        and segfaults.
        Thank You, Wedarobi! <3
        '''
        self._write_bytes_from_int(0x1D5EC, 0x03E0000800000000, byte_count=8)
        self._write_bytes_from_int(0x1D5F4, 0x1100000D000000008D0A0000000A4E0234010080552100083C098000012A4826, byte_count=32)
        self._write_bytes_from_int(0x1D626, 0x3C0100400121482A1120000300000000080E1C2200000000080E1C2800000000, byte_count=32)
    
    def booting_up_map(self, map_id:int):
        '''
        When loading the game, this is the location the player boots up at
        Typically used to skip the Rareware & N64 logo cutscene and the concert
        '''
        self._write_bytes_from_int(0x18B, map_id, byte_count=1)
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
##### MUMBOS MOUNTAIN CODE CLASS #####
######################################

class MUMBOS_MOUNTAIN_CODE_CLASS(Generic_Bin_File_Class):
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
        Disables the anti-tampering functions for Mumbo's Mountain assembly
        Thank You, Wedarobi! <3
        '''
        self._write_bytes_from_int(0x1B7C, 0x1000, byte_count=2)
    
    #################
    ##### CONGA #####
    #################

    def all_transformations_conga_text(self):
        '''
        Pass
        '''
        # Checks If You Are Banjo Or Wishywashy
        self._write_bytes_from_int(0x1520, 0x0C0A3C35, byte_count=4)
        # Set Comparison To 0 (False)
        self._write_bytes_from_int(0x1528, 0x24010000, byte_count=4)
    
    def agro_conga(self):
        '''
        Pass
        '''
        # ASSET_51_ANIM_CONGA_IDLE
        # self._write_bytes_from_int(0x1488, 0x24050007, byte_count=4)
        # ASSET_54_ANIM_CONGA_THROW
        # self._write_bytes_from_int(0x16C0, 0x24050007, byte_count=4)
        # ASSET_A2_ANIM_CONGA_THROW_2
        # self._write_bytes_from_int(0x1714, 0x24050007, byte_count=4)
        # ASSET_55_ANIM_CONGA_BEAT_CHEST
        self._write_bytes_from_int(0x1770, 0x24050007, byte_count=4)
        # ASSET_51_ANIM_CONGA_IDLE
        # self._write_bytes_from_int(0x17B4, 0x24050007, byte_count=4)
        # ASSET_51_ANIM_CONGA_IDLE
        # self._write_bytes_from_int(0x18FC, 0x24050007, byte_count=4)
        # ASSET_51_ANIM_CONGA_IDLE
        # self._write_bytes_from_int(0x193C, 0x24050007, byte_count=4)
        # ASSET_53_ANIM_CONGA_DEFEAT
        # self._write_bytes_from_int(0x1984, 0x24050007, byte_count=4)
        # ASSET_51_ANIM_CONGA_IDLE
        # self._write_bytes_from_int(0x19E0, 0x24050007, byte_count=4)
        # ASSET_56_ANIM_CONGA_RAISE_ARMS
        # self._write_bytes_from_int(0x1A2C, 0x24050007, byte_count=4)
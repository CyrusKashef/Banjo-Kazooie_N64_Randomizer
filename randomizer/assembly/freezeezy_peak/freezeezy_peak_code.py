'''
Purpose:
*
'''

###################
##### IMPORTS #####
###################

from randomizer.generic_bin_file_class import Generic_Bin_File_Class

from randomizer.constants.str_values.string_constants import STRING_CONSTANTS as STR_CONST

#####################################
##### FREEZEEZY PEAK CODE CLASS #####
#####################################

class FREEZEEZY_PEAK_CODE_CLASS(Generic_Bin_File_Class):
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
    ##### BOGGY RACE #####
    ######################

    def all_transformations_boggy_2(self):
        '''
        src/FP/ch/boggy2.c#L135
        src/FP/ch/boggy2.c#L477
        '''
        # Boggy Asks Walrus For Race & Rematch
        self._write_bytes_from_int(0x2748, 0x0C0A3C35, byte_count=4)
        self._write_bytes_from_int(0x2750, 0x24010000, byte_count=4)
        ############################################################
        # Boggy Rejects Banjo For Sled Race
        self._write_bytes_from_int(0x3690, 0x0C0A3C35, byte_count=4)
        self._write_bytes_from_int(0x3698, 0x24010000, byte_count=4)
    
    def all_transformations_race_sled(self):
        '''
        src/FP/ch/racesled.c#L60
        '''
        # Checks If You Are Banjo Or Wishywashy
        self._write_bytes_from_int(0x674, 0x0C0A3C35, byte_count=4)
        # Set Comparison To 0 (False)
        self._write_bytes_from_int(0x67C, 0x24010000, byte_count=4)
        # Skip Animation Check Step
        self._write_bytes_from_int(0x694, 0x10400003, byte_count=4)
    
    #################
    ##### WOZZA #####
    #################
    
    def all_transformations_wozza(self):
        '''
        src/FP/ch/cavewozza.c#L70
        src/FP/ch/wozza.c#L225
        src/FP/ch/wozza.c#L297
        '''
        # Cave Wozza Dialog
        self._write_bytes_from_int(0xA460, 0x0C0A3C35, byte_count=4)
        self._write_bytes_from_int(0xA468, 0x24010000, byte_count=4)
        # Wozza Face Walrus
        self._write_bytes_from_int(0x95C8, 0x0C0A3C35, byte_count=4)
        self._write_bytes_from_int(0x95D0, 0x24010000, byte_count=4)
        # Wozza Avoiding Non-Walrus
        self._write_bytes_from_int(0x98C0, 0x0C0A3C35, byte_count=4)
        self._write_bytes_from_int(0x98C8, 0x24010000, byte_count=4)
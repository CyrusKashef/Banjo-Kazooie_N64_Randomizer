'''
Purpose:
*
'''

###################
##### IMPORTS #####
###################

from randomizer.generic_bin_file_class import Generic_Bin_File_Class

from randomizer.constants.str_values.string_constants import STRING_CONSTANTS as STR_CONST

###################################
##### FINAL BATTLE CODE CLASS #####
###################################

class FINAL_BATTLE_CODE_CLASS(Generic_Bin_File_Class):
    '''
    Pass
    '''
    def __init__(self, file_name:str):
        '''
        Constructor
        '''
        file_path:str = STR_CONST.extracted_files_dir + file_name + STR_CONST.decompressed_bin_extension
        super().__init__(file_path)
    
    def adjust_final_battle_phases(self,
            phase1_hits:int|None=None,
            phase2_hits:int|None=None, phase2_spots:int|None=None,
            phase3_hits:int|None=None,
            phase4_num_of_jinjos:int|None=None, phase4_egg_per_jinjo:int|None=None,
            phase5_eggs_per_hole:int|None=None):
        '''
        Pass
        '''
        # Phase 1 (Complete)
        if(phase1_hits != None):
            self._write_byte(0x2147, phase1_hits) # honeycomb
            self._write_byte(0x2DBF, phase1_hits) # next phase
        # Phase 2 (Complete)
        if(phase2_hits != None):
            self._write_byte(0x5683, phase2_hits)
        if(phase2_spots != None):
            self._write_byte(0x3297, phase2_spots)
        # Phase 3 (Complete)
        if(phase3_hits != None):
            self._write_byte(0x39EB, phase3_hits) # next phase
            self._write_byte(0x576F, phase3_hits) # honeycomb
        # Phase 4
        if(phase4_num_of_jinjos != None):
            self._write_byte(0x42E3, phase4_num_of_jinjos)
        if(phase4_egg_per_jinjo != None):
            self._write_byte(0x709B, phase4_egg_per_jinjo)
        # Phase 5
        if(phase5_eggs_per_hole != None):
            self._write_byte(0x7F9B, phase5_eggs_per_hole)
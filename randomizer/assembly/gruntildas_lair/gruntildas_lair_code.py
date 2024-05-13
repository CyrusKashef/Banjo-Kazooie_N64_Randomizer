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
    
    #######################
    ##### FURNACE FUN #####
    #######################
    # lair/code_5ED0.c
        
    def furnace_fun_picture_questions_extend(self):
        '''
        Pass
        '''
        # Always Calculate With The 9 Section
        # BNE $v0 $s4 0x000C -> BNE $zero $zero 0x000C
        self._write_bytes_from_int(0x7B14, 0x1000000C, byte_count=4)
        #
        #
        #
        #
        # Don't Calculate With The 9 Section
        # BNE $v0 $s4 0x000C -> BNE $zero $zero 0x000C
        # self._write_bytes_from_int(0x7B14, 0x1400000C, byte_count=4)
        # Divide By 0x1 Instead Of 0xC
        # DIV $t8 $s2 -> DIV $t8 $at
        # self._write_bytes_from_int(0x7B64, 0x0301001A, byte_count=4)
    
    ### JOKER/SKULL QUESTIONS
    
    def _set_rng_tile_to_one_type(self, tile_type:int):
        '''
        Pass
        '''
        self._write_bytes_from_int(0x7968, 0x24020000 + tile_type, byte_count=4) # Text
        self._write_bytes_from_int(0x7988, 0x24020000 + tile_type, byte_count=4) # Picture
        self._write_bytes_from_int(0x7990, 0x24020000 + tile_type, byte_count=4) # Grunty
        self._write_bytes_from_int(0x79A8, 0x24020000 + tile_type, byte_count=4) # Sound
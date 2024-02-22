'''
Purpose:
* Modifies data written for the c libraries
'''

###################
##### IMPORTS #####
###################

from randomizer.generic_bin_file_class import Generic_Bin_File_Class

from randomizer.constants.str_values.string_constants import STRING_CONSTANTS as STR_CONST

##################################
##### C LIBRARIES DATA CLASS #####
##################################

class C_LIBRARIES_DATA_CLASS(Generic_Bin_File_Class):
    '''
    Class for modifying data written for the c libraries
    '''
    def __init__(self, file_name:str):
        '''
        Constructor
        '''
        file_path:str = STR_CONST.extracted_files_dir + file_name + STR_CONST.decompressed_bin_extension
        super().__init__(file_path)
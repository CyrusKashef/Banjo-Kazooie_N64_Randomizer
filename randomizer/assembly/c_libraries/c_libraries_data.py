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
##### C LIBRARIES DATA CLASS #####
##################################

class C_LIBRARIES_DATA_CLASS(Generic_Bin_File_Class):
    '''
    Pass
    '''
    def __init__(self, file_name:str):
        '''
        Constructor
        '''
        file_path:str = EXTRACTED_FILES_DIR + file_name + DECOMPRESSED_BIN_EXTENSION
        super().__init__(file_path)
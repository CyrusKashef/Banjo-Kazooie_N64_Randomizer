'''
Purpose:
* Class for running the compression and decompression algorithms on files.
'''

###################
##### IMPORTS #####
###################

from shutil import copy
import zlib

from randomizer.generic_bin_file_class import Generic_Bin_File_Class

#############################
##### COMPRESSION CLASS #####
#############################

class COMPRESSION_CLASS(Generic_Bin_File_Class):
    '''
    Runs the compression and decompression algorithms on files.
    '''
    def __init__(self, file_name:str, file_type:str):
        '''
        Constructor
        '''
        ### CONSTANTS ###
        self._WBITS:int = -15
        self._BK_COMPRESSED_FILE_HEADER = b"\x11\x72"
        self._EXTRACTED_FILES_DIR:str = "randomizer/extracted_files/"
        self._COMPRESSED_BIN_EXTENSION:str = "-Compressed.bin"
        self._DECOMPRESSED_BIN_EXTENSION:str = "-Decompressed.bin"
        self._RAW_BIN_EXTENSION:str = "-Raw.bin"
        self._FILE_EMPTY_STR:str = "File Empty"
        self._DECOMPRESSED_STR:str = "Decompressed"
        self._COMPRESSED_STR:str = "Compressed"
        self._RAW_STR:str = "Raw"
        self._TEMPORARY_BIN:str = "tmp.bin"

        ### VARIABLES ###
        self._file_name:str = file_name
        self._file_path:str = None
        self._file_content = None
        self._determine_file_path(file_type)
        self._read_file()

    ###################
    ##### GENERIC #####
    ###################
    
    def _determine_file_path(self, file_type:str):
        '''
        Sets the current file's path based on the file extention.
        '''
        if(file_type == self._COMPRESSED_STR):
            file_ext = self._COMPRESSED_BIN_EXTENSION
        elif(file_type == self._DECOMPRESSED_STR):
            file_ext = self._DECOMPRESSED_BIN_EXTENSION
        elif(file_type == self._RAW_STR):
            file_ext = self._RAW_BIN_EXTENSION
        else:
            raise Exception("ERROR: _read_file_contents: Unknown File Extension")
        self._file_path:str = self._EXTRACTED_FILES_DIR + self._file_name + file_ext

    ######################
    ##### DECOMPRESS #####
    ######################
    
    def _check_extracted_file_type(self):
        '''
        Determines whether the current file is empty, compressed, or decompressed.
        '''
        if(len(self._file_content) == 0):
            return self._FILE_EMPTY_STR
        elif(self._file_content[:2] == self._BK_COMPRESSED_FILE_HEADER):
            return self._COMPRESSED_STR
        return self._DECOMPRESSED_STR
    
    def _decompress_file(self):
        '''
        Creates a decompressed version of a compressed file.
        '''
        compressor_obj = zlib.decompressobj(wbits=self._WBITS)
        decompressed_file_bytes = compressor_obj.decompress(self._file_content[6:])
        decompressed_file_path:str = self._EXTRACTED_FILES_DIR + self._file_name + self._DECOMPRESSED_BIN_EXTENSION
        with open(decompressed_file_path, "wb+") as decompressed_file:
            decompressed_file.write(decompressed_file_bytes)

    def _copy_file_as_raw(self):
        '''
        Copies an extracted file as a raw file.
        '''
        raw_file_path:str = self._EXTRACTED_FILES_DIR + self._file_name + self._RAW_BIN_EXTENSION
        copy(self._file_path, raw_file_path)
    
    ####################
    ##### COMPRESS #####
    ####################
    
    ##########################
    ##### MAIN FUNCTIONS #####
    ##########################

    def decompress_file_main(self):
        '''
        Runs the main workflow for decompressing a file.
        '''
        file_type:str = self._check_extracted_file_type()
        if(file_type == self._COMPRESSED_STR):
            self._decompress_file()
        elif(file_type == self._DECOMPRESSED_STR):
            self._copy_file_as_raw()

    def compress_file_main(self):
        '''
        Pass
        '''
        pass
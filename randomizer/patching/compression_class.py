'''
Purpose:
* Class for running the compression and decompression algorithms on files.
'''

###################
##### IMPORTS #####
###################

import os
import zlib
import gzip
from shutil import copy

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
        self._BK_COMPRESSED_FILE_HEADER:bytes = b"\x11\x72"
        self._EXTRACTED_FILES_DIR:str = "randomizer/extracted_files/"
        self._COMPRESSED_BIN_EXTENSION:str = "-Compressed.bin"
        self._DECOMPRESSED_BIN_EXTENSION:str = "-Decompressed.bin"
        self._RAW_BIN_EXTENSION:str = "-Raw.bin"
        self._DECOMPRESSED_STR:str = "Decompressed"
        self._COMPRESSED_STR:str = "Compressed"
        self._RAW_STR:str = "Raw"
        self._TEMPORARY_BIN:str = "tmp.bin"
        self._ASSET_FILE:str = "Asset"
        self._ASSEMBLY_FILE:str = "Assembly"
        self._PADDING_BYTE:str = "Padding Byte"
        self._PADDING_INTERVAL:str = "Padding Interval"
        self._PADDING_DICT:dict = {
            self._ASSET_FILE: {
                self._PADDING_BYTE: b"\xAA",
                self._PADDING_INTERVAL: 0x08,
            },
            self._ASSEMBLY_FILE: {
                self._PADDING_BYTE: b"\x00",
                self._PADDING_INTERVAL: 0x10,
            },
        }

        ### VARIABLES ###
        self._file_name:str = file_name
        self._file_type:str = file_type
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
            raise Exception("ERROR: _determine_file_path: Unknown File Extension")
        self._file_path:str = self._EXTRACTED_FILES_DIR + self._file_name + file_ext

    ######################
    ##### DECOMPRESS #####
    ######################
    
    def _check_extracted_file_type(self):
        '''
        Determines whether the current file is empty, compressed, or decompressed.
        '''
        if(len(self._file_content) == 0):
            return self._DECOMPRESSED_STR
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

    def _copy_compressed_to_raw(self):
        '''
        Copies an extracted file as a raw file.
        '''
        raw_file_path:str = self._EXTRACTED_FILES_DIR + self._file_name + self._RAW_BIN_EXTENSION
        copy(self._file_path, raw_file_path)
    
    ####################
    ##### COMPRESS #####
    ####################
    
    def _compress_file(self, padding_byte:bytes, padding_interval:int):
        '''
        Pass
        '''
        # Read Decompressed File
        # Align In-Game Post-Inflate Buffer To 16
        while(len(self._file_content) % 0x10):
            self._file_content.append(0x00)
        decompressed_file_length:int = len(self._file_content)
        # Deflate & Build
        compressed_body = gzip.compress(data=self._file_content, compresslevel=9, mtime=None)[10:-8]
        compressed_content = self._BK_COMPRESSED_FILE_HEADER + decompressed_file_length.to_bytes(4, "big") + compressed_body
        # Align
        while(len(compressed_content) % padding_interval):
            compressed_content += padding_byte
        compressed_content_length:int = len(compressed_content)
        # Create Compressed File
        compressed_file_path:str = self._EXTRACTED_FILES_DIR + self._file_name + self._COMPRESSED_BIN_EXTENSION
        with open(compressed_file_path, "wb+") as compressed_file:
            compressed_file.write(compressed_content)
        return compressed_content_length

    def _copy_raw_to_compressed(self):
        '''
        Pass
        '''
        compressed_content_length:int = len(self._file_content)
        compressed_file_path:str = self._EXTRACTED_FILES_DIR + self._file_name + self._COMPRESSED_BIN_EXTENSION
        copy(self._file_path, compressed_file_path)
        return compressed_content_length

    ##########################
    ##### MAIN FUNCTIONS #####
    ##########################

    def decompress_file_main(self):
        '''
        Runs the main workflow for prepping a file for modifying.
        The file may be decompressed or copied as raw.
        '''
        file_type:str = self._check_extracted_file_type()
        if(file_type == self._COMPRESSED_STR):
            self._decompress_file()
        elif(file_type == self._DECOMPRESSED_STR):
            self._copy_compressed_to_raw()

    def compress_file_main(self, file_category:str):
        '''
        Runs the main workflow for prepping a file for insersion.
        The file may be compressed or copied as raw.
        '''
        padding_byte:bytes = self._PADDING_DICT[file_category][self._PADDING_BYTE]
        padding_interval:int = self._PADDING_DICT[file_category][self._PADDING_INTERVAL]
        if(self._file_type == self._DECOMPRESSED_STR):
            compressed_content_length:int = self._compress_file(padding_byte, padding_interval)
        elif(self._file_type == self._RAW_STR):
            compressed_content_length:int = self._copy_raw_to_compressed()
        else:
            raise Exception(f"Error: compress_file_main: Unidentified file type '{self._file_type}'")
        return compressed_content_length
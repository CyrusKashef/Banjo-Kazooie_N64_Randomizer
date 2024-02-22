'''
Purpose:
* Class for running the compression and decompression algorithms on files.
'''

###################
##### IMPORTS #####
###################

import zlib
import gzip
import shutil

from randomizer.generic_bin_file_class import Generic_Bin_File_Class

from randomizer.constants.str_values.string_constants import STRING_CONSTANTS as STR_CONST
from randomizer.constants.int_values.int_constants import INTEGER_CONSTANTS as INT_CONST
from randomizer.constants.byte_values.byte_constants import BYTE_CONSTANTS as BYTE_CONST

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
        if(file_type == STR_CONST.compressed):
            file_ext = STR_CONST.compressed_bin_extension
        elif(file_type == STR_CONST.decompressed):
            file_ext = STR_CONST.decompressed_bin_extension
        elif(file_type == STR_CONST.raw):
            file_ext = STR_CONST.raw_bin_extension
        else:
            raise Exception("ERROR: _determine_file_path: Unknown File Extension")
        self._file_path:str = STR_CONST.extracted_files_dir + self._file_name + file_ext

    ######################
    ##### DECOMPRESS #####
    ######################
    
    def _check_extracted_file_type(self):
        '''
        Determines whether the current file is empty, compressed, or decompressed.
        '''
        if(len(self._file_content) == 0):
            return STR_CONST.decompressed
        elif(self._file_content[:2] == BYTE_CONST.bk_compressed_file_header):
            return STR_CONST.compressed
        return STR_CONST.decompressed
    
    def _decompress_file(self):
        '''
        Creates a decompressed version of a compressed file.
        '''
        compressor_obj = zlib.decompressobj(wbits=INT_CONST.wbits)
        decompressed_file_bytes = compressor_obj.decompress(self._file_content[6:])
        decompressed_file_path:str = STR_CONST.extracted_files_dir + self._file_name + STR_CONST.decompressed_bin_extension
        with open(decompressed_file_path, "wb+") as decompressed_file:
            decompressed_file.write(decompressed_file_bytes)

    def _copy_compressed_to_raw(self):
        '''
        Copies an extracted file as a raw file.
        '''
        raw_file_path:str = STR_CONST.extracted_files_dir + self._file_name + STR_CONST.raw_bin_extension
        shutil.copy(self._file_path, raw_file_path)
    
    ####################
    ##### COMPRESS #####
    ####################
    
    def _compress_asset_file(self, padding_byte:bytes, padding_interval:int):
        '''
        Compresses an asset file.
        Thank you Wedarobi! <3
        '''
        # Read Decompressed File
        # Align In-Game Post-Inflate Buffer To 16
        while(len(self._file_content) % 0x10):
            self._file_content.append(0x00)
        decompressed_file_length:int = len(self._file_content)
        # Deflate & Build
        compressed_body = gzip.compress(data=self._file_content, compresslevel=9, mtime=None)[10:-8]
        compressed_content = BYTE_CONST.bk_compressed_file_header + decompressed_file_length.to_bytes(4, "big") + compressed_body
        # Align
        while(len(compressed_content) % padding_interval):
            compressed_content += padding_byte
        compressed_content_length:int = len(compressed_content)
        # Create Compressed File
        compressed_file_path:str = STR_CONST.extracted_files_dir + self._file_name + STR_CONST.compressed_bin_extension
        with open(compressed_file_path, "wb+") as compressed_file:
            compressed_file.write(compressed_content)
        return compressed_content_length
    
    def compress_assembly_file(self):
        '''
        Compresses an assembly file.
        Thank you Wedarobi! <3
        '''
        while(len(self._file_content) % 0x10):
            self._file_content.append(0x00)
        decompressed_file_length:int = len(self._file_content)
        # Deflate & Build
        compressed_body = gzip.compress(data=self._file_content, compresslevel=9, mtime=None)[10:-8]
        compressed_content = BYTE_CONST.bk_compressed_file_header + decompressed_file_length.to_bytes(4, "big") + compressed_body
        # Create Compressed File
        compressed_file_path:str = STR_CONST.extracted_files_dir + self._file_name + STR_CONST.compressed_bin_extension
        with open(compressed_file_path, "wb+") as compressed_file:
            compressed_file.write(compressed_content)
        return compressed_file_path

    def _copy_raw_to_compressed(self):
        '''
        Copies a decompressed file to another file with the compressed extension.
        '''
        compressed_content_length:int = len(self._file_content)
        compressed_file_path:str = STR_CONST.extracted_files_dir + self._file_name + STR_CONST.compressed_bin_extension
        shutil.copy(self._file_path, compressed_file_path)
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
        if(file_type == STR_CONST.compressed):
            self._decompress_file()
        elif(file_type == STR_CONST.decompressed):
            self._copy_compressed_to_raw()

    def compress_asset_file_main(self):
        '''
        Runs the main workflow for prepping a file for insersion.
        The file may be compressed or copied as raw.
        '''
        if(self._file_type == STR_CONST.decompressed):
            compressed_content_length:int = self._compress_asset_file(b"\xAA", 0x08)
        elif(self._file_type == STR_CONST.raw):
            compressed_content_length:int = self._copy_raw_to_compressed()
        else:
            raise Exception(f"Error: compress_file_main: Unidentified file type '{self._file_type}'")
        return compressed_content_length
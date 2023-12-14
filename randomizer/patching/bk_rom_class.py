'''
Purpose:
* Class for running the ROM extracting and inserting workflows.
'''

###################
##### IMPORTS #####
###################

import os

from randomizer.generic_bin_file_class import Generic_Bin_File_Class
from randomizer.patching.compression_class import COMPRESSION_CLASS

########################
##### BK ROM CLASS #####
########################

class BK_ROM_CLASS(Generic_Bin_File_Class):
    '''
    Runs the ROM extracting and inserting workflows.
    '''
    def __init__(self, file_path:str):
        '''
        Constructor
        '''
        ### SUPER ###
        super().__init__(file_path)

        ### CONSTANTS ###
        self._ASSET_TABLE_START_INDEX:int = 0x5E98
        self._ASSET_TABLE_END_INDEX:int = 0x10CC8
        self._ASSET_TABLE_OFFSET:int = 0x10CD0
        self._ROM_END_INDEX:int = 0x1000000
        self._ASM_END:int = 0xFDAA10
        # self._CIC = 0xA3886759
        # self._CIC_DICT = {
        #     '6101': 0x00000000, # nope
        #     '6102': 0xF8CA4DDC,
        #     '6103': 0xA3886759,
        #     '6105': 0xDF26F436,
        #     '6106': 0x1FEA617A
        # }
        self._CRC1_INDEX_START:int = 0x10
        self._CRC1_BYTE_COUNT:int = 0x4
        self._CRC2_INDEX_START:int = 0x14
        self._CRC2_BYTE_COUNT:int = 0x4
        self._BOOT_CODE_INDEX_START:int = 0x40
        self._BOOT_CODE_BYTE_COUNT:int = 0xFC0
        self._EXTRACTED_FILES_DIR:str = "randomizer/extracted_files/"
        self._COMPRESSED_BIN_EXTENSION:str = "-Compressed.bin"
        self._DECOMPRESSED_BIN_EXTENSION:str = "-Decompressed.bin"
        self._RAW_BIN_EXTENSION:str = "-Raw.bin"
        self._FILE_EMPTY_STR:str = "File Empty"
        self._DECOMPRESSED_STR:str = "Decompressed"
        self._COMPRESSED_STR:str = "Compressed"

        ### VARIABLES ###
        self._create_extracted_files_directory()
    
    #################
    ##### SETUP #####
    #################
        
    def _create_extracted_files_directory(self):
        '''
        Creates an extracted files directory.
        '''
        if(not os.path.exists(self._EXTRACTED_FILES_DIR)):
            os.mkdir(self._EXTRACTED_FILES_DIR)

    ################################
    ##### EXTRACT & DECOMPRESS #####
    ################################

    def _extract_by_asset_pointer(self, pointer_index_start:int, file_name:str):
        '''
        Extracts a singular compressed bin file from the ROM
        '''
        asset_index_start:int = self._read_bytes_as_int(pointer_index_start, 4) + self._ASSET_TABLE_OFFSET
        asset_index_end:int = self._read_bytes_as_int(pointer_index_start + 0x8, 4) + self._ASSET_TABLE_OFFSET
        file_path:str = f"{self._EXTRACTED_FILES_DIR}{file_name}{self._COMPRESSED_BIN_EXTENSION}"
        with open(file_path, "wb+") as comp_file:
            comp_file.write(self._file_content[asset_index_start:asset_index_end])

    def extract_and_decompress_all_asset_table_pointers(self):
        '''
        Extracts all of the compressed bin files from the ROM into an individual bin file and
        runs the decompression algorithm to create the decompressed bin file.
        '''
        for pointer_index_start in range(self._ASSET_TABLE_START_INDEX, self._ASSET_TABLE_END_INDEX + 1, 0x8):
            pointer_index_start = 0x97A0
            file_name:str = self._convert_int_to_hex_str(pointer_index_start)
            self._extract_by_asset_pointer(pointer_index_start, file_name)
            compressed_obj = COMPRESSION_CLASS(file_name, self._COMPRESSED_STR)
            compressed_obj.decompress_file_main()

if __name__ == '__main__':
    file_path:str = "C:/Users/Cyrus/Documents/VS_Code/BK_Randomizer/BK_Randomizer_v3/Banjo-Kazooie.z64"
    bk_rom = BK_ROM_CLASS(file_path)
    bk_rom.extract_and_decompress_all_asset_table_pointers()
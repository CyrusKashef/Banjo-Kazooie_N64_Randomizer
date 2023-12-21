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
        self._CIC = 0xA3886759
        self._CRC1_INDEX_START:int = 0x10
        self._CRC2_INDEX_START:int = 0x14
        self._CHECK_ROM_START_INDEX:int = 0x1000
        self._CHECK_ROM_END_INDEX:int = 0x101000
        self._EXTRACTED_FILES_DIR:str = "randomizer/extracted_files/"
        self._BIN_EXTENSION:str = ".bin"
        self._COMPRESSED_BIN_EXTENSION:str = f"-Compressed{self._BIN_EXTENSION}"
        self._DECOMPRESSED_BIN_EXTENSION:str = f"-Decompressed{self._BIN_EXTENSION}"
        self._RAW_BIN_EXTENSION:str = f"-Raw{self._BIN_EXTENSION}"
        self._FILE_EMPTY_STR:str = "File Empty"
        self._DECOMPRESSED_STR:str = "Decompressed"
        self._COMPRESSED_STR:str = "Compressed"
        self._RAW_STR:str = "Raw"
        self._ASSET_FILE:str = "Asset"
        self._ASSEMBLY_FILE:str = "Assembly"
        ### SETUP ###
        self._create_extracted_files_directory()
    
    #################
    ##### SETUP #####
    #################
        
    def _create_extracted_files_directory(self):
        '''
        Creates an extracted files directory.
        '''
        print(f"INFO: _create_extracted_files_directory: Creating extracted files directory...")
        if(not os.path.exists(self._EXTRACTED_FILES_DIR)):
            os.mkdir(self._EXTRACTED_FILES_DIR)
        print(f"INFO: _create_extracted_files_directory: Creation complete!")

    ################################
    ##### EXTRACT & DECOMPRESS #####
    ################################

    def _extract_asset_by_pointer(self, pointer_index_start:int, file_name:str):
        '''
        Extracts a singular compressed bin file from the ROM
        '''
        asset_index_start:int = self._read_bytes_as_int(pointer_index_start, 4) + self._ASSET_TABLE_OFFSET
        asset_index_end:int = self._read_bytes_as_int(pointer_index_start + 0x8, 4) + self._ASSET_TABLE_OFFSET
        file_path:str = f"{self._EXTRACTED_FILES_DIR}{file_name}{self._COMPRESSED_BIN_EXTENSION}"
        with open(file_path, "wb+") as comp_file:
            comp_file.write(self._file_content[asset_index_start:asset_index_end])

    def extract_asset_table_pointers(self):
        '''
        Extracts all of the compressed bin files from the ROM into an individual bin file and
        runs the decompression algorithm to create the decompressed bin file.
        '''
        print(f"INFO: extract_and_decompress_all_asset_table_pointers: Extracting and decompressing all assets...")
        for pointer_count, pointer_index_start in enumerate(range(
                self._ASSET_TABLE_START_INDEX,
                self._ASSET_TABLE_END_INDEX,
                0x8)):
            if(pointer_count % 100 == 0):
                pointer_hex_str:str = self._convert_int_to_hex_str(pointer_index_start, byte_count=4)
                print(f"DEBUG: extract_and_decompress_all_asset_table_pointers: Current pointer {pointer_hex_str}")
            file_name:str = self._convert_int_to_hex_str(pointer_index_start)
            self._extract_asset_by_pointer(pointer_index_start, file_name)
            compressed_obj = COMPRESSION_CLASS(file_name, self._COMPRESSED_STR)
            compressed_obj.decompress_file_main()
        print(f"INFO: extract_and_decompress_all_asset_table_pointers: Extraction and decompression complete!")

    #####################################
    ##### COMPRESSION AND INSERTION #####
    #####################################
    
    def _append_asset_to_rom(self, file_name:str):
        '''
        Adds the asset file to the back of the Banjo-Kazooie ROM.
        '''
        file_path:str = f"{self._EXTRACTED_FILES_DIR}{file_name}{self._COMPRESSED_BIN_EXTENSION}"
        with open(file_path, "rb") as comp_file:
           self._file_content.extend(bytearray(comp_file.read()))

    def _adjust_asset_pointer_table(self,
            pointer_index_start:int, start_address:int, compressed_content_length:int):
        '''
        Adjusts the asset pointer table to reflect the new locations of the asset files.
        '''
        end_address:int = start_address + compressed_content_length
        pointer_start_address:int = start_address - self._ASSET_TABLE_OFFSET
        self._write_bytes_from_int(pointer_index_start, pointer_start_address, 4)
        pointer_end_address:int = end_address - self._ASSET_TABLE_OFFSET
        self._write_bytes_from_int(pointer_index_start + 0x08, pointer_end_address, 4)
        return end_address

    def append_asset_table_pointers(self):
        '''
        Readies all asset files for insertion and recalculates the CRC checksum values.
        '''
        print(f"INFO: append_asset_table_pointers: Start...")
        start_address:int = self._ROM_END_INDEX
        bin_files_list = os.listdir(self._EXTRACTED_FILES_DIR)
        for pointer_index_start in range(self._ASSET_TABLE_START_INDEX, self._ASSET_TABLE_END_INDEX, 0x8):
            file_name:str = self._convert_int_to_hex_str(pointer_index_start)
            raw_file_name:str = file_name + self._RAW_BIN_EXTENSION
            compressed_file_name:str = file_name + self._COMPRESSED_BIN_EXTENSION
            if(raw_file_name in bin_files_list):
                file_type:str = self._RAW_STR
            elif(compressed_file_name in bin_files_list):
                file_type:str = self._DECOMPRESSED_STR
            else:
                raise Exception(f"ERROR: append_asset_table_pointers: Pointer '{self._convert_int_to_hex_str(pointer_index_start)}' file not found!")
            compressed_obj = COMPRESSION_CLASS(file_name, file_type)
            compressed_content_length:int = compressed_obj.compress_file_main(self._ASSET_FILE)
            self._append_asset_to_rom(file_name)
            start_address:int = self._adjust_asset_pointer_table(
                pointer_index_start, start_address, compressed_content_length
                )
        print(f"INFO: append_asset_table_pointers: Calculating New CRC Checksum...")
        self._calculate_new_crc()
        print(f"INFO: append_asset_table_pointers: Complete!")

    ####################
    ##### CHECKSUM #####
    ####################

    def _unsigned_long(self, int_val:int):
        '''
        Returns the last four bytes of the given integer.
        '''
        return int_val & 0xFFFFFFFF
    
    def _rotate_left(self, j:int, b:int):
        '''
        Rotate left machine language function.
        '''
        return self._unsigned_long(j << b) | (j >> (-b & 0x1F))

    def _calculate_new_crc(self):
        '''
        Calculates the new CRC checksum values for Banjo-Kazooie.
        '''
        t1 = t2 = t3 = t4 = t5 = t6 = self._CIC
        for check_index in range(self._CHECK_ROM_START_INDEX, self._CHECK_ROM_END_INDEX, 0x4):
            d = self._read_bytes_as_int(check_index, byte_count=4)
            t6d = self._unsigned_long(t6 + d)
            if(t6d < t6):
                t4 = self._unsigned_long(t4 + 1)
            t6 = t6d
            t3 ^= d
            r = self._rotate_left(d, d & 0x1F)
            t5 = self._unsigned_long(t5 + r)
            if(t2 > d):
                t2 ^= r
            else:
                t2 ^= t6 ^ d
            t1 = self._unsigned_long(t1 + (t5 ^ d))
        crc1 = self._unsigned_long((t6 ^ t4) + t3)
        crc2 = self._unsigned_long((t5 ^ t2) + t1)
        self._write_bytes_from_int(self._CRC1_INDEX_START, crc1, 4)
        self._write_bytes_from_int(self._CRC2_INDEX_START, crc2, 4)

    ##########################
    ##### POST FUNCTIONS #####
    ##########################

    def save_as_new_rom(self, new_file_path:str):
        '''
        Saves the Banjo-Kazooie Rom to new destination.
        '''
        print(f"INFO: save_as_new_rom: Saving new ROM to '{new_file_path}'...")
        self._save_changes(new_file_path)
        print(f"INFO: save_as_new_rom: New ROM saved!")
    
    def clear_extracted_files_dir(self, filter:str):
        '''
        Removes bin files from the extracted files directory that end with a certain filter
        '''
        print(f"INFO: _clear_extracted_files_dir: Cleaning files ending in {filter}...")
        bin_files_list = os.listdir(self._EXTRACTED_FILES_DIR)
        for file_name in bin_files_list:
            if(file_name.endswith(filter)):
                os.remove(os.path.join(self._EXTRACTED_FILES_DIR, file_name))
        print(f"INFO: _clear_extracted_files_dir: Cleaning complete!")

################
##### MAIN #####
################

if __name__ == '__main__':
    file_path:str = "C:/Users/Cyrus/Documents/VS_Code/BK_Randomizer/BK_Randomizer_v3/Banjo-Kazooie.z64"
    new_file_path:str = "C:/Users/Cyrus/Documents/VS_Code/BK_Randomizer/BK_Randomizer_v3/Banjo-Kazooie-TEST.z64"
    bk_rom = BK_ROM_CLASS(file_path)
    bk_rom.extract_asset_table_pointers()
    bk_rom.append_asset_table_pointers()
    bk_rom.save_as_new_rom(new_file_path)
    bk_rom.clear_extracted_files_dir(bk_rom._BIN_EXTENSION)
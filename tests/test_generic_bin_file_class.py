'''
Purpose:
'''

###################
##### IMPORTS #####
###################

import os
import shutil
import pytest

from randomizer.generic_bin_file_class import Generic_Bin_File_Class

######################
##### TEST CLASS #####
######################

class Test_Generic_Bin_File_Class():

    ### SETUP ###

    def setup_method(self):
        print("Setup Method")
        test_folder:str = "tests/test_files/"
        self.original_test_file_path:str = f"{test_folder}original_generic_bin_file.bin"
        self.duplicate_test_file_path:str = f"{test_folder}test_generic_bin_file.bin"

    ### READ ###

    @pytest.mark.parametrize(
            "index_start,byte_count,check_for_negative,expected_val",
            [
                (0x0F, 1, False, 0xF0),
                (0x0E, 2, False, 0xE0F0),
                (0x0C, 4, False, 0xC0D0E0F0),
                (0x08, 8, False, 0x8090A0B0C0D0E0F0),
                (0x0F, 1, True, -0x10),
                (0x0E, 2, True, -0x1F10),
                (0x0C, 4, True, -0x3F2F1F10),
                (0x08, 8, True, -0x7F6F5F4F3F2F1F10),
            ]
        )
    def test_read_bytes(self, index_start:int, byte_count:int,
                        check_for_negative:bool, expected_val:int):
        print("Test Read Bytes")
        generic_bin_file_obj = Generic_Bin_File_Class(self.original_test_file_path)
        this_byte:int = generic_bin_file_obj._read_bytes_as_int(index_start, byte_count, check_for_negative)
        assert this_byte == expected_val

    @pytest.mark.parametrize(
            "index_start,expected_val",
            [
                (0x10, 1.0),
                (0x14, 3.14),
                (0x18, -1.0),
                (0x1C, -420.69)
            ]
        )
    def test_read_float(self, index_start:int, expected_val:float):
        print("Test Read Float")
        generic_bin_file_obj = Generic_Bin_File_Class(self.original_test_file_path)
        this_float:float = generic_bin_file_obj._read_bytes_as_float(index_start)
        assert round(this_float, 2) == expected_val

    @pytest.mark.parametrize(
            "index_start,byte_count,expected_val",
            [
                (0x00, 0x10, '00102030405060708090A0B0C0D0E0F0'),
                (0x10, 0x10, '3F80000040490FDABF800000C3D25852'),
                (0x20, 0x10, '2248656C6C6F2C20576F726C64212220'),
            ]
        )
    def test_read_hex_str(self, index_start:int, byte_count:int, expected_val:str):
        print("Test Read Hex Str")
        generic_bin_file_obj = Generic_Bin_File_Class(self.original_test_file_path)
        hex_str_val:str = generic_bin_file_obj._read_bytes_as_hex_str(index_start, byte_count)
        assert hex_str_val == expected_val

    @pytest.mark.parametrize(
            "index_start,byte_count,expected_val",
            [
                (0x20, 0xF, '"Hello, World!"'),
            ]
        )
    def test_read_str(self, index_start:int, byte_count:int, expected_val:str):
        print("Test Read Str")
        generic_bin_file_obj = Generic_Bin_File_Class(self.original_test_file_path)
        this_string:str = generic_bin_file_obj._read_bytes_as_str(index_start, byte_count)
        assert this_string == expected_val

    # WRITE

    @pytest.mark.parametrize(
            "index_start,int_val,byte_count,expected_val",
            [
                (0x01, 0x11, 1, 0x11),
                (0x02, 0x2233, 2, 0x2233),
                (0x03, 0x44556677, 4, 0x44556677),
                (0x04, 0x8899AABBCCDDEEFF, 8, 0x8899AABBCCDDEEFF),
                (0x05, -0x11, 1, -0x11),
                (0x06, -0x2233, 2, -0x2233),
                (0x07, -0x44556677, 4, -0x44556677),
                (0x08, -0x7799AABBCCDDEEFF, 8, -0x7799AABBCCDDEEFF),
            ]
        )
    def test_write_bytes(self, index_start:int, int_val:int, byte_count:int, expected_val:int):
        print("Test Write Bytes")
        generic_bin_file_obj = Generic_Bin_File_Class(self.original_test_file_path)
        generic_bin_file_obj._write_bytes_from_int(index_start, int_val, byte_count)
        generic_bin_file_obj._save_changes(self.duplicate_test_file_path)
        generic_bin_file_obj = Generic_Bin_File_Class(self.duplicate_test_file_path)
        check_for_negative = False
        if(int_val < 0):
            check_for_negative:bool = True
        this_byte:int = generic_bin_file_obj._read_bytes_as_int(index_start, byte_count, check_for_negative)
        assert this_byte == expected_val


    @pytest.mark.parametrize(
            "index_start,float_val",
            [
                (0x10, 1.0),
                (0x14, 3.14),
                (0x18, -1.0),
                (0x1C, -420.69)
            ]
        )
    def test_write_float(self, index_start:int, float_val:float):
        print("Test Write Float")
        generic_bin_file_obj = Generic_Bin_File_Class(self.original_test_file_path)
        generic_bin_file_obj._write_bytes_from_float(index_start, float_val)
        generic_bin_file_obj._save_changes(self.duplicate_test_file_path)
        generic_bin_file_obj = Generic_Bin_File_Class(self.duplicate_test_file_path)
        this_float:float = generic_bin_file_obj._read_bytes_as_float(index_start)
        assert round(this_float, 2) == float_val


    @pytest.mark.parametrize(
            "index_start,hex_str_val",
            [
                (0x00, '123456789ABDEF123456789ABDEF'),
            ]
        )
    def test_write_hex_str(self, index_start:int, hex_str_val:str):
        print("Test Write Hex Str")
        generic_bin_file_obj = Generic_Bin_File_Class(self.original_test_file_path)
        generic_bin_file_obj._write_bytes_from_hex_str(index_start, hex_str_val)
        generic_bin_file_obj._save_changes(self.duplicate_test_file_path)
        generic_bin_file_obj = Generic_Bin_File_Class(self.duplicate_test_file_path)
        byte_count:int = len(hex_str_val) // 2
        this_hex_str:str = generic_bin_file_obj._read_bytes_as_hex_str(index_start, byte_count)
        assert this_hex_str == hex_str_val

    @pytest.mark.parametrize(
            "index_start,str_val",
            [
                (0x20, 'Guh-Huh! ~ Roo!'),
            ]
        )
    def test_write_str(self, index_start:int, str_val:str):
        print("Test Write Str")
        generic_bin_file_obj = Generic_Bin_File_Class(self.original_test_file_path)
        generic_bin_file_obj._write_bytes_from_str(index_start, str_val)
        generic_bin_file_obj._save_changes(self.duplicate_test_file_path)
        generic_bin_file_obj = Generic_Bin_File_Class(self.duplicate_test_file_path)
        byte_count:int = len(str_val)
        this_str:str = generic_bin_file_obj._read_bytes_as_str(index_start, byte_count)
        assert this_str == str_val

if __name__ == '__main__':
    pytest.main()
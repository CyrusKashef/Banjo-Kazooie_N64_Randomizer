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

    # SETUP

    def setup_method(self):
        print("Running Setup")
        original_test_file_path:str = "tests/test_files/original_generic_bin_file.bin"
        self.duplicate_test_file_path:str = "tests/test_files/test_generic_bin_file.bin"
        print("Copying Generic Bin File")
        shutil.copy(original_test_file_path, self.duplicate_test_file_path)
        print("Creating Generic Bin File Object")
        self.generic_bin_file_obj = Generic_Bin_File_Class(self.duplicate_test_file_path)
        print("Setup Complete!")

    # READ

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
        print("Running Test Read Unsigned Byte")
        this_byte:int = self.generic_bin_file_obj._read_bytes_as_int(index_start, byte_count, check_for_negative)
        print(f"This Byte: {this_byte}")
        print(f"Expected Val: {expected_val}")
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
        this_float:float = self.generic_bin_file_obj._read_bytes_as_float(index_start)
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
        hex_str:str = self.generic_bin_file_obj._read_bytes_as_hex_str(index_start, byte_count)
        assert hex_str == expected_val

    @pytest.mark.parametrize(
            "index_start,byte_count,expected_val",
            [
                (0x20, 0xF, '"Hello, World!"'),
            ]
        )
    def test_read_str(self, index_start:int, byte_count:int, expected_val:str):
        this_string:str = self.generic_bin_file_obj._read_bytes_as_str(index_start, byte_count)
        assert this_string == expected_val

    # WRITE

    # def test_write_bytes():
    #     pass

    # def test_write_float():
    #     pass

    # def test_write_hex_str():
    #     pass

    # def test_write_str():
    #     pass

if __name__ == '__main__':
    pytest.main()
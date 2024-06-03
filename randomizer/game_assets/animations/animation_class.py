'''
Purpose:
*
'''

###################
##### IMPORTS #####
###################

from randomizer.generic_bin_file_class import Generic_Bin_File_Class
from randomizer.constants.int_values.animation_constants import ANIMATION_CONSTANTS as CONSTANT

###########################
##### ANIMATION CLASS #####
###########################

class ANIMATION_CLASS(Generic_Bin_File_Class):
    '''
    Class for reading and modifying object 3D model files.
    '''
    def __init__(self, file_path:str):
        '''
        Constructor
        '''
        # Variables
        self._file_path = file_path
        self._file_content = None
        self._animation_dict:dict = {}

        # Startup Function
        self.read_animation_file()

    #############################
    ##### UTILITY FUNCTIONS #####
    #############################

    ###################
    ##### PARSING #####
    ###################

    def _parse_animation_element_data(self,
            curr_index:int, curr_element_count:int, curr_data_count:int):
        '''
        Pass
        '''
        unk0_bit_count_list:list = [
            1, 1, 14
        ]
        unk0_count_list = self._parse_int_by_bits(
            curr_index,
            byte_count=0x2,
            bit_count_list=unk0_bit_count_list)
        unk2 = self._read_bytes_as_int(curr_index + 0x2, byte_count=2, check_for_negative=True)
        self._animation_dict[CONSTANT.element_list][curr_element_count][CONSTANT.element_data_list][curr_data_count] = {
            CONSTANT.element_data_unk0_2: unk0_count_list[2],
            CONSTANT.element_data_unk0_1: unk0_count_list[1],
            CONSTANT.element_data_unk0_0: unk0_count_list[0],
            CONSTANT.element_data_unk2: unk2,
        }
        return curr_index + 0x4

    def _parse_animation_element(self, curr_index:int, curr_element_count:int):
        '''
        Pass
        '''
        unk0_bit_count_list:list = [
            4,  # element_unk0_0
            12, # element_unk0_1
        ]
        unk0_count_list = self._parse_int_by_bits(
            curr_index,
            byte_count=0x2,
            bit_count_list=unk0_bit_count_list)
        self._animation_dict[CONSTANT.element_list][curr_element_count] = {
            CONSTANT.element_unk0_1: unk0_count_list[1],
            CONSTANT.element_unk0_0: unk0_count_list[0],
            CONSTANT.element_data_list: {},
        }
        element_data_count:int = self._read_bytes_as_int(curr_index + 0x2, byte_count=2, check_for_negative=True)
        for curr_data_count in range(element_data_count):
            curr_index:int = self._parse_animation_element_data(curr_index, curr_element_count, curr_data_count)
        return curr_index

    def _parse_animation_elements(self, element_count:int):
        '''
        Pass
        '''
        curr_index:int = 0x8
        self._animation_dict[CONSTANT.element_list] = {}
        for curr_element_count in range(element_count):
            self._animation_dict[CONSTANT.element_list][curr_element_count] = {}
            curr_index:int = self._parse_animation_element(curr_index, curr_element_count)

    def _parse_animation_header(self):
        '''
        Pass
        '''
        self._animation_dict[CONSTANT.header_unk0] = self._read_bytes_as_int(0x0, byte_count=2, check_for_negative=True)
        self._animation_dict[CONSTANT.header_unk2] = self._read_bytes_as_int(0x2, byte_count=2, check_for_negative=True)
        element_count = self._read_bytes_as_int(0x4, byte_count=2, check_for_negative=True)
        # padding 2 bytes
        return element_count

    ###################
    ##### LOGGING #####
    ###################

    ##########################
    ##### EDIT FUNCTIONS #####
    ##########################

    #################
    ##### WRITE #####
    #################

    def _write_animation_element_data(self, new_content:bytearray, element_data_dict:dict):
        '''
        Pass
        '''
        unk0_bit_count_list:list = [
            (element_data_dict[CONSTANT.element_data_unk0_2], 14),
            (element_data_dict[CONSTANT.element_data_unk0_1], 1),
            (element_data_dict[CONSTANT.element_data_unk0_0], 1),
        ]
        unk0:int = self._construct_int_from_bits(unk0_bit_count_list)
        unk2:int = self._possible_neg_to_pos(element_data_dict[CONSTANT.element_data_unk2], byte_count=2)
        new_content += \
            unk0.to_bytes(2, 'big') + \
            unk2.to_bytes(2, 'big')
        return new_content

    def _write_animation_element(self, new_content:bytearray, element_dict:dict):
        '''
        Pass
        '''
        unk0_bit_count_list:list = [
            (element_dict[CONSTANT.element_unk0_1], 12),
            (element_dict[CONSTANT.element_unk0_0], 4),
        ]
        unk0:int = self._construct_int_from_bits(unk0_bit_count_list)
        element_data_count:int = len(element_dict[CONSTANT.element_data_list])
        new_content += \
            unk0.to_bytes(2, 'big') + \
            element_data_count.to_bytes(2, 'big')
        for curr_element_data_count in element_dict[CONSTANT.element_data_list]:
            element_data_dict:dict = element_dict[CONSTANT.element_data_list][curr_element_data_count]
            new_content = self._write_animation_element_data(new_content, element_data_dict)
        return new_content

    def _write_animation_elements(self, new_content:bytearray):
        '''
        Pass
        '''
        for curr_element_count in self._animation_dict[CONSTANT.element_list]:
            element_dict:dict = self._animation_dict[CONSTANT.element_list][curr_element_count]
            new_content = self._write_animation_element(new_content, element_dict)
        return new_content

    def _write_animation_header(self, ):
        '''
        Pass
        '''
        header_unk0:int = self._possible_neg_to_pos(self._animation_dict[CONSTANT.header_unk0], byte_count=2)
        header_unk2:int = self._possible_neg_to_pos(self._animation_dict[CONSTANT.header_unk2], byte_count=2)
        element_count:int = len(self._animation_dict[CONSTANT.element_list])
        new_content:bytearray = \
            header_unk0.to_bytes(2, 'big') + \
            header_unk2.to_bytes(2, 'big') + \
            element_count.to_bytes(2, 'big')
        return new_content

    ##########################
    ##### MAIN FUNCTIONS #####
    ##########################
        
    def read_animation_file(self):
        '''
        Pass
        '''
        super()._read_file()
        element_count:int = self._parse_animation_header()
        self._parse_animation_elements(element_count)
    
    def save_animation_file(self, file_path:str|None=None):
        '''
        Pass
        '''
        new_content:bytearray = self._write_animation_header()
        new_content:bytearray = self._write_animation_elements(new_content)
        super()._save_changes(file_path)
        del new_content

################
##### MAIN #####
################
    
if __name__ == '__main__':
    file_dir:str = "C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/test2/"
    save_file_dir:str = "C:/Users/Cyrus/Documents/VS_Code/Banjo-Kazooie_Randomizer/Banjo-Kazooie_N64_Randomizer/randomizer/extracted_files/"
    file_list:list = [
        "0F6AE0" # Web Floor (Dying)
        ]
    import filecmp
    for file_name in file_list:
        old_file_name:str = f"{file_dir}{file_name}.bin"
        new_file_name:str = f"{save_file_dir}{file_name}-TEST.bin"
        animation_obj = ANIMATION_CLASS(old_file_name)
        animation_obj.read_animation_file()
        print(animation_obj._animation_dict)
        animation_obj.save_animation_file(new_file_name)
        files_are_copies:bool = filecmp.cmp(old_file_name, new_file_name)
        if(files_are_copies):
            print("Copies")
        else:
            print(f"Not Copies: {file_name}")
            exit(0)
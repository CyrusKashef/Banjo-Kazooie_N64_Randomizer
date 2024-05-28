'''
Purpose:
*
'''

###################
##### IMPORTS #####
###################

from randomizer.generic_bin_file_class import Generic_Bin_File_Class
from randomizer.constants.int_values.object_model_constants import OBJECT_MODEL_CONSTANTS as CONSTANT

##############################
##### OBJECT MODEL CLASS #####
##############################

class OBJECT_2D_MODEL_CLASS(Generic_Bin_File_Class):
    '''
    Class for reading and modifying object 2D model files.
    '''
    def setup_object_3d_model_class(self, file_path:str):
        '''
        Pass
        '''
        # Constants
        self._CI4_VALUE:int = 1 # 1 << 0
        self._CI8_VALUE:int = 2 # 1 << 1
        self._RGBA5551_VALUE:int = 4 # 1 << 2
        self._RGBA8888_VALUE:int = 8 # 1 << 3
        self._IA8_VALUE:int = 16 # 1 << 4

        # Variables
        self._file_path = file_path
        self._file_content = None
        self._object_model_dict:dict = {}
        self._model_type:int = None

        # Class Specific
        self.setup_object_2d_model_class()

    def setup_object_3d_model_class(self):
        '''
        Pass
        '''
        pass

    #############################
    ##### UTILITY FUNCTIONS #####
    #############################

    ###################
    ##### PARSING #####
    ###################
    
    def _parse_sprite_texture_block(self, start_index:int):
        '''
        Pass
        '''
        x_position:int = self._read_bytes_as_int(start_index, byte_count=2)
        y_position:int = self._read_bytes_as_int(start_index + 0x2, byte_count=2)
        width:int = self._read_bytes_as_int(start_index + 0x4, byte_count=2)
        height:int = self._read_bytes_as_int(start_index + 0x6, byte_count=2)
        return x_position, y_position, width, height

    def _parse_color_index(self, start_index:int):
        '''
        Pass
        '''
        sprite_type:int = self._object_model_dict[CONSTANT.sprite_type]
        if(sprite_type == 0x01):
            end_index:int = start_index + 0x20
        elif(sprite_type == 0x02):
            end_index:int = start_index + 0x200
        color_index_list:list = []
        for curr_index in range(start_index, end_index, 0x2):
            curr_color:int = self._read_bytes_as_int(curr_index, byte_count=2)
            color_index_list.append(curr_color)
        return color_index_list, end_index
    
    def _parse_ci4_sprite_pixels(self, start_index:int, sprite_x_dimension:int, sprite_y_dimension:int):
        '''
        Pass
        '''
        sprite_pixel_list:list = []
        for y_position in range(sprite_y_dimension):
            for x_position in range(sprite_x_dimension // 2):
                curr_index = start_index + y_position * sprite_x_dimension // 2 + x_position
                curr_color_index_nums:int = self._read_bytes_as_int(curr_index, byte_count=1)
                curr_pixel_left:int = curr_color_index_nums // 0x10
                curr_pixel_right:int = curr_color_index_nums % 0x10
                sprite_pixel_list.append(curr_pixel_left)
                sprite_pixel_list.append(curr_pixel_right)
        return sprite_pixel_list

    def _parse_ci4_sprites(self, start_index:int):
        '''
        Pass
        '''
        for sprite_count in range(self._object_model_dict[CONSTANT.frame_count]):
            # Color Index
            color_index_list, sprite_texture_block_index_start = self._parse_ci4_color_index(start_index)
            self._object_model_dict[CONSTANT.sprite_list][sprite_count][CONSTANT.sprite_color_index] = color_index_list
            # Sprite Texture Block
            x_position, y_position, width, height = self._parse_sprite_texture_block(sprite_texture_block_index_start)
            # Image
            image_start_index:int = sprite_texture_block_index_start + 0x08
            sprite_x_dimension:int = self._object_model_dict[CONSTANT.sprite_list][sprite_count][CONSTANT.sprite_x_dimension]
            sprite_y_dimension:int = self._object_model_dict[CONSTANT.sprite_list][sprite_count][CONSTANT.sprite_y_dimension]
            sprite_pixel_list:list = self._parse_ci4_sprite_pixels(image_start_index, sprite_x_dimension, sprite_y_dimension)
            self._object_model_dict[CONSTANT.sprite_list][sprite_count][CONSTANT.sprite_pixels] = sprite_pixel_list

    def _parse_frame_header(self, start_index:int):
        '''
        Pass
        '''
        frame_unk_0 = self._read_bytes_as_int(start_index, byte_count=2)
        frame_unk_2 = self._read_bytes_as_int(start_index + 0x02, byte_count=2)
        frame_width = self._read_bytes_as_int(start_index + 0x04, byte_count=2)
        frame_height = self._read_bytes_as_int(start_index + 0x06, byte_count=2)
        frame_chunk_count = self._read_bytes_as_int(start_index + 0x08, byte_count=2)
        frame_unk_a = self._read_bytes_as_int(start_index + 0x0A, byte_count=2)
        frame_unk_c = self._read_bytes_as_int(start_index + 0x0C, byte_count=2)
        frame_unk_e = self._read_bytes_as_int(start_index + 0x0E, byte_count=2)
        frame_unk_10 = self._read_bytes_as_int(start_index + 0x10, byte_count=2)
        frame_unk_12 = self._read_bytes_as_int(start_index + 0x12, byte_count=2)
        curr_index:int = start_index + 0x14
        sprite_type:int = self._object_model_dict[CONSTANT.sprite_type]
        if(sprite_type == 0x01):
            self._parse_ci4_sprites(curr_index)
        else:
            raise Exception(f"Unknown Frame Sprite Type: {hex(sprite_type)}")

    def _parse_frame_offset_list(self, frame_count:int):
        '''
        Pass
        '''
        self._object_model_dict[CONSTANT.frame_offset_dict] = {}
        offset_index_start:int = 0x10
        frames_start_index:int = offset_index_start + frame_count * 0x4
        for frame_offset_count in range(frame_count):
            curr_index:int = offset_index_start + frame_offset_count * 0x4
            frame_offset:int = self._read_bytes_as_int(curr_index, byte_count=4)
            frame_start_index:int = frames_start_index + frame_offset
            self._parse_frame_header(frame_start_index)

    def _parse_2d_model_file_header(self):
        '''
        Pass
        '''
        frame_count:int = self._read_bytes_as_int(0x0, byte_count=2)
        sprite_type:int = self._read_bytes_as_int(0x2, byte_count=2)
        unk4:int = self._read_bytes_as_int(0x4, byte_count=2)
        unk6:int = self._read_bytes_as_int(0x6, byte_count=2)
        unk8:int = self._read_bytes_as_int(0x8, byte_count=2)
        unkA:int = self._read_bytes_as_int(0xA, byte_count=2)
        unkC:int = self._read_bytes_as_int(0xC, byte_count=4)
        self._parse_frame_offset_list(frame_count)

    ###################
    ##### LOGGING #####
    ###################

    ##########################
    ##### EDIT FUNCTIONS #####
    ##########################

    #################
    ##### WRITE #####
    #################

    ##########################
    ##### MAIN FUNCTIONS #####
    ##########################
        
    def read_object_2d_model_file(self):
        '''
        Pass
        '''
        super()._read_file()
        self._parse_2d_model_file_header()

################
##### MAIN #####
################
    
if __name__ == '__main__':
    pass
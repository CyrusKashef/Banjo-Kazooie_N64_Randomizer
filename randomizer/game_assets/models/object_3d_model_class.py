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

class OBJECT_3D_MODEL_CLASS(Generic_Bin_File_Class):
    '''
    Class for reading and modifying object 3D model files.
    '''
    def __init__(self, file_path:str):
        '''
        Constructor
        '''
        # Constant
        self._3d_model_header:int = 0x0000000B

        # Variables
        self._file_path = file_path
        self._file_content = None
        self._object_model_dict:dict = {}
        self._model_type:int = None

        # Class Specific
        self.setup_object_3d_model_class()

    def setup_object_3d_model_class(self):
        '''
        Pass
        '''
        # Constants
        self._CI4_VALUE:int = 1 # 1 << 0
        self._CI8_VALUE:int = 2 # 1 << 1
        self._RGBA5551_VALUE:int = 4 # 1 << 2
        self._RGBA8888_VALUE:int = 8 # 1 << 3
        self._IA8_VALUE:int = 16 # 1 << 4
        self._GEO_TYPE_NORMAL:int = 0
        self._GEO_TYPE_TRILINEAR_MIPMAPPING:int = 2
        self._GEO_TYPE_ENV_MIPMAPPING:int = 4
        self._GEO_TYPE_TRILINEAR_ENV_MIPMAPPING:int = 6

    #############################
    ##### UTILITY FUNCTIONS #####
    #############################

    ###################
    ##### PARSING #####
    ###################

    def _parse_3d_model_file_header(self):
        '''
        Pass
        '''
        self._object_model_dict[CONSTANT.geometry_layout_setup_offset] = self._read_bytes_as_int(0x04, byte_count=4)
        self._object_model_dict[CONSTANT.texture_setup_offset] = self._read_bytes_as_int(0x08, byte_count=2)
        self._object_model_dict[CONSTANT.object_model_geo_type] = self._read_bytes_as_int(0x0A, byte_count=2)
        self._object_model_dict[CONSTANT.display_list_setup_offset] = self._read_bytes_as_int(0x0C, byte_count=4)
        self._object_model_dict[CONSTANT.vertex_setup_offset] = self._read_bytes_as_int(0x10, byte_count=4)
        self._object_model_dict[CONSTANT.hitbox_setup_offset] = self._read_bytes_as_int(0x14, byte_count=4)
        self._object_model_dict[CONSTANT.animation_setup_offset] = self._read_bytes_as_int(0x18, byte_count=4)
        self._object_model_dict[CONSTANT.collision_setup_offset] = self._read_bytes_as_int(0x1C, byte_count=4)
        self._object_model_dict[CONSTANT.unknown_20_setup_offset] = self._read_bytes_as_int(0x20, byte_count=4)
        self._object_model_dict[CONSTANT.effect_setup_offset] = self._read_bytes_as_int(0x24, byte_count=4)
        self._object_model_dict[CONSTANT.unknown_28_setup_offset] = self._read_bytes_as_int(0x28, byte_count=4)
        self._object_model_dict[CONSTANT.animated_textures_offset] = self._read_bytes_as_int(0x2C, byte_count=4)
        self._object_model_dict[CONSTANT.unknown_count] = self._read_bytes_as_int(0x30, byte_count=2)
        self._object_model_dict[CONSTANT.vert_count] = self._read_bytes_as_int(0x32, byte_count=2)
        self._object_model_dict[CONSTANT.unknown_34_header] = self._read_bytes_as_float(0x34)

    ### TEXTURE LIST

    def _parse_texture_list(self, start_index:int, texture_count:int):
        '''
        Pass
        '''
        self._object_model_dict[CONSTANT.texture_list] = {}
        for curr_count in range(texture_count):
            curr_index:int = start_index + 0x10 * curr_count
            print(f"Curr Count, Index: {curr_count}, {hex(curr_index)}")
            self._object_model_dict[CONSTANT.texture_list][curr_count] = {
                CONSTANT.texture_offset: self._read_bytes_as_int(curr_index, byte_count=4),
                CONSTANT.texture_type: self._read_bytes_as_int(curr_index + 0x4, byte_count=2),
                CONSTANT.texture_x_dimension: self._read_bytes_as_int(curr_index + 0x8, byte_count=1),
                CONSTANT.texture_y_dimension: self._read_bytes_as_int(curr_index + 0x9, byte_count=1),
            }
    
    def _parse_ci4_texture(self, start_index:int, texture_count:int):
        '''
        Pass
        '''
        image_start_index:int = start_index + 0x20
        texture_x_dimension:int = self._object_model_dict[CONSTANT.texture_list][texture_count][CONSTANT.texture_x_dimension]
        texture_y_dimension:int = self._object_model_dict[CONSTANT.texture_list][texture_count][CONSTANT.texture_y_dimension]
        # Color Index
        self._object_model_dict[CONSTANT.texture_list][texture_count][CONSTANT.texture_color_index] = []
        for curr_index in range(start_index, image_start_index, 0x2):
            curr_color:int = self._read_bytes_as_int(curr_index, byte_count=2)
            (self._object_model_dict[CONSTANT.texture_list][texture_count][CONSTANT.texture_color_index]).append(curr_color)
        # Image
        self._object_model_dict[CONSTANT.texture_list][texture_count][CONSTANT.texture_pixels] = []
        for y_position in range(texture_y_dimension):
            for x_position in range(texture_x_dimension // 2):
                curr_index:int = image_start_index + y_position * texture_x_dimension // 2 + x_position
                curr_color_index_nums:int = self._read_bytes_as_int(curr_index, byte_count=1)
                curr_pixel_left:int = curr_color_index_nums // 0x10
                curr_pixel_right:int = curr_color_index_nums % 0x10
                (self._object_model_dict[CONSTANT.texture_list][texture_count][CONSTANT.texture_pixels]).append(curr_pixel_left)
                (self._object_model_dict[CONSTANT.texture_list][texture_count][CONSTANT.texture_pixels]).append(curr_pixel_right)
        return curr_index + 0x1
    
    def _parse_ci8_texture(self, start_index:int, texture_count:int):
        '''
        Pass
        '''
        image_start_index:int = start_index + 0x200
        texture_x_dimension:int = self._object_model_dict[CONSTANT.texture_list][texture_count][CONSTANT.texture_x_dimension]
        texture_y_dimension:int = self._object_model_dict[CONSTANT.texture_list][texture_count][CONSTANT.texture_y_dimension]
        # Color Index
        self._object_model_dict[CONSTANT.texture_list][texture_count][CONSTANT.texture_color_index] = []
        for curr_index in range(start_index, image_start_index, 0x2):
            curr_color:int = self._read_bytes_as_int(curr_index, byte_count=2)
            (self._object_model_dict[CONSTANT.texture_list][texture_count][CONSTANT.texture_color_index]).append(curr_color)
        # Image
        self._object_model_dict[CONSTANT.texture_list][texture_count][CONSTANT.texture_pixels] = []
        for y_position in range(texture_y_dimension):
            for x_position in range(texture_x_dimension):
                curr_index:int = image_start_index + y_position * texture_x_dimension + x_position
                curr_pixel:int = self._read_bytes_as_int(curr_index, byte_count=1)
                (self._object_model_dict[CONSTANT.texture_list][texture_count][CONSTANT.texture_pixels]).append(curr_pixel)
        return curr_index + 0x1
    
    def _parse_rgba5551_texture(self, start_index:int, texture_count:int):
        '''
        Pass
        '''
        texture_x_dimension:int = self._object_model_dict[CONSTANT.texture_list][texture_count][CONSTANT.texture_x_dimension]
        texture_y_dimension:int = self._object_model_dict[CONSTANT.texture_list][texture_count][CONSTANT.texture_y_dimension]
        # print(f"Texture X Dimension: {hex(texture_x_dimension)}")
        # print(f"Texture Y Dimension: {hex(texture_y_dimension)}")
        # Note: Might Wanna Put "Not Geo Type Normal"
        using_mipmapping:bool = (self._object_model_dict[CONSTANT.object_model_geo_type] == self._GEO_TYPE_TRILINEAR_MIPMAPPING)
        additional_y:int = 0
        if(using_mipmapping):
            additional_y:int = texture_y_dimension // 2
        self._object_model_dict[CONSTANT.texture_list][texture_count][CONSTANT.texture_pixels] = []
        for y_position in range(texture_y_dimension + additional_y):
            for x_position in range(texture_x_dimension):
                curr_index = start_index + y_position * texture_x_dimension * 2 + x_position * 2
                curr_pixel:int = self._read_bytes_as_int(curr_index, byte_count=2)
                (self._object_model_dict[CONSTANT.texture_list][texture_count][CONSTANT.texture_pixels]).append(curr_pixel)
        # print(f"Num Of Pixels: {hex(len(self._object_model_dict[CONSTANT.texture_list][texture_count][CONSTANT.texture_pixels]))}")
        # print(f"Ending Index: {hex(curr_index + 2)}")
        return curr_index + 0x2
    
    def _parse_rgba8888_texture(self, start_index:int, texture_count:int):
        '''
        Pass
        '''
        texture_x_dimension:int = self._object_model_dict[CONSTANT.texture_list][texture_count][CONSTANT.texture_x_dimension]
        texture_y_dimension:int = self._object_model_dict[CONSTANT.texture_list][texture_count][CONSTANT.texture_y_dimension]
        self._object_model_dict[CONSTANT.texture_list][texture_count][CONSTANT.texture_pixels] = []
        for y_position in range(texture_y_dimension):
            for x_position in range(texture_x_dimension):
                curr_index = start_index + y_position * texture_x_dimension * 4 + x_position * 4
                curr_pixel:int = self._read_bytes_as_int(curr_index, byte_count=4)
                (self._object_model_dict[CONSTANT.texture_list][texture_count][CONSTANT.texture_pixels]).append(curr_pixel)
        return curr_index + 0x4
    
    def _parse_ia8_texture(self, start_index:int, texture_count:int):
        '''
        Pass
        '''
        texture_x_dimension:int = self._object_model_dict[CONSTANT.texture_list][texture_count][CONSTANT.texture_x_dimension]
        texture_y_dimension:int = self._object_model_dict[CONSTANT.texture_list][texture_count][CONSTANT.texture_y_dimension]
        self._object_model_dict[CONSTANT.texture_list][texture_count][CONSTANT.texture_pixels] = []
        for y_position in range(texture_y_dimension):
            for x_position in range(texture_x_dimension):
                curr_index = start_index + y_position * texture_x_dimension + x_position
                curr_pixel:int = self._read_bytes_as_int(curr_index, byte_count=1)
                (self._object_model_dict[CONSTANT.texture_list][texture_count][CONSTANT.texture_pixels]).append(curr_pixel)
        return curr_index + 0x1

    def _get_extra_texture_bytes(self, texture_count:int, texture_end_index:int, next_texture_start_index:int):
        '''
        Pass
        '''
        extra_bytes_list:list = []
        for curr_index in range(texture_end_index, next_texture_start_index):
            curr_byte:int = self._read_bytes_as_int(curr_index, byte_count=1)
            extra_bytes_list.append(curr_byte)
        self._object_model_dict[CONSTANT.texture_list][texture_count][CONSTANT.texture_extra_bytes] = extra_bytes_list

    def _parse_textures(self):
        '''
        Pass
        '''
        texture_setup_offset:int = self._object_model_dict[CONSTANT.texture_setup_offset]
        texture_header_length:int = 0x8
        total_texture_count:int = len(self._object_model_dict[CONSTANT.texture_list])
        texture_info_length:int = 0x10
        texture_begin_offset:int = texture_setup_offset + texture_header_length + total_texture_count * texture_info_length
        for curr_count in self._object_model_dict[CONSTANT.texture_list]:
            texture_offset:int = self._object_model_dict[CONSTANT.texture_list][curr_count][CONSTANT.texture_offset]
            texture_type:int = self._object_model_dict[CONSTANT.texture_list][curr_count][CONSTANT.texture_type]
            texture_start_index:int = texture_begin_offset + texture_offset
            if(curr_count < (total_texture_count - 1)):
                next_texture_offset:int = self._object_model_dict[CONSTANT.texture_list][curr_count + 1][CONSTANT.texture_offset]
                next_texture_start_index:int = texture_begin_offset + next_texture_offset
            else:
                next_texture_start_index:int = self._object_model_dict[CONSTANT.display_list_setup_offset]
            # print(f"Texture Offset: {hex(texture_offset)}")
            # print(f"Texture Type: {hex(texture_type)}")
            # print(f"Texture Start Index: {hex(texture_start_index)}")
            if(texture_type == self._CI4_VALUE):
                texture_end_index:int = self._parse_ci4_texture(start_index=texture_start_index, texture_count=curr_count)
            elif(texture_type == self._CI8_VALUE):
                texture_end_index:int = self._parse_ci8_texture(start_index=texture_start_index, texture_count=curr_count)
            elif(texture_type == self._RGBA5551_VALUE):
                texture_end_index:int = self._parse_rgba5551_texture(start_index=texture_start_index, texture_count=curr_count)
            elif(texture_type == self._RGBA8888_VALUE):
                texture_end_index:int = self._parse_rgba8888_texture(start_index=texture_start_index, texture_count=curr_count)
            elif(texture_type == self._IA8_VALUE):
                texture_end_index:int = self._parse_ia8_texture(start_index=texture_start_index, texture_count=curr_count)
            else:
                raise Exception(f"Texture '{curr_count}' has invalid type '{hex(texture_type)}'")
            self._get_extra_texture_bytes(curr_count, texture_end_index, next_texture_start_index)

    def _parse_texture(self):
        '''
        Pass
        '''
        start_index:int = self._object_model_dict[CONSTANT.texture_setup_offset]
        if(start_index == 0x0):
            return
        self._object_model_dict[CONSTANT.texture_bytes_to_load] = self._read_bytes_as_int(start_index, byte_count=4)
        texture_count:int = self._read_bytes_as_int(start_index + 0x04, byte_count=2)
        if(texture_count > 100):
            print("WTF Is Going On")
            exit(0)
        self._parse_texture_list(start_index + 0x08, texture_count)
        self._parse_textures()

    ### DISPLAY LIST

    def _parse_display_list(self, start_index:int, display_list_command_count:int):
        '''
        Pass
        '''
        self._object_model_dict[CONSTANT.display_list] = {}
        for curr_count in range(display_list_command_count):
            curr_index:int = start_index + 0x8 * curr_count
            self._object_model_dict[CONSTANT.display_list][curr_count] = self._read_bytes_as_int(curr_index, byte_count=8)

    def _parse_display_list_section(self):
        '''
        Pass
        '''
        start_index:int = self._object_model_dict[CONSTANT.display_list_setup_offset]
        if(start_index == 0x0):
            return
        display_list_command_count:int = self._read_bytes_as_int(start_index, byte_count=4)
        self._object_model_dict[CONSTANT.display_list_header_unk_4] = self._read_bytes_as_int(start_index + 0x4, byte_count=1)
        self._object_model_dict[CONSTANT.display_list_header_unk_5] = self._read_bytes_as_int(start_index + 0x5, byte_count=1)
        self._object_model_dict[CONSTANT.display_list_header_unk_6] = self._read_bytes_as_int(start_index + 0x6, byte_count=1)
        self._object_model_dict[CONSTANT.display_list_header_unk_7] = self._read_bytes_as_int(start_index + 0x7, byte_count=1)
        # padding
        self._parse_display_list(start_index + 0x08, display_list_command_count)

    ### VERTEX LIST

    def _parse_vertex_section_header(self, start_index:int):
        '''
        Pass
        '''
        self._object_model_dict[CONSTANT.vertex_min_x_coord] = self._read_bytes_as_int(start_index, byte_count=2)
        self._object_model_dict[CONSTANT.vertex_min_y_coord] = self._read_bytes_as_int(start_index + 0x02, byte_count=2)
        self._object_model_dict[CONSTANT.vertex_min_z_coord] = self._read_bytes_as_int(start_index + 0x04, byte_count=2)
        self._object_model_dict[CONSTANT.vertex_max_x_coord] = self._read_bytes_as_int(start_index + 0x06, byte_count=2)
        self._object_model_dict[CONSTANT.vertex_max_y_coord] = self._read_bytes_as_int(start_index + 0x08, byte_count=2)
        self._object_model_dict[CONSTANT.vertex_max_z_coord] = self._read_bytes_as_int(start_index + 0x0A, byte_count=2)
        self._object_model_dict[CONSTANT.vertex_center_x_coord] = self._read_bytes_as_int(start_index + 0x0C, byte_count=2)
        self._object_model_dict[CONSTANT.vertex_center_y_coord] = self._read_bytes_as_int(start_index + 0x0E, byte_count=2)
        self._object_model_dict[CONSTANT.vertex_center_z_coord] = self._read_bytes_as_int(start_index + 0x10, byte_count=2)
        # distance to furthest vtx relative to model center
        self._object_model_dict[CONSTANT.vertex_local_norm] = self._read_bytes_as_int(start_index + 0x12, byte_count=2)
        # distance to furthest vtx relative to model origin
        self._object_model_dict[CONSTANT.vertex_global_norm] = self._read_bytes_as_int(start_index + 0x16, byte_count=2)

    def _parse_vertex_list(self, start_index:int, vertex_count:int):
        '''
        Pass
        '''
        self._object_model_dict[CONSTANT.vertex_list] = {}
        for curr_count in range(vertex_count):
            curr_index: int = start_index + 0x10 * curr_count
            self._object_model_dict[CONSTANT.vertex_list][curr_count] = {
                CONSTANT.vertex_x_position: self._read_bytes_as_int(curr_index, byte_count=2),
                CONSTANT.vertex_y_position: self._read_bytes_as_int(curr_index + 0x2, byte_count=2),
                CONSTANT.vertex_z_position: self._read_bytes_as_int(curr_index + 0x4, byte_count=2),
                # padding
                CONSTANT.vertex_u_coordinate: self._read_bytes_as_int(curr_index + 0x8, byte_count=2),
                CONSTANT.vertex_v_coordinate: self._read_bytes_as_int(curr_index + 0xA, byte_count=2),
                CONSTANT.vertex_red_value: self._read_bytes_as_int(curr_index + 0xC, byte_count=1),
                CONSTANT.vertex_green_value: self._read_bytes_as_int(curr_index + 0xD, byte_count=1),
                CONSTANT.vertex_blue_value: self._read_bytes_as_int(curr_index + 0xE, byte_count=1),
                CONSTANT.vertex_alpha_value: self._read_bytes_as_int(curr_index + 0xF, byte_count=1),
            }

    def _parse_vertex_section(self):
        '''
        Pass
        '''
        start_index:int = self._object_model_dict[CONSTANT.vertex_setup_offset]
        if(start_index == 0x0):
            return
        self._parse_vertex_section_header(start_index)
        vertex_count:int = self._read_bytes_as_int(start_index + 0x14, byte_count=2)
        self._parse_vertex_list(start_index + 0x18, vertex_count)

    ### ANIMATION LIST

    def _parse_animation_list(self, start_index:int, animation_count:int):
        '''
        Pass
        '''
        self._object_model_dict[CONSTANT.animation_list] = {}
        for curr_count in range(animation_count):
            curr_index:int = start_index + 0x10 * curr_count
            self._object_model_dict[CONSTANT.animation_list][curr_count] = {
                CONSTANT.animation_unk_0: self._read_bytes_as_float(curr_index),
                CONSTANT.animation_unk_4: self._read_bytes_as_float(curr_index + 0x4),
                CONSTANT.animation_unk_8: self._read_bytes_as_float(curr_index + 0x8),
                CONSTANT.animation_bone_id: self._read_bytes_as_int(curr_index + 0xC, byte_count=2),
                CONSTANT.animation_parent_bone_id: self._read_bytes_as_int(curr_index + 0xE, byte_count=2),
            }

    def _parse_animation_section(self):
        '''
        Pass
        '''
        start_index:int = self._object_model_dict[CONSTANT.animation_setup_offset]
        if(start_index == 0x0):
            return
        self._object_model_dict[CONSTANT.animation_unk_header] = self._read_bytes_as_float(start_index)
        animation_count:int = self._read_bytes_as_int(start_index + 0x4, byte_count=2, check_for_negative=True)
        # padding
        animation_list_start_index:int = start_index + 8
        self._parse_animation_list(animation_list_start_index, animation_count)

    ### EFFECTS LIST

    def _parse_effects_list(self, curr_index:int, effects_count:int):
        '''
        Pass
        '''
        self._object_model_dict[CONSTANT.effects_vertex_list] = {}
        self._object_model_dict[CONSTANT.effects_list] = {}
        for curr_count in range(effects_count):
            unk_header:int = self._read_bytes_as_int(curr_index, byte_count=2)
            vertex_count:int = self._read_bytes_as_int(curr_index + 0x2, byte_count=2)
            vertext_list:list = []
            curr_index += 0x4
            curr_vertex_count = 0
            while(curr_vertex_count < vertex_count):
                vertex_id = self._read_bytes_as_int(curr_index, byte_count=2)
                vertext_list.append(vertex_id)
                curr_index += 0x2
                curr_vertex_count += 1
            self._object_model_dict[CONSTANT.effects_list][curr_count] = {
                CONSTANT.effects_section_unk_header: unk_header,
                CONSTANT.effects_vertex_list: vertext_list,
            }

    def _parse_effects_section(self):
        '''
        Pass
        '''
        start_index:int = self._object_model_dict[CONSTANT.effect_setup_offset]
        if(start_index == 0x0):
            return
        effects_count:int = self._read_bytes_as_int(start_index, byte_count=2)
        effects_start_index:int = start_index + 0x2
        self._parse_effects_list(effects_start_index, effects_count)
    
    ### HITBOX LIST

    def _parse_hitbox_type_0_list(self, start_index:int, hitbox_type_0_count:int):
        '''
        Pass
        '''
        hitbox_length:int = 0x18
        self._object_model_dict[CONSTANT.hitbox_type_0_list] = {}
        for curr_count in range(hitbox_type_0_count):
            curr_index:int = start_index + curr_count * hitbox_length
            self._object_model_dict[CONSTANT.hitbox_type_0_list][curr_count] = {
                CONSTANT.hitbox_type_0_unk_0: self._read_bytes_as_int(curr_index, byte_count=2, check_for_negative=True),
                CONSTANT.hitbox_type_0_unk_2: self._read_bytes_as_int(curr_index + 0x2, byte_count=2, check_for_negative=True),
                CONSTANT.hitbox_type_0_unk_4: self._read_bytes_as_int(curr_index + 0x4, byte_count=2, check_for_negative=True),
                CONSTANT.hitbox_type_0_unk_6: self._read_bytes_as_int(curr_index + 0x6, byte_count=2, check_for_negative=True),
                CONSTANT.hitbox_type_0_unk_8: self._read_bytes_as_int(curr_index + 0x8, byte_count=2, check_for_negative=True),
                CONSTANT.hitbox_type_0_unk_A: self._read_bytes_as_int(curr_index + 0xA, byte_count=2, check_for_negative=True),
                CONSTANT.hitbox_type_0_unk_C: self._read_bytes_as_int(curr_index + 0xC, byte_count=2, check_for_negative=True),
                CONSTANT.hitbox_type_0_unk_E: self._read_bytes_as_int(curr_index + 0xE, byte_count=2, check_for_negative=True),
                CONSTANT.hitbox_type_0_unk_10: self._read_bytes_as_int(curr_index + 0x10, byte_count=2, check_for_negative=True),
                CONSTANT.hitbox_type_0_unk_12: self._read_bytes_as_int(curr_index + 0x12, byte_count=1),
                CONSTANT.hitbox_type_0_unk_13: self._read_bytes_as_int(curr_index + 0x13, byte_count=1),
                CONSTANT.hitbox_type_0_unk_14: self._read_bytes_as_int(curr_index + 0x14, byte_count=1),
                CONSTANT.hitbox_type_0_unk_15: self._read_bytes_as_int(curr_index + 0x15, byte_count=1),
                CONSTANT.hitbox_type_0_unk_16: self._read_bytes_as_int(curr_index + 0x16, byte_count=1, check_for_negative=True),
                CONSTANT.hitbox_type_0_unk_17: self._read_bytes_as_int(curr_index + 0x17, byte_count=1),
            }
        curr_index = start_index + hitbox_type_0_count * hitbox_length
        return curr_index

    def _parse_hitbox_type_1_list(self, start_index:int, hitbox_type_1_count:int):
        '''
        Pass
        '''
        hitbox_length:int = 0x10
        self._object_model_dict[CONSTANT.hitbox_type_1_list] = {}
        for curr_count in range(hitbox_type_1_count):
            curr_index:int = start_index + curr_count * hitbox_length
            self._object_model_dict[CONSTANT.hitbox_type_1_list][curr_count] = {
                CONSTANT.hitbox_type_1_unk_0: self._read_bytes_as_int(curr_index, byte_count=2, check_for_negative=True),
                CONSTANT.hitbox_type_1_unk_2: self._read_bytes_as_int(curr_index + 0x2, byte_count=2, check_for_negative=True),
                CONSTANT.hitbox_type_1_unk_4: self._read_bytes_as_int(curr_index + 0x4, byte_count=2, check_for_negative=True),
                CONSTANT.hitbox_type_1_unk_6: self._read_bytes_as_int(curr_index + 0x6, byte_count=2, check_for_negative=True),
                CONSTANT.hitbox_type_1_unk_8: self._read_bytes_as_int(curr_index + 0x8, byte_count=2, check_for_negative=True),
                CONSTANT.hitbox_type_1_unk_A: self._read_bytes_as_int(curr_index + 0xA, byte_count=1),
                CONSTANT.hitbox_type_1_unk_B: self._read_bytes_as_int(curr_index + 0xB, byte_count=1),
                CONSTANT.hitbox_type_1_unk_C: self._read_bytes_as_int(curr_index + 0xC, byte_count=1),
                CONSTANT.hitbox_type_1_unk_D: self._read_bytes_as_int(curr_index + 0xD, byte_count=1),
                CONSTANT.hitbox_type_1_unk_E: self._read_bytes_as_int(curr_index + 0xE, byte_count=1, check_for_negative=True),
                CONSTANT.hitbox_type_1_unk_F: self._read_bytes_as_int(curr_index + 0xF, byte_count=1),
            }
        curr_index = start_index + hitbox_type_1_count * hitbox_length
        return curr_index

    def _parse_hitbox_type_2_list(self, start_index:int, hitbox_type_2_count:int):
        '''
        Pass
        '''
        hitbox_length:int = 0xC
        self._object_model_dict[CONSTANT.hitbox_type_2_list] = {}
        for curr_count in range(hitbox_type_2_count):
            curr_index:int = start_index + curr_count * hitbox_length
            self._object_model_dict[CONSTANT.hitbox_type_2_list][curr_count] = {
                CONSTANT.hitbox_type_2_unk_0: self._read_bytes_as_int(curr_index, byte_count=2, check_for_negative=True),
                CONSTANT.hitbox_type_2_unk_2: self._read_bytes_as_int(curr_index + 0x2, byte_count=2, check_for_negative=True),
                CONSTANT.hitbox_type_2_unk_4: self._read_bytes_as_int(curr_index + 0x4, byte_count=2, check_for_negative=True),
                CONSTANT.hitbox_type_2_unk_6: self._read_bytes_as_int(curr_index + 0x6, byte_count=2, check_for_negative=True),
                CONSTANT.hitbox_type_2_unk_8: self._read_bytes_as_int(curr_index + 0x8, byte_count=1),
                CONSTANT.hitbox_type_2_unk_9: self._read_bytes_as_int(curr_index + 0xA, byte_count=1, check_for_negative=True),
                CONSTANT.hitbox_type_2_unk_A: self._read_bytes_as_int(curr_index + 0xB, byte_count=1),
                CONSTANT.hitbox_type_2_unk_B: self._read_bytes_as_int(curr_index + 0xC, byte_count=1),
            }
        curr_index = start_index + hitbox_type_2_count * hitbox_length
        return curr_index

    def _parse_hitbox_section(self):
        '''
        Pass
        '''
        start_index:int = self._object_model_dict[CONSTANT.hitbox_setup_offset]
        if(start_index == 0x0):
            return
        hitbox_type_0_count:int = self._read_bytes_as_int(start_index, byte_count=2)
        hitbox_type_1_count:int = self._read_bytes_as_int(start_index + 0x2, byte_count=2)
        hitbox_type_2_count:int = self._read_bytes_as_int(start_index + 0x4, byte_count=2)
        self._object_model_dict[CONSTANT.hitbox_header_unk] = self._read_bytes_as_int(start_index + 0x6, byte_count=2)
        curr_index:int = start_index + 0x8
        curr_index:int = self._parse_hitbox_type_0_list(curr_index, hitbox_type_0_count)
        curr_index:int = self._parse_hitbox_type_1_list(curr_index, hitbox_type_1_count)
        self._parse_hitbox_type_2_list(curr_index, hitbox_type_2_count)

    ### ANIMATION TEXTURE LIST

    def _parse_animated_texture_list(self):
        '''
        Pass
        '''
        start_index:int = self._object_model_dict[CONSTANT.animated_textures_offset]
        if(start_index == 0x0):
            return
        self._object_model_dict[CONSTANT.animation_texture_frame_size] = self._read_bytes_as_int(start_index, byte_count=2, check_for_negative=True)
        self._object_model_dict[CONSTANT.animation_texture_frame_count] = self._read_bytes_as_int(start_index + 0x2, byte_count=2, check_for_negative=True)
        self._object_model_dict[CONSTANT.animation_texture_frame_rate] = self._read_bytes_as_float(start_index + 0x4)
        # padding

    ### COLLISION LIST

    def _parse_collision_geo_list(self, start_index:int, geo_count:int):
        '''
        Pass
        '''
        self._object_model_dict[CONSTANT.collision_geo_list] = {}
        curr_index:int = start_index
        for curr_count in range(geo_count):
            curr_index:int = start_index + 0x04 * curr_count
            self._object_model_dict[CONSTANT.collision_geo_list][curr_count] = {
                CONSTANT.collision_start_tri_index: self._read_bytes_as_int(curr_index, byte_count=2),
                CONSTANT.collision_geo_tri_count: self._read_bytes_as_int(curr_index + 0x2, byte_count=2),
            }
        curr_index += 0x04
        return curr_index

    def _parse_collision_collision_tri_list(self, start_index:int, tri_count:int):
        '''
        Pass
        '''
        self._object_model_dict[CONSTANT.collision_tri_list] = {}
        for curr_count in range(tri_count):
            curr_index: int = start_index + 0x0C * curr_count
            self._object_model_dict[CONSTANT.collision_tri_list][curr_count] = {
                CONSTANT.collision_vertex_1: self._read_bytes_as_int(curr_index, byte_count=2),
                CONSTANT.collision_vertex_2: self._read_bytes_as_int(curr_index + 0x2, byte_count=2),
                CONSTANT.collision_vertex_3: self._read_bytes_as_int(curr_index + 0x4, byte_count=2),
                CONSTANT.collision_tri_unk: self._read_bytes_as_int(curr_index + 0x6, byte_count=2),
                CONSTANT.collision_flags: self._read_bytes_as_int(curr_index + 0x8, byte_count=4),
            }

    def _parse_collision_list(self):
        '''
        Pass
        '''
        start_index:int = self._object_model_dict[CONSTANT.collision_setup_offset]
        if(start_index == 0x0):
            return
        self._object_model_dict[CONSTANT.collision_min_x] = self._read_bytes_as_int(start_index, byte_count=2)
        self._object_model_dict[CONSTANT.collision_min_y] = self._read_bytes_as_int(start_index + 0x02, byte_count=2)
        self._object_model_dict[CONSTANT.collision_min_z] = self._read_bytes_as_int(start_index + 0x04, byte_count=2)
        self._object_model_dict[CONSTANT.collision_max_x] = self._read_bytes_as_int(start_index + 0x06, byte_count=2)
        self._object_model_dict[CONSTANT.collision_max_y] = self._read_bytes_as_int(start_index + 0x08, byte_count=2)
        self._object_model_dict[CONSTANT.collision_max_z] = self._read_bytes_as_int(start_index + 0x0A, byte_count=2)
        self._object_model_dict[CONSTANT.collision_y_stride] = self._read_bytes_as_int(start_index + 0x0C, byte_count=2)
        self._object_model_dict[CONSTANT.collision_z_stride] = self._read_bytes_as_int(start_index + 0x0E, byte_count=2)
        collision_geo_count:int = self._read_bytes_as_int(start_index + 0x10, byte_count=2)
        self._object_model_dict[CONSTANT.collision_scale] = self._read_bytes_as_int(start_index + 0x12, byte_count=2)
        collision_tri_count:int = self._read_bytes_as_int(start_index + 0x14, byte_count=2)
        # padding
        curr_index:int = self._parse_collision_geo_list(start_index + 0x18, collision_geo_count)
        self._parse_collision_collision_tri_list(curr_index, collision_tri_count)

    ### GEOMETRY LIST

    def _parse_geometry_list(self):
        '''
        Pass
        '''
        start_index:int = self._object_model_dict[CONSTANT.geometry_layout_setup_offset]
        if(start_index == 0x0):
            return
        self._object_model_dict[CONSTANT.geometry_list] = {}
        rom_end_index:int = len(self._file_content) - 1
        for curr_count, curr_index in enumerate(range(start_index, rom_end_index, 0x4)):
            self._object_model_dict[CONSTANT.geometry_list][curr_count] = self._read_bytes_as_int(curr_index, byte_count=4)

    ###################
    ##### LOGGING #####
    ###################

    ##########################
    ##### EDIT FUNCTIONS #####
    ##########################

    def _replace_textures(self, replacement_dict:dict):
        '''
        Pass
        '''
        for texture_count in replacement_dict:
            self._object_model_dict[CONSTANT.texture_list][texture_count][CONSTANT.texture_pixels] = \
                self._object_model_dict[CONSTANT.texture_list][replacement_dict[texture_count]][CONSTANT.texture_pixels]

    def _replace_display_list_commands(self, replacement_dict:dict):
        '''
        Pass
        '''
        for curr_count in self._object_model_dict[CONSTANT.display_list]:
            curr_command:int = self._object_model_dict[CONSTANT.display_list][curr_count]
            if(curr_command in replacement_dict):
                self._object_model_dict[CONSTANT.display_list][curr_count] = replacement_dict[curr_command]

    #################
    ##### WRITE #####
    #################

    def _write_file_header(self, new_content:bytearray):
        '''
        Pass
        '''
        geometry_layout_setup_offset:int = self._object_model_dict[CONSTANT.geometry_layout_setup_offset]
        texture_setup_offset:int = self._object_model_dict[CONSTANT.texture_setup_offset]
        object_model_geo_type:int = self._object_model_dict[CONSTANT.object_model_geo_type]
        display_list_setup_offset:int = self._object_model_dict[CONSTANT.display_list_setup_offset]
        vertex_setup_offset:int = self._object_model_dict[CONSTANT.vertex_setup_offset]
        hitbox_setup_offset:int = self._object_model_dict[CONSTANT.hitbox_setup_offset]
        animation_setup_offset:int = self._object_model_dict[CONSTANT.animation_setup_offset]
        collision_setup_offset:int = self._object_model_dict[CONSTANT.collision_setup_offset]
        unknown_20_setup_offset:int = self._object_model_dict[CONSTANT.unknown_20_setup_offset]
        effect_setup_offset:int = self._object_model_dict[CONSTANT.effect_setup_offset]
        unknown_28_setup_offset:int = self._object_model_dict[CONSTANT.unknown_28_setup_offset]
        animated_textures_offset:int = self._object_model_dict[CONSTANT.animated_textures_offset]
        unknown_count:int = self._object_model_dict[CONSTANT.unknown_count]
        vert_count:int = self._object_model_dict[CONSTANT.vert_count]
        unknown_34_header:float = self._object_model_dict[CONSTANT.unknown_34_header]
        new_content += \
            geometry_layout_setup_offset.to_bytes(4, 'big') + \
            texture_setup_offset.to_bytes(2, 'big') + \
            object_model_geo_type.to_bytes(2, 'big') + \
            display_list_setup_offset.to_bytes(4, 'big') + \
            vertex_setup_offset.to_bytes(4, 'big') + \
            hitbox_setup_offset.to_bytes(4, 'big') + \
            animation_setup_offset.to_bytes(4, 'big') + \
            collision_setup_offset.to_bytes(4, 'big') + \
            unknown_20_setup_offset.to_bytes(4, 'big') + \
            effect_setup_offset.to_bytes(4, 'big') + \
            unknown_28_setup_offset.to_bytes(4, 'big') + \
            animated_textures_offset.to_bytes(4, 'big') + \
            unknown_count.to_bytes(2, 'big') + \
            vert_count.to_bytes(2, 'big') + \
            self._convert_float_to_hex_bytes(unknown_34_header)
        return new_content

    ### TEXTURE LIST

    def _write_texture_list(self, new_content:bytearray):
        '''
        Pass
        '''
        for curr_count in self._object_model_dict[CONSTANT.texture_list]:
            curr_texture_info:dict = self._object_model_dict[CONSTANT.texture_list][curr_count]
            texture_offset:int = curr_texture_info[CONSTANT.texture_offset]
            texture_type:int = curr_texture_info[CONSTANT.texture_type]
            texture_x_dimension:int = curr_texture_info[CONSTANT.texture_x_dimension]
            texture_y_dimension:int = curr_texture_info[CONSTANT.texture_y_dimension]
            new_content += \
                texture_offset.to_bytes(4, 'big') + \
                texture_type.to_bytes(2, 'big') + \
                (0x0000).to_bytes(2, 'big') + \
                texture_x_dimension.to_bytes(1, 'big') + \
                texture_y_dimension.to_bytes(1, 'big') + \
                (0x000000000000).to_bytes(6, 'big')
        return new_content
    
    def _write_ci4_texture(self, new_content:bytearray, texture_count:int):
        '''
        Pass
        '''
        # Color Index
        for curr_color in self._object_model_dict[CONSTANT.texture_list][texture_count][CONSTANT.texture_color_index]:
            new_content += curr_color.to_bytes(2, 'big')
        # Image
        total_pixel_count:int = len(self._object_model_dict[CONSTANT.texture_list][texture_count][CONSTANT.texture_pixels])
        for curr_pixel_count in range(0, total_pixel_count, 2):
            curr_pixel_left:int = self._object_model_dict[CONSTANT.texture_list][texture_count][CONSTANT.texture_pixels][curr_pixel_count]
            curr_pixel_right:int = self._object_model_dict[CONSTANT.texture_list][texture_count][CONSTANT.texture_pixels][curr_pixel_count + 1]
            curr_color_index_nums:int = curr_pixel_left * 0x10 + curr_pixel_right
            new_content += curr_color_index_nums.to_bytes(1, 'big')
        return new_content
    
    def _write_ci8_texture(self, new_content:bytearray, texture_count:int):
        '''
        Pass
        '''
        # Color Index
        for curr_color in self._object_model_dict[CONSTANT.texture_list][texture_count][CONSTANT.texture_color_index]:
            new_content += curr_color.to_bytes(2, 'big')
        # Image
        for curr_pixel in self._object_model_dict[CONSTANT.texture_list][texture_count][CONSTANT.texture_pixels]:
            new_content += curr_pixel.to_bytes(1, 'big')
        return new_content
    
    def _write_rgba5551_texture(self, new_content:bytearray, texture_count:int):
        '''
        Pass
        '''
        print(len(self._object_model_dict[CONSTANT.texture_list][texture_count][CONSTANT.texture_pixels]))
        for curr_pixel in self._object_model_dict[CONSTANT.texture_list][texture_count][CONSTANT.texture_pixels]:
            new_content += curr_pixel.to_bytes(2, 'big')
        return new_content
    
    def _write_rgba8888_texture(self, new_content:bytearray, texture_count:int):
        '''
        Pass
        '''
        for curr_pixel in self._object_model_dict[CONSTANT.texture_list][texture_count][CONSTANT.texture_pixels]:
            new_content += curr_pixel.to_bytes(4, 'big')
        return new_content
    
    def _write_ia8_texture(self, new_content:bytearray, texture_count:int):
        '''
        Pass
        '''
        for curr_pixel in self._object_model_dict[CONSTANT.texture_list][texture_count][CONSTANT.texture_pixels]:
            new_content += curr_pixel.to_bytes(1, 'big')
        return new_content

    def _write_texture_extra_bytes(self, new_content:bytearray, texture_count:int):
        '''
        Pass
        '''
        extra_byte_list:list = self._object_model_dict[CONSTANT.texture_list][texture_count][CONSTANT.texture_extra_bytes]
        for curr_byte in extra_byte_list:
            new_content += curr_byte.to_bytes(1, 'big')
        return new_content

    def _write_textures(self, new_content:bytearray):
        '''
        Pass
        '''
        for curr_count in self._object_model_dict[CONSTANT.texture_list]:
            texture_type:int = self._object_model_dict[CONSTANT.texture_list][curr_count][CONSTANT.texture_type]
            if(texture_type == self._CI4_VALUE):
                new_content = self._write_ci4_texture(new_content, texture_count=curr_count)
            elif(texture_type == self._CI8_VALUE):
                new_content = self._write_ci8_texture(new_content, texture_count=curr_count)
            elif(texture_type == self._RGBA5551_VALUE):
                new_content = self._write_rgba5551_texture(new_content, texture_count=curr_count)
            elif(texture_type == self._RGBA8888_VALUE):
                new_content = self._write_rgba8888_texture(new_content, texture_count=curr_count)
            elif(texture_type == self._IA8_VALUE):
                new_content = self._write_ia8_texture(new_content, texture_count=curr_count)
            else:
                raise Exception(f"Texture type not found: '{texture_type}'")
            new_content = self._write_texture_extra_bytes(new_content, texture_count=curr_count)
        return new_content

    def _write_texture(self, new_content:bytearray):
        '''
        Pass
        '''
        start_index:int = self._object_model_dict[CONSTANT.texture_setup_offset]
        if(start_index == 0x0):
            return new_content
        # TODO: Update Header Offset & Texture Offsets
        texture_bytes_to_load:int = self._object_model_dict[CONSTANT.texture_bytes_to_load]
        texture_count:int = len(self._object_model_dict[CONSTANT.texture_list])
        new_content += \
            texture_bytes_to_load.to_bytes(4, 'big') + \
            texture_count.to_bytes(2, 'big') + \
                (0x0000).to_bytes(2, 'big')
        new_content = self._write_texture_list(new_content)
        new_content = self._write_textures(new_content)
        return new_content

    ### DISPLAY LIST

    def _write_display_list(self, new_content:bytearray):
        '''
        Pass
        '''
        for curr_count in self._object_model_dict[CONSTANT.display_list]:
            display_list_command:int = self._object_model_dict[CONSTANT.display_list][curr_count]
            new_content += display_list_command.to_bytes(8, 'big')
        return new_content

    def _write_display_list_section(self, new_content:bytearray):
        '''
        Pass
        '''
        start_index:int = self._object_model_dict[CONSTANT.display_list_setup_offset]
        if(start_index == 0x0):
            return new_content
        # TODO: Update Header Offset & Texture Offsets
        display_list_command_count:int = len(self._object_model_dict[CONSTANT.display_list])
        display_list_header_unk_4:int = self._object_model_dict[CONSTANT.display_list_header_unk_4]
        display_list_header_unk_5:int = self._object_model_dict[CONSTANT.display_list_header_unk_5]
        display_list_header_unk_6:int = self._object_model_dict[CONSTANT.display_list_header_unk_6]
        display_list_header_unk_7:int = self._object_model_dict[CONSTANT.display_list_header_unk_7]
        new_content += \
            display_list_command_count.to_bytes(4, 'big') + \
            display_list_header_unk_4.to_bytes(1, 'big') + \
            display_list_header_unk_5.to_bytes(1, 'big') + \
            display_list_header_unk_6.to_bytes(1, 'big') + \
            display_list_header_unk_7.to_bytes(1, 'big')
        new_content = self._write_display_list(new_content)
        return new_content

    ### VERTEX LIST

    def _write_vertex_section_header(self, new_content:bytearray):
        '''
        Pass
        '''
        vertex_min_x_coord:int = self._object_model_dict[CONSTANT.vertex_min_x_coord]
        vertex_min_y_coord:int = self._object_model_dict[CONSTANT.vertex_min_y_coord]
        vertex_min_z_coord:int = self._object_model_dict[CONSTANT.vertex_min_z_coord]
        vertex_max_x_coord:int = self._object_model_dict[CONSTANT.vertex_max_x_coord]
        vertex_max_y_coord:int = self._object_model_dict[CONSTANT.vertex_max_y_coord]
        vertex_max_z_coord:int = self._object_model_dict[CONSTANT.vertex_max_z_coord]
        vertex_center_x_coord:int = self._object_model_dict[CONSTANT.vertex_center_x_coord]
        vertex_center_y_coord:int = self._object_model_dict[CONSTANT.vertex_center_y_coord]
        vertex_center_z_coord:int = self._object_model_dict[CONSTANT.vertex_center_z_coord]
        vertex_local_norm:int = self._object_model_dict[CONSTANT.vertex_local_norm]
        vertex_count:int = len(self._object_model_dict[CONSTANT.vertex_list])
        vertex_global_norm:int = self._object_model_dict[CONSTANT.vertex_global_norm]
        new_content += \
            vertex_min_x_coord.to_bytes(2, 'big') + \
            vertex_min_y_coord.to_bytes(2, 'big') + \
            vertex_min_z_coord.to_bytes(2, 'big') + \
            vertex_max_x_coord.to_bytes(2, 'big') + \
            vertex_max_y_coord.to_bytes(2, 'big') + \
            vertex_max_z_coord.to_bytes(2, 'big') + \
            vertex_center_x_coord.to_bytes(2, 'big') + \
            vertex_center_y_coord.to_bytes(2, 'big') + \
            vertex_center_z_coord.to_bytes(2, 'big') + \
            vertex_local_norm.to_bytes(2, 'big') + \
            vertex_count.to_bytes(2, 'big') + \
            vertex_global_norm.to_bytes(2, 'big')
        return new_content

    def _write_vertex_list(self, new_content:bytearray):
        '''
        Pass
        '''
        for curr_count in self._object_model_dict[CONSTANT.vertex_list]:
            vertex_info:dict = self._object_model_dict[CONSTANT.vertex_list][curr_count]
            vertex_x_position:int = vertex_info[CONSTANT.vertex_x_position]
            vertex_y_position:int = vertex_info[CONSTANT.vertex_y_position]
            vertex_z_position:int = vertex_info[CONSTANT.vertex_z_position]
            vertex_u_coordinate:int = vertex_info[CONSTANT.vertex_u_coordinate]
            vertex_v_coordinate:int = vertex_info[CONSTANT.vertex_v_coordinate]
            vertex_red_value:int = vertex_info[CONSTANT.vertex_red_value]
            vertex_green_value:int = vertex_info[CONSTANT.vertex_green_value]
            vertex_blue_value:int = vertex_info[CONSTANT.vertex_blue_value]
            vertex_alpha_value:int = vertex_info[CONSTANT.vertex_alpha_value]
            new_content += \
                vertex_x_position.to_bytes(2, 'big') + \
                vertex_y_position.to_bytes(2, 'big') + \
                vertex_z_position.to_bytes(2, 'big') + \
                (0x0000).to_bytes(2, 'big') + \
                vertex_u_coordinate.to_bytes(2, 'big') + \
                vertex_v_coordinate.to_bytes(2, 'big') + \
                vertex_red_value.to_bytes(1, 'big') + \
                vertex_green_value.to_bytes(1, 'big') + \
                vertex_blue_value.to_bytes(1, 'big') + \
                vertex_alpha_value.to_bytes(1, 'big')
        return new_content

    def _write_vertex_section(self, new_content:bytearray):
        '''
        Pass
        '''
        start_index:int = self._object_model_dict[CONSTANT.vertex_setup_offset]
        if(start_index == 0x0):
            return new_content
        # TODO: Update Header Offset
        new_content = self._write_vertex_section_header(new_content)
        new_content = self._write_vertex_list(new_content)
        return new_content

    ### ANIMATION LIST

    def _write_animation_list(self, new_content:bytearray):
        '''
        Pass
        '''
        for curr_count in self._object_model_dict[CONSTANT.animation_list]:
            curr_animation_info:dict = self._object_model_dict[CONSTANT.animation_list][curr_count]
            bone_id:int = curr_animation_info[CONSTANT.animation_bone_id]
            animation_parent_bone_id:int = curr_animation_info[CONSTANT.animation_parent_bone_id]
            new_content += \
                self._convert_float_to_hex_bytes(curr_animation_info[CONSTANT.animation_unk_0]) + \
                self._convert_float_to_hex_bytes(curr_animation_info[CONSTANT.animation_unk_4]) + \
                self._convert_float_to_hex_bytes(curr_animation_info[CONSTANT.animation_unk_8]) + \
                bone_id.to_bytes(2, 'big') + \
                animation_parent_bone_id.to_bytes(2, 'big')
        return new_content

    def _write_animation_section(self, new_content:bytearray):
        '''
        Pass
        '''
        start_index:int = self._object_model_dict[CONSTANT.animation_setup_offset]
        if(start_index == 0x0):
            return new_content
        # TODO: Update Header Offset
        animation_unk_header:float = self._object_model_dict[CONSTANT.animation_unk_header]
        animation_count:int = len(self._object_model_dict[CONSTANT.animation_list])
        new_content += \
            self._convert_float_to_hex_bytes(animation_unk_header) + \
            animation_count.to_bytes(2, 'big') + \
            (0x0000).to_bytes(2, 'big')
        new_content = self._write_animation_list(new_content)
        return new_content

    ### EFFECTS LIST

    def _write_effects_list(self, new_content:bytearray, effects_info:dict):
        '''
        Pass
        '''
        effects_section_unk_header:int = effects_info[CONSTANT.effects_section_unk_header]
        new_content += effects_section_unk_header.to_bytes(2, 'big')
        effects_vertex_list:list = effects_info[CONSTANT.effects_vertex_list]
        new_content += len(effects_vertex_list).to_bytes(2, 'big')
        for effects_vertex in effects_vertex_list:
            new_content += effects_vertex.to_bytes(2, 'big')
        return new_content
        
    def _write_effects_section(self, new_content:bytearray):
        '''
        Pass
        '''
        start_index:int = self._object_model_dict[CONSTANT.effect_setup_offset]
        if(start_index == 0x0):
            return new_content
        # TODO: Update Header Offset
        total_effects_count:int = len(self._object_model_dict[CONSTANT.effects_list])
        new_content += total_effects_count.to_bytes(2, 'big')
        for effects_count in self._object_model_dict[CONSTANT.effects_list]:
            effects_info:dict = self._object_model_dict[CONSTANT.effects_list][effects_count]
            new_content = self._write_effects_list(new_content, effects_info)
        return new_content
    
    ### HITBOX LIST

    def _write_hitbox_type_0_list(self, new_content:bytearray):
        '''
        Pass
        '''
        for curr_count in self._object_model_dict[CONSTANT.hitbox_type_0_list]:
            hitbox_info:dict = self._object_model_dict[CONSTANT.hitbox_type_0_list][curr_count]
            hitbox_type_0_unk_0:int = hitbox_info[CONSTANT.hitbox_type_0_unk_0]
            hitbox_type_0_unk_2:int = hitbox_info[CONSTANT.hitbox_type_0_unk_2]
            hitbox_type_0_unk_4:int = hitbox_info[CONSTANT.hitbox_type_0_unk_4]
            hitbox_type_0_unk_6:int = hitbox_info[CONSTANT.hitbox_type_0_unk_6]
            hitbox_type_0_unk_8:int = hitbox_info[CONSTANT.hitbox_type_0_unk_8]
            hitbox_type_0_unk_A:int = hitbox_info[CONSTANT.hitbox_type_0_unk_A]
            hitbox_type_0_unk_C:int = hitbox_info[CONSTANT.hitbox_type_0_unk_C]
            hitbox_type_0_unk_E:int = hitbox_info[CONSTANT.hitbox_type_0_unk_E]
            hitbox_type_0_unk_10:int = hitbox_info[CONSTANT.hitbox_type_0_unk_10]
            hitbox_type_0_unk_12:int = hitbox_info[CONSTANT.hitbox_type_0_unk_12]
            hitbox_type_0_unk_13:int = hitbox_info[CONSTANT.hitbox_type_0_unk_13]
            hitbox_type_0_unk_14:int = hitbox_info[CONSTANT.hitbox_type_0_unk_14]
            hitbox_type_0_unk_15:int = hitbox_info[CONSTANT.hitbox_type_0_unk_15]
            hitbox_type_0_unk_16:int = hitbox_info[CONSTANT.hitbox_type_0_unk_16]
            hitbox_type_0_unk_17:int = hitbox_info[CONSTANT.hitbox_type_0_unk_17]
            new_content += \
                hitbox_type_0_unk_0.to_bytes(2, 'big', signed=True) + \
                hitbox_type_0_unk_2.to_bytes(2, 'big', signed=True) + \
                hitbox_type_0_unk_4.to_bytes(2, 'big', signed=True) + \
                hitbox_type_0_unk_6.to_bytes(2, 'big', signed=True) + \
                hitbox_type_0_unk_8.to_bytes(2, 'big', signed=True) + \
                hitbox_type_0_unk_A.to_bytes(2, 'big', signed=True) + \
                hitbox_type_0_unk_C.to_bytes(2, 'big', signed=True) + \
                hitbox_type_0_unk_E.to_bytes(2, 'big', signed=True) + \
                hitbox_type_0_unk_10.to_bytes(2, 'big', signed=True) + \
                hitbox_type_0_unk_12.to_bytes(1, 'big') + \
                hitbox_type_0_unk_13.to_bytes(1, 'big') + \
                hitbox_type_0_unk_14.to_bytes(1, 'big') + \
                hitbox_type_0_unk_15.to_bytes(1, 'big') + \
                hitbox_type_0_unk_16.to_bytes(1, 'big', signed=True) + \
                hitbox_type_0_unk_17.to_bytes(1, 'big')
        return new_content

    def _write_hitbox_type_1_list(self, new_content:bytearray):
        '''
        Pass
        '''
        for curr_count in self._object_model_dict[CONSTANT.hitbox_type_1_list]:
            hitbox_info:dict = self._object_model_dict[CONSTANT.hitbox_type_1_list][curr_count]
            hitbox_type_1_unk_0:int = hitbox_info[CONSTANT.hitbox_type_1_unk_0]
            hitbox_type_1_unk_2:int = hitbox_info[CONSTANT.hitbox_type_1_unk_2]
            hitbox_type_1_unk_4:int = hitbox_info[CONSTANT.hitbox_type_1_unk_4]
            hitbox_type_1_unk_6:int = hitbox_info[CONSTANT.hitbox_type_1_unk_6]
            hitbox_type_1_unk_8:int = hitbox_info[CONSTANT.hitbox_type_1_unk_8]
            hitbox_type_1_unk_A:int = hitbox_info[CONSTANT.hitbox_type_1_unk_A]
            hitbox_type_1_unk_B:int = hitbox_info[CONSTANT.hitbox_type_1_unk_B]
            hitbox_type_1_unk_C:int = hitbox_info[CONSTANT.hitbox_type_1_unk_C]
            hitbox_type_1_unk_D:int = hitbox_info[CONSTANT.hitbox_type_1_unk_D]
            hitbox_type_1_unk_E:int = hitbox_info[CONSTANT.hitbox_type_1_unk_E]
            hitbox_type_1_unk_F:int = hitbox_info[CONSTANT.hitbox_type_1_unk_F]
            new_content += \
                hitbox_type_1_unk_0.to_bytes(2, 'big', signed=True) + \
                hitbox_type_1_unk_2.to_bytes(2, 'big', signed=True) + \
                hitbox_type_1_unk_4.to_bytes(2, 'big', signed=True) + \
                hitbox_type_1_unk_6.to_bytes(2, 'big', signed=True) + \
                hitbox_type_1_unk_8.to_bytes(2, 'big', signed=True) + \
                hitbox_type_1_unk_A.to_bytes(1, 'big') + \
                hitbox_type_1_unk_B.to_bytes(1, 'big') + \
                hitbox_type_1_unk_C.to_bytes(1, 'big') + \
                hitbox_type_1_unk_D.to_bytes(1, 'big') + \
                hitbox_type_1_unk_E.to_bytes(1, 'big', signed=True) + \
                hitbox_type_1_unk_F.to_bytes(1, 'big')
        return new_content

    def _write_hitbox_type_2_list(self, new_content:bytearray):
        '''
        Pass
        '''
        for curr_count in self._object_model_dict[CONSTANT.hitbox_type_2_list]:
            hitbox_info:dict = self._object_model_dict[CONSTANT.hitbox_type_2_list][curr_count]
            hitbox_type_2_unk_0:int = hitbox_info[CONSTANT.hitbox_type_2_unk_0]
            hitbox_type_2_unk_2:int = hitbox_info[CONSTANT.hitbox_type_2_unk_2]
            hitbox_type_2_unk_4:int = hitbox_info[CONSTANT.hitbox_type_2_unk_4]
            hitbox_type_2_unk_6:int = hitbox_info[CONSTANT.hitbox_type_2_unk_6]
            hitbox_type_2_unk_8:int = hitbox_info[CONSTANT.hitbox_type_2_unk_8]
            hitbox_type_2_unk_9:int = hitbox_info[CONSTANT.hitbox_type_2_unk_9]
            hitbox_type_2_unk_A:int = hitbox_info[CONSTANT.hitbox_type_2_unk_A]
            hitbox_type_2_unk_B:int = hitbox_info[CONSTANT.hitbox_type_2_unk_B]
            new_content += \
                hitbox_type_2_unk_0.to_bytes(2, 'big', signed=True) + \
                hitbox_type_2_unk_2.to_bytes(2, 'big', signed=True) + \
                hitbox_type_2_unk_4.to_bytes(2, 'big', signed=True) + \
                hitbox_type_2_unk_6.to_bytes(2, 'big', signed=True) + \
                hitbox_type_2_unk_8.to_bytes(1, 'big') + \
                hitbox_type_2_unk_9.to_bytes(1, 'big', signed=True) + \
                hitbox_type_2_unk_A.to_bytes(1, 'big') + \
                hitbox_type_2_unk_B.to_bytes(1, 'big')
        return new_content

    def _write_hitbox_section(self, new_content:bytearray):
        '''
        Pass
        '''
        start_index:int = self._object_model_dict[CONSTANT.hitbox_setup_offset]
        if(start_index == 0x0):
            return new_content
        # TODO: Update Header Offset
        hitbox_type_0_count:int = len(self._object_model_dict[CONSTANT.hitbox_type_0_list])
        hitbox_type_1_count:int = len(self._object_model_dict[CONSTANT.hitbox_type_1_list])
        hitbox_type_2_count:int = len(self._object_model_dict[CONSTANT.hitbox_type_2_list])
        hitbox_header_unk:int = self._object_model_dict[CONSTANT.hitbox_header_unk]
        new_content += \
            hitbox_type_0_count.to_bytes(2, 'big') + \
            hitbox_type_1_count.to_bytes(2, 'big') + \
            hitbox_type_2_count.to_bytes(2, 'big') + \
            hitbox_header_unk.to_bytes(2, 'big')
        new_content = self._write_hitbox_type_0_list(new_content)
        new_content = self._write_hitbox_type_1_list(new_content)
        new_content = self._write_hitbox_type_2_list(new_content)
        return new_content

    ### ANIMATION TEXTURE LIST

    def _write_animated_texture_list(self, new_content:bytearray):
        '''
        Pass
        '''
        start_index:int = self._object_model_dict[CONSTANT.animated_textures_offset]
        if(start_index == 0x0):
            return new_content
        # TODO: Update Header Offset
        animation_texture_frame_size:int = self._object_model_dict[CONSTANT.animation_texture_frame_size]
        animation_texture_frame_count:int = self._object_model_dict[CONSTANT.animation_texture_frame_count]
        animation_texture_frame_rate:float = self._object_model_dict[CONSTANT.animation_texture_frame_rate]
        # padding
        new_content += \
            animation_texture_frame_size.to_bytes(2, 'big') + \
            animation_texture_frame_count.to_bytes(2, 'big') + \
            self._convert_float_to_hex_bytes(animation_texture_frame_rate) + \
            (0).to_bytes(0x18, 'big')
        return new_content

    ### COLLISION LIST

    def _write_collision_geo_list(self, new_content:bytearray):
        '''
        Pass
        '''
        for curr_count in self._object_model_dict[CONSTANT.collision_geo_list]:
            curr_geo_info:dict = self._object_model_dict[CONSTANT.collision_geo_list][curr_count]
            collision_start_tri_index:int = curr_geo_info[CONSTANT.collision_start_tri_index]
            collision_geo_tri_count:int = curr_geo_info[CONSTANT.collision_geo_tri_count]
            new_content += \
                collision_start_tri_index.to_bytes(2, 'big') + \
                collision_geo_tri_count.to_bytes(2, 'big')
        return new_content

    def _write_collision_collision_tri_list(self, new_content:bytearray):
        '''
        Pass
        '''
        for curr_count in self._object_model_dict[CONSTANT.collision_tri_list]:
            curr_tri_info:dict = self._object_model_dict[CONSTANT.collision_tri_list][curr_count]
            collision_vertex_1:int = curr_tri_info[CONSTANT.collision_vertex_1]
            collision_vertex_2:int = curr_tri_info[CONSTANT.collision_vertex_2]
            collision_vertex_3:int = curr_tri_info[CONSTANT.collision_vertex_3]
            collision_tri_unk:int = curr_tri_info[CONSTANT.collision_tri_unk]
            collision_flags:int = curr_tri_info[CONSTANT.collision_flags]
            new_content += \
                collision_vertex_1.to_bytes(2, 'big') + \
                collision_vertex_2.to_bytes(2, 'big') + \
                collision_vertex_3.to_bytes(2, 'big') + \
                collision_tri_unk.to_bytes(2, 'big') + \
                collision_flags.to_bytes(4, 'big')
        return new_content

    def _write_collision_list(self, new_content:bytearray):
        '''
        Pass
        '''
        start_index:int = self._object_model_dict[CONSTANT.collision_setup_offset]
        if(start_index == 0x0):
            return new_content
        # TODO: Update Header Offset
        collision_min_x:int = self._object_model_dict[CONSTANT.collision_min_x]
        collision_min_y:int = self._object_model_dict[CONSTANT.collision_min_y]
        collision_min_z:int = self._object_model_dict[CONSTANT.collision_min_z]
        collision_max_x:int = self._object_model_dict[CONSTANT.collision_max_x]
        collision_max_y:int = self._object_model_dict[CONSTANT.collision_max_y]
        collision_max_z:int = self._object_model_dict[CONSTANT.collision_max_z]
        collision_y_stride:int = self._object_model_dict[CONSTANT.collision_y_stride]
        collision_z_stride:int = self._object_model_dict[CONSTANT.collision_z_stride]
        collision_geo_count:int = len(self._object_model_dict[CONSTANT.collision_geo_list])
        collision_scale:int = self._object_model_dict[CONSTANT.collision_scale]
        collision_tri_count:int = len(self._object_model_dict[CONSTANT.collision_tri_list])
        new_content += \
            collision_min_x.to_bytes(2, 'big') + \
            collision_min_y.to_bytes(2, 'big') + \
            collision_min_z.to_bytes(2, 'big') + \
            collision_max_x.to_bytes(2, 'big') + \
            collision_max_y.to_bytes(2, 'big') + \
            collision_max_z.to_bytes(2, 'big') + \
            collision_y_stride.to_bytes(2, 'big') + \
            collision_z_stride.to_bytes(2, 'big') + \
            collision_geo_count.to_bytes(2, 'big') + \
            collision_scale.to_bytes(2, 'big') + \
            collision_tri_count.to_bytes(2, 'big') + \
            (0x0000).to_bytes(2, 'big')
        new_content = self._write_collision_geo_list(new_content)
        new_content = self._write_collision_collision_tri_list(new_content)
        while(len(new_content) % 8 > 0):
            new_content += (0x00).to_bytes(1, 'big')
        return new_content

    ### GEOMETRY LIST

    def _write_geometry_list(self, new_content:bytearray):
        '''
        Pass
        '''
        start_index:int = self._object_model_dict[CONSTANT.geometry_layout_setup_offset]
        if(start_index == 0x0):
            return new_content
        # TODO: Update Header Offset
        for curr_count in self._object_model_dict[CONSTANT.geometry_list]:
            geometry_command:int = self._object_model_dict[CONSTANT.geometry_list][curr_count]
            new_content += geometry_command.to_bytes(4, 'big')
        return new_content

    ##########################
    ##### MAIN FUNCTIONS #####
    ##########################
        
    def read_object_3d_model_file(self):
        '''
        Pass
        '''
        super()._read_file()
        self._parse_3d_model_file_header()
        self._parse_texture()
        self._parse_display_list_section()
        self._parse_vertex_section()
        self._parse_animation_section()
        self._parse_effects_section()
        self._parse_hitbox_section()
        self._parse_animated_texture_list()
        self._parse_collision_list()
        self._parse_geometry_list()
    
    def save_object_3d_model_file(self, file_path:str|None=None):
        '''
        Pass
        '''
        new_content:bytearray = (self._3d_model_header).to_bytes(4, 'big')
        new_content = self._write_file_header(new_content)
        new_content = self._write_texture(new_content)
        new_content = self._write_display_list_section(new_content)
        new_content = self._write_vertex_section(new_content)
        new_content = self._write_animation_section(new_content)
        new_content = self._write_collision_list(new_content)
        new_content = self._write_effects_section(new_content)
        new_content = self._write_hitbox_section(new_content)
        new_content = self._write_animated_texture_list(new_content)
        new_content = self._write_geometry_list(new_content)
        self._file_content = new_content
        super()._save_changes(file_path)
        del new_content

################
##### MAIN #####
################
    
if __name__ == '__main__':
    old_file_path:str = "C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/test2/"
    # new_file_path:str = "C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/test/"
    new_file_path:str = "C:/Users/Cyrus/Documents/VS_Code/BKDecompressor/BKDecompressor/decompressor/custom_files/"
    file_list:list = [
        # "19D530", # Banjo Kazooie High Poly Model
        # "3AAA50", # Secret SNS Egg
        # "3B4E20", # Iron Gate (No Lock)
        # "1466E8", # MM Chimpy's Orange
        # "146BD8", # MM Conga Tree
        # "1484D0", # FP Blue Present (No Eyes)
        # "153698", # MM Orange Pad
        # "1B4C40", # Walrus Banjo
        "A795B8", # Furnace Fun
        ]
    import filecmp
    for file_name in file_list:
        old_file_name:str = f"{old_file_path}{file_name}.bin"
        # new_file_name:str = f"{new_file_path}{file_name}-TEST.bin"
        new_file_name:str = f"{new_file_path}14E8-Decompressed.bin"
        object_model_obj = OBJECT_3D_MODEL_CLASS(old_file_name)
        object_model_obj.read_object_3d_model_file()
        texture_replacement_dict:dict = {
            17: 22,
            18: 22,
            20: 22,
            23: 22,
            44: 49,
            45: 49,
            47: 49,
            50: 49,
        }
        object_model_obj._replace_textures(texture_replacement_dict)
        dlist_command_replacement_dict:dict = {
            0xFD100000020097A0: 0xFD1000000200C040, # bk -> eye
            0xFD10000002009FC0: 0xFD1000000200C040, # note -> eye
            0xFD1000000200B000: 0xFD1000000200C040, # grunty -> eye
            0xFD1000000200C860: 0xFD1000000200C040, # timer -> eye
            0xFD10000002015760: 0xFD10000002019360, # blue -> orange
            0xFD10000002016360: 0xFD10000002019360, # green -> orange
            0xFD10000002017B60: 0xFD10000002019360, # purple -> orange
            0xFD10000002019F60: 0xFD10000002019360, # magenta -> orange
        }
        object_model_obj._replace_display_list_commands(dlist_command_replacement_dict)
        object_model_obj.save_object_3d_model_file(new_file_name)
        # files_are_copies:bool = filecmp.cmp(old_file_name, new_file_name)
        # if(files_are_copies):
        #     print("Copies")
        # else:
        #     print(f"Not Copies: {file_name}")
        #     exit(0)
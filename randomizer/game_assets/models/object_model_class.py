'''
Purpose:
*
'''

###################
##### IMPORTS #####
###################

from randomizer.generic_bin_file_class import Generic_Bin_File_Class
from randomizer.contants.int_enums.object_model_constants import OBJECT_MODEL_CONSTANTS as CONSTANT

##############################
##### OBJECT MODEL CLASS #####
##############################

class OBJECT_MODEL_CLASS(Generic_Bin_File_Class):
    '''
    Class for reading and modifying object model files.
    '''
    def __init__(self, file_path:str):
        '''
        Constructor
        '''
        self._object_model_dict:dict = {}

    #############################
    ##### UTILITY FUNCTIONS #####
    #############################

    ###################
    ##### PARSING #####
    ###################

    def _parse_file_header(self):
        '''
        Pass
        '''
        self._object_model_dict[CONSTANT.geometry_layout_setup_offset] = self._read_bytes_as_int(0x04, byte_count=4)
        self._object_model_dict[CONSTANT.texture_setup_offset] = self._read_bytes_as_int(0x08, byte_count=2)
        self._object_model_dict[CONSTANT.object_model_geo_type] = self._read_bytes_as_int(0x0A, byte_count=2)
        self._object_model_dict[CONSTANT.display_list_setup_offset] = self._read_bytes_as_int(0x0C, byte_count=4)
        self._object_model_dict[CONSTANT.vertex_setup_offset] = self._read_bytes_as_int(0x10, byte_count=4)
        self._object_model_dict[CONSTANT.animation_setup_offset] = self._read_bytes_as_int(0x18, byte_count=4)
        self._object_model_dict[CONSTANT.collision_setup_offset] = self._read_bytes_as_int(0x1C, byte_count=4)
        self._object_model_dict[CONSTANT.unknown1_setup_offset] = self._read_bytes_as_int(0x20, byte_count=4)
        self._object_model_dict[CONSTANT.effect_setup_offset] = self._read_bytes_as_int(0x24, byte_count=4)
        self._object_model_dict[CONSTANT.unknown2_setup_offset] = self._read_bytes_as_int(0x2C, byte_count=4)

    ### TEXTURE LIST

    def _parse_texture_list(self, start_index:int, texture_count:int):
        '''
        Pass
        '''
        self._object_model_dict[CONSTANT.texture_list] = {}
        for curr_count in range(texture_count):
            curr_index:int = start_index + 0x10 * curr_count
            self._object_model_dict[CONSTANT.textures][CONSTANT.texture_list][curr_count] = {
                CONSTANT.texture_offset: self._read_bytes_as_int(curr_index, byte_count=4),
                CONSTANT.texture_type: self._read_bytes_as_int(curr_index + 0x5, byte_count=1),
                CONSTANT.texture_x_dimension: self._read_bytes_as_int(curr_index + 0x8, byte_count=1),
                CONSTANT.texture_y_dimension: self._read_bytes_as_int(curr_index + 0x9, byte_count=1),
            }

    def _parse_texture(self):
        '''
        Pass
        '''
        start_index:int = self._object_model_dict[CONSTANT.texture_setup_offset]
        self._object_model_dict[CONSTANT.texture_bytes_to_load] = self._read_bytes_as_int(self._texture_setup_offset, byte_count=4)
        texture_count:int = self._read_bytes_as_int(self._texture_setup_offset + 0x04, byte_count=2)
        self._parse_texture_list(start_index + 0x08, texture_count)

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
        display_list_command_count:int = self._read_bytes_as_int(start_index, byte_count=4)
        self._parse_display_list(start_index + 0x08, display_list_command_count)

    ### VERTEX LIST

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
        vertex_count:int = self._read_bytes_as_int(start_index + 0x14, byte_count=2)
        self._parse_vertex_list(start_index + 0x18, vertex_count)

    ### ANIMATION LIST

    def _parse_animation_list(self):
        '''
        Pass
        '''
        start_index:int = self._object_model_dict[CONSTANT.animation_setup_offset]

    ### EFFECTS LIST

    def _parse_effects_list(self):
        '''
        Pass
        '''
        start_index:int = self._object_model_dict[CONSTANT.effect_setup_offset]

    ### ANIMATION TEXTURE LIST

    def _parse_animated_texture_list(self):
        '''
        Pass
        '''
        start_index:int = None

    ### COLLISION LIST

    def _parse_collision_geo_list(self, start_index:int, geo_count:int):
        '''
        Pass
        '''
        self._object_model_dict[CONSTANT.collision_geo_list] = {}
        for curr_count in range(geo_count):
            curr_index: int = start_index + 0x04 * curr_count
            self._object_model_dict[CONSTANT.collision_geo_list][curr_count] = {
                CONSTANT.collision_start_tri_index: self._read_bytes_as_int(curr_index, byte_count=2),
                CONSTANT.collision_geo_tri_count: self._read_bytes_as_int(curr_index + 0x2, byte_count=2),
            }
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
        return curr_index

    def _parse_collision_list(self):
        '''
        Pass
        '''
        start_index:int = self._object_model_dict[CONSTANT.collision_setup_offset]
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

################
##### MAIN #####
################
    
if __name__ == '__main__':
    pass
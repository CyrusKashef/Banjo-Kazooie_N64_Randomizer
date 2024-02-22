'''
Purpose:
*
'''

###################
##### IMPORTS #####
###################

from enum import IntEnum, unique, auto

##########################
##### ASSET ID ENUMS #####
##########################

@unique
class OBJECT_MODEL_CONSTANTS(IntEnum):
    # FILE HEADER
    geometry_layout_setup_offset = auto()
    texture_setup_offset = auto()
    object_model_geo_type = auto()
    display_list_setup_offset = auto()
    vertex_setup_offset = auto()
    hitbox_setup_offset = auto()
    animation_setup_offset = auto()
    collision_setup_offset = auto()
    unknown_20_setup_offset = auto()
    effect_setup_offset = auto()
    unknown_28_setup_offset = auto()
    animated_textures_offset = auto()
    unknown_count = auto()
    vert_count = auto()
    # GEOMETRY LIST
    # TEXTURE LIST
    textures = auto()
    texture_list = auto()
    texture_bytes_to_load = auto()
    texture_offset = auto()
    texture_type = auto()
    texture_x_dimension = auto()
    texture_y_dimension = auto()
    # DISPLAY LIST
    display_list = auto()
    # VERTEX
    vertex_x_position = auto()
    vertex_y_position = auto()
    vertex_z_position = auto()
    vertex_u_coordinate = auto()
    vertex_v_coordinate = auto()
    vertex_red_value = auto()
    vertex_green_value = auto()
    vertex_blue_value = auto()
    vertex_alpha_value = auto()
    # VERTEX LIST
    vertex_index = auto()
    vertex_list = auto()
    vertex_min_x_coord = auto()
    vertex_min_y_coord = auto()
    vertex_min_z_coord = auto()
    vertex_max_x_coord = auto()
    vertex_max_y_coord = auto()
    vertex_max_z_coord = auto()
    vertex_center_x_coord = auto()
    vertex_center_y_coord = auto()
    vertex_center_z_coord = auto()
    vertex_local_norm = auto()
    vertex_global_norm = auto()
    # ANIMATION LIST
    # EFFECTS LIST
    # ANIMATION TEXTURE LIST
    # COLLISION LIST
    collision_min_x = auto()
    collision_min_y = auto()
    collision_min_z = auto()
    collision_max_x = auto()
    collision_max_y = auto()
    collision_max_z = auto()
    collision_y_stride = auto()
    collision_z_stride = auto()
    collision_geo_count = auto()
    collision_scale = auto()
    collision_tri_count = auto()
    collision_geo_list = auto()
    collision_tri_list = auto()
    collision_start_tri_index = auto()
    collision_geo_tri_count = auto()
    collision_vertex_1 = auto()
    collision_vertex_2 = auto()
    collision_vertex_3 = auto()
    collision_tri_unk = auto()
    collision_flags = auto()
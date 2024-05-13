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
    # FILE TYPES
    object_3d_model = auto()
    object_2d_model = auto()
    ####################
    ##### 3D MODEL #####
    ####################
    # 3D FILE HEADER
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
    unknown_34_header = auto()
    # GEOMETRY LIST
    geometry_list = auto()
    # TEXTURE LIST
    textures = auto()
    texture_list = auto()
    texture_bytes_to_load = auto()
    texture_offset = auto()
    texture_type = auto()
    texture_x_dimension = auto()
    texture_y_dimension = auto()
    texture_color_index = auto()
    texture_pixels = auto()
    # DISPLAY LIST
    display_list = auto()
    display_list_header_unk_0 = auto()
    display_list_header_unk_1 = auto()
    display_list_header_unk_2 = auto()
    display_list_header_unk_4 = auto()
    display_list_header_unk_5 = auto()
    display_list_header_unk_6 = auto()
    display_list_header_unk_7 = auto()
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
    animation_unk_header = auto()
    animation_list = auto()
    animation_unk_0 = auto()
    animation_unk_4 = auto()
    animation_unk_8 = auto()
    animation_bone_id = auto()
    animation_parent_bone_id = auto()
    # EFFECTS LIST
    effects_count = auto()
    effects_list = auto()
    effects_section_unk_header = auto()
    effects_vertex_list = auto()
    # ANIMATION TEXTURE LIST
    animation_texture_frame_size = auto()
    animation_texture_frame_count = auto()
    animation_texture_frame_rate = auto()
    # HITBOX LIST
    hitbox_type_0_list = auto()
    hitbox_type_1_list = auto()
    hitbox_type_2_list = auto()
    hitbox_header_unk = auto()
    hitbox_type_0_unk_0 = auto()
    hitbox_type_0_unk_2 = auto()
    hitbox_type_0_unk_4 = auto()
    hitbox_type_0_unk_6 = auto()
    hitbox_type_0_unk_8 = auto()
    hitbox_type_0_unk_A = auto()
    hitbox_type_0_unk_C = auto()
    hitbox_type_0_unk_E = auto()
    hitbox_type_0_unk_10 = auto()
    hitbox_type_0_unk_12 = auto()
    hitbox_type_0_unk_13 = auto()
    hitbox_type_0_unk_14 = auto()
    hitbox_type_0_unk_15 = auto()
    hitbox_type_0_unk_16 = auto()
    hitbox_type_0_unk_17 = auto()
    hitbox_type_1_unk_0 = auto()
    hitbox_type_1_unk_2 = auto()
    hitbox_type_1_unk_4 = auto()
    hitbox_type_1_unk_6 = auto()
    hitbox_type_1_unk_8 = auto()
    hitbox_type_1_unk_A = auto()
    hitbox_type_1_unk_B = auto()
    hitbox_type_1_unk_C = auto()
    hitbox_type_1_unk_D = auto()
    hitbox_type_1_unk_E = auto()
    hitbox_type_1_unk_F = auto()
    hitbox_type_2_unk_0 = auto()
    hitbox_type_2_unk_2 = auto()
    hitbox_type_2_unk_4 = auto()
    hitbox_type_2_unk_6 = auto()
    hitbox_type_2_unk_8 = auto()
    hitbox_type_2_unk_9 = auto()
    hitbox_type_2_unk_A = auto()
    hitbox_type_2_unk_B = auto()
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
    ####################
    ##### 2D MODEL #####
    ####################
    # 2D FILE HEADER
    frame_count = auto()
    file_type = auto()
    header_unk_4 = auto()
    header_unk_6 = auto()
    header_unk_8 = auto()
    header_unk_A = auto()
    frame_offset_dict = auto()
    frame_header_info = auto()
    # FRAME HEADER
    frame_unk_0 = auto()
    frame_unk_2 = auto()
    frame_width = auto()
    frame_height = auto()
    frame_chunk_count = auto()
    frame_unk_a = auto()
    frame_unk_c = auto()
    frame_unk_e = auto()
    frame_unk_10 = auto()
    frame_unk_12 = auto()
    # SPRITE
    sprite_x_position = auto()
    sprite_y_position = auto()
    sprite_width = auto()
    sprite_height = auto()
    sprite_color_index = auto()
    sprite_pixels = auto()
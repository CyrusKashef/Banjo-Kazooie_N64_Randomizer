'''
Purpose:
* Modifies data written for the game engine
'''

###################
##### IMPORTS #####
###################

from randomizer.generic_bin_file_class import Generic_Bin_File_Class

from randomizer.constants.str_values.string_constants import STRING_CONSTANTS as STR_CONST

from randomizer.constants.int_values.marker_enums import \
    PARAMETERS_ENUM, COLLISION_ENUMS, \
    MARKER_ID_ENUMS, BK_EFFECT_ENUMS, \
    ENTITY_NEXT_STATE_ENUM, COLLISION_SFX_ENUM

SPRITE_STR:str = "Sprite"
SFX_LIST_STR:str = "SFX List"
SFX_ID_STR:str = "SFX Id"
UNKNOWN_2_STR:str = "Unknown 2"
UNKNOWN_3_STR:str = "Unknown 3"
UNKNOWN_4_STR:str = "Unknown 4"

ZOOMBOX_SPRITE_SFX_START_INDEX:int = 0x9130
ZOOMBOX_SPRITE_SFX_END_INDEX:int = 0xA394
ZOOMBOX_SPRITE_SFX_INTERVAL:int =0x2C

#############################
##### C LIBRARIES CLASS #####
#############################

class GAME_ENGINE_DATA_CLASS(Generic_Bin_File_Class):
    '''
    Class for modifying code written for the game engine
    '''
    def __init__(self, file_name:str):
        '''
        Constructor
        '''
        file_path:str = STR_CONST.extracted_files_dir + file_name + STR_CONST.decompressed_bin_extension
        super().__init__(file_path)
    
    ######################
    ##### PAUSE MENU #####
    ######################
        
    def adjust_menu_for_witchs_lair(self):
        '''
        Changes the positioning, ordering, and sprite of
        the pause menu when 'Exit To Witch's Lair' is added.
        '''
        # Positioning
        self._write_bytes_from_int(0x8F5C, 0x002D, byte_count=2) # "RETURN TO GAME"
        self._write_bytes_from_int(0x8F6C, 0x004C, byte_count=2) # "EXIT TO WITCH'S LAIR"
        self._write_bytes_from_int(0x8F7C, 0x006B, byte_count=2) # "VIEW TOTALS"
        self._write_bytes_from_int(0x8F8C, 0x008A, byte_count=2) # "SAVE AND QUIT"
        # Ordering
        self._write_bytes_from_int(0x8F60, 0x3DCCCCCD, byte_count=4) # "EXIT TO WITCH'S LAIR"
        self._write_bytes_from_int(0x8F70, 0x3E4CCCCD, byte_count=4) # "VIEW TOTALS"
        self._write_bytes_from_int(0x8F80, 0x3E99999A, byte_count=4) # "SAVE AND QUIT"
        # Sprite
        self._write_bytes_from_int(0x8F6E, 0x05, byte_count=1) # Give "EXIT TO WITCH'S LAIR" the Gruntilda Sprite
    
    def transform_witchs_lair_to_level_start(self):
        '''
        Changes the text of 'Exit To Witch's Lair' to
        'Warp To World Exit' to adjust for new setting.
        '''
        # Adjusting Text
        self._write_bytes_from_int(0x14FC0, 0x5741525020544F20574F524C4420455849540000, byte_count=20)

    def set_level_start_warp_pad_destinations(self, warp_dict:dict):
        '''
        Sets the level start warp pads to different maps and entries.
        Also affects 'Exit To Witch's Lair' feature unless function
        'transform_witchs_lair_to_level_start' is ran.
        '''
        # Mumbo's Mountain
        self._write_bytes_from_int(0x8FD0, warp_dict[STR_CONST.mumbos_mountain][STR_CONST.map_enum], byte_count=2)
        self._write_bytes_from_int(0x8FD2, warp_dict[STR_CONST.mumbos_mountain][STR_CONST.entry_point], byte_count=2)
        # Treasure Trove Cove
        self._write_bytes_from_int(0x8FD4, warp_dict[STR_CONST.treasure_trove_cove][STR_CONST.map_enum], byte_count=2)
        self._write_bytes_from_int(0x8FD6, warp_dict[STR_CONST.treasure_trove_cove][STR_CONST.entry_point], byte_count=2)
        # Clanker's Cavern
        self._write_bytes_from_int(0x8FD8, warp_dict[STR_CONST.clankers_cavern][STR_CONST.map_enum], byte_count=2)
        self._write_bytes_from_int(0x8FDA, warp_dict[STR_CONST.clankers_cavern][STR_CONST.entry_point], byte_count=2)
        # Bubblegloop Swamp
        self._write_bytes_from_int(0x8FDC, warp_dict[STR_CONST.bubblegloop_swamp][STR_CONST.map_enum], byte_count=2)
        self._write_bytes_from_int(0x8FDE, warp_dict[STR_CONST.bubblegloop_swamp][STR_CONST.entry_point], byte_count=2)
        # Freezeezy Peak
        self._write_bytes_from_int(0x8FE0, warp_dict[STR_CONST.freezeezy_peak][STR_CONST.map_enum], byte_count=2)
        self._write_bytes_from_int(0x8FE2, warp_dict[STR_CONST.freezeezy_peak][STR_CONST.entry_point], byte_count=2)
        # Gruntilda's Lair (Left at -1, -1 to prevent warping?)
        self._write_bytes_from_int(0x8FE4, 0xFFFF, byte_count=2)
        self._write_bytes_from_int(0x8FE6, 0xFFFF, byte_count=2)
        # Gobi's Valley
        self._write_bytes_from_int(0x8FE8, warp_dict[STR_CONST.gobis_valley][STR_CONST.map_enum], byte_count=2)
        self._write_bytes_from_int(0x8FEA, warp_dict[STR_CONST.gobis_valley][STR_CONST.entry_point], byte_count=2)
        # Click Clock Wood
        self._write_bytes_from_int(0x8FEC, warp_dict[STR_CONST.click_clock_wood][STR_CONST.map_enum], byte_count=2)
        self._write_bytes_from_int(0x8FEE, warp_dict[STR_CONST.click_clock_wood][STR_CONST.entry_point], byte_count=2)
        # Rusty Bucket Bay
        self._write_bytes_from_int(0x8FF0, warp_dict[STR_CONST.rusty_bucket_bay][STR_CONST.map_enum], byte_count=2)
        self._write_bytes_from_int(0x8FF2, warp_dict[STR_CONST.rusty_bucket_bay][STR_CONST.entry_point], byte_count=2)
        # Mad Monster Mansion
        self._write_bytes_from_int(0x8FF4, warp_dict[STR_CONST.mad_monster_mansion][STR_CONST.map_enum], byte_count=2)
        self._write_bytes_from_int(0x8FF6, warp_dict[STR_CONST.mad_monster_mansion][STR_CONST.entry_point], byte_count=2)
        # Spiral Mountain
        self._write_bytes_from_int(0x8FF8, warp_dict[STR_CONST.spiral_mountain][STR_CONST.map_enum], byte_count=2)
        self._write_bytes_from_int(0x8FFA, warp_dict[STR_CONST.spiral_mountain][STR_CONST.entry_point], byte_count=2)

    ###################
    ##### ZOOMBOX #####
    ###################
    # core2/gc/zoombox.c
    
    def get_zoombox_sprite_sfx_dict(self):
        '''
        Pass
        '''
        zoombox_dict:dict = {}
        for curr_count, curr_index in range(
                ZOOMBOX_SPRITE_SFX_START_INDEX,
                ZOOMBOX_SPRITE_SFX_END_INDEX,
                ZOOMBOX_SPRITE_SFX_INTERVAL):
            zoombox_dict[curr_count] = {
                SPRITE_STR: self._read_bytes_as_int(curr_index, byte_count=2),
                UNKNOWN_2_STR: self._read_bytes_as_int(curr_index + 0x2, byte_count=1),
                UNKNOWN_3_STR: self._read_bytes_as_int(curr_index + 0x3, byte_count=1),
                SFX_LIST_STR: [],
            }
            curr_index += 0x4
            sfx_count:int = 0
            while(sfx_count < 5):
                zoombox_dict[curr_count][SFX_LIST_STR][sfx_count] = {
                    SFX_ID_STR: self._read_bytes_as_int(curr_index, byte_count=2),
                    UNKNOWN_2_STR: self._read_bytes_as_int(curr_index + 0x2, byte_count=2),
                    UNKNOWN_4_STR: self._read_bytes_as_float(curr_index + 0x4),
                }
                curr_index += 0x8
                sfx_count += 1
        return zoombox_dict
    
    def set_zoombox_sprite_sfx_dict(self, zoombox_dict:dict):
        '''
        Pass
        '''
        for curr_count, curr_index in range(
                ZOOMBOX_SPRITE_SFX_START_INDEX,
                ZOOMBOX_SPRITE_SFX_END_INDEX,
                ZOOMBOX_SPRITE_SFX_INTERVAL):
            zoombox_item:dict = zoombox_dict[curr_count]
            self._write_bytes_from_int(curr_index, zoombox_item[SPRITE_STR], byte_count=2)
            self._write_bytes_from_int(curr_index + 0x2, zoombox_item[UNKNOWN_2_STR], byte_count=1)
            self._write_bytes_from_int(curr_index + 0x3, zoombox_item[UNKNOWN_3_STR], byte_count=1)
            curr_count += 0x4
            sfx_count:int = 0
            while(sfx_count < 5):
                sfx_item:dict = zoombox_dict[curr_count][SFX_LIST_STR]
                self._write_bytes_from_int(curr_index, sfx_item[SFX_ID_STR], byte_count=2)
                self._write_bytes_from_int(curr_index, sfx_item[UNKNOWN_2_STR], byte_count=2)
                self._write_bytes_from_float(curr_index, sfx_item[UNKNOWN_4_STR])
                curr_count += 0x8
                sfx_count += 1
    
    #############################
    ##### MARKER COLLISIONS #####
    #############################

    def _parse_marker_collision_value(self, parameter_value:int):
        '''
        Pass
        '''
        bk_effect:int = (parameter_value >> 12) & 0b1111
        entity_next_state:int = (parameter_value >> 10) & 0b11
        collision_sfx:int = (parameter_value >> 7) & 0b111
        bk_damage:int = (parameter_value >> 5) & 0b11
        hits_to_trigger:int = (parameter_value >> 2) & 0b111
        item_drop_slot:int = parameter_value & 0b11
        marker_collision_values:dict = {
            COLLISION_ENUMS.bk_effect: bk_effect,
            COLLISION_ENUMS.entity_next_state: entity_next_state,
            COLLISION_ENUMS.collision_sfx: collision_sfx,
            COLLISION_ENUMS.bk_damage: bk_damage,
            COLLISION_ENUMS.hits_to_trigger: hits_to_trigger,
            COLLISION_ENUMS.item_drop_slot: item_drop_slot,
        }
        return marker_collision_values

    def _create_marker_collision_value(self, marker_collision_values:dict):
        '''
        Pass
        '''
        pass

    def _get_marker_collision_item(self, item_count):
        '''
        Pass
        '''
        index_start:int = 0xD530
        index_increment:int = 0x1A
        parameter_increment:int = 0x2
        marker_collision_item:dict = {}
        for parameter in PARAMETERS_ENUM:
            curr_index:int = index_start + index_increment * item_count + parameter * parameter_increment
            curr_parameter_value:int = self._read_bytes_as_int(curr_index, byte_count=2)
            if(parameter == PARAMETERS_ENUM.marker_id):
                marker_collision_item[parameter] = curr_parameter_value
                continue
            marker_collision_values:dict = self._parse_marker_collision_value(curr_parameter_value)
            marker_collision_item[parameter] =  marker_collision_values
        return marker_collision_item

    def get_marker_collision_table(self):
        '''
        Pass
        '''
        table_count:int = 0xBB
        marker_collision_dict:dict = {}
        for item_count in range(table_count):
            marker_collision_item:dict = self._get_marker_collision_item(item_count)
            marker_collision_dict[item_count] = marker_collision_item
        return marker_collision_dict
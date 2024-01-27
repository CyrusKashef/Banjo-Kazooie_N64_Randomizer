'''
Purpose:
* Modifies code written for the c libraries
'''

###################
##### IMPORTS #####
###################

from randomizer.generic_bin_file_class import Generic_Bin_File_Class

from randomizer.contants.variables.assembly_variables import \
    EXTRACTED_FILES_DIR, DECOMPRESSED_BIN_EXTENSION

X_POSITION_VALUE_STR:str = "X Position Value"
X_POSITION_INDEX_STR:str = "X Position Index"
Z_POSITION_VALUE_STR:str = "Z Position Value"
Z_POSITION_INDEX_STR:str = "Z Position Index"
RADIUS_VALUE_STR:str = "Radius Value"
RADIUS_INDEX_STR:str = "Radius Index"
TRACK_LIST_STR:str = "Track List"
TRACK_INDEX_STR:str = "Track Index"

##################################
##### C LIBRARIES CODE CLASS #####
##################################

class C_LIBRARIES_CODE_CLASS(Generic_Bin_File_Class):
    '''
    Class for modifying code written for the c libraries
    '''
    def __init__(self, file_name:str):
        '''
        Constructor
        '''
        file_path:str = EXTRACTED_FILES_DIR + file_name + DECOMPRESSED_BIN_EXTENSION
        super().__init__(file_path)
    
    def disable_anti_tamper(self):
        '''
        Disables the anti-tampering functions for C Libraries assembly
        Thank You, Wedarobi! <3
        '''
        # code_10A00.c
        # if ((D_80379B90.unk4 != core2_D_803727F4) || (D_80379B90.unkC != D_80276574))
        self._write_bytes_from_int(0x10A1C, 0x00000000, byte_count=4)
        self._write_bytes_from_int(0x10A30, 0x1000, byte_count=2)
    
    def patch_yum_yum_crash_fix(self):
        '''
        Fixes a vanilla bug: 
        When a yumyum in TTC tries to eat a sprite in a cube,
        the game treats it as an actor, derefs an invalid pointer,
        and segfaults.
        Thank You, Wedarobi! <3
        '''
        # Write fix handler over vanilla debug strings
        # Might be replacing "u32 sns_get_next_key_in_range(void)"?
        # Part 1
        self._write_bytes_from_int(0x1D5EC, 0x03E00008, byte_count=4)
        self._write_bytes_from_int(0x1D5F0, 0x00000000, byte_count=4)
        # Part 2
        self._write_bytes_from_int(0x1D5F4, 0x1100000D, byte_count=4)
        self._write_bytes_from_int(0x1D5F8, 0x00000000, byte_count=4)
        self._write_bytes_from_int(0x1D5FC, 0x8D0A0000, byte_count=4)
        self._write_bytes_from_int(0x1D600, 0x000A4E02, byte_count=4)
        self._write_bytes_from_int(0x1D604, 0x34010080, byte_count=4)
        self._write_bytes_from_int(0x1D608, 0x55210008, byte_count=4)
        self._write_bytes_from_int(0x1D60C, 0x3C098000, byte_count=4)
        self._write_bytes_from_int(0x1D610, 0x012A4826, byte_count=4)
        # Part 3
        self._write_bytes_from_int(0x1D614, 0x3C010040, byte_count=4)
        self._write_bytes_from_int(0x1D618, 0x0121482A, byte_count=4)
        self._write_bytes_from_int(0x1D61C, 0x11200003, byte_count=4)
        self._write_bytes_from_int(0x1D620, 0x00000000, byte_count=4)
        self._write_bytes_from_int(0x1D624, 0x080E1C22, byte_count=4)
        self._write_bytes_from_int(0x1D628, 0x00000000, byte_count=4)
        self._write_bytes_from_int(0x1D62C, 0x080E1C28, byte_count=4)
        self._write_bytes_from_int(0x1D630, 0x00000000, byte_count=4)
    
    def booting_up_map(self, map_id:int=0x1F):
        '''
        When loading the game, this is the location the player boots up at
        Typically used to skip the Rareware & N64 logo cutscene and the concert
        '''
        # func_8023DBA4
        # default: MAP_1F_CS_START_RAREWARE
        self._write_bytes_from_int(0x18B, map_id, byte_count=1)
    
    #######################
    ##### MUSIC ZONES #####
    #######################
    # core1/code_CE60.c#L195
    # func_8024A880(0xTRACK_HEX);
    # Each bit in the TRACK_HEX is the track id
    # Example:
    # 0x1cc0 -> 0001 1100 1100 0000
    # Which Is Tracks 7, 8, 11, 12, 13
    
    def convert_track_list_to_hex(self, track_list:list):
        '''
        Pass
        '''
        hex_val:int = 0
        for track_id in track_list:
            hex_val += (1 << (track_id - 1))
        return hex_val

    def _set_music_zone(self, music_zone_dict:dict):
        '''
        Pass
        '''
        # X Position
        if(X_POSITION_VALUE_STR in music_zone_dict):
            x_position_val:int = music_zone_dict[X_POSITION_VALUE_STR]
            x_position_index:int = music_zone_dict[X_POSITION_INDEX_STR]
            self._write_bytes_from_int(x_position_index, x_position_val, byte_count=2)
        # Z Position
        if(Z_POSITION_VALUE_STR in music_zone_dict):
            z_position_val:int = music_zone_dict[Z_POSITION_VALUE_STR]
            z_position_index:int = music_zone_dict[Z_POSITION_INDEX_STR]
            self._write_bytes_from_int(z_position_index, z_position_val, byte_count=2)
        # Radius
        if(RADIUS_VALUE_STR in music_zone_dict):
            radius_val:int = music_zone_dict[RADIUS_VALUE_STR]
            radius_index:int = music_zone_dict[RADIUS_INDEX_STR]
            self._write_bytes_from_int(radius_index, radius_val, byte_count=2)
        # Tracks
        if(TRACK_LIST_STR in music_zone_dict):
            track_list:list = music_zone_dict[TRACK_LIST_STR]
            track_index:int = music_zone_dict[TRACK_INDEX_STR]
            track_hex:int = self.convert_track_list_to_hex(track_list)
            self._write_bytes_from_int(track_index, track_hex, byte_count=2)

    def set_mumbos_mountain_music_zone(self,
            conga_1_dict:dict=None,
            conga_2_dict:dict=None,
            juju_dict:dict=None,
            tickers_tower_dict:dict=None,
            main_area_dict:dict=None,
            swimming_dict:dict=None):
        '''
        Pass
        '''
        # Conga 1
        conga_1_dict[X_POSITION_INDEX_STR] = 0x0
        conga_1_dict[Z_POSITION_INDEX_STR] = 0x0
        conga_1_dict[RADIUS_INDEX_STR] = 0x0
        conga_1_dict[TRACK_INDEX_STR] = 0x0
        self._set_music_zone(conga_1_dict)
        # Conga 2
        conga_2_dict[X_POSITION_INDEX_STR] = 0x0
        conga_2_dict[Z_POSITION_INDEX_STR] = 0x0
        conga_2_dict[RADIUS_INDEX_STR] = 0x0
        conga_2_dict[TRACK_INDEX_STR] = 0x0
        self._set_music_zone(conga_2_dict)
        # Juju Dict
        juju_dict[X_POSITION_INDEX_STR] = 0x0
        juju_dict[Z_POSITION_INDEX_STR] = 0x0
        juju_dict[RADIUS_INDEX_STR] = 0x0
        juju_dict[TRACK_INDEX_STR] = 0x0
        self._set_music_zone(juju_dict)
        # Tickers Tower
        tickers_tower_dict[X_POSITION_INDEX_STR] = 0x0
        tickers_tower_dict[Z_POSITION_INDEX_STR] = 0x0
        tickers_tower_dict[RADIUS_INDEX_STR] = 0xD64A
        tickers_tower_dict[TRACK_INDEX_STR] = 0xD65A
        self._set_music_zone(tickers_tower_dict)
        # Swimming
        swimming_dict[TRACK_INDEX_STR] = 0x0
        self._set_music_zone(swimming_dict)
        # Main Area
        main_area_dict[TRACK_INDEX_STR] = 0xD66A
        self._set_music_zone(main_area_dict)
        ### TIP TO MYSELF IN THE MORNING
        # ADDIU 4, 0, X is for positive numbers
        # ADDIU 5, 0, X is for negative numbers
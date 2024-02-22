'''
Purpose:
*
'''

###################
##### IMPORTS #####
###################

from randomizer.generic_bin_file_class import Generic_Bin_File_Class
from randomizer.game_assets.map_setups.map_setup_class import Map_Setup_Class
from randomizer.game_assets.speeches.speech_class import Speech_Class

from randomizer.constants.int_values.speech_constants import SPEECH_CONSTANTS

from randomizer.constants.dict_values.speeches.geoguesser_speech_dict import GEOGUESSER_SPEECH_MEDIUM_LIST

from randomizer.constants.str_values.string_constants import STRING_CONSTANTS as STR_CONST

######################
##### GAME ASSET #####
######################

class GAME_ASSET_CLASS():
    '''
    Pass
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self._OBJECT_ANIMATION_ASSETS_START_ID:int = 0x0000
        self._OBJECT_MODEL_ASSETS_START_ID:int = 0x02C9
        self._MAP_SETUP_ASSETS_START_ID:int = 0x071C
        self._SPRITE_ASSETS_START_ID:int = 0x07B9
        self._BUTTON_INPUT_ASSETS_START_ID:int = 0x09A3
        self._SPEECH_ASSETS_START_ID:int = 0x0A0B
        self._LEVEL_MODEL_ASSETS_START_ID:int = 0x146A
        self._MUSIC_ASSETS_START_ID:int = 0x1516
        self._ASSETS_END_ID:int = 0x15C7

    ################################
    ####### MASS RUN FUNCTIONS #####
    ################################

    def _return_file_name(self, asset_id:int):
        '''
        Pass
        '''
        byte_count:int = 2
        file_name:str = (str(hex(asset_id))[2:]).zfill(byte_count * 2).upper()
        return file_name

    def _mass_object_animation_editing(self):
        '''
        Pass
        '''
        for asset_id in range(
                self._OBJECT_ANIMATION_ASSETS_START_ID,
                self._OBJECT_MODEL_ASSETS_START_ID):
            file_name:str = self._return_file_name(asset_id)
            try:
                file_path:str = STR_CONST.extracted_files_dir + file_name + STR_CONST.decompressed_bin_extension
                animation_obj:Generic_Bin_File_Class = Generic_Bin_File_Class(file_path)
                yield animation_obj
            except FileNotFoundError:
                pass

    def _mass_object_model_editing(self):
        '''
        Pass
        '''
        for asset_id in range(
                self._OBJECT_MODEL_ASSETS_START_ID,
                self._MAP_SETUP_ASSETS_START_ID):
            file_name:str = self._return_file_name(asset_id)
            try:
                file_path:str = STR_CONST.extracted_files_dir + file_name + STR_CONST.decompressed_bin_extension
                model_obj:Generic_Bin_File_Class = Generic_Bin_File_Class(file_path)
                yield model_obj
            except FileNotFoundError:
                pass

    def _mass_map_setup_editing(self):
        '''
        Pass
        '''
        for asset_id in range(
                self._MAP_SETUP_ASSETS_START_ID,
                self._SPRITE_ASSETS_START_ID):
            file_name:str = self._return_file_name(asset_id)
            print(f"File Name: {file_name}")
            try:
                file_path:str = STR_CONST.extracted_files_dir + file_name + STR_CONST.decompressed_bin_extension
                map_setup_obj:Map_Setup_Class = Map_Setup_Class(file_path)
                yield map_setup_obj
            except FileNotFoundError:
                pass

    def _mass_sprite_editing(self):
        '''
        Pass
        '''
        for asset_id in range(
                self._SPRITE_ASSETS_START_ID,
                self._BUTTON_INPUT_ASSETS_START_ID):
            file_name:str = self._return_file_name(asset_id)
            try:
                file_path:str = STR_CONST.extracted_files_dir + file_name + STR_CONST.decompressed_bin_extension
                sprite_obj:Generic_Bin_File_Class = Generic_Bin_File_Class(file_path)
                yield sprite_obj
            except FileNotFoundError:
                pass

    def _mass_button_input_editing(self):
        '''
        Pass
        '''
        for asset_id in range(
                self._BUTTON_INPUT_ASSETS_START_ID,
                self._SPEECH_ASSETS_START_ID):
            file_name:str = self._return_file_name(asset_id)
            try:
                file_path:str = STR_CONST.extracted_files_dir + file_name + STR_CONST.decompressed_bin_extension
                button_input_obj:Generic_Bin_File_Class = Generic_Bin_File_Class(file_path)
                yield button_input_obj
            except FileNotFoundError:
                pass

    def _mass_speech_editing(self, start_asset_id:int=None, end_asset_id:int=None):
        '''
        Pass
        '''
        if(start_asset_id is None):
            start_asset_id:int = self._SPEECH_ASSETS_START_ID
        if(end_asset_id is None):
            end_asset_id:int = self._LEVEL_MODEL_ASSETS_START_ID
        for asset_id in range(
                start_asset_id,
                end_asset_id):
            file_name:str = self._return_file_name(asset_id)
            try:
                file_path:str = STR_CONST.extracted_files_dir + file_name + STR_CONST.decompressed_bin_extension
                speech_obj:Speech_Class = Speech_Class(file_path)
                yield speech_obj
            except FileNotFoundError:
                pass

    def _mass_level_model_editing(self):
        '''
        Pass
        '''
        for asset_id in range(
                self._LEVEL_MODEL_ASSETS_START_ID,
                self._MUSIC_ASSETS_START_ID):
            file_name:str = self._return_file_name(asset_id)
            try:
                file_path:str = STR_CONST.extracted_files_dir + file_name + STR_CONST.decompressed_bin_extension
                level_modeling_obj:Generic_Bin_File_Class = Generic_Bin_File_Class(file_path)
                yield level_modeling_obj
            except FileNotFoundError:
                pass

    def _mass_music_editing(self):
        '''
        Pass
        '''
        for asset_id in range(
                self._MUSIC_ASSETS_START_ID,
                self._ASSETS_END_ID):
            file_name:str = self._return_file_name(asset_id)
            try:
                file_path:str = STR_CONST.extracted_files_dir + file_name + STR_CONST.decompressed_bin_extension
                music_obj:Generic_Bin_File_Class = Generic_Bin_File_Class(file_path)
                yield music_obj
            except FileNotFoundError:
                pass
    
    ############################
    ##### OBJECT ANIMATION #####
    ############################
    
    ########################
    ##### OBJECT MODEL #####
    ########################
    
    #####################
    ##### MAP SETUP #####
    #####################
    
    def validate_file_editing(self):
        import filecmp
        map_setup_generator = self._mass_map_setup_editing()
        for map_setup in map_setup_generator:
            old_file_path:str = map_setup._file_path
            print(f"File Path: {old_file_path}")
            new_file_path:str = (old_file_path).replace(STR_CONST.decompressed_bin_extension, f"-NEW{STR_CONST.decompressed_bin_extension}")
            logging_path:str = "C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/Breakdown_Notes/Setup_Files_Updated/"
            map_setup.log_map_setup_file_as_text(file_path=logging_path)
            map_setup.save_map_setup_file(file_path=new_file_path)
            same_file:bool = filecmp.cmp(old_file_path, new_file_path)
            if(not same_file):
                print(f"ERROR: validate_file_editing: Copied file at '{old_file_path}' is not the same!")
                exit(0)

    def add_topper_to_spiral_mountain(self):
        '''
        Pass
        '''
        # X_POSITION_STR
        # Y_POSITION_STR
        # Z_POSITION_STR
        # BYTE_6_UNK_0_STR -> Selector/Volume/Diameter?
        # BYTE_6_UNK_1_STR -> Category?
        # BYTE_6_UNK_2_STR
        # ACTOR_ID_STR
        # MARKER_ID_STR
        # BYTE_B_UNK_0_STR
        # BYTE_B_UNK_1_STR
        # BYTE_B_UNK_2_STR
        # BYTE_B_UNK_3_STR
        # BYTE_B_UNK_4_STR
        # ROTATION_Y_AXIS_STR
        # BYTE_C_UNK_1_STR
        # BYTE_10_UNK_0_STR
        # BYTE_10_UNK_1_STR
        # BYTE_10_UNK_2_STR
        # BYTE_10_UNK_3_STR
        # BYTE_10_UNK_4_STR
        # BYTE_10_UNK_5_STR
        complex_object_dict:dict = {
            STR_CONST.x_position: 1850,
            STR_CONST.y_position: 1,
            STR_CONST.z_position: 1850,
            STR_CONST.byte_6_unk_0: 0b000110010,
            STR_CONST.byte_6_unk_1: 0b000110,
            STR_CONST.byte_6_unk_2: 0b0,
            STR_CONST.actor_id: 0x036F,
            STR_CONST.marker_id: 0x00,
            STR_CONST.byte_b_unk_0: 0b00,
            STR_CONST.byte_b_unk_1: 0b0,
            STR_CONST.byte_b_unk_2: 0b0,
            STR_CONST.byte_b_unk_3: 0b000,
            STR_CONST.byte_b_unk_4: 0b0,
            STR_CONST.rotation_y_axis: 0b001011110,
            STR_CONST.byte_c_unk_1: 0b00000000000000001100100,
            STR_CONST.byte_10_unk_0: 0b000011001000,
            STR_CONST.byte_10_unk_1: 0b000000000000,
            STR_CONST.byte_10_unk_2: 0b0,
            STR_CONST.byte_10_unk_3: 0b1,
            STR_CONST.byte_10_unk_4: 0b0000,
            STR_CONST.byte_10_unk_5: 0b01,
        }
        file_name:str = self._return_file_name(0x071D) # Spiral Mountain
        print(f"File Name: {file_name}")
        file_path:str = STR_CONST.extracted_files_dir + file_name + STR_CONST.decompressed_bin_extension
        map_setup_obj:Map_Setup_Class = Map_Setup_Class(file_path)
        map_setup_obj.add_complex_object(complex_object_dict)
        # old_file_path:str = map_setup_obj._file_path
        # new_file_path:str = (old_file_path).replace(STR_CONST.decompressed_bin_extension, f"-NEW{STR_CONST.decompressed_bin_extension}")
        # map_setup_obj.save_map_setup_file(new_file_path)
        map_setup_obj.save_map_setup_file()
    
    def add_note_to_spiral_mountain(self):
        '''
        Pass
        '''
        # BYTE_0_UNK_7_STR -> Actor Id (Note, Tree, etc)
        # BYTE_0_UNK_6_STR -> 
        # BYTE_0_UNK_5_STR ->
        # BYTE_0_UNK_4_STR ->
        # BYTE_0_UNK_3_STR ->
        # BYTE_0_UNK_2_STR -> Size
        # BYTE_0_UNK_1_STR ->
        # BYTE_0_UNK_0_STR ->
        # X_POSITION_STR
        # Y_POSITION_STR
        # Z_POSITION_STR
        # BYTE_8_UNK_7_STR -> UNK
        # BYTE_8_UNK_6_STR -> Y Axis Rotation?
        # BYTE_8_UNK_5_STR ->
        # BYTE_8_UNK_4_STR ->
        # BYTE_8_UNK_3_STR ->
        # BYTE_8_UNK_2_STR ->
        # BYTE_8_UNK_1_STR ->
        # BYTE_8_UNK_0_STR ->
        simple_object_dict_1 = simple_object_dict_2 = simple_object_dict_3 = \
        simple_object_dict_4 = simple_object_dict_5 = {
            STR_CONST.byte_0_unk_7: 0b000101000000,
            STR_CONST.byte_0_unk_6: 0b0,
            STR_CONST.byte_0_unk_5: 0b000,
            STR_CONST.byte_0_unk_4: 0b000,
            STR_CONST.byte_0_unk_3: 0b000,
            STR_CONST.byte_0_unk_2: 0b00101101,
            STR_CONST.byte_0_unk_1: 0b0,
            STR_CONST.byte_0_unk_0: 0b0,
            STR_CONST.x_position: 3700,
            STR_CONST.y_position: -500,
            STR_CONST.z_position: 6300,
            STR_CONST.byte_8_unk_7: 0b00010,
            STR_CONST.byte_8_unk_6: 0b00001,
            STR_CONST.byte_8_unk_5: 0b0,
            STR_CONST.byte_8_unk_4: 0b1,
            STR_CONST.byte_8_unk_3: 0b0,
            STR_CONST.byte_8_unk_2: 0b0,
            STR_CONST.byte_8_unk_1: 0b0,
            STR_CONST.byte_8_unk_0: 0b0,
        }
        file_name:str = self._return_file_name(0x071D) # Spiral Mountain
        print(f"File Name: {file_name}")
        file_path:str = STR_CONST.extracted_files_dir + file_name + STR_CONST.decompressed_bin_extension
        map_setup_obj:Map_Setup_Class = Map_Setup_Class(file_path)
        map_setup_obj.add_simple_object(simple_object_dict_1)
        # map_setup_obj.add_simple_object(simple_object_dict_2)
        # map_setup_obj.add_simple_object(simple_object_dict_3)
        # map_setup_obj.add_simple_object(simple_object_dict_4)
        # map_setup_obj.add_simple_object(simple_object_dict_5)
        map_setup_obj.save_map_setup_file()

    def log_all_complex_objects(self):
        '''
        Pass
        '''
        complex_object_dict:dict = {}
        map_setup_generator = self._mass_map_setup_editing()
        for map_setup in map_setup_generator:
            for lowest_position in map_setup._cube_dict:
                curr_cube:dict = map_setup._cube_dict[lowest_position]
                for complex_object in curr_cube[map_setup._COMPLEX_OBJECT_LIST_STR]:
                    byte_6_unk_1 = complex_object[STR_CONST.byte_6_unk_1]
                    actor_id = complex_object[STR_CONST.actor_id]
                    byte_6_unk_0 = complex_object[STR_CONST.byte_6_unk_0]
                    if(byte_6_unk_1 not in complex_object_dict):
                        complex_object_dict[byte_6_unk_1] = {}
                    if(actor_id not in complex_object_dict[byte_6_unk_1]):
                        complex_object_dict[byte_6_unk_1][actor_id] = {}
                    complex_object_dict[byte_6_unk_1][actor_id][byte_6_unk_0] = "UNKNOWN"
        print("Grabbing Objects Complete! Logging...")
        four_spaces = " " * 4
        open_parenthesis = "{"
        close_parenthesis = "},"
        with open("C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/complex_object_dict_2.txt", "w+") as complex_file:
            complex_file.write("COMPLEX_OBJECT_DICT:dict = {\n")
            for byte_6_unk_1 in sorted(complex_object_dict):
                byte_6_unk_1_str_val:str = (str(bin(byte_6_unk_1))[2:]).zfill(6).upper()
                complex_file.write(f'{four_spaces}0b{byte_6_unk_1_str_val}: {open_parenthesis}\n')
                for actor_id in sorted(complex_object_dict[byte_6_unk_1]):
                    actor_id_str_val = (str(hex(actor_id))[2:]).zfill(4).upper()
                    complex_file.write(f'{four_spaces}{four_spaces}0x{actor_id_str_val}: {open_parenthesis}\n')
                    for byte_6_unk_0 in sorted(complex_object_dict[byte_6_unk_1][actor_id]):
                        byte_6_unk_0_str_val:str = (str(bin(byte_6_unk_0))[2:]).zfill(9).upper()
                        complex_file.write(f'{four_spaces}{four_spaces}{four_spaces}0b{byte_6_unk_0_str_val}: "UNKNOWN",\n')
                    complex_file.write(f'{four_spaces}{four_spaces}{close_parenthesis}\n')
                complex_file.write(f'{four_spaces}{close_parenthesis}\n')
            complex_file.write("}")
        print("Logging Done!")
        exit(0)

    def log_all_objects(self):
        '''
        Pass
        '''
        complex_object_list:list = []
        simple_object_list:list = []
        map_setup_generator = self._mass_map_setup_editing()
        for map_setup in map_setup_generator:
            for lowest_position in map_setup._cube_dict:
                curr_cube:dict = map_setup._cube_dict[lowest_position]
                for complex_object in curr_cube[map_setup._COMPLEX_OBJECT_LIST_STR]:
                    actor_id = complex_object[STR_CONST.actor_id]
                    if(actor_id not in complex_object_list):
                        complex_object_list.append(actor_id)
                for simple_object in curr_cube[map_setup._SIMPLE_OBJECT_LIST_STR]:
                    actor_id = simple_object[STR_CONST.byte_0_unk_7]
                    if(actor_id not in simple_object_list):
                        simple_object_list.append(actor_id)
        print("Grabbing Objects Complete! Logging...")
        with open("C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/complex_object_dict.txt", "w+") as complex_file:
            for item in sorted(complex_object_list):
                str_val:str = (str(hex(item))[2:]).zfill(4)
                complex_file.write(f'    0x{str_val.upper()}: "UNKNOWN",\n')
        with open("C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/simple_object_dict.txt", "w+") as simple_file:
            for item in sorted(simple_object_list):
                str_val:str = (str(bin(item))[2:]).zfill(9)
                simple_file.write(f'    0b{str_val.upper()}: "UNKNOWN",\n')
        print("Logging Done!")
        exit(0)

    # def geoguesser_map_setup_files(self):
    #     '''
    #     Pass
    #     '''
    #     camera_dict:dict = GEOGUESSER_SPEECH_LIST[0][CAMERA_DICT_STR]
    #     camera_dict[STR_CONST.camera_id] = 0x7F
    #     file_name:str = self._return_file_name(0x071D) # Spiral Mountain
    #     print(f"File Name: {file_name}")
    #     file_path:str = STR_CONST.extracted_files_dir + file_name + STR_CONST.decompressed_bin_extension
    #     map_setup_obj:Map_Setup_Class = Map_Setup_Class(file_path)
    #     map_setup_obj.add_camera(camera_dict)
    #     map_setup_obj.save_map_setup_file()

    def geoguesser_map_setup_files(self):
        '''
        Pass
        '''
        camera_dict:dict = GEOGUESSER_SPEECH_MEDIUM_LIST[0][STR_CONST.camera_dict]
        camera_dict[STR_CONST.camera_id] = 0x7F
        file_name:str = self._return_file_name(0x071D) # Spiral Mountain
        print(f"File Name: {file_name}")
        file_path:str = STR_CONST.extracted_files_dir + file_name + STR_CONST.decompressed_bin_extension
        map_setup_obj:Map_Setup_Class = Map_Setup_Class(file_path)
        map_setup_obj.add_camera(camera_dict)
        map_setup_obj.save_map_setup_file()

    ##################
    ##### SPRITE #####
    ##################
    
    ########################
    ##### BUTTON INPUT #####
    ########################
    
    ##################
    ##### SPEECH #####
    ##################
            
    def reverse_all_speech_texts(self):
        '''
        Pass
        '''
        speech_obj_generator = self._mass_speech_editing()
        for speech_obj in speech_obj_generator:
            for curr_section in speech_obj._speech_dict:
                for curr_section_count in speech_obj._speech_dict[curr_section]:
                    curr_speech:str = speech_obj._speech_dict[curr_section][curr_section_count][SPEECH_CONSTANTS.speech]
                    curr_speech = curr_speech[::-1]
                    speech_obj._speech_dict[curr_section][curr_section_count][SPEECH_CONSTANTS.speech] = curr_speech
            speech_obj.save_speech_file()
            
    def log_all_speech_texts(self):
        '''
        Pass
        '''
        four_spaces:str = " " * 4
        eight_spaces:str = " " * 8
        twelve_spaces:str = " " * 12
        speech_str:str = "DEFAULT_SPEECH_DICT:dict = {\n"
        speech_obj_generator = self._mass_speech_editing()
        asset_id:int = self._SPEECH_ASSETS_START_ID
        for speech_obj in speech_obj_generator:
            file_name:str = self._return_file_name(asset_id)
            speech_str += four_spaces + "0x" + file_name + ": {\n"
            for curr_section in speech_obj._speech_dict:
                speech_str += eight_spaces + f'{curr_section}' + ": {\n"
                for curr_section_count in speech_obj._speech_dict[curr_section]:
                    curr_sprite:int = speech_obj._speech_dict[curr_section][curr_section_count][SPEECH_CONSTANTS.sprite]
                    curr_speech:str = speech_obj._speech_dict[curr_section][curr_section_count][SPEECH_CONSTANTS.speech]
                    speech_str += twelve_spaces + f'{curr_sprite}: "{curr_speech}"' + ",\n"
                speech_str += eight_spaces + "},\n"
            speech_str += four_spaces + "},\n"
            asset_id += 1
        speech_str += "}"
        with open("C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/default_speech_dict.txt", "w+") as default_speech_file:
            default_speech_file.write(speech_str)
        exit(0)

    def geoguesser_speech_files(self):
        '''
        Pass
        '''
        speech_obj_generator = self._mass_speech_editing(start_asset_id=0x1277, end_asset_id=0x12EE)
        for speech_obj in speech_obj_generator:
            speech_option:dict = GEOGUESSER_SPEECH_MEDIUM_LIST[0]
            speech_obj.replace_entire_speech_dict(speech_option[STR_CONST.question_dict])
            speech_obj.save_speech_file()
    
    #######################
    ##### LEVEL MODEL #####
    #######################
    
    ########################
    ##### MUSIC ASSETS #####
    ########################
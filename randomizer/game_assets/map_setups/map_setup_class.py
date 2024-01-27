'''
Purpose:
* Class for reading and modifying setup files.
'''

###################
##### IMPORTS #####
###################

from randomizer.generic_bin_file_class import Generic_Bin_File_Class

from randomizer.contants.variables.map_setup_variables import \
    X_POSITION_STR, Y_POSITION_STR, Z_POSITION_STR, \
    BYTE_6_UNK_0_STR, BYTE_6_UNK_1_STR, BYTE_6_UNK_2_STR, \
    ACTOR_ID_STR, MARKER_ID_STR, \
    BYTE_B_UNK_0_STR, BYTE_B_UNK_1_STR, BYTE_B_UNK_2_STR, \
    BYTE_B_UNK_3_STR, BYTE_B_UNK_4_STR, \
    ROTATION_Y_AXIS_STR, BYTE_C_UNK_1_STR, \
    BYTE_10_UNK_0_STR, BYTE_10_UNK_1_STR, BYTE_10_UNK_2_STR, \
    BYTE_10_UNK_3_STR, BYTE_10_UNK_4_STR, BYTE_10_UNK_5_STR, \
    BYTE_0_UNK_0_STR, BYTE_0_UNK_1_STR, BYTE_0_UNK_2_STR, \
    BYTE_0_UNK_3_STR, BYTE_0_UNK_4_STR, BYTE_0_UNK_5_STR, \
    BYTE_0_UNK_6_STR, BYTE_0_UNK_7_STR, \
    BYTE_8_UNK_0_STR, BYTE_8_UNK_1_STR, BYTE_8_UNK_2_STR, \
    BYTE_8_UNK_3_STR, BYTE_8_UNK_4_STR, BYTE_8_UNK_5_STR, \
    BYTE_8_UNK_6_STR, BYTE_8_UNK_7_STR, \
    CAMERA_ID_INDICATOR_STR, CAMERA_TYPE_INDICATOR_STR, \
    CAMERA_END_INDICATOR_STR, \
    CAMERA_SECTION_1_INDICATOR_STR, CAMERA_SECTION_2_INDICATOR_STR, \
    CAMERA_SECTION_3_INDICATOR_STR, CAMERA_SECTION_4_INDICATOR_STR, \
    CAMERA_SECTION_5_INDICATOR_STR, CAMERA_SECTION_6_INDICATOR_STR, \
    CAMERA_ID_STR, CAMERA_TYPE_STR, \
    HORIZONTAL_SPEED_STR, VERTICAL_SPEED_STR, \
    ROTATION_STR, ACCELERATION_STR, \
    PITCH_STR, YAW_STR, ROLL_STR, \
    CAMERA_UNK_BYTE_STR, \
    CLOSE_DISTANCE_STR, FAR_DISTANCE_STR, \
    LIGHTING_START_INDICATOR_STR, \
    LIGHTING_SECTION_1_INDICATOR_STR, LIGHTING_SECTION_2_INDICATOR_STR, \
    LIGHTING_SECTION_3_INDICATOR_STR, LIGHTING_SECTION_4_INDICATOR_STR, \
    BYTE_F_STR, BYTE_13_STR, \
    RED_STR, GREEN_STR, BLUE_STR, \
    FILE_END_INDICATOR_STR

########################
##### SPEECH CLASS #####
########################

class Map_Setup_Class(Generic_Bin_File_Class):
    '''
    Class for reading and modifying speech files.
    '''
    def __init__(self, file_path:str):
        '''
        Constructor
        '''
        # Constants
        self._MAP_SETUP_HEADER:int = 0x0101
        self._CUBE_SEPERATOR:int = 0x01
        self._CUBE_START_INDICATOR:int = 0x030A
        self._COMPLEX_OBJECT_LIST_START_INDICATOR:int = 0x0B
        self._COMPLEX_OBJECT_LIST_END_INDICATOR:int = 0x08
        self._SIMPLE_OBJECT_LIST_START_INDICATOR:int = 0x09
        self._COMPLEX_OBJECT_LENGTH:int = 0x14
        self._SIMPLE_OBJECT_LENGTH:int = 0xC
        self._EMPTY_CUBE_STR:str = "Empty Cube"
        self._COMPLEX_OBJECT_LIST_STR:str = "Complex Object List"
        self._SIMPLE_OBJECT_LIST_STR:str = "Simple Object List"
        self._CAMERA_LIST_START_INDICATOR:int = 0x0003
        self._CAMERA_ID_INDICATOR:int = 0x01
        self._CAMERA_TYPE_INDICATOR:int = 0x02
        self._CAMERA_SECTION_1_INDICATOR:int = 0x01
        self._CAMERA_SECTION_1_INDICATOR:int = 0x01
        self._CAMERA_SECTION_2_INDICATOR:int = 0x02
        self._CAMERA_SECTION_3_INDICATOR:int = 0x03
        self._CAMERA_SECTION_4_INDICATOR:int = 0x04
        self._CAMERA_SECTION_5_INDICATOR:int = 0x05
        self._CAMERA_SECTION_6_INDICATOR:int = 0x06
        self._CAMERA_END_INDICATOR:int = 0x00
        self._LIGHTING_START_INDICATOR:int = 0x0004
        self._LIGHTING_SECTION_1_INDICATOR:int = 0x01
        self._LIGHTING_SECTION_2_INDICATOR:int = 0x02
        self._LIGHTING_SECTION_3_INDICATOR:int = 0x03
        self._LIGHTING_SECTION_4_INDICATOR:int = 0x04
        self._FILE_END_INDICATOR:int = 0x0000

        # Variables
        self._file_path = file_path
        self._file_content = None
        self._cube_dict:dict = {}
        self._camera_dict:dict = {}
        self._lighting_dict:dict = {}

        # Post Actions
        self.read_map_setup_file()

    #############################
    ##### UTILITY FUNCTIONS #####
    #############################
    
    def _verify_indicator(self, start_index:int, byte_count:int, expected_value:int):
        '''
        Pass
        '''
        found_value:int = self._read_bytes_as_int(start_index, byte_count=byte_count)
        if(found_value != expected_value):
            found_value_str:str = self._convert_int_to_hex_str(found_value, byte_count=byte_count)
            start_index_str:str = self._convert_int_to_hex_str(start_index, byte_count=1)
            expected_value_str:str = self._convert_int_to_hex_str(expected_value, byte_count=byte_count)
            error_message:str = f"Error: _verify_indicator: File header 0x{found_value_str} at index 0x{start_index_str} does not match expected value 0x{expected_value_str}."
            print(error_message)
            raise Exception(error_message)

    def _verify_camera_sections(self, verify_camera_dict:dict):
        '''
        Pass
        '''
        for curr_index in verify_camera_dict:
            self._verify_indicator(
                start_index=curr_index,
                byte_count=1,
                expected_value=verify_camera_dict[curr_index])

    def _parse_int_by_bits(self, start_index:int, byte_count:int, bit_count_list:list):
        '''
        Pass
        '''
        # Example:
        # int_val = 0x0B -> 0b00001011
        # start_bit = 1
        # bit_count = 3
        # -> bit_val = 0b101 -> 0x05
        int_val:int = self._read_bytes_as_int(start_index, byte_count)
        bit_val_list:list = []
        expected_bit_count:int = byte_count * 8
        curr_bit_start:int = 0
        for bit_count in bit_count_list:
            bit_val:bin = (int_val >> curr_bit_start) & ((1 << bit_count) - 1)
            bit_val_list.append(bit_val)
            curr_bit_start += bit_count
        if(curr_bit_start != expected_bit_count):
            error_message:str = f"Error: _parse_int_by_bits: Bitfield at index 0x{start_index} exceeds expected bit count."
            print(error_message)
            raise Exception(error_message)
        return bit_val_list

    ###################
    ##### PARSING #####
    ###################

    # COMPLEX OBJECTS

    def _parse_complex_object(self, start_index:int):
        '''
        Pass
        '''
        # Byte 0-6
        x_position:int = self._read_bytes_as_int(start_index, byte_count=2, check_for_negative=True)
        y_position:int = self._read_bytes_as_int(start_index + 0x2, byte_count=2, check_for_negative=True)
        z_position:int = self._read_bytes_as_int(start_index + 0x4, byte_count=2, check_for_negative=True)
        complex_object_bit_count_list:list = [
            2, 4, 1, 1, 12, 12, # Byte 10-13
            23, 9,              # Byte C-F
            1, 3, 1, 1, 2,      # Byte B
            8,                  # Byte A
            16,                 # Byte 8-9
            1, 6, 9,            # Byte 6-7
        ]
        complex_object_count_list:list = self._parse_int_by_bits(
            start_index + 0x6,
            byte_count=(self._COMPLEX_OBJECT_LENGTH - 0x6),
            bit_count_list=complex_object_bit_count_list)
        complex_object_dict:dict = {
            X_POSITION_STR: x_position,
            Y_POSITION_STR: y_position,
            Z_POSITION_STR: z_position,
            BYTE_6_UNK_0_STR: complex_object_count_list[17],
            BYTE_6_UNK_1_STR: complex_object_count_list[16],
            BYTE_6_UNK_2_STR: complex_object_count_list[15],
            ACTOR_ID_STR: complex_object_count_list[14],
            MARKER_ID_STR: complex_object_count_list[13],
            BYTE_B_UNK_0_STR: complex_object_count_list[12],
            BYTE_B_UNK_1_STR: complex_object_count_list[11],
            BYTE_B_UNK_2_STR: complex_object_count_list[10],
            BYTE_B_UNK_3_STR: complex_object_count_list[9],
            BYTE_B_UNK_4_STR: complex_object_count_list[8],
            ROTATION_Y_AXIS_STR: complex_object_count_list[7],
            BYTE_C_UNK_1_STR: complex_object_count_list[6],
            BYTE_10_UNK_0_STR: complex_object_count_list[5],
            BYTE_10_UNK_1_STR: complex_object_count_list[4],
            BYTE_10_UNK_2_STR: complex_object_count_list[3],
            BYTE_10_UNK_3_STR: complex_object_count_list[2],
            BYTE_10_UNK_4_STR: complex_object_count_list[1],
            BYTE_10_UNK_5_STR: complex_object_count_list[0],
        }
        return complex_object_dict

    def _parse_complex_object_list(self, start_index:int, lowest_position:tuple):
        '''
        Pass
        '''
        complex_object_count:int = self._read_bytes_as_int(start_index, byte_count=1)
        # Verify Complex Object List Start Indicator (0x0B)
        self._verify_indicator(
            start_index=(start_index + 0x1),
            byte_count=1,
            expected_value=self._COMPLEX_OBJECT_LIST_START_INDICATOR)
        # Grab Complex Objects
        complex_object_start_index:int = start_index + 0x2
        complex_object_end_index:int = complex_object_start_index + complex_object_count * self._COMPLEX_OBJECT_LENGTH
        for curr_index in range(
                complex_object_start_index,
                complex_object_end_index,
                self._COMPLEX_OBJECT_LENGTH):
            complex_object_dict:dict = self._parse_complex_object(curr_index)
            self._cube_dict[lowest_position][self._COMPLEX_OBJECT_LIST_STR].append(complex_object_dict)
        # Verify Complex Object List End Indicator (0x08)
        self._verify_indicator(
            start_index=complex_object_end_index,
            byte_count=1,
            expected_value=self._COMPLEX_OBJECT_LIST_END_INDICATOR)
        return complex_object_end_index + 0x1

    # SIMPLE OBJECTS

    def _parse_simple_object(self, start_index:int):
        '''
        Pass
        '''
        simple_object_bit_count_list:list = [
            1, 1, 8, 3, 3, 3, 1, 12
        ]
        simple_object_count_list_1:list = self._parse_int_by_bits(
            start_index,
            byte_count=0x4,
            bit_count_list=simple_object_bit_count_list)
        x_position:int = self._read_bytes_as_int(start_index + 0x4, byte_count=2, check_for_negative=True)
        y_position:int = self._read_bytes_as_int(start_index + 0x6, byte_count=2, check_for_negative=True)
        z_position:int = self._read_bytes_as_int(start_index + 0x8, byte_count=2, check_for_negative=True)
        simple_object_bit_count_list:list = [
            1, 1, 1, 1, 1, 1, 5, 5
        ]
        simple_object_count_list_2:list = self._parse_int_by_bits(
            start_index,
            byte_count=0x2,
            bit_count_list=simple_object_bit_count_list)
        simple_object_dict:dict = {
            BYTE_0_UNK_7_STR: simple_object_count_list_1[7],
            BYTE_0_UNK_6_STR: simple_object_count_list_1[6],
            BYTE_0_UNK_5_STR: simple_object_count_list_1[5],
            BYTE_0_UNK_4_STR: simple_object_count_list_1[4],
            BYTE_0_UNK_3_STR: simple_object_count_list_1[3],
            BYTE_0_UNK_2_STR: simple_object_count_list_1[2],
            BYTE_0_UNK_1_STR: simple_object_count_list_1[1],
            BYTE_0_UNK_0_STR: simple_object_count_list_1[0],
            X_POSITION_STR: x_position,
            Y_POSITION_STR: y_position,
            Z_POSITION_STR: z_position,
            BYTE_8_UNK_7_STR: simple_object_count_list_2[7],
            BYTE_8_UNK_6_STR: simple_object_count_list_2[6],
            BYTE_8_UNK_5_STR: simple_object_count_list_2[5],
            BYTE_8_UNK_4_STR: simple_object_count_list_2[4],
            BYTE_8_UNK_3_STR: simple_object_count_list_2[3],
            BYTE_8_UNK_2_STR: simple_object_count_list_2[2],
            BYTE_8_UNK_1_STR: simple_object_count_list_2[1],
            BYTE_8_UNK_0_STR: simple_object_count_list_2[0],
        }
        return simple_object_dict

    def _parse_simple_object_list(self, start_index:int, lowest_position:tuple):
        '''
        Pass
        '''
        simple_object_count:int = self._read_bytes_as_int(start_index, byte_count=1)
        if(simple_object_count == 0x00):
            return start_index + 0x1
        # Verify Simple Object List Start Indicator (0x09)
        self._verify_indicator(
            start_index=(start_index + 0x1),
            byte_count=1,
            expected_value=self._SIMPLE_OBJECT_LIST_START_INDICATOR)
        # Grab Simple Objects
        simple_object_start_index:int = start_index + 0x2
        simple_object_end_index:int = simple_object_start_index + simple_object_count * self._SIMPLE_OBJECT_LENGTH
        for curr_index in range(
                simple_object_start_index,
                simple_object_end_index,
                self._SIMPLE_OBJECT_LENGTH):
            simple_object_dict:dict = self._parse_simple_object(curr_index)
            self._cube_dict[lowest_position][self._SIMPLE_OBJECT_LIST_STR].append(simple_object_dict)
        return simple_object_end_index

    ### CUBES

    def _parse_cube_counts(self):
        '''
        Pass
        '''
        negative_x_cube_count:int = \
            self._read_bytes_as_int(index_start=0x02, byte_count=4, check_for_negative=True)
        negative_y_cube_count:int = \
            self._read_bytes_as_int(index_start=0x06, byte_count=4, check_for_negative=True)
        negative_z_cube_count:int = \
            self._read_bytes_as_int(index_start=0x0A, byte_count=4, check_for_negative=True)
        positive_x_cube_count:int = \
            self._read_bytes_as_int(index_start=0x0E, byte_count=4)
        positive_y_cube_count:int = \
            self._read_bytes_as_int(index_start=0x12, byte_count=4)
        positive_z_cube_count:int = \
            self._read_bytes_as_int(index_start=0x16, byte_count=4)
        return \
            negative_x_cube_count, negative_y_cube_count, negative_z_cube_count, \
            positive_x_cube_count, positive_y_cube_count, positive_z_cube_count

    def _parse_cube(self, start_index:int, lowest_position:tuple):
        '''
        Pass
        '''
        check_for_empty_cube:int = self._read_bytes_as_int(start_index, byte_count=1)
        check_for_existing_cube:int = self._read_bytes_as_int(start_index, byte_count=2)
        if(check_for_empty_cube == self._CUBE_SEPERATOR):
            self._cube_dict[lowest_position] = {
                self._EMPTY_CUBE_STR: True,
                self._COMPLEX_OBJECT_LIST_STR: [],
                self._SIMPLE_OBJECT_LIST_STR: [],
            }
            return start_index
        elif(check_for_existing_cube == self._CUBE_START_INDICATOR):
            self._cube_dict[lowest_position] = {
                self._EMPTY_CUBE_STR: False,
                self._COMPLEX_OBJECT_LIST_STR: [],
                self._SIMPLE_OBJECT_LIST_STR: [],
            }
        else:
            unknown_bytes:str = self._convert_int_to_hex_str(check_for_existing_cube, byte_count=2)
            start_index_str:str = self._convert_int_to_hex_str(start_index, byte_count=1)
            error_message:str = f"ERROR: _parse_cube: Unknown cube bytes 0x{unknown_bytes} at index 0x{start_index_str}."
            print(error_message)
            raise Exception(error_message)
        curr_index:int = start_index + 0x2
        curr_index:int = self._parse_complex_object_list(curr_index, lowest_position)
        curr_index:int = self._parse_simple_object_list(curr_index, lowest_position)
        return curr_index

    def _parse_cubes(self):
        '''
        Pass
        '''
        print("INFO: _parse_cubes: Start!")
        negative_x_cube_count, negative_y_cube_count, negative_z_cube_count, \
        positive_x_cube_count, positive_y_cube_count, positive_z_cube_count = \
            self._parse_cube_counts()
        curr_index:int = 0x1A
        for x_cube_count in range(negative_x_cube_count, positive_x_cube_count + 1):
            lower_x_position:int = (x_cube_count * 1000)
            for y_cube_count in range(negative_y_cube_count, positive_y_cube_count + 1):
                lower_y_position:int = (y_cube_count * 1000)
                for z_cube_count in range(negative_z_cube_count, positive_z_cube_count + 1):
                    lower_z_position:int = (z_cube_count * 1000)
                    lowest_position:tuple = (lower_x_position, lower_y_position, lower_z_position)
                    curr_index:int = self._parse_cube(curr_index, lowest_position)
                    # Verify Cube Seperator (0x01)
                    self._verify_indicator(
                        start_index=curr_index,
                        byte_count=1,
                        expected_value=self._CUBE_SEPERATOR)
                    curr_index += 1
        print("INFO: _parse_cubes: Complete!")
        return curr_index

    ### CAMERAS

    def _parse_unknown_camera(self, start_index:int):
        '''
        Pass
        '''
        verify_camera_dict:dict = {
            (start_index + 0x00): self._CAMERA_ID_INDICATOR,
            (start_index + 0x03): self._CAMERA_TYPE_INDICATOR,
            (start_index + 0x04): self._CAMERA_END_INDICATOR,
        }
        self._verify_camera_sections(verify_camera_dict)
        camera_id:int = self._read_bytes_as_int(start_index + 0x1, byte_count=2)
        self._camera_dict[camera_id] = {
            CAMERA_ID_STR: camera_id,
            CAMERA_TYPE_STR: 0,
        }
        return start_index + 0x5

    def _parse_pivot_camera(self, start_index:int):
        '''
        Pass
        '''
        verify_camera_dict:dict = {
            (start_index + 0x00): self._CAMERA_ID_INDICATOR,
            (start_index + 0x03): self._CAMERA_TYPE_INDICATOR,
            (start_index + 0x05): self._CAMERA_SECTION_1_INDICATOR,
            (start_index + 0x12): self._CAMERA_SECTION_2_INDICATOR,
            (start_index + 0x1B): self._CAMERA_SECTION_3_INDICATOR,
            (start_index + 0x24): self._CAMERA_SECTION_4_INDICATOR,
            (start_index + 0x31): self._CAMERA_SECTION_5_INDICATOR,
            (start_index + 0x36): self._CAMERA_END_INDICATOR,
        }
        self._verify_camera_sections(verify_camera_dict)
        camera_id:int = self._read_bytes_as_int(start_index + 0x1, byte_count=2)
        self._camera_dict[camera_id] = {
            CAMERA_ID_STR: camera_id,
            CAMERA_TYPE_STR: 1,
            X_POSITION_STR: self._read_bytes_as_float(start_index + 0x06),
            Y_POSITION_STR: self._read_bytes_as_float(start_index + 0x0A),
            Z_POSITION_STR: self._read_bytes_as_float(start_index + 0x0E),
            HORIZONTAL_SPEED_STR: self._read_bytes_as_float(start_index + 0x13),
            VERTICAL_SPEED_STR: self._read_bytes_as_float(start_index + 0x17),
            ROTATION_STR: self._read_bytes_as_float(start_index + 0x1C),
            ACCELERATION_STR: self._read_bytes_as_float(start_index + 0x20),
            PITCH_STR: self._read_bytes_as_float(start_index + 0x25),
            YAW_STR: self._read_bytes_as_float(start_index + 0x29),
            ROLL_STR: self._read_bytes_as_float(start_index + 0x2D),
            CAMERA_UNK_BYTE_STR: self._read_bytes_as_int(start_index + 0x32, byte_count=4),
        }
        return start_index + 0x37

    def _parse_static_camera(self, start_index:int):
        '''
        Pass
        '''
        verify_camera_dict:dict = {
            (start_index + 0x00): self._CAMERA_ID_INDICATOR,
            (start_index + 0x03): self._CAMERA_TYPE_INDICATOR,
            (start_index + 0x05): self._CAMERA_SECTION_1_INDICATOR,
            (start_index + 0x12): self._CAMERA_SECTION_2_INDICATOR,
            (start_index + 0x1F): self._CAMERA_END_INDICATOR,
        }
        self._verify_camera_sections(verify_camera_dict)
        camera_id:int = self._read_bytes_as_int(start_index + 0x1, byte_count=2)
        self._camera_dict[camera_id] = {
            CAMERA_ID_STR: camera_id,
            CAMERA_TYPE_STR: 2,
            X_POSITION_STR: self._read_bytes_as_float(start_index + 0x06),
            Y_POSITION_STR: self._read_bytes_as_float(start_index + 0x0A),
            Z_POSITION_STR: self._read_bytes_as_float(start_index + 0x0E),
            PITCH_STR: self._read_bytes_as_float(start_index + 0x13),
            YAW_STR: self._read_bytes_as_float(start_index + 0x17),
            ROLL_STR: self._read_bytes_as_float(start_index + 0x1B),
        }
        return start_index + 0x20

    def _parse_zoom_camera(self, start_index:int):
        '''
        Pass
        '''
        verify_camera_dict:dict = {
            (start_index + 0x00): self._CAMERA_ID_INDICATOR,
            (start_index + 0x03): self._CAMERA_TYPE_INDICATOR,
            (start_index + 0x05): self._CAMERA_SECTION_1_INDICATOR,
            (start_index + 0x12): self._CAMERA_SECTION_2_INDICATOR,
            (start_index + 0x1B): self._CAMERA_SECTION_3_INDICATOR,
            (start_index + 0x24): self._CAMERA_SECTION_4_INDICATOR,
            (start_index + 0x31): self._CAMERA_SECTION_5_INDICATOR,
            (start_index + 0x36): self._CAMERA_SECTION_6_INDICATOR,
            (start_index + 0x3F): self._CAMERA_END_INDICATOR,
        }
        self._verify_camera_sections(verify_camera_dict)
        camera_id:int = self._read_bytes_as_int(start_index + 0x1, byte_count=2)
        self._camera_dict[camera_id] = {
            CAMERA_ID_STR: camera_id,
            CAMERA_TYPE_STR: 3,
            X_POSITION_STR: self._read_bytes_as_float(start_index + 0x06),
            Y_POSITION_STR: self._read_bytes_as_float(start_index + 0x0A),
            Z_POSITION_STR: self._read_bytes_as_float(start_index + 0x0E),
            HORIZONTAL_SPEED_STR: self._read_bytes_as_float(start_index + 0x13),
            VERTICAL_SPEED_STR: self._read_bytes_as_float(start_index + 0x17),
            ROTATION_STR: self._read_bytes_as_float(start_index + 0x1C),
            ACCELERATION_STR: self._read_bytes_as_float(start_index + 0x20),
            PITCH_STR: self._read_bytes_as_float(start_index + 0x25),
            YAW_STR: self._read_bytes_as_float(start_index + 0x29),
            ROLL_STR: self._read_bytes_as_float(start_index + 0x2D),
            CAMERA_UNK_BYTE_STR: self._read_bytes_as_int(start_index + 0x32, byte_count=4),
            CLOSE_DISTANCE_STR: self._read_bytes_as_float(start_index + 0x37),
            FAR_DISTANCE_STR: self._read_bytes_as_float(start_index + 0x3B),
        }
        return start_index + 0x40

    def _parse_random_camera(self, start_index:int):
        '''
        Pass
        '''
        verify_camera_dict:dict = {
            (start_index + 0x00): self._CAMERA_ID_INDICATOR,
            (start_index + 0x03): self._CAMERA_TYPE_INDICATOR,
            (start_index + 0x05): self._CAMERA_SECTION_1_INDICATOR,
            (start_index + 0x0A): self._CAMERA_END_INDICATOR,
        }
        self._verify_camera_sections(verify_camera_dict)
        camera_id:int = self._read_bytes_as_int(start_index + 0x1, byte_count=2)
        self._camera_dict[camera_id] = {
            CAMERA_ID_STR: camera_id,
            CAMERA_TYPE_STR: 4,
            CAMERA_UNK_BYTE_STR: self._read_bytes_as_int(start_index + 0x06, byte_count=4),
        }
        return start_index + 0xB

    def _parse_camera_list(self, start_index:int):
        '''
        Pass
        '''
        print("INFO: _parse_cameras: Start!")
        # Verify Camera Start Indicator (0x0003)
        self._verify_indicator(
            start_index=start_index,
            byte_count=2,
            expected_value=self._CAMERA_LIST_START_INDICATOR)
        self._camera_type_dict:dict = {
            0: self._parse_unknown_camera,
            1: self._parse_pivot_camera,
            2: self._parse_static_camera,
            3: self._parse_zoom_camera,
            4: self._parse_random_camera,
        }
        curr_index:int = start_index + 0x2
        while(self._read_bytes_as_int(curr_index, byte_count=2) != self._LIGHTING_START_INDICATOR):
            print(f"Curr Index: {self._convert_int_to_hex_str(curr_index, byte_count=2)}")
            camera_type:int = self._read_bytes_as_int(curr_index + 0x4, byte_count=1)
            curr_index = self._camera_type_dict[camera_type](curr_index)
        print("INFO: _parse_cameras: Complete!")
        return curr_index

    ### LIGHTING
    
    def _parse_lighting(self, start_index:int):
        '''
        Pass
        '''
        # Verify Lighting Part 1 Indicator (0x01)
        self._verify_indicator(
            start_index=start_index,
            byte_count=1,
            expected_value=self._LIGHTING_SECTION_1_INDICATOR)
        # Verify Lighting Part 2 Indicator (0x02)
        self._verify_indicator(
            start_index=(start_index + 0x01),
            byte_count=1,
            expected_value=self._LIGHTING_SECTION_2_INDICATOR)
        # Verify Lighting Part 3 Indicator (0x03)
        self._verify_indicator(
            start_index=(start_index + 0x0E),
            byte_count=1,
            expected_value=self._LIGHTING_SECTION_3_INDICATOR)
        # Verify Lighting Part 4 Indicator (0x04)
        self._verify_indicator(
            start_index=(start_index + 0x17),
            byte_count=1,
            expected_value=self._LIGHTING_SECTION_4_INDICATOR)
        lighting_dict:dict = {
            X_POSITION_STR: self._read_bytes_as_float(start_index + 0x2),
            Y_POSITION_STR: self._read_bytes_as_float(start_index + 0x6),
            Z_POSITION_STR: self._read_bytes_as_float(start_index + 0xA),
            BYTE_F_STR: self._read_bytes_as_float(start_index + 0xF),
            BYTE_13_STR: self._read_bytes_as_float(start_index + 0x13),
            RED_STR: self._read_bytes_as_int(start_index + 0x18, byte_count=4),
            GREEN_STR: self._read_bytes_as_int(start_index + 0x1C, byte_count=4),
            BLUE_STR: self._read_bytes_as_int(start_index + 0x20, byte_count=4),
        }
        return lighting_dict

    def _parse_lighting_list(self, start_index:int):
        '''
        Pass
        '''
        print("INFO: _parse_lighting: Start!")
        curr_index:int = start_index + 0x2
        lighting_count:int = 0
        while(self._read_bytes_as_int(curr_index, byte_count=2) != self._FILE_END_INDICATOR):
            lighting_dict:dict = self._parse_lighting(curr_index)
            self._lighting_dict[lighting_count] = lighting_dict
            lighting_count += 1
            curr_index += 0x24
        print("INFO: _parse_lighting: Complete!")
        return curr_index

    ###################
    ##### LOGGING #####
    ###################
    
    def _log_hex_line(self,
            curr_index:int, int_val:int,
            byte_count:int, convert_hex_to_num:bool,
            description:str="Unknown", new_line_count:int=1):
        '''
        Pass
        '''
        curr_index_str:str = self._convert_int_to_hex_str(curr_index, byte_count=2)
        int_val_str:str = f"{self._convert_int_to_hex_str(int_val, byte_count)}"
        if(convert_hex_to_num):
            int_val_str += f" -> {int_val_str}"
        new_lines:str = "\n" * new_line_count
        self._log_file.write(f"0x{curr_index_str}: // {description}\n\t{int_val_str}{new_lines}")
        return curr_index + byte_count
    
    def _log_number(self,
            num_val:int, convert_hex_to_num:bool,
            num_type:str, num_count:int=None,
            tab_count:int=2, description:str="Unknown"):
        '''
        Pass
        '''
        if(num_type.lower() == "hex"):
            num_val_str:str = f"0x{self._convert_int_to_hex_str(num_val, num_count)}"
        elif(num_type.lower() == "bit"):
            num_val_str:str = f"0b{self._convert_int_to_bin_str(num_val, num_count)}"
        elif(num_type.lower() == "float"):
            num_val_str:str = f"0x{self._convert_float_to_hex_str(num_val)}"
        if(convert_hex_to_num):
            num_val_str += f" -> {num_val}"
        tab_str:str = "\t" * tab_count
        self._log_file.write(f"{tab_str}{num_val_str} // {description}\n")

    ### HEADER

    def _log_file_header(self, file_name:str):
        '''
        Pass
        '''
        self._log_file.write(f"Normal ROM Address: 0x{file_name}\n\n")
        self._log_file.write(f"######################\n")
        self._log_file.write(f"##### FILE START #####\n")
        self._log_file.write(f"######################\n\n")
        self._log_hex_line(
            0x0, self._MAP_SETUP_HEADER, byte_count=2, convert_hex_to_num=False,
            description="Map Setup Header", new_line_count=2)

    ### CUBES

    def _log_cube_counts(self):
        '''
        Pass
        '''
        min_x = max_x = min_y = max_y = min_z = max_z = 0
        for (x, y, z) in self._cube_dict:
            if(x < min_x):
                min_x = x
            elif(x > max_x):
                max_x = x
            if(y < min_y):
                min_y = y
            elif(y > max_y):
                max_y = y
            if(z < min_z):
                min_z = z
            elif(z > max_z):
                max_z = z
        self._log_file.write(f"Cube Dimensions:\n")
        # X Dimensions
        min_x_dimension:int = min_x // 1000
        min_x_dimension_str:str = self._convert_int_to_hex_str(min_x_dimension, byte_count=4)
        self._log_file.write(f"0x0002: // Negative X Dimension\n\t{min_x_dimension_str} -> {min_x_dimension}\n")
        max_x_dimension:int = max_x // 1000
        max_x_dimension_str:str = self._convert_int_to_hex_str(max_x_dimension, byte_count=4)
        self._log_file.write(f"0x0006: // Positive X Dimension\n\t{max_x_dimension_str} -> {max_x_dimension}\n")
        # Y Dimensions
        min_y_dimension:int = min_y // 1000
        min_y_dimension_str:str = self._convert_int_to_hex_str(min_y_dimension, byte_count=4)
        self._log_file.write(f"0x000A: // Negative Y Dimension\n\t{min_y_dimension_str} -> {min_y_dimension}\n")
        max_y_dimension:int = max_y // 1000
        max_y_dimension_str:str = self._convert_int_to_hex_str(max_y_dimension, byte_count=4)
        self._log_file.write(f"0x000E: // Positive Y Dimension\n\t{max_y_dimension_str} -> {max_y_dimension}\n")
        # Z Dimensions
        min_z_dimension:int = min_z // 1000
        min_z_dimension_str:str = self._convert_int_to_hex_str(min_z_dimension, byte_count=4)
        self._log_file.write(f"0x0012: // Negative Z Dimension\n\t{min_z_dimension_str} -> {min_z_dimension}\n")
        max_z_dimension:int = max_z // 1000
        max_z_dimension_str:str = self._convert_int_to_hex_str(max_z_dimension, byte_count=4)
        self._log_file.write(f"0x0016: // Positive Z Dimension\n\t{max_z_dimension_str} -> {max_z_dimension}\n\n")

    def _log_complex_object(self, complex_object_dict:dict):
        '''
        Pass
        '''
        self._log_number(
            complex_object_dict[X_POSITION_STR], convert_hex_to_num=True,
            num_type="hex", num_count=2, description=X_POSITION_STR)
        self._log_number(
            complex_object_dict[Y_POSITION_STR], convert_hex_to_num=True,
            num_type="hex", num_count=2, description=Y_POSITION_STR)
        self._log_number(
            complex_object_dict[Z_POSITION_STR], convert_hex_to_num=True,
            num_type="hex", num_count=2, description=Z_POSITION_STR)
        self._log_number(
            complex_object_dict[BYTE_6_UNK_0_STR], convert_hex_to_num=True,
            num_type="bit", num_count=9, description=BYTE_6_UNK_0_STR)
        self._log_number(
            complex_object_dict[BYTE_6_UNK_1_STR], convert_hex_to_num=True,
            num_type="bit", num_count=6, description=BYTE_6_UNK_1_STR)
        self._log_number(
            complex_object_dict[BYTE_6_UNK_2_STR], convert_hex_to_num=True,
            num_type="bit", num_count=1, description=BYTE_6_UNK_2_STR)
        self._log_number(
            complex_object_dict[ACTOR_ID_STR], convert_hex_to_num=True,
            num_type="hex", num_count=2, description=ACTOR_ID_STR)
        self._log_number(
            complex_object_dict[MARKER_ID_STR], convert_hex_to_num=True,
            num_type="hex", num_count=1, description=MARKER_ID_STR)
        self._log_number(
            complex_object_dict[BYTE_B_UNK_0_STR], convert_hex_to_num=True,
            num_type="bit", num_count=2, description=BYTE_B_UNK_0_STR)
        self._log_number(
            complex_object_dict[BYTE_B_UNK_1_STR], convert_hex_to_num=True,
            num_type="bit", num_count=1, description=BYTE_B_UNK_1_STR)
        self._log_number(
            complex_object_dict[BYTE_B_UNK_2_STR], convert_hex_to_num=True,
            num_type="bit", num_count=1, description=BYTE_B_UNK_2_STR)
        self._log_number(
            complex_object_dict[BYTE_B_UNK_3_STR], convert_hex_to_num=True,
            num_type="bit", num_count=3, description=BYTE_B_UNK_3_STR)
        self._log_number(
            complex_object_dict[BYTE_B_UNK_4_STR], convert_hex_to_num=True,
            num_type="bit", num_count=1, description=BYTE_B_UNK_4_STR)
        self._log_number(
            complex_object_dict[ROTATION_Y_AXIS_STR], convert_hex_to_num=True,
            num_type="bit", num_count=9, description=ROTATION_Y_AXIS_STR)
        self._log_number(
            complex_object_dict[BYTE_C_UNK_1_STR], convert_hex_to_num=True,
            num_type="bit", num_count=23, description=BYTE_C_UNK_1_STR)
        self._log_number(
            complex_object_dict[BYTE_10_UNK_0_STR], convert_hex_to_num=True,
            num_type="bit", num_count=12, description=BYTE_10_UNK_0_STR)
        self._log_number(
            complex_object_dict[BYTE_10_UNK_1_STR], convert_hex_to_num=True,
            num_type="bit", num_count=12, description=BYTE_10_UNK_1_STR)
        self._log_number(
            complex_object_dict[BYTE_10_UNK_2_STR], convert_hex_to_num=True,
            num_type="bit", num_count=1, description=BYTE_10_UNK_2_STR)
        self._log_number(
            complex_object_dict[BYTE_10_UNK_3_STR], convert_hex_to_num=True,
            num_type="bit", num_count=1, description=BYTE_10_UNK_3_STR)
        self._log_number(
            complex_object_dict[BYTE_10_UNK_4_STR], convert_hex_to_num=True,
            num_type="bit", num_count=4, description=BYTE_10_UNK_4_STR)
        self._log_number(
            complex_object_dict[BYTE_10_UNK_5_STR], convert_hex_to_num=True,
            num_type="bit", num_count=2, description=BYTE_10_UNK_5_STR)

    def _log_complex_object_list(self, curr_index:int, position_tuple:tuple):
        '''
        Pass
        '''
        complex_object_count:int = len(self._cube_dict[position_tuple][self._COMPLEX_OBJECT_LIST_STR])
        curr_index = self._log_hex_line(
            curr_index, 0x030A, byte_count=2, convert_hex_to_num=False,
            description="Cube Start Indicator", new_line_count=1)
        complex_object_count:int = len(self._cube_dict[position_tuple][self._COMPLEX_OBJECT_LIST_STR])
        curr_index = self._log_hex_line(
            curr_index, complex_object_count, byte_count=1, convert_hex_to_num=True,
            description="Complex Object Count", new_line_count=1)
        curr_index = self._log_hex_line(
            curr_index, 0x0B, byte_count=1, convert_hex_to_num=False,
            description="Complex Object List Start", new_line_count=1)
        for curr_complex_object in self._cube_dict[position_tuple][self._COMPLEX_OBJECT_LIST_STR]:
            self._log_file.write(f"0x{self._convert_int_to_hex_str(curr_index, byte_count=2)}: // Complex Object\n")
            self._log_complex_object(curr_complex_object)
            curr_index += self._COMPLEX_OBJECT_LENGTH
        curr_index = self._log_hex_line(
            curr_index, 0x08, byte_count=1, convert_hex_to_num=False,
            description="Complex Object List End", new_line_count=1)
        return curr_index

    def _log_simple_object(self, simple_object_dict:dict):
        '''
        Pass
        '''
        self._log_number(
            simple_object_dict[BYTE_0_UNK_0_STR], convert_hex_to_num=True,
            num_type="bit", num_count=1, description=BYTE_0_UNK_0_STR)
        self._log_number(
            simple_object_dict[BYTE_0_UNK_1_STR], convert_hex_to_num=True,
            num_type="bit", num_count=1, description=BYTE_0_UNK_1_STR)
        self._log_number(
            simple_object_dict[BYTE_0_UNK_2_STR], convert_hex_to_num=True,
            num_type="bit", num_count=8, description=BYTE_0_UNK_2_STR)
        self._log_number(
            simple_object_dict[BYTE_0_UNK_3_STR], convert_hex_to_num=True,
            num_type="bit", num_count=3, description=BYTE_0_UNK_3_STR)
        self._log_number(
            simple_object_dict[BYTE_0_UNK_4_STR], convert_hex_to_num=True,
            num_type="bit", num_count=3, description=BYTE_0_UNK_4_STR)
        self._log_number(
            simple_object_dict[BYTE_0_UNK_5_STR], convert_hex_to_num=True,
            num_type="bit", num_count=3, description=BYTE_0_UNK_5_STR)
        self._log_number(
            simple_object_dict[BYTE_0_UNK_6_STR], convert_hex_to_num=True,
            num_type="bit", num_count=1, description=BYTE_0_UNK_6_STR)
        self._log_number(
            simple_object_dict[BYTE_0_UNK_7_STR], convert_hex_to_num=True,
            num_type="bit", num_count=12, description=BYTE_0_UNK_7_STR)
        self._log_number(
            simple_object_dict[X_POSITION_STR], convert_hex_to_num=True,
            num_type="hex", num_count=2, description=X_POSITION_STR)
        self._log_number(
            simple_object_dict[Y_POSITION_STR], convert_hex_to_num=True,
            num_type="hex", num_count=2, description=Y_POSITION_STR)
        self._log_number(
            simple_object_dict[Z_POSITION_STR], convert_hex_to_num=True,
            num_type="hex", num_count=2, description=Z_POSITION_STR)
        self._log_number(
            simple_object_dict[BYTE_8_UNK_0_STR], convert_hex_to_num=True,
            num_type="bit", num_count=1, description=BYTE_8_UNK_0_STR)
        self._log_number(
            simple_object_dict[BYTE_8_UNK_1_STR], convert_hex_to_num=True,
            num_type="bit", num_count=1, description=BYTE_8_UNK_1_STR)
        self._log_number(
            simple_object_dict[BYTE_8_UNK_2_STR], convert_hex_to_num=True,
            num_type="bit", num_count=1, description=BYTE_8_UNK_2_STR)
        self._log_number(
            simple_object_dict[BYTE_8_UNK_3_STR], convert_hex_to_num=True,
            num_type="bit", num_count=1, description=BYTE_8_UNK_3_STR)
        self._log_number(
            simple_object_dict[BYTE_8_UNK_4_STR], convert_hex_to_num=True,
            num_type="bit", num_count=1, description=BYTE_8_UNK_4_STR)
        self._log_number(
            simple_object_dict[BYTE_8_UNK_5_STR], convert_hex_to_num=True,
            num_type="bit", num_count=1, description=BYTE_8_UNK_5_STR)
        self._log_number(
            simple_object_dict[BYTE_8_UNK_6_STR], convert_hex_to_num=True,
            num_type="bit", num_count=5, description=BYTE_8_UNK_6_STR)
        self._log_number(
            simple_object_dict[BYTE_8_UNK_7_STR], convert_hex_to_num=True,
            num_type="bit", num_count=5, description=BYTE_8_UNK_7_STR)

    def _log_simple_object_list(self, curr_index:int, position_tuple:tuple):
        '''
        Pass
        '''
        simple_object_count:int = len(self._cube_dict[position_tuple][self._SIMPLE_OBJECT_LIST_STR])
        curr_index = self._log_hex_line(
            curr_index, simple_object_count, byte_count=1, convert_hex_to_num=True,
            description="Simple Object Count", new_line_count=1)
        if(simple_object_count > 0):
            curr_index = self._log_hex_line(
                curr_index, self._SIMPLE_OBJECT_LIST_START_INDICATOR, byte_count=1, convert_hex_to_num=False,
                description="Simple Object List Indicator", new_line_count=1)
            for simple_object_dict in self._cube_dict[position_tuple][self._SIMPLE_OBJECT_LIST_STR]:
                self._log_file.write(f"0x{self._convert_int_to_hex_str(curr_index, byte_count=2)}: // Simple Object\n")
                self._log_simple_object(simple_object_dict)
                curr_index += self._SIMPLE_OBJECT_LENGTH
        return curr_index

    def _log_cubes(self):
        '''
        Pass
        '''
        self._log_cube_counts()
        curr_index:int = 0x1A
        for position_tuple in sorted(self._cube_dict):
            if(self._cube_dict[position_tuple][self._EMPTY_CUBE_STR]):
                self._log_file.write(f"Empty Cube:\n")
                curr_index = self._log_hex_line(
                    curr_index, self._CUBE_SEPERATOR, byte_count=1, convert_hex_to_num=False,
                    description="Cube Seperator", new_line_count=2)
                continue
            self._log_file.write(f"Existing Cube:\n")
            curr_index:int = self._log_complex_object_list(curr_index, position_tuple)
            curr_index:int = self._log_simple_object_list(curr_index, position_tuple)
            curr_index = self._log_hex_line(
                curr_index, self._CUBE_SEPERATOR, byte_count=1, convert_hex_to_num=False,
                description="Cube Seperator", new_line_count=2)
        return curr_index
    
    ### CAMERAS

    def _log_unknown_camera(self, camera_dict:dict):
        '''
        Pass
        '''
        self._log_number(
            self._CAMERA_ID_INDICATOR, convert_hex_to_num=False,
            num_type="hex", num_count=1, description=CAMERA_ID_INDICATOR_STR)
        self._log_number(
            camera_dict[CAMERA_ID_STR], convert_hex_to_num=True,
            num_type="hex", num_count=2, tab_count=3, description=CAMERA_ID_STR)
        self._log_number(
            self._CAMERA_TYPE_INDICATOR, convert_hex_to_num=True,
            num_type="hex", num_count=1, tab_count=2, description=CAMERA_TYPE_INDICATOR_STR)
        self._log_number(
            camera_dict[CAMERA_TYPE_STR], convert_hex_to_num=True,
            num_type="hex", num_count=2, tab_count=3, description=CAMERA_TYPE_STR)
        self._log_number(
            self._CAMERA_END_INDICATOR, convert_hex_to_num=False,
            num_type="hex", num_count=1, description=CAMERA_END_INDICATOR_STR)

    def _log_pivot_camera(self, camera_dict:dict):
        '''
        Pass
        '''
        self._log_number(
            self._CAMERA_ID_INDICATOR, convert_hex_to_num=False,
            num_type="hex", num_count=1, description=CAMERA_ID_INDICATOR_STR)
        self._log_number(
            camera_dict[CAMERA_ID_STR], convert_hex_to_num=True,
            num_type="hex", num_count=2, tab_count=3, description=CAMERA_ID_STR)
        self._log_number(
            self._CAMERA_TYPE_INDICATOR, convert_hex_to_num=True,
            num_type="hex", num_count=1, tab_count=2, description=CAMERA_TYPE_INDICATOR_STR)
        self._log_number(
            camera_dict[CAMERA_TYPE_STR], convert_hex_to_num=True,
            num_type="hex", num_count=2, tab_count=3, description=CAMERA_TYPE_STR)
        self._log_number(
            self._CAMERA_SECTION_1_INDICATOR, convert_hex_to_num=False,
            num_type="hex", num_count=1, description=CAMERA_SECTION_1_INDICATOR_STR)
        self._log_number(
            camera_dict[X_POSITION_STR], convert_hex_to_num=True,
            num_type="float", num_count=4, tab_count=3, description=X_POSITION_STR)
        self._log_number(
            camera_dict[Y_POSITION_STR], convert_hex_to_num=True,
            num_type="float", num_count=4, tab_count=3, description=Y_POSITION_STR)
        self._log_number(
            camera_dict[Z_POSITION_STR], convert_hex_to_num=True,
            num_type="float", num_count=4, tab_count=3, description=Z_POSITION_STR)
        self._log_number(
            self._CAMERA_SECTION_2_INDICATOR, convert_hex_to_num=False,
            num_type="hex", num_count=1, description=CAMERA_SECTION_2_INDICATOR_STR)
        self._log_number(
            camera_dict[HORIZONTAL_SPEED_STR], convert_hex_to_num=True,
            num_type="float", num_count=4, tab_count=3, description=HORIZONTAL_SPEED_STR)
        self._log_number(
            camera_dict[VERTICAL_SPEED_STR], convert_hex_to_num=True,
            num_type="float", num_count=4, tab_count=3, description=VERTICAL_SPEED_STR)
        self._log_number(
            self._CAMERA_SECTION_3_INDICATOR, convert_hex_to_num=False,
            num_type="hex", num_count=1, description=CAMERA_SECTION_3_INDICATOR_STR)
        self._log_number(
            camera_dict[ROTATION_STR], convert_hex_to_num=True,
            num_type="float", num_count=4, tab_count=3, description=ROTATION_STR)
        self._log_number(
            camera_dict[ACCELERATION_STR], convert_hex_to_num=True,
            num_type="float", num_count=4, tab_count=3, description=ACCELERATION_STR)
        self._log_number(
            self._CAMERA_SECTION_4_INDICATOR, convert_hex_to_num=False,
            num_type="hex", num_count=1, description=CAMERA_SECTION_4_INDICATOR_STR)
        self._log_number(
            camera_dict[PITCH_STR], convert_hex_to_num=True,
            num_type="float", num_count=4, tab_count=3, description=PITCH_STR)
        self._log_number(
            camera_dict[YAW_STR], convert_hex_to_num=True,
            num_type="float", num_count=4, tab_count=3, description=YAW_STR)
        self._log_number(
            camera_dict[ROLL_STR], convert_hex_to_num=True,
            num_type="float", num_count=4, tab_count=3, description=ROLL_STR)
        self._log_number(
            self._CAMERA_SECTION_5_INDICATOR, convert_hex_to_num=False,
            num_type="hex", num_count=1, description=CAMERA_SECTION_5_INDICATOR_STR)
        self._log_number(
            camera_dict[CAMERA_UNK_BYTE_STR], convert_hex_to_num=True,
            num_type="hex", num_count=4, tab_count=3, description=CAMERA_UNK_BYTE_STR)
        self._log_number(
            self._CAMERA_END_INDICATOR, convert_hex_to_num=False,
            num_type="hex", num_count=1, description=CAMERA_END_INDICATOR_STR)

    def _log_static_camera(self, camera_dict:dict):
        '''
        Pass
        '''
        self._log_number(
            self._CAMERA_ID_INDICATOR, convert_hex_to_num=False,
            num_type="hex", num_count=1, description=CAMERA_ID_INDICATOR_STR)
        self._log_number(
            camera_dict[CAMERA_ID_STR], convert_hex_to_num=True,
            num_type="hex", num_count=2, tab_count=3, description=CAMERA_ID_STR)
        self._log_number(
            self._CAMERA_TYPE_INDICATOR, convert_hex_to_num=True,
            num_type="hex", num_count=1, tab_count=2, description=CAMERA_TYPE_INDICATOR_STR)
        self._log_number(
            camera_dict[CAMERA_TYPE_STR], convert_hex_to_num=True,
            num_type="hex", num_count=2, tab_count=3, description=CAMERA_TYPE_STR)
        self._log_number(
            self._CAMERA_SECTION_1_INDICATOR, convert_hex_to_num=False,
            num_type="hex", num_count=1, description=CAMERA_SECTION_1_INDICATOR_STR)
        self._log_number(
            camera_dict[X_POSITION_STR], convert_hex_to_num=True,
            num_type="float", num_count=4, tab_count=3, description=X_POSITION_STR)
        self._log_number(
            camera_dict[Y_POSITION_STR], convert_hex_to_num=True,
            num_type="float", num_count=4, tab_count=3, description=Y_POSITION_STR)
        self._log_number(
            camera_dict[Z_POSITION_STR], convert_hex_to_num=True,
            num_type="float", num_count=4, tab_count=3, description=Z_POSITION_STR)
        self._log_number(
            self._CAMERA_SECTION_2_INDICATOR, convert_hex_to_num=False,
            num_type="hex", num_count=1, description=CAMERA_SECTION_2_INDICATOR_STR)
        self._log_number(
            camera_dict[PITCH_STR], convert_hex_to_num=True,
            num_type="float", num_count=4, tab_count=3, description=PITCH_STR)
        self._log_number(
            camera_dict[YAW_STR], convert_hex_to_num=True,
            num_type="float", num_count=4, tab_count=3, description=YAW_STR)
        self._log_number(
            camera_dict[ROLL_STR], convert_hex_to_num=True,
            num_type="float", num_count=4, tab_count=3, description=ROLL_STR)
        self._log_number(
            self._CAMERA_END_INDICATOR, convert_hex_to_num=False,
            num_type="hex", num_count=1, description=CAMERA_END_INDICATOR_STR)

    def _log_zoom_camera(self, camera_dict:dict):
        '''
        Pass
        '''
        self._log_number(
            self._CAMERA_ID_INDICATOR, convert_hex_to_num=False,
            num_type="hex", num_count=1, description=CAMERA_ID_INDICATOR_STR)
        self._log_number(
            camera_dict[CAMERA_ID_STR], convert_hex_to_num=True,
            num_type="hex", num_count=2, tab_count=3, description=CAMERA_ID_STR)
        self._log_number(
            self._CAMERA_TYPE_INDICATOR, convert_hex_to_num=True,
            num_type="hex", num_count=1, tab_count=2, description=CAMERA_TYPE_INDICATOR_STR)
        self._log_number(
            camera_dict[CAMERA_TYPE_STR], convert_hex_to_num=True,
            num_type="hex", num_count=2, tab_count=3, description=CAMERA_TYPE_STR)
        self._log_number(
            self._CAMERA_SECTION_1_INDICATOR, convert_hex_to_num=False,
            num_type="hex", num_count=1, description=CAMERA_SECTION_1_INDICATOR_STR)
        self._log_number(
            camera_dict[X_POSITION_STR], convert_hex_to_num=True,
            num_type="float", num_count=4, tab_count=3, description=X_POSITION_STR)
        self._log_number(
            camera_dict[Y_POSITION_STR], convert_hex_to_num=True,
            num_type="float", num_count=4, tab_count=3, description=Y_POSITION_STR)
        self._log_number(
            camera_dict[Z_POSITION_STR], convert_hex_to_num=True,
            num_type="float", num_count=4, tab_count=3, description=Z_POSITION_STR)
        self._log_number(
            self._CAMERA_SECTION_2_INDICATOR, convert_hex_to_num=False,
            num_type="hex", num_count=1, description=CAMERA_SECTION_2_INDICATOR_STR)
        self._log_number(
            camera_dict[HORIZONTAL_SPEED_STR], convert_hex_to_num=True,
            num_type="float", num_count=4, tab_count=3, description=HORIZONTAL_SPEED_STR)
        self._log_number(
            camera_dict[VERTICAL_SPEED_STR], convert_hex_to_num=True,
            num_type="float", num_count=4, tab_count=3, description=VERTICAL_SPEED_STR)
        self._log_number(
            self._CAMERA_SECTION_3_INDICATOR, convert_hex_to_num=False,
            num_type="hex", num_count=1, description=CAMERA_SECTION_3_INDICATOR_STR)
        self._log_number(
            camera_dict[ROTATION_STR], convert_hex_to_num=True,
            num_type="float", num_count=4, tab_count=3, description=ROTATION_STR)
        self._log_number(
            camera_dict[ACCELERATION_STR], convert_hex_to_num=True,
            num_type="float", num_count=4, tab_count=3, description=ACCELERATION_STR)
        self._log_number(
            self._CAMERA_SECTION_4_INDICATOR, convert_hex_to_num=False,
            num_type="hex", num_count=1, description=CAMERA_SECTION_4_INDICATOR_STR)
        self._log_number(
            camera_dict[PITCH_STR], convert_hex_to_num=True,
            num_type="float", num_count=4, tab_count=3, description=PITCH_STR)
        self._log_number(
            camera_dict[YAW_STR], convert_hex_to_num=True,
            num_type="float", num_count=4, tab_count=3, description=YAW_STR)
        self._log_number(
            camera_dict[ROLL_STR], convert_hex_to_num=True,
            num_type="float", num_count=4, tab_count=3, description=ROLL_STR)
        self._log_number(
            self._CAMERA_SECTION_5_INDICATOR, convert_hex_to_num=False,
            num_type="hex", num_count=1, description=CAMERA_SECTION_5_INDICATOR_STR)
        self._log_number(
            camera_dict[CAMERA_UNK_BYTE_STR], convert_hex_to_num=True,
            num_type="hex", num_count=4, tab_count=3, description=CAMERA_UNK_BYTE_STR)
        self._log_number(
            self._CAMERA_SECTION_6_INDICATOR, convert_hex_to_num=False,
            num_type="hex", num_count=1, description=CAMERA_SECTION_6_INDICATOR_STR)
        self._log_number(
            camera_dict[CLOSE_DISTANCE_STR], convert_hex_to_num=True,
            num_type="float", num_count=4, tab_count=3, description=CLOSE_DISTANCE_STR)
        self._log_number(
            camera_dict[FAR_DISTANCE_STR], convert_hex_to_num=True,
            num_type="float", num_count=4, tab_count=3, description=FAR_DISTANCE_STR)
        self._log_number(
            self._CAMERA_END_INDICATOR, convert_hex_to_num=False,
            num_type="hex", num_count=1, description=CAMERA_END_INDICATOR_STR)

    def _log_random_camera(self, camera_dict:dict):
        '''
        Pass
        '''
        self._log_number(
            self._CAMERA_ID_INDICATOR, convert_hex_to_num=False,
            num_type="hex", num_count=1, description=CAMERA_ID_INDICATOR_STR)
        self._log_number(
            camera_dict[CAMERA_ID_STR], convert_hex_to_num=True,
            num_type="hex", num_count=2, tab_count=3, description=CAMERA_ID_STR)
        self._log_number(
            self._CAMERA_TYPE_INDICATOR, convert_hex_to_num=True,
            num_type="hex", num_count=1, tab_count=2, description=CAMERA_TYPE_INDICATOR_STR)
        self._log_number(
            camera_dict[CAMERA_TYPE_STR], convert_hex_to_num=True,
            num_type="hex", num_count=2, tab_count=3, description=CAMERA_TYPE_STR)
        self._log_number(
            self._CAMERA_SECTION_1_INDICATOR, convert_hex_to_num=False,
            num_type="hex", num_count=1, description=CAMERA_SECTION_1_INDICATOR_STR)
        self._log_number(
            camera_dict[CAMERA_UNK_BYTE_STR], convert_hex_to_num=True,
            num_type="hex", num_count=4, tab_count=3, description=CAMERA_UNK_BYTE_STR)
        self._log_number(
            self._CAMERA_END_INDICATOR, convert_hex_to_num=False,
            num_type="hex", num_count=1, description=CAMERA_END_INDICATOR_STR)

    def _log_cameras(self, start_index:int):
        '''
        Pass
        '''
        curr_index = self._log_hex_line(
            start_index, self._CAMERA_LIST_START_INDICATOR, byte_count=2, convert_hex_to_num=False,
            description="Camera List Start Indicator", new_line_count=2)
        for curr_camera_id in sorted(self._camera_dict):
            camera_dict:dict = self._camera_dict[curr_camera_id]
            camera_type:int = camera_dict[CAMERA_TYPE_STR]
            self._log_file.write(f"0x{self._convert_int_to_hex_str(curr_index, byte_count=2)}:\n")
            self._log_file.write(f"\tCamera Type {camera_type} Here\n")
            if(camera_type == 0):
                curr_index += 0x05
            elif(camera_type == 1):
                curr_index += 0x37
            elif(camera_type == 2):
                self._log_static_camera(camera_dict)
                curr_index += 0x20
            elif(camera_type == 3):
                self._log_zoom_camera(camera_dict)
                curr_index += 0x40
            elif(camera_type == 4):
                curr_index += 0x0B
            else:
                error_message:str = f"ERROR: _log_cameras: Unknown camera type {camera_type} found!"
                print(error_message)
                raise Exception(error_message)
            self._log_file.write("\n")
        return curr_index

    ### LIGHTING

    def _log_lighting(self, light_dict:dict):
        '''
        Pass
        '''
        self._log_number(
            self._LIGHTING_SECTION_1_INDICATOR, convert_hex_to_num=False,
            num_type="hex", num_count=1, description=LIGHTING_SECTION_1_INDICATOR_STR)
        self._log_number(
            self._LIGHTING_SECTION_2_INDICATOR, convert_hex_to_num=False,
            num_type="hex", num_count=1, description=LIGHTING_SECTION_2_INDICATOR_STR)
        self._log_number(
            light_dict[X_POSITION_STR], convert_hex_to_num=True,
            num_type="float", num_count=4, tab_count=3, description=X_POSITION_STR)
        self._log_number(
            light_dict[Y_POSITION_STR], convert_hex_to_num=True,
            num_type="float", num_count=4, tab_count=3, description=Y_POSITION_STR)
        self._log_number(
            light_dict[Z_POSITION_STR], convert_hex_to_num=True,
            num_type="float", num_count=4, tab_count=3, description=Z_POSITION_STR)
        self._log_number(
            self._LIGHTING_SECTION_3_INDICATOR, convert_hex_to_num=False,
            num_type="hex", num_count=1, description=LIGHTING_SECTION_3_INDICATOR_STR)
        self._log_number(
            light_dict[BYTE_F_STR], convert_hex_to_num=True,
            num_type="float", num_count=4, tab_count=3, description=BYTE_F_STR)
        self._log_number(
            light_dict[BYTE_13_STR], convert_hex_to_num=True,
            num_type="float", num_count=4, tab_count=3, description=BYTE_13_STR)
        self._log_number(
            self._LIGHTING_SECTION_4_INDICATOR, convert_hex_to_num=False,
            num_type="hex", num_count=1, description=LIGHTING_SECTION_4_INDICATOR_STR)
        self._log_number(
            light_dict[RED_STR], convert_hex_to_num=True,
            num_type="float", num_count=4, tab_count=3, description=RED_STR)
        self._log_number(
            light_dict[GREEN_STR], convert_hex_to_num=True,
            num_type="float", num_count=4, tab_count=3, description=GREEN_STR)
        self._log_number(
            light_dict[BLUE_STR], convert_hex_to_num=True,
            num_type="float", num_count=4, tab_count=3, description=BLUE_STR)

    def _log_lighting_list(self, start_index:int):
        '''
        Pass
        '''
        curr_index = self._log_hex_line(
            start_index, self._LIGHTING_START_INDICATOR, byte_count=2, convert_hex_to_num=False,
            description=LIGHTING_START_INDICATOR_STR, new_line_count=2)
        for curr_lighting_count in sorted(self._lighting_dict):
            self._log_file.write(f"0x{self._convert_int_to_hex_str(curr_index, byte_count=2)}:\n")
            self._log_file.write(f"\tLighting Here\n")
            light_dict:dict = self._lighting_dict[curr_lighting_count]
            self._log_lighting(light_dict)
            curr_index += 0x24
            self._log_file.write("\n")
        return curr_index
    
    ### FILE ENDER
    
    def _log_file_end(self, start_index:int):
        '''
        Pass
        '''
        self._log_file.write(f"####################\n")
        self._log_file.write(f"##### FILE END #####\n")
        self._log_file.write(f"####################\n\n")
        self._log_hex_line(
            start_index, self._FILE_END_INDICATOR, byte_count=2, convert_hex_to_num=False,
            description=FILE_END_INDICATOR_STR, new_line_count=0)

    ##########################
    ##### EDIT FUNCTIONS #####
    ##########################

    #################
    ##### WRITE #####
    #################

    ##########################
    ##### MAIN FUNCTIONS #####
    ##########################
        
    def read_map_setup_file(self):
        '''
        Pass
        '''
        super()._read_file()
        curr_index:int = self._parse_cubes()
        curr_index:int = self._parse_camera_list(curr_index)
        curr_index:int = self._parse_lighting_list(curr_index)
    
    def log_map_setup_file_as_text(self):
        '''
        Pass
        '''
        file_name:str = (self._file_path).rsplit("/", 1)[1].replace(".bin", "")
        print(file_name)
        with open(f"randomizer/extracted_files/{file_name}.txt", "w+") as self._log_file:
            self._log_file_header(file_name)
            self._log_file.write(f"#################\n")
            self._log_file.write(f"##### CUBES #####\n")
            self._log_file.write(f"#################\n\n")
            curr_index:int = self._log_cubes()
            self._log_file.write(f"###################\n")
            self._log_file.write(f"##### CAMERAS #####\n")
            self._log_file.write(f"###################\n\n")
            curr_index:int = self._log_cameras(curr_index)
            self._log_file.write(f"####################\n")
            self._log_file.write(f"##### LIGHTING #####\n")
            self._log_file.write(f"####################\n\n")
            curr_index:int = self._log_lighting_list(curr_index)
            self._log_file_end(curr_index)
    
    def save_map_setup_file(self, file_path:str|None=None):
        '''
        Pass
        '''
        pass

################
##### MAIN #####
################

if __name__ == '__main__':
    file_dir:str = "C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/test2/"
    save_file_dir:str = "C:/Users/Cyrus/Documents/VS_Code/Banjo-Kazooie_Randomizer/Banjo-Kazooie_N64_Randomizer/randomizer/extracted_files/"
    print("\nClanker's Cavern Wonderwing Room:")
    file_name:str = "4DA1B8.bin"
    file_path:str = f"{file_dir}{file_name}"
    map_setup_obj = Map_Setup_Class(file_path)
    map_setup_obj.log_map_setup_file_as_text()
    map_setup_obj.save_map_setup_file(f"{save_file_dir}{file_name}")
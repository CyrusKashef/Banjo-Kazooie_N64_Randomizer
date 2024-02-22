'''
Purpose:
* Class for reading and modifying speech files.
'''

###################
##### IMPORTS #####
###################

from randomizer.generic_bin_file_class import Generic_Bin_File_Class
from randomizer.constants.dict_values.speech_syntax_dicts import \
    FANCY_FONT_DICT, FURNACE_FUN_SPRITE_DICT, \
    GENERAL_SPRITE_DICT, ACTION_DICT

from randomizer.constants.int_values.speech_constants import SPEECH_CONSTANTS

########################
##### SPEECH CLASS #####
########################

class Speech_Class(Generic_Bin_File_Class):
    '''
    Class for reading and modifying speech files.
    '''
    def __init__(self, file_path:str):
        '''
        Constructor
        '''
        self._file_path = file_path
        self._file_content = None
        self.read_speech_file()

    #################################
    ##### DETERMINE SPEECH TYPE #####
    #################################

    def _determine_speech_type(self):
        '''
        Checks the first few bytes of the file to determine
        whether the speech is a Furnace Fun Gruntilda question,
        Furnace Fun Generic question, or Generic speech file.
        '''
        first_five_bytes:int = self._read_bytes_as_int(index_start=0, byte_count=5)
        first_three_bytes:int = self._read_bytes_as_int(index_start=0, byte_count=3)
        if(first_five_bytes == 0x0103000500):
            return SPEECH_CONSTANTS.furnace_fun_gruntilda_question
        elif(first_five_bytes == 0x0101020500):
            return SPEECH_CONSTANTS.furnace_fun_other_question
        elif(first_three_bytes == 0x010300):
            return SPEECH_CONSTANTS.generic_speech
        raise Exception("ERROR: _determine_speech_type: Unknown Speech File Type")

    ###################
    ##### PARSING #####
    ###################

    def _translate_action(self, start_index:int, speech_length:int):
        '''
        Attempts to give a description of what
        the action function does.
        '''
        if(speech_length != 0x2):
            raise Exception("ERROR: _translate_action: Action not length of 2")
        action = self._read_bytes_as_hex_str(start_index, byte_count=2)
        if(action in ACTION_DICT):
            action_description:str = ACTION_DICT[action]
        else:
            camera_id = self._read_bytes_as_hex_str(start_index, byte_count=1)
            action_description = f"Unknown Action/Use Camera 0x{camera_id}?"
        return action_description

    def _translate_speech(self, start_index:int, speech_length:int):
        '''
        Translates the speech string from
        bytes to latin.
        '''
        speech:str = ""
        while(len(speech) < (speech_length - 1)):
            speech += chr(self._read_bytes_as_int(start_index, byte_count=1))
            start_index += 1
        return speech

    def _parse_speech_section(self, section_name:str, num_of_speeches:int, start_index:int):
        '''
        Reads a speech section and translates the
        actions and the strings and places them
        into a dictionary.
        '''
        self._speech_dict[section_name] = {}
        for speech_num in range(num_of_speeches):
            sprite:int = self._read_bytes_as_int(start_index, byte_count=1)
            speech_length:int = self._read_bytes_as_int(start_index + 0x1, byte_count=1)
            start_index += 0x2
            if(sprite == 0x7):
                translation:str = self._translate_action(start_index, speech_length)
            else:
                translation:str = self._translate_speech(start_index, speech_length)
            self._speech_dict[section_name][speech_num] = {
                SPEECH_CONSTANTS.sprite: sprite,
                SPEECH_CONSTANTS.speech: translation,
            }
            start_index += speech_length
        return start_index

    def _parse_furance_fun_speech(self):
        '''
        Reads a furnace fun speech file.
        '''
        section_name:str = SPEECH_CONSTANTS.full_screen
        start_index:int = 5
        num_of_speeches:int = self._read_bytes_as_int(start_index, byte_count=1)
        start_index += 0x1
        start_index:int = self._parse_speech_section(section_name, num_of_speeches, start_index)

    def _parse_generic_speech(self):
        '''
        Reads a generic speech file.
        '''
        start_index:int = 3
        # Bottom Speeches
        section_name:str = SPEECH_CONSTANTS.bottom_section
        num_of_bottom_speeches:int =  self._read_bytes_as_int(start_index, byte_count=1)
        start_index += 0x1
        start_index:int = self._parse_speech_section(section_name, num_of_bottom_speeches, start_index)
        # Top Speeches
        section_name:str = SPEECH_CONSTANTS.top_section
        num_of_top_speeches:int =  self._read_bytes_as_int(start_index, byte_count=1)
        start_index += 0x1
        start_index:int = self._parse_speech_section(section_name, num_of_top_speeches, start_index)

    ####################
    ##### PRINTING #####
    ####################
    
    def _translate_fancy_font(self, speech:str):
        '''
        Translates the fancy font options.
        '''
        for fancy_font in FANCY_FONT_DICT:
            speech = speech.replace(fancy_font, FANCY_FONT_DICT[fancy_font])
        return speech

    def _print_furnace_fun_speech(self):
        '''
        Prints the Furnace Fun speech to the console.
        '''
        speech_count:int = len(self._speech_dict[SPEECH_CONSTANTS.full_screen])
        for curr_speech_count in range(speech_count):
            curr_sprite = self._speech_dict[SPEECH_CONSTANTS.full_screen][curr_speech_count][SPEECH_CONSTANTS.sprite]
            sprite_translation:str = FURNACE_FUN_SPRITE_DICT[curr_sprite]
            curr_speech = self._speech_dict[SPEECH_CONSTANTS.full_screen][curr_speech_count][SPEECH_CONSTANTS.speech]
            curr_speech = self._translate_fancy_font(curr_speech)
            print(f"{SPEECH_CONSTANTS.full_screen}: {sprite_translation}: '{curr_speech}'")

    def _print_generic_speech(self):
        '''
        Prints the generic speech to the console.
        '''
        curr_section:str = SPEECH_CONSTANTS.top_section
        section_count:dict = {
            SPEECH_CONSTANTS.bottom_section: 0,
            SPEECH_CONSTANTS.top_section: 0,
        }
        bottom_section_count:int = len(self._speech_dict[SPEECH_CONSTANTS.bottom_section])
        top_section_count:int = len(self._speech_dict[SPEECH_CONSTANTS.top_section])
        while((section_count[SPEECH_CONSTANTS.bottom_section] < bottom_section_count)
              or (section_count[SPEECH_CONSTANTS.top_section] < top_section_count)):
            curr_section_count:int = section_count[curr_section]
            if(curr_section_count > len(self._speech_dict[curr_section])):
                break
            curr_sprite:int = self._speech_dict[curr_section][curr_section_count][SPEECH_CONSTANTS.sprite]
            sprite_translation:str = GENERAL_SPRITE_DICT[curr_sprite]
            curr_speech:str = self._speech_dict[curr_section][curr_section_count][SPEECH_CONSTANTS.speech]
            curr_speech = self._translate_fancy_font(curr_speech)
            print(f"{curr_section}:\t{sprite_translation}: '{curr_speech}'")
            section_count[curr_section] += 1
            if(curr_sprite in [0x04, 0x06]):
                if(curr_section == SPEECH_CONSTANTS.bottom_section):
                    curr_section = SPEECH_CONSTANTS.top_section
                elif(curr_section == SPEECH_CONSTANTS.top_section):
                    curr_section = SPEECH_CONSTANTS.bottom_section
    
    #############################
    ##### UTILITY FUNCTIONS #####
    #############################
    
    def find_speech_line(self,
            sprite_id:int=None, speech_str:str=None):
        '''
        Finds all instances of a sprite/speech combo
        and returns a list of the findings.
        '''
        found_speech_list:list = []
        for curr_section in self._speech_dict:
            for curr_section_count in self._speech_dict[curr_section]:
                viable_match:bool = True
                # Sprite
                curr_sprite:int = self._speech_dict[curr_section][curr_section_count][SPEECH_CONSTANTS.sprite]
                if(sprite_id and sprite_id != curr_sprite):
                    viable_match = False
                # Speech
                curr_speech:str = self._speech_dict[curr_section][curr_section_count][SPEECH_CONSTANTS.speech]
                if(speech_str and speech_str not in curr_speech):
                    viable_match = False
                # Record
                if(viable_match):
                    found_speech_list.append((curr_section, curr_section_count))
        return found_speech_list
    
    def verify_speech_functionality(self):
        '''
        Verifies that the speech dict is allowed.
        ToDo:
          * Character Limit
        '''
        for curr_section in self._speech_dict:
            for curr_section_count in self._speech_dict[curr_section]:
                curr_sprite:int = self._speech_dict[curr_section][curr_section_count][SPEECH_CONSTANTS.sprite]
                if(curr_sprite not in GENERAL_SPRITE_DICT):
                    return False
        return True

    ##########################
    ##### EDIT FUNCTIONS #####
    ##########################

    def modify_speech_line(self,
            section:str, section_count:int,
            new_sprite:int, new_speech:str):
        '''
        Replaces a speech line with a new sprite
        and speech string.
        '''
        self._speech_dict[section][section_count][SPEECH_CONSTANTS.sprite] = new_sprite
        self._speech_dict[section][section_count][SPEECH_CONSTANTS.speech] = new_speech
                    
    def append_speech_line(self,
            section:str,
            new_sprite:int, new_speech:str):
        '''
        Adds a speech line to the end of a section.
        '''
        section_count = len(self._speech_dict[section])
        self._speech_dict[section][section_count] = {
            SPEECH_CONSTANTS.sprite: new_sprite,
            SPEECH_CONSTANTS.speech: new_speech,
        }
                    
    def insert_speech_line(self,
            section:str, section_count:int,
            new_sprite:int, new_speech:str):
        '''
        Injects a speech line into a section, shifting
        everything after it backward by one.
        '''
        curr_section_count:int = len(self._speech_dict[section])
        while(curr_section_count > section_count):
            self._speech_dict[section][curr_section_count] = self._speech_dict[section][curr_section_count - 1]
            curr_section_count -= 1
        self._speech_dict[section][section_count][SPEECH_CONSTANTS.sprite] = new_sprite
        self._speech_dict[section][section_count][SPEECH_CONSTANTS.speech] = new_speech
                    
    def delete_speech_line(self,
            section:str, section_count:int):
        '''
        Removes a speech line from a section, shifting
        everything after it forward by one.
        '''
        last_section_count:int = len(self._speech_dict[section]) - 1
        while(section_count < last_section_count):
            self._speech_dict[section][section_count] = self._speech_dict[section][section_count + 1]
            section_count += 1
        del self._speech_dict[section][last_section_count]
    
    def replace_entire_speech_dict(self, new_speech_dict:dict):
        '''
        Replaces the speech dict with a custom one.
        '''
        self._speech_dict = new_speech_dict
    
    #################
    ##### WRITE #####
    #################
    
    def _write_furnace_fun_speech_file(self, new_content:bytearray):
        '''
        Writes a furnace fun speech in byte format.
        '''
        num_of_speeches:int = len(self._speech_dict[SPEECH_CONSTANTS.full_screen])
        new_content += num_of_speeches.to_bytes(1, 'big')
        for curr_section_count in sorted(self._speech_dict[SPEECH_CONSTANTS.full_screen]):
            curr_sprite:int = self._speech_dict[SPEECH_CONSTANTS.full_screen][curr_section_count][SPEECH_CONSTANTS.sprite]
            curr_speech:str = self._speech_dict[SPEECH_CONSTANTS.full_screen][curr_section_count][SPEECH_CONSTANTS.speech]
            speech_length:int = len(curr_speech) + 1
            new_content += \
                curr_sprite.to_bytes(1, 'big') + \
                speech_length.to_bytes(1, 'big') + \
                curr_speech.encode("latin-1") + b"\x00"
        return new_content

    def _write_generic_speech_file(self, new_content:bytearray):
        '''
        Writes a generic speech in byte format.
        '''
        for curr_section in [SPEECH_CONSTANTS.bottom_section, SPEECH_CONSTANTS.top_section]:
            curr_section_length:int = len(self._speech_dict[curr_section])
            new_content += curr_section_length.to_bytes(1, 'big')
            for curr_section_count in sorted(self._speech_dict[curr_section]):
                curr_sprite:int = self._speech_dict[curr_section][curr_section_count][SPEECH_CONSTANTS.sprite]
                curr_speech:str = self._speech_dict[curr_section][curr_section_count][SPEECH_CONSTANTS.speech]
                speech_length:int = len(curr_speech) + 1
                new_content += \
                    curr_sprite.to_bytes(1, 'big') + \
                    speech_length.to_bytes(1, 'big') + \
                    curr_speech.encode("latin-1") + b"\x00"
        return new_content

    ##########################
    ##### MAIN FUNCTIONS #####
    ##########################

    def read_speech_file(self):
        '''
        Reads the speech file and places contents
        in a dictionary.
        '''
        super()._read_file()
        self._speech_type:str = self._determine_speech_type()
        self._speech_dict:dict = {}
        if(self._speech_type in [SPEECH_CONSTANTS.furnace_fun_gruntilda_question,
                                 SPEECH_CONSTANTS.furnace_fun_other_question]):
            self._parse_furance_fun_speech()
        elif(self._speech_type == SPEECH_CONSTANTS.generic_speech):
            self._parse_generic_speech()
    
    def print_speech_file(self):
        '''
        Prints the speech file to the console.
        Attempts to display generic speeches
        in game-presenting order.
        '''
        if(self._speech_type in [SPEECH_CONSTANTS.furnace_fun_gruntilda_question,
                                 SPEECH_CONSTANTS.furnace_fun_other_question]):
            self._print_furnace_fun_speech()
        elif(self._speech_type == SPEECH_CONSTANTS.generic_speech):
            self._print_generic_speech()
    
    def save_speech_file(self, file_path:str|None=None):
        '''
        Writes the speech file in binary mode.
        '''
        if(self._speech_type == SPEECH_CONSTANTS.furnace_fun_gruntilda_question):
            header:int = 0x0103000500
            new_content:bytearray = header.to_bytes(5, 'big')
            new_content = self._write_furnace_fun_speech_file(new_content)
        if(self._speech_type == SPEECH_CONSTANTS.furnace_fun_other_question):
            header:int = 0x0101020500
            new_content:bytearray = header.to_bytes(5, 'big')
            new_content = self._write_furnace_fun_speech_file(new_content)
        elif(self._speech_type == SPEECH_CONSTANTS.generic_speech):
            header:int = 0x010300
            new_content:bytearray = header.to_bytes(3, 'big')
            new_content = self._write_generic_speech_file(new_content)
        self._file_content = new_content
        super()._save_changes(file_path)

################
##### MAIN #####
################

if __name__ == '__main__':
    file_dir:str = "C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/test2/"
    save_file_dir:str = "C:/Users/Cyrus/Documents/VS_Code/Banjo-Kazooie_Randomizer/Banjo-Kazooie_N64_Randomizer/randomizer/extracted_files/"
    # Generic
    print("Generic:")
    file_path:str = f"{file_dir}5C21F8.bin"
    speech_obj = Speech_Class(file_path)
    print(speech_obj._speech_dict)
    # speech_obj.print_speech_file()
    # print("~~~~~ SPACES ~~~~~")
    # print("~~~~~ SPACES ~~~~~")
    # print("~~~~~ SPACES ~~~~~")
    # speech_obj.modify_speech_line(SPEECH_CONSTANTS.bottom_section, 0, 0x90, "THIS IS A TEST OF THE EMERGENCY SAFETY PROTOCOL")
    # speech_obj.print_speech_file()
    # print("~~~~~ SPACES ~~~~~")
    # print("~~~~~ SPACES ~~~~~")
    # print("~~~~~ SPACES ~~~~~")
    # speech_obj.append_speech_line(SPEECH_CONSTANTS.bottom_section, 0x90, "DO NOT BE ALARMED!")
    # speech_obj.print_speech_file()
    # print("~~~~~ SPACES ~~~~~")
    # print("~~~~~ SPACES ~~~~~")
    # print("~~~~~ SPACES ~~~~~")
    # found_speech_list = speech_obj.find_speech_line(sprite_id=None, speech_str="EMERGENCY")
    # for (section, section_count) in found_speech_list:
    #     speech_obj.delete_speech_line(section, section_count)
    # speech_obj.print_speech_file()
    # speech_obj.save_speech_file(f"{save_file_dir}5C21F8.bin")
    # # Brentilda
    # print("\nBrentilda:")
    # file_path:str = f"{file_dir}5CFDC0.bin"
    # speech_obj = Speech_Class(file_path)
    # speech_obj.print_speech_file()
    # # Press A Or B
    # print("\nPress A Or B:")
    # file_path:str = f"{file_dir}5C4B28.bin"
    # speech_obj = Speech_Class(file_path)
    # speech_obj.print_speech_file()
    # # Camera Switch
    # print("\nCamera Switch:")
    # file_path:str = f"{file_dir}5CE8D8.bin"
    # speech_obj = Speech_Class(file_path)
    # speech_obj.print_speech_file()
    # # Non-Special Action
    # print("\nNon-Special Action:")
    # file_path:str = f"{file_dir}5C22E0.bin"
    # speech_obj = Speech_Class(file_path)
    # speech_obj.print_speech_file()
    # Special Action
    # print("\nSpecial Action:")
    # file_path:str = f"{file_dir}5C50B0.bin"
    # speech_obj = Speech_Class(file_path)
    # speech_obj.print_speech_file()
    # speech_obj.save_speech_file(f"{save_file_dir}5C50B0.bin")
    # # Furnace Fun Gruntilda Question
    # print("\nFurnace Fun Gruntilda Question:")
    # file_path:str = f"{file_dir}5D3228.bin"
    # speech_obj = Speech_Class(file_path)
    # speech_obj.print_speech_file()
    # speech_obj.save_speech_file(f"{save_file_dir}5D3228.bin")
    # # Furnace Fun Other Question
    # print("\nFurnace Fun Other Question:")
    # file_path:str = f"{file_dir}5D9348.bin"
    # speech_obj = Speech_Class(file_path)
    # speech_obj.print_speech_file()
    # speech_obj.save_speech_file(f"{save_file_dir}5D9348.bin")
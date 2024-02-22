'''
Purpose:
'''

###################
##### IMPORTS #####
###################

import os
import shutil
import pytest

from randomizer.game_assets.speeches.speech_class import Speech_Class

from randomizer.constants.variables.speech_variables import \
    GENERIC_SPEECH_STR, FURNACE_FUN_GRUNTILDA_QUESTION_STR, \
    FURNACE_FUN_OTHER_QUESTION_STR, FULL_SCREEN_STR, \
    TOP_SECTION_STR, BOTTOM_SECTION_STR, \
    SPRITE_STR, SPEECH_STR

######################
##### TEST CLASS #####
######################

class Test_Speech_Class():
    
    ### SETUP ###

    def setup_method(self):
        print("Setup Method")
        test_folder:str = "tests/test_files/game_assets/speeches/"
        self.original_generic_speech_file_path:str = f"{test_folder}original_generic_speech_bin_file.bin"
        self.duplicate_generic_speech_file_path:str = f"{test_folder}duplicate_generic_speech_bin_file.bin"
        self.original_furnace_fun_guntilda_speech_file_path:str = f"{test_folder}original_furnace_fun_gruntilda_speech_bin_file.bin"
        self.duplicate_furnace_fun_guntilda_speech_file_path:str = f"{test_folder}duplicate_furnace_fun_gruntilda_speech_bin_file.bin"
        self.original_furnace_fun_other_speech_file_path:str = f"{test_folder}original_furnace_fun_other_speech_bin_file.bin"
        self.duplicate_furnace_fun_other_speech_file_path:str = f"{test_folder}duplicate_furnace_fun_other_speech_bin_file.bin"
    
    ### READ ###

    @pytest.mark.parametrize(
            "section,section_count,expected_sprite,expected_speech",
            [
                (BOTTOM_SECTION_STR, 0, 0x87, "THIS IS GENERIC TEXT SO I DON'T GET SUED FOR PUBLISHING GAME ASSETS HAHAHA!"),
                (BOTTOM_SECTION_STR, 1, 0x06, ""),
                (BOTTOM_SECTION_STR, 2, 0x87, "YEAH IT WOULD HAVE SUCKED TO BE TRACKED DOWN FOR THIS."),
                (BOTTOM_SECTION_STR, 3, 0x04, ""),
                (TOP_SECTION_STR,    0, 0x06, ""),
                (TOP_SECTION_STR,    1, 0x82, "IT'S A GOOD THING I THOUGHT OF THIS"),
                (TOP_SECTION_STR,    2, 0x06, ""),
                (TOP_SECTION_STR,    3, 0x80, "THEY WILL NEVER FIND ME LOL!"),
                (TOP_SECTION_STR,    4, 0x04, ""),
            ]
        )
    def test_read_generic_speech_file(self,
            section:str, section_count:int,
            expected_sprite:int, expected_speech:str):
        speech_obj = Speech_Class(self.original_generic_speech_file_path)
        curr_sprite:int = speech_obj._speech_dict[section][section_count][SPRITE_STR]
        curr_speech:int = speech_obj._speech_dict[section][section_count][SPEECH_STR]
        assert (curr_sprite == expected_sprite) and (curr_speech == expected_speech)

    @pytest.mark.parametrize(
            "section,section_count,expected_sprite,expected_speech",
            [
                (FULL_SCREEN_STR, 0, 0x80, "YOU FART CAUSE YOU ATE ALL THE CHEESE"),
                (FULL_SCREEN_STR, 1, 0x80, "HOW MANY CHEESE CUBES DO YOU PLEASE...?"),
                (FULL_SCREEN_STR, 2, 0x81, "ýl69"),
                (FULL_SCREEN_STR, 3, 0x82, "ýl420"),
                (FULL_SCREEN_STR, 4, 0x83, "ýl21"),
            ]
        )
    def test_read_furnace_fun_gruntilda_speech_file(self,
            section:str, section_count:int,
            expected_sprite:int, expected_speech:str):
        speech_obj = Speech_Class(self.original_furnace_fun_guntilda_speech_file_path)
        curr_sprite:int = speech_obj._speech_dict[section][section_count][SPRITE_STR]
        curr_speech:int = speech_obj._speech_dict[section][section_count][SPEECH_STR]
        assert (curr_sprite == expected_sprite) and (curr_speech == expected_speech)

    @pytest.mark.parametrize(
            "section,section_count,expected_sprite,expected_speech",
            [
                (FULL_SCREEN_STR, 0, 0x80, "THIS SENTENCE RHYMES, I'M SMART,"),
                (FULL_SCREEN_STR, 1, 0x80, "HOW MANY TIMES DOES JIGGLY FART?"),
                (FULL_SCREEN_STR, 2, 0x81, "ýlALL DAY EVERY DAY BABY!!!!"),
                (FULL_SCREEN_STR, 3, 0x82, "ýlI HAVE NEVER FARTED IN MY LIFE"),
                (FULL_SCREEN_STR, 4, 0x83, "ýlWHEN I'M WITH THE BROOOOOOOS"),
            ]
        )
    def test_read_furnace_fun_other_speech_file(self,
            section:str, section_count:int,
            expected_sprite:int, expected_speech:str):
        speech_obj = Speech_Class(self.original_furnace_fun_other_speech_file_path)
        curr_sprite:int = speech_obj._speech_dict[section][section_count][SPRITE_STR]
        curr_speech:int = speech_obj._speech_dict[section][section_count][SPEECH_STR]
        assert (curr_sprite == expected_sprite) and (curr_speech == expected_speech)
    
    ### EDIT ###
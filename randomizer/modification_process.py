'''
Purpose:
* Class to run the functions that implement modifying the ROM

ToDo:
* Add more features
'''

###################
##### IMPORTS #####
###################

import json

from randomizer.patching.bk_rom_class import BK_ROM_CLASS
from randomizer.assembly.assembly import ASSEMBLY_CLASS
from randomizer.game_assets.game_assets_class import GAME_ASSET_CLASS
from randomizer.constants.str_values.string_constants import STRING_CONSTANTS as STR_CONST
from randomizer.settings_functions import SETTINGS_FUNCTIONS

######################################
##### MODIFICATION PROCESS CLASS #####
######################################

class MODIFICATION_PROCESS_CLASS(SETTINGS_FUNCTIONS):
    '''
    Class to run the functions that implement modifying the ROM
    '''
    def __init__(self):
        self._game_asset_obj = GAME_ASSET_CLASS()
        self._asm_obj = ASSEMBLY_CLASS()

    def _load_settings(self, settings_file:str):
        '''
        Sets hardcoded values to be passed as if
        selected settings from a user-interface.
        '''
        randomizer_dir:str = "randomizer/settings/"
        with open(randomizer_dir + settings_file) as json_file:
            self._settings_dict:dict = json.load(json_file)

    def _modification_setup(self):
        '''
        Extracts the assets and assembly files
        '''
        self._bk_rom = BK_ROM_CLASS(self._settings_dict[STR_CONST.rom_paths][STR_CONST.original_rom_path])
        self._bk_rom.extract_asset_table_pointers()
        self._bk_rom.extract_assembly_files()
    
    def _logic_process(self):
        '''
        Runs the functions for locations of items and starting moves
        '''
        pass

    def _apply_modifications(self):
        '''
        Runs through each setting and makes modifications to
        the assets and assembly files.
        '''
        print("INFO: _apply_modifications: Start...")
        # Always Run These
        self._asm_obj.disable_anti_tamper()
        self._asm_obj.patch_yum_yum_crash_fix()
        # Options
        self._starting_moves_and_inventory()
        self._alternate_win_conditions()
        self._note_doors()
        self._jigsaw_puzzles()
        self._transformations()
        self._furnace_fun()
        self._boot_to_file_select()
        self._skippable_cutscenes()
        self._skip_jiggy_jig()
        self._enable_fallproof()
        self._singular_inventory_item()
        # Save Asssembly Files
        self._asm_obj.save_all_assembly_changes()
        print("INFO: _apply_modifications: Complete!")
    
    def _modification_finalization(self):
        '''
        Appends asset files and inserts assembly files
        '''
        self._bk_rom.append_asset_table_pointers()
        self._bk_rom.insert_assembly_files()
        self._bk_rom.rename_bk_rom()
        self._bk_rom.calculate_new_crc()
        self._bk_rom.save_as_new_rom(self._settings_dict[STR_CONST.rom_paths][STR_CONST.new_rom_path])

    def _cleanup(self):
        '''
        Removes bin files from extraction folder
        '''
        self._bk_rom.clear_extracted_files_dir(STR_CONST.bin_extension)

    ################
    ##### MAIN #####
    ################

    def main(self):
        '''
        Runs through the entire process of extracting,
        modifying, and replacing files
        '''
        self._load_settings("testing.json")
        self._modification_setup()
        self._logic_process()
        self._apply_modifications()
        self._modification_finalization()
        # self._cleanup()
    
if __name__ == '__main__':
    modification_process_obj = MODIFICATION_PROCESS_CLASS()
    modification_process_obj.main()
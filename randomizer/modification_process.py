'''
Purpose:
* Class to run the functions that implement modifying the ROM

ToDo:
* Add more features
'''

###################
##### IMPORTS #####
###################

from randomizer.patching.bk_rom_class import BK_ROM_CLASS
from randomizer.assembly.assembly import ASSEMBLY_CLASS
from randomizer.contants.variables.patching_variables import BIN_EXTENSION
from randomizer.contants.enums.ability_enums import ABILITY_ENUMS

#####################
##### CONSTANTS #####
#####################

from randomizer.contants.variables.gui_variables import \
    ORIGINAL_ROM_PATH_STR, NEW_ROM_PATH_STR, \
    BOOT_TO_FILE_SELECT_STR, SKIPPABLE_CUTSCENES_STR, \
    STARTING_BLUE_EGG_COUNT_STR, STARTING_RED_FEATHER_COUNT_STR, \
    STARTING_GOLD_FEATHER_COUNT_STR, STARTING_MUMBO_TOKEN_COUNT_STR, \
    ENABLE_FALLPROOF_STR, \
    START_WITH_ALL_MOVES_STR

######################################
##### MODIFICATION PROCESS CLASS #####
######################################

class MODIFICATION_PROCESS_CLASS():
    '''
    Class to run the functions that implement modifying the ROM
    '''
    def __init__(self):
        pass

    def _hardcoded_settings(self):
        '''
        Sets hardcoded values to be passed as if
        selected settings from a user-interface.
        '''
        self._settings_dict:dict = {
            ORIGINAL_ROM_PATH_STR: "C:/Users/Cyrus/Documents/VS_Code/Banjo-Kazooie_Randomizer/Banjo-Kazooie_N64_Randomizer/Banjo-Kazooie.z64",
            NEW_ROM_PATH_STR: "C:/Users/Cyrus/Documents/VS_Code/Banjo-Kazooie_Randomizer/Banjo-Kazooie_N64_Randomizer/Banjo-Kazooie-TEST.z64",
            # Quality Of Life
            BOOT_TO_FILE_SELECT_STR: 1,
            SKIPPABLE_CUTSCENES_STR: 1,
            # Difficulty
            STARTING_BLUE_EGG_COUNT_STR: 69,
            STARTING_RED_FEATHER_COUNT_STR: 27,
            STARTING_GOLD_FEATHER_COUNT_STR: 4,
            STARTING_MUMBO_TOKEN_COUNT_STR: 5,
            ENABLE_FALLPROOF_STR: 1,
            # Logic
            START_WITH_ALL_MOVES_STR: 1,
        }

    def _modification_setup(self):
        '''
        Extracts the assets and assembly files
        '''
        self._bk_rom = BK_ROM_CLASS(self._settings_dict[ORIGINAL_ROM_PATH_STR])
        self._bk_rom.extract_asset_table_pointers()
        self._bk_rom.extract_assembly_files()
    
    def _logic_process(self):
        '''
        Runs the functions for locations of items and starting moves
        '''
        pass

    def _asset_modifications(self):
        '''
        Runs the functions for modifying asset files
        '''
        pass

    def _assembly_modifications(self):
        '''
        Runs the functions for modifying assembly files
        '''
        asm_obj = ASSEMBLY_CLASS()
        asm_obj.disable_anti_tamper()
        asm_obj.patch_yum_yum_crash_fix()
        if(self._settings_dict[BOOT_TO_FILE_SELECT_STR]):
            asm_obj.boot_to_file_select()
        if(self._settings_dict[SKIPPABLE_CUTSCENES_STR]):
            asm_obj.skippable_cutscenes()
        if(self._settings_dict[START_WITH_ALL_MOVES_STR]):
            ability_enum_list:list = [
                ABILITY_ENUMS.beak_barge,
                ABILITY_ENUMS.climb,
                ABILITY_ENUMS.flap_flip,
                ABILITY_ENUMS.talon_trot,
                ABILITY_ENUMS.egg_firing,
                ABILITY_ENUMS.flight,
                ABILITY_ENUMS.wonderwing,
                ]
            asm_obj.bottles_tutorial_moves(
                ability_enum_list,
                self._settings_dict[STARTING_BLUE_EGG_COUNT_STR],
                self._settings_dict[STARTING_RED_FEATHER_COUNT_STR],
                self._settings_dict[STARTING_GOLD_FEATHER_COUNT_STR],
                self._settings_dict[STARTING_MUMBO_TOKEN_COUNT_STR]
                )
        else:
            asm_obj.starting_inventory_counts(
                self._settings_dict[STARTING_BLUE_EGG_COUNT_STR],
                self._settings_dict[STARTING_RED_FEATHER_COUNT_STR],
                self._settings_dict[STARTING_GOLD_FEATHER_COUNT_STR]
                )
        if(self._settings_dict[ENABLE_FALLPROOF_STR]):
            asm_obj.enable_fallproof()
        asm_obj.save_all_assembly_changes()
    
    def _modification_finalization(self):
        '''
        Appends asset files and inserts assembly files
        '''
        self._bk_rom.append_asset_table_pointers()
        self._bk_rom.insert_assembly_files()
        self._bk_rom.rename_bk_rom()
        self._bk_rom.calculate_new_crc()
        self._bk_rom.save_as_new_rom(self._settings_dict[NEW_ROM_PATH_STR])

    def _cleanup(self):
        '''
        Removes bin files from extraction folder
        '''
        self._bk_rom.clear_extracted_files_dir(BIN_EXTENSION)

    ################
    ##### MAIN #####
    ################

    def main(self):
        '''
        Runs through the entire process of extracting,
        modifying, and replacing files
        '''
        self._hardcoded_settings()
        self._modification_setup()
        self._logic_process()
        self._asset_modifications()
        self._assembly_modifications()
        self._modification_finalization()
        self._cleanup()
    
if __name__ == '__main__':
    modification_process_obj = MODIFICATION_PROCESS_CLASS()
    modification_process_obj.main()
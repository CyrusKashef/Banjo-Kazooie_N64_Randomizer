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
from randomizer.contants.dicts.gui_move_dict import GUI_MOVE_ENUM_DICT

#####################
##### CONSTANTS #####
#####################

from randomizer.contants.variables.gui_variables import \
    ORIGINAL_ROM_PATH_STR, NEW_ROM_PATH_STR, \
    BOOT_TO_FILE_SELECT_STR, SKIPPABLE_CUTSCENES_STR, \
    SKIP_JIGGY_JIG_STR, \
    STARTING_BLUE_EGG_COUNT_STR, STARTING_RED_FEATHER_COUNT_STR, \
    STARTING_GOLD_FEATHER_COUNT_STR, STARTING_MUMBO_TOKEN_COUNT_STR, \
    ENABLE_FALLPROOF_STR, \
    SELECT_STARTING_MOVES_STR, BEAK_BARGE_STR, BEAK_BOMB_STR, \
    BEAK_BUSTER_STR, CLAW_SWIPE_STR, CLIMB_STR, \
    EGG_FIRING_STR, FEATHERY_FLAP_STR, FLAP_FLIP_STR, \
    FLIGHT_STR, HIGH_JUMP_STR, RAT_A_TAP_RAP_STR, \
    ROLL_STR, SHOCK_JUMP_STR, STILT_STRIDE_STR, \
    DIVE_STR, TALON_TROT_STR, TURBO_TALON_TROT_STR, \
    WONDERWING_STR, NOTE_DOOR_STR, \
    SHOCK_JUMP_PAD_ANYWHERE_STR, \
    LOW_POLY_MODEL_STR, HIGH_POLY_MODEL_STR

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
            SKIP_JIGGY_JIG_STR: 1,
            # Difficulty
            STARTING_BLUE_EGG_COUNT_STR: 0,
            STARTING_RED_FEATHER_COUNT_STR: 0,
            STARTING_GOLD_FEATHER_COUNT_STR: 0,
            STARTING_MUMBO_TOKEN_COUNT_STR: 0,
            ENABLE_FALLPROOF_STR: 0,
            # Logic
            SELECT_STARTING_MOVES_STR: 0,
            BEAK_BARGE_STR: 1,
            BEAK_BARGE_STR: 1,
            BEAK_BOMB_STR: 1,
            BEAK_BUSTER_STR: 1,
            CLAW_SWIPE_STR: 1,
            CLIMB_STR: 1,
            EGG_FIRING_STR: 1,
            FEATHERY_FLAP_STR: 1,
            FLAP_FLIP_STR: 1,
            FLIGHT_STR: 1,
            HIGH_JUMP_STR: 1,
            RAT_A_TAP_RAP_STR: 1,
            ROLL_STR: 1,
            SHOCK_JUMP_STR: 1,
            STILT_STRIDE_STR: 1,
            DIVE_STR: 1,
            TALON_TROT_STR: 1,
            TURBO_TALON_TROT_STR: 1,
            WONDERWING_STR: 1,
            NOTE_DOOR_STR: 1,
            SHOCK_JUMP_PAD_ANYWHERE_STR: 0,
            # COSMETICS & SOUNDS
            LOW_POLY_MODEL_STR: 0x34D,
            HIGH_POLY_MODEL_STR: 0x34E,
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
        # Boot To File Select
        if(self._settings_dict[BOOT_TO_FILE_SELECT_STR]):
            asm_obj.boot_to_file_select()
        # Skippable Cutscenes
        if(self._settings_dict[SKIPPABLE_CUTSCENES_STR]):
            asm_obj.skippable_cutscenes()
        # Skip Jiggy Jig
        if(self._settings_dict[SKIP_JIGGY_JIG_STR]):
            asm_obj.skip_jiggy_jig()
        # Starting Moves/Inventory
        if(self._settings_dict[SELECT_STARTING_MOVES_STR]):
            ability_enum_list:list = [ABILITY_ENUMS.camera_control]
            for move_variable in GUI_MOVE_ENUM_DICT:
                if(self._settings_dict[move_variable]):
                    ability_enum_list.append(GUI_MOVE_ENUM_DICT[move_variable])
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
        # Shock Jump Pad Anywhere
        if(self._settings_dict[SHOCK_JUMP_PAD_ANYWHERE_STR]):
            asm_obj.shock_jump_pad_anywhere()
        # Fallproof
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
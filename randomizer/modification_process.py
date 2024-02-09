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
from randomizer.game_assets.game_assets_class import GAME_ASSET_CLASS
from randomizer.contants.variables.patching_variables import BIN_EXTENSION
from randomizer.contants.int_enums.ability_enums import ABILITY_ENUMS
from randomizer.contants.dicts.gui_move_dict import GUI_MOVE_ENUM_DICT
from randomizer.contants.dicts.win_condition_dict import SAMPLE_WIN_CONDITIONS_DICT
from randomizer.contants.variables.win_condition_variables import \
    ALL_JINJOS_STR, TROTLESS_STR

from randomizer.contants.str_enums.gui_selections import GUI_SELECTIONS

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
            GUI_SELECTIONS.original_rom_path: "C:/Users/Cyrus/Documents/VS_Code/Banjo-Kazooie_Randomizer/Banjo-Kazooie_N64_Randomizer/Banjo-Kazooie.z64",
            GUI_SELECTIONS.new_rom_path: "C:/Users/Cyrus/Documents/VS_Code/Banjo-Kazooie_Randomizer/Banjo-Kazooie_N64_Randomizer/Banjo-Kazooie-TEST.z64",
            #######################
            ### Quality Of Life ###
            #######################
            GUI_SELECTIONS.boot_to_file_select: 1,
            GUI_SELECTIONS.skippable_cutscenes: 1,
            GUI_SELECTIONS.skip_jiggy_jig: 1,
            ##################
            ### Difficulty ###
            ##################
            GUI_SELECTIONS.starting_blue_egg_count: 69,
            GUI_SELECTIONS.starting_red_feather_count: 42,
            GUI_SELECTIONS.starting_gold_feather_count: 9,
            GUI_SELECTIONS.starting_mumbo_token_count: 21,
            GUI_SELECTIONS.enable_fallproof: 1,
            #############
            ### Logic ###
            #############
            # Starting Moves
            GUI_SELECTIONS.select_starting_moves: 1,
            GUI_SELECTIONS.beak_barge: 1,
            GUI_SELECTIONS.beak_bomb: 1,
            GUI_SELECTIONS.beak_buster: 1,
            GUI_SELECTIONS.claw_swipe: 1,
            GUI_SELECTIONS.climb: 1,
            GUI_SELECTIONS.egg_firing: 1,
            GUI_SELECTIONS.feather_flap: 1,
            GUI_SELECTIONS.flap_flip: 1,
            GUI_SELECTIONS.flight: 1,
            GUI_SELECTIONS.high_jump: 1,
            GUI_SELECTIONS.rat_a_tap_rap: 1,
            GUI_SELECTIONS.roll_attack: 1,
            GUI_SELECTIONS.shock_jump: 1,
            GUI_SELECTIONS.stilt_stride: 1,
            GUI_SELECTIONS.dive: 1,
            GUI_SELECTIONS.talon_trot: 1,
            GUI_SELECTIONS.turbo_talon_trot: 1,
            GUI_SELECTIONS.wonderwing: 1,
            GUI_SELECTIONS.open_note_door: 1,
            GUI_SELECTIONS.shock_jump_pad_anywhere: 0,
            # Win Condition
            GUI_SELECTIONS.alternate_win_condition: TROTLESS_STR,
            # Note Doors
            GUI_SELECTIONS.note_door_50_cost: 0,
            GUI_SELECTIONS.note_door_180_cost: 0,
            GUI_SELECTIONS.note_door_260_cost: 0,
            GUI_SELECTIONS.note_door_350_cost: 0,
            GUI_SELECTIONS.note_door_450_cost: 0,
            GUI_SELECTIONS.note_door_640_cost: 0,
            GUI_SELECTIONS.note_door_765_cost: 0,
            GUI_SELECTIONS.note_door_810_cost: 0,
            GUI_SELECTIONS.note_door_828_cost: 0,
            GUI_SELECTIONS.note_door_846_cost: 0,
            GUI_SELECTIONS.note_door_864_cost: 0,
            GUI_SELECTIONS.note_door_882_cost: 0,
            # Jigsaw Puzzles
            GUI_SELECTIONS.jigsaw_puzzle_1_cost: 0,
            GUI_SELECTIONS.jigsaw_puzzle_2_cost: 0,
            GUI_SELECTIONS.jigsaw_puzzle_3_cost: 0,
            GUI_SELECTIONS.jigsaw_puzzle_4_cost: 0,
            GUI_SELECTIONS.jigsaw_puzzle_5_cost: 0,
            GUI_SELECTIONS.jigsaw_puzzle_6_cost: 0,
            GUI_SELECTIONS.jigsaw_puzzle_7_cost: 0,
            GUI_SELECTIONS.jigsaw_puzzle_8_cost: 0,
            GUI_SELECTIONS.jigsaw_puzzle_9_cost: 0,
            GUI_SELECTIONS.jigsaw_puzzle_10_cost: 0,
            GUI_SELECTIONS.jigsaw_puzzle_11_cost: 0,
            ##########################
            ### COSMETICS & SOUNDS ###
            ##########################
            GUI_SELECTIONS.low_poly_model: 0x34D,
            GUI_SELECTIONS.high_poly_model: 0x34E,
        }

    def _modification_setup(self):
        '''
        Extracts the assets and assembly files
        '''
        self._bk_rom = BK_ROM_CLASS(self._settings_dict[GUI_SELECTIONS.original_rom_path])
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
        print("INFO: _asset_modifications: Start...")
        game_asset_obj = GAME_ASSET_CLASS()
        game_asset_obj.reverse_all_speech_texts()
        # game_asset_obj.add_topper_to_spiral_mountain()
        # game_asset_obj.add_note_to_spiral_mountain()
        # game_asset_obj.log_all_complex_objects()
        print("INFO: _asset_modifications: Complete!")

    def _assembly_modifications(self):
        '''
        Runs the functions for modifying assembly files
        '''
        asm_obj = ASSEMBLY_CLASS()
        asm_obj.disable_anti_tamper()
        asm_obj.patch_yum_yum_crash_fix()
        asm_obj.chinker_stop_spinning()
        # Boot To File Select
        if(self._settings_dict[GUI_SELECTIONS.boot_to_file_select]):
            asm_obj.boot_to_file_select()
        # Skippable Cutscenes
        if(self._settings_dict[GUI_SELECTIONS.skippable_cutscenes]):
            asm_obj.skippable_cutscenes()
        # Skip Jiggy Jig
        if(self._settings_dict[GUI_SELECTIONS.skip_jiggy_jig]):
            asm_obj.skip_jiggy_jig()
        # Starting Moves/Inventory
        if(self._settings_dict[GUI_SELECTIONS.select_starting_moves]):
            ability_enum_list:list = [ABILITY_ENUMS.camera_control]
            for move_variable in GUI_MOVE_ENUM_DICT:
                if(self._settings_dict[move_variable]):
                    ability_enum_list.append(GUI_MOVE_ENUM_DICT[move_variable])
            asm_obj.bottles_tutorial_moves(
                ability_enum_list,
                self._settings_dict[GUI_SELECTIONS.starting_blue_egg_count],
                self._settings_dict[GUI_SELECTIONS.starting_red_feather_count],
                self._settings_dict[GUI_SELECTIONS.starting_gold_feather_count],
                self._settings_dict[GUI_SELECTIONS.starting_mumbo_token_count]
                )
        else:
            asm_obj.starting_inventory_counts(
                self._settings_dict[GUI_SELECTIONS.starting_blue_egg_count],
                self._settings_dict[GUI_SELECTIONS.starting_red_feather_count],
                self._settings_dict[GUI_SELECTIONS.starting_gold_feather_count]
                )
        # Alternate Win Condition
        alternate_win_condition:str = self._settings_dict[GUI_SELECTIONS.alternate_win_condition]
        if(alternate_win_condition != ""):
            possible_win_condition_list:list = SAMPLE_WIN_CONDITIONS_DICT[alternate_win_condition]
            asm_obj.set_alternate_win_conditions(possible_win_condition_list)
        # Note Doors
        asm_obj.set_note_door_values(note_door_list=[
            self._settings_dict[GUI_SELECTIONS.note_door_50_cost],
            self._settings_dict[GUI_SELECTIONS.note_door_180_cost],
            self._settings_dict[GUI_SELECTIONS.note_door_260_cost],
            self._settings_dict[GUI_SELECTIONS.note_door_350_cost],
            self._settings_dict[GUI_SELECTIONS.note_door_450_cost],
            self._settings_dict[GUI_SELECTIONS.note_door_640_cost],
            self._settings_dict[GUI_SELECTIONS.note_door_765_cost],
            self._settings_dict[GUI_SELECTIONS.note_door_810_cost],
            self._settings_dict[GUI_SELECTIONS.note_door_828_cost],
            self._settings_dict[GUI_SELECTIONS.note_door_846_cost],
            self._settings_dict[GUI_SELECTIONS.note_door_864_cost],
            self._settings_dict[GUI_SELECTIONS.note_door_882_cost]
        ])
        # Jigsaw Puzzles
        asm_obj.set_jigsaw_puzzle_costs(jigsaw_puzzle_list=[
            self._settings_dict[GUI_SELECTIONS.jigsaw_puzzle_1_cost],
            self._settings_dict[GUI_SELECTIONS.jigsaw_puzzle_2_cost],
            self._settings_dict[GUI_SELECTIONS.jigsaw_puzzle_3_cost],
            self._settings_dict[GUI_SELECTIONS.jigsaw_puzzle_4_cost],
            self._settings_dict[GUI_SELECTIONS.jigsaw_puzzle_5_cost],
            self._settings_dict[GUI_SELECTIONS.jigsaw_puzzle_6_cost],
            self._settings_dict[GUI_SELECTIONS.jigsaw_puzzle_7_cost],
            self._settings_dict[GUI_SELECTIONS.jigsaw_puzzle_8_cost],
            self._settings_dict[GUI_SELECTIONS.jigsaw_puzzle_9_cost],
            self._settings_dict[GUI_SELECTIONS.jigsaw_puzzle_10_cost],
            self._settings_dict[GUI_SELECTIONS.jigsaw_puzzle_11_cost]
        ])
        # Shock Jump Pad Anywhere
        if(self._settings_dict[GUI_SELECTIONS.shock_jump_pad_anywhere]):
            asm_obj.shock_jump_pad_anywhere()
        # Fallproof
        if(self._settings_dict[GUI_SELECTIONS.enable_fallproof]):
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
        self._bk_rom.save_as_new_rom(self._settings_dict[GUI_SELECTIONS.new_rom_path])

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
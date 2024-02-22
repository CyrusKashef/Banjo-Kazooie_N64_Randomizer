##################
##### IMPORT #####
##################

import random

### CLASSES

from randomizer.assembly.assembly import ASSEMBLY_CLASS
from randomizer.game_assets.game_assets_class import GAME_ASSET_CLASS
from randomizer.assembly.assembly import ASSEMBLY_CLASS
from randomizer.game_assets.game_assets_class import GAME_ASSET_CLASS

### CONSTANTS

from randomizer.constants.str_values.string_constants import STRING_CONSTANTS as STR_CONST
from randomizer.constants.dict_values.dict_constants import DICT_CONSTANTS as DICT_CONST

### DICTS

from randomizer.constants.dict_values.win_condition_dict import SAMPLE_WIN_CONDITIONS_DICT

### ENUMS

from randomizer.constants.int_values.ability_enums import ABILITY_ENUMS

##############################
##### SETTINGS FUNCTIONS #####
##############################

class SETTINGS_FUNCTIONS():
    '''
    Pass
    '''
    def __init__(self):
        self._game_asset_obj = GAME_ASSET_CLASS()
        self._asm_obj = ASSEMBLY_CLASS()
    
    ###############################################
    ##### STARTING MOVES AND INVENTORY COUNTS #####
    ###############################################
    
    def _starting_moves_and_inventory(self):
        '''
        Pass
        '''
        ability_enum_list:list = [ABILITY_ENUMS.camera_control]
        for move_variable in DICT_CONST.gui_move_enum_dict:
            if(self._settings_dict[STR_CONST.select_starting_moves][move_variable]):
                ability_enum_list.append(DICT_CONST.gui_move_enum_dict[move_variable])
        self._asm_obj.bottles_tutorial_moves(
            ability_enum_list,
            self._settings_dict[STR_CONST.starting_inventory_counts][STR_CONST.starting_blue_egg_count],
            self._settings_dict[STR_CONST.starting_inventory_counts][STR_CONST.starting_red_feather_count],
            self._settings_dict[STR_CONST.starting_inventory_counts][STR_CONST.starting_gold_feather_count],
            self._settings_dict[STR_CONST.starting_inventory_counts][STR_CONST.starting_mumbo_token_count]
            )

    ###################################
    ##### ALTERNATE WIN CONDITION #####
    ###################################
    
    def _alternate_win_conditions(self):
        '''
        Pass
        '''
        alternate_win_conditions_option_list:list = []
        alternate_win_conditions_option_dict:dict = \
            self._settings_dict[STR_CONST.alternate_win_condition]
        for alternate_win_conditions_option in alternate_win_conditions_option_dict:
            if(alternate_win_conditions_option_dict[alternate_win_conditions_option]):
                alternate_win_conditions_option_list.append(alternate_win_conditions_option)
        if(alternate_win_conditions_option_list == []):
            return
        print(f"INFO: {STR_CONST.alternate_win_condition}")
        alternate_win_conditions_choice:str = random.choice(alternate_win_conditions_option_list)
        print(f"INFO: {STR_CONST.alternate_win_conditions_choice}")
        possible_win_condition_list:list = SAMPLE_WIN_CONDITIONS_DICT[alternate_win_conditions_choice]
        self._asm_obj.set_alternate_win_conditions(possible_win_condition_list)

    ###########################
    ##### NOTE DOOR COSTS #####
    ###########################

    def _note_door_item_requirement(self, note_door_item_requirement_dict:dict):
        '''
        Pass
        '''
        # Adjust Assembly
        # Adjust Object Model Asset
        pass

    def _note_door_costs(self, note_door_costs_dict:dict):
        '''
        Pass
        '''
        # Adjust Assembly
        self._asm_obj.set_note_door_values(note_door_list=[
            note_door_costs_dict[STR_CONST.note_door_50_cost],
            note_door_costs_dict[STR_CONST.note_door_180_cost],
            note_door_costs_dict[STR_CONST.note_door_260_cost],
            note_door_costs_dict[STR_CONST.note_door_350_cost],
            note_door_costs_dict[STR_CONST.note_door_450_cost],
            note_door_costs_dict[STR_CONST.note_door_640_cost],
            note_door_costs_dict[STR_CONST.note_door_765_cost],
            note_door_costs_dict[STR_CONST.note_door_810_cost],
            note_door_costs_dict[STR_CONST.note_door_828_cost],
            note_door_costs_dict[STR_CONST.note_door_846_cost],
            note_door_costs_dict[STR_CONST.note_door_864_cost],
            note_door_costs_dict[STR_CONST.note_door_882_cost]
        ])
        # Adjust Object Model Asset

    def _note_doors(self):
        '''
        Pass
        '''
        print(f"INFO: {STR_CONST.note_doors}")
        note_door_dict:dict = self._settings_dict[STR_CONST.note_doors]
        # Item Requirement
        note_door_item_requirement_dict:dict = note_door_dict[STR_CONST.note_door_item_requirement]
        self._note_door_item_requirement(note_door_item_requirement_dict)
        # Costs
        note_door_costs_dict:dict = note_door_dict[STR_CONST.note_door_costs]
        self._note_door_costs(note_door_costs_dict)

    ###############################
    ##### JIGSAW PUZZLE COSTS #####
    ###############################

    def _jigsaw_puzzle_item_requirement(self, jigsaw_puzzle_item_requirement_dict:dict):
        '''
        Pass
        '''
        # Adjust Assembly
        # Adjust Speech Assets
        pass

    def _jigsaw_puzzle_costs(self, jigsaw_puzzle_costs_dict:dict):
        '''
        Pass
        '''
        # Adjust Assembly
        self._asm_obj.set_jigsaw_puzzle_costs(jigsaw_puzzle_list=[
            jigsaw_puzzle_costs_dict[STR_CONST.mumbos_mountain_puzzle_cost],
            jigsaw_puzzle_costs_dict[STR_CONST.treasure_trove_cove_puzzle_cost],
            jigsaw_puzzle_costs_dict[STR_CONST.clankers_cavern_puzzle_cost],
            jigsaw_puzzle_costs_dict[STR_CONST.bubblegloop_swamp_puzzle_cost],
            jigsaw_puzzle_costs_dict[STR_CONST.freezeezy_peak_puzzle_cost],
            jigsaw_puzzle_costs_dict[STR_CONST.gobis_valley_puzzle_cost],
            jigsaw_puzzle_costs_dict[STR_CONST.mad_monster_mansion_puzzle_cost],
            jigsaw_puzzle_costs_dict[STR_CONST.rusty_bucket_bay_puzzle_cost],
            jigsaw_puzzle_costs_dict[STR_CONST.click_clock_wood_puzzle_cost],
            jigsaw_puzzle_costs_dict[STR_CONST.final_battle_puzzle_cost],
            jigsaw_puzzle_costs_dict[STR_CONST.double_health_puzzle_cost]
        ])

    def _jigsaw_puzzles(self):
        '''
        Pass
        '''
        print(f"INFO: {STR_CONST.jigsaw_puzzles}")
        jigsaw_puzzle_dict:dict = self._settings_dict[STR_CONST.jigsaw_puzzles]
        # Item Requirement
        jigsaw_puzzle_item_requirement_dict:dict = jigsaw_puzzle_dict[STR_CONST.jigsaw_puzzle_item_requirement]
        self._jigsaw_puzzle_item_requirement(jigsaw_puzzle_item_requirement_dict)
        # Costs
        jigsaw_puzzle_costs_dict:dict = jigsaw_puzzle_dict[STR_CONST.jigsaw_puzzle_costs]
        self._jigsaw_puzzle_costs(jigsaw_puzzle_costs_dict)
    
    ################################
    ##### TRANSFORMATION COSTS #####
    ################################

    def _transformation_item_requirement(self, transformation_item_requirement_dict:dict):
        '''
        Pass
        '''
        # Adjust Assembly
        # Adjust Speech Assets
        pass

    def _transformation_costs(self, transformation_costs_dict:dict):
        '''
        Pass
        '''
        # Adjust Assembly
        pass

    def _transformations(self):
        '''
        Pass
        '''
        print(f"INFO: {STR_CONST.transformations}")
        transformation_dict:dict = self._settings_dict[STR_CONST.transformations]
        # Item Requirement
        transformation_item_requirement_dict:dict = transformation_dict[STR_CONST.transformation_item_requirement]
        self._transformation_item_requirement(transformation_item_requirement_dict)
        # Costs
        transformation_costs_dict:dict = transformation_dict[STR_CONST.transformation_costs]
        self._transformation_costs(transformation_costs_dict)

    #######################
    ##### FURNACE FUN #####
    #######################

    def _geoguesser(self):
        '''
        Pass
        '''
        self._game_asset_obj.geoguesser_speech_files()
        self._game_asset_obj.geoguesser_map_setup_files()
        self._asm_obj.geoguesser_furnace_fun()
    
    def _death_squares_only(self):
        '''
        Pass
        '''
        pass
    
    def _furnace_fun(self):
        '''
        Pass
        '''
        furnace_fun_option_list:list = []
        furnace_fun_options_dict:dict = \
            self._settings_dict[STR_CONST.furnace_fun]
        for furnace_fun_option in furnace_fun_options_dict:
            if(furnace_fun_options_dict[furnace_fun_option]):
                furnace_fun_option_list.append(furnace_fun_option)
        if(furnace_fun_option == []):
            return
        print(f"INFO: {STR_CONST.furnace_fun}")
        furnace_fun_choice:str = random.choice(furnace_fun_option_list)
        if(furnace_fun_choice == STR_CONST.geoguesser):
            print(f"INFO: {STR_CONST.geoguesser}")
            self._geoguesser()
        elif(furnace_fun_choice == STR_CONST.death_squares_only):
            print(f"INFO: {STR_CONST.death_squares_only}")
            self._death_squares_only()
    
    #########################
    ##### OTHER OPTIONS #####
    #########################
    
    def _boot_to_file_select(self):
        '''
        Pass
        '''
        boot_to_file_select_bool:bool = \
            self._settings_dict[STR_CONST.other_options][STR_CONST.boot_to_file_select]
        if(boot_to_file_select_bool):
            print(f"INFO: {STR_CONST.boot_to_file_select}")
            self._asm_obj.boot_to_file_select()
    
    def _skippable_cutscenes(self):
        '''
        Pass
        '''
        skippable_cutscenes_bool:bool = \
            self._settings_dict[STR_CONST.other_options][STR_CONST.skippable_cutscenes]
        if(skippable_cutscenes_bool):
            print(f"INFO: {STR_CONST.skippable_cutscenes}")
            self._asm_obj.skippable_cutscenes()
    
    def _skip_jiggy_jig(self):
        '''
        Pass
        '''
        skip_jiggy_jig_bool:bool = \
            self._settings_dict[STR_CONST.other_options][STR_CONST.skip_jiggy_jig]
        if(skip_jiggy_jig_bool):
            print(f"INFO: {STR_CONST.skip_jiggy_jig}")
            self._asm_obj.skip_jiggy_jig()
    
    def _enable_fallproof(self):
        '''
        Pass
        '''
        enable_fallproof_bool:bool = \
            self._settings_dict[STR_CONST.other_options][STR_CONST.enable_fallproof]
        if(enable_fallproof_bool):
            print(f"INFO: {STR_CONST.enable_fallproof}")
            self._asm_obj.enable_fallproof()
    
    def _shock_jump_pad_anywhere(self):
        '''
        Pass
        '''
        shock_jump_pad_anywhere_bool:bool = \
            self._settings_dict[STR_CONST.other_options][STR_CONST.shock_jump_pad_anywhere]
        if(shock_jump_pad_anywhere_bool):
            print(f"INFO: {STR_CONST.shock_jump_pad_anywhere}")
            self._asm_obj.shock_jump_pad_anywhere()
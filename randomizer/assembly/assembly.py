'''
Purpose:
*
'''

###################
##### IMPORTS #####
###################

import pandas as pd
from IPython.display import display, HTML

from randomizer.assembly.c_libraries.c_libraries_code import C_LIBRARIES_CODE_CLASS
from randomizer.assembly.c_libraries.c_libraries_data import C_LIBRARIES_DATA_CLASS
from randomizer.assembly.game_engine.game_engine_code import GAME_ENGINE_CODE_CLASS
from randomizer.assembly.game_engine.game_engine_data import GAME_ENGINE_DATA_CLASS
from randomizer.assembly.spiral_mountain.spiral_mountain_code import SPIRAL_MOUNTAIN_CODE_CLASS
from randomizer.assembly.spiral_mountain.spiral_mountain_data import SPIRAL_MOUNTAIN_DATA_CLASS
from randomizer.assembly.mumbos_mountain.mumbos_mountain_code import MUMBOS_MOUNTAIN_CODE_CLASS
from randomizer.assembly.mumbos_mountain.mumbos_mountain_data import MUMBOS_MOUNTAIN_DATA_CLASS
from randomizer.assembly.treasure_trove_cove.treasure_trove_cove_code import TREASURE_TROVE_COVE_CODE_CLASS
from randomizer.assembly.treasure_trove_cove.treasure_trove_cove_data import TREASURE_TROVE_COVE_DATA_CLASS
from randomizer.assembly.clankers_cavern.clankers_cavern_code import CLANKERS_CAVERN_CODE_CLASS
from randomizer.assembly.clankers_cavern.clankers_cavern_data import CLANKERS_CAVERN_DATA_CLASS
from randomizer.assembly.bubblegloop_swamp.bubblegloop_swamp_code import BUBBLEGLOOP_SWAMP_CODE_CLASS
from randomizer.assembly.bubblegloop_swamp.bubblegloop_swamp_data import BUBBLEGLOOP_SWAMP_DATA_CLASS
from randomizer.assembly.freezeezy_peak.freezeezy_peak_code import FREEZEEZY_PEAK_CODE_CLASS
from randomizer.assembly.freezeezy_peak.freezeezy_peak_data import FREEZEEZY_PEAK_DATA_CLASS
from randomizer.assembly.gobis_valley.gobis_valley_code import GOBIS_VALLEY_CODE_CLASS
from randomizer.assembly.gobis_valley.gobis_valley_data import GOBIS_VALLEY_DATA_CLASS
from randomizer.assembly.mad_monster_mansion.mad_monster_mansion_code import MAD_MONSTER_MANSION_CODE_CLASS
from randomizer.assembly.mad_monster_mansion.mad_monster_mansion_data import MAD_MONSTER_MANSION_DATA_CLASS
from randomizer.assembly.rusty_bucket_bay.rusty_bucket_bay_code import RUSTY_BUCKET_BAY_CODE_CLASS
from randomizer.assembly.rusty_bucket_bay.rusty_bucket_bay_data import RUSTY_BUCKET_BAY_DATA_CLASS
from randomizer.assembly.click_clock_wood.click_clock_wood_code import CLICK_CLOCK_WOOD_CODE_CLASS
from randomizer.assembly.click_clock_wood.click_clode_wood_data import CLICK_CLOCK_WOOD_DATA_CLASS
from randomizer.assembly.gruntildas_lair.gruntildas_lair_code import GRUNTILDAS_LAIR_CODE_CLASS
from randomizer.assembly.gruntildas_lair.gruntildas_lair_data import GRUNTILDAS_LAIR_DATA_CLASS
from randomizer.assembly.final_battle.final_battle_code import FINAL_BATTLE_CODE_CLASS
from randomizer.assembly.final_battle.final_battle_data import FINAL_BATTLE_DATA_CLASS
from randomizer.assembly.cutscenes.cutscenes_code import CUTSCENES_CODE_CLASS
from randomizer.assembly.cutscenes.cutscenes_data import CUTSCENES_DATA_CLASS

from randomizer.constants.int_values.jiggy_enums import JIGGY_ENUMS
from randomizer.constants.int_values.empty_honeycomb_enums import EMPTY_HONEYCOMB_ENUMS
from randomizer.constants.str_values.string_constants import STRING_CONSTANTS as STR_CONST
# from randomizer.constants.dict_values.win_condition_dict import \
#     WIN_CONDITION_FUNCTION_DICT, WIN_CONDITION_COMMANDS_DICT

from randomizer.constants.int_values.map_enums import MAP_ENUMS
from randomizer.constants.dict_values.warp_entry_dict import WARP_ENTRY_DICT
from randomizer.constants.int_values.furnace_fun_tile_type_enums import FURNACE_FUN_TILE_TYPE_ENUMS as FF_TT_ENUMS
from randomizer.constants.int_values.furnace_fun_question_type_enums import FURNACE_FUN_QUESTION_TYPE_ENUMS as FF_QT_ENUMS

from randomizer.constants.int_values.marker_enums import \
    PARAMETERS_ENUM, COLLISION_ENUMS, \
    MARKER_ID_ENUMS, BK_EFFECT_ENUMS, \
    ENTITY_NEXT_STATE_ENUM, COLLISION_SFX_ENUM

####################
##### ASSEMBLY #####
####################

class ASSEMBLY_CLASS():
    '''
    Pass
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self._create_assembly_file_objects()

    ################################
    ##### ALWAYS RUN FUNCTIONS #####
    ################################

    def _create_assembly_file_objects(self):
        '''
        Creates object files for all of the assembly code and data.
        ToDo: Automate the file names
        '''
        self._c_libraries_code_obj = C_LIBRARIES_CODE_CLASS(file_name="F19250")
        self._c_libraries_data_obj = C_LIBRARIES_DATA_CLASS(file_name="F362EB")
        self._game_engine_code_obj = GAME_ENGINE_CODE_CLASS(file_name="F37F90")
        self._game_engine_data_obj = GAME_ENGINE_DATA_CLASS(file_name="F9CAE0")
        self._spiral_mountain_code_obj = SPIRAL_MOUNTAIN_CODE_CLASS(file_name="FC4810")
        self._spiral_mountain_data_obj = SPIRAL_MOUNTAIN_DATA_CLASS(file_name="FC6C0F")
        self._mumbos_mountain_code_obj = MUMBOS_MOUNTAIN_CODE_CLASS(file_name="FB24A0")
        self._mumbos_mountain_data_obj = MUMBOS_MOUNTAIN_DATA_CLASS(file_name="FB42D9")
        self._treasure_trove_cove_code_obj = TREASURE_TROVE_COVE_CODE_CLASS(file_name="FAE860")
        self._treasure_trove_cove_data_obj = TREASURE_TROVE_COVE_DATA_CLASS(file_name="FB1AEB")
        self._clankers_cavern_code_obj = CLANKERS_CAVERN_CODE_CLASS(file_name="FA3FD0")
        self._clankers_cavern_data_obj = CLANKERS_CAVERN_DATA_CLASS(file_name="FA5D96")
        self._bubblegloop_swamp_code_obj = BUBBLEGLOOP_SWAMP_CODE_CLASS(file_name="FB44E0")
        self._bubblegloop_swamp_data_obj = BUBBLEGLOOP_SWAMP_DATA_CLASS(file_name="FB9610")
        self._freezeezy_peak_code_obj = FREEZEEZY_PEAK_CODE_CLASS(file_name="FBEBE0")
        self._freezeezy_peak_data_obj = FREEZEEZY_PEAK_DATA_CLASS(file_name="FC3FEF")
        self._gobis_valley_code_obj = GOBIS_VALLEY_CODE_CLASS(file_name="FA9150")
        self._gobis_valley_data_obj = GOBIS_VALLEY_DATA_CLASS(file_name="FAE27E")
        self._mad_monster_mansion_code_obj = MAD_MONSTER_MANSION_CODE_CLASS(file_name="FA5F50")
        self._mad_monster_mansion_data_obj = MAD_MONSTER_MANSION_DATA_CLASS(file_name="FA8CE6")
        self._rusty_bucket_bay_code_obj = RUSTY_BUCKET_BAY_CODE_CLASS(file_name="FB9A30")
        self._rusty_bucket_bay_data_obj = RUSTY_BUCKET_BAY_DATA_CLASS(file_name="FBE5E2")
        self._click_clock_wood_code_obj = CLICK_CLOCK_WOOD_CODE_CLASS(file_name="FD6190")
        self._click_clock_wood_data_obj = CLICK_CLOCK_WOOD_DATA_CLASS(file_name="FDA2FF")
        self._gruntildas_lair_code_obj = GRUNTILDAS_LAIR_CODE_CLASS(file_name="FC9150")
        self._gruntildas_lair_data_obj = GRUNTILDAS_LAIR_DATA_CLASS(file_name="FCF698")
        self._final_battle_code_obj = FINAL_BATTLE_CODE_CLASS(file_name="FD0420")
        self._final_battle_data_obj = FINAL_BATTLE_DATA_CLASS(file_name="FD5A60")
        self._cutscenes_code_obj = CUTSCENES_CODE_CLASS(file_name="FC6F20")
        self._cutscenes_data_obj = CUTSCENES_DATA_CLASS(file_name="FC8AFC")

    def disable_anti_tamper(self):
        '''
        Disables all known anti-tampering code.
        Thank you, Wedarobi! <3
        '''
        self._c_libraries_code_obj.disable_anti_tamper()
        self._spiral_mountain_code_obj.disable_anti_tamper()
        self._mumbos_mountain_code_obj.disable_anti_tamper()
        self._treasure_trove_cove_code_obj.disable_anti_tamper()
        self._clankers_cavern_code_obj.disable_anti_tamper()
        self._bubblegloop_swamp_code_obj.disable_anti_tamper()
        self._gobis_valley_code_obj.disable_anti_tamper()
        self._mad_monster_mansion_code_obj.disable_anti_tamper()
    
    def save_all_assembly_changes(self):
        '''
        Saves the files with their respective changes.
        '''
        self._c_libraries_code_obj._save_changes()
        self._c_libraries_data_obj._save_changes()
        self._game_engine_code_obj._save_changes()
        self._game_engine_data_obj._save_changes()
        self._spiral_mountain_code_obj._save_changes()
        self._spiral_mountain_data_obj._save_changes()
        self._mumbos_mountain_code_obj._save_changes()
        self._mumbos_mountain_data_obj._save_changes()
        self._treasure_trove_cove_code_obj._save_changes()
        self._treasure_trove_cove_data_obj._save_changes()
        self._clankers_cavern_code_obj._save_changes()
        self._clankers_cavern_data_obj._save_changes()
        self._bubblegloop_swamp_code_obj._save_changes()
        self._bubblegloop_swamp_data_obj._save_changes()
        self._freezeezy_peak_code_obj._save_changes()
        self._freezeezy_peak_data_obj._save_changes()
        self._gobis_valley_code_obj._save_changes()
        self._gobis_valley_data_obj._save_changes()
        self._mad_monster_mansion_code_obj._save_changes()
        self._mad_monster_mansion_data_obj._save_changes()
        self._rusty_bucket_bay_code_obj._save_changes()
        self._rusty_bucket_bay_data_obj._save_changes()
        self._click_clock_wood_code_obj._save_changes()
        self._click_clock_wood_data_obj._save_changes()
        self._gruntildas_lair_code_obj._save_changes()
        self._gruntildas_lair_data_obj._save_changes()
        self._final_battle_code_obj._save_changes()
        self._final_battle_data_obj._save_changes()
        self._cutscenes_code_obj._save_changes()
        self._cutscenes_data_obj._save_changes()
    
    #####################
    ##### BUG FIXES #####
    #####################
    
    def patch_yum_yum_crash_fix(self):
        '''
        Fixes a bug where Yum-Yums touching non-eggs/feathers will
        cause the game to crash.
        '''
        self._c_libraries_code_obj.patch_yum_yum_crash_fix()
        self._treasure_trove_cove_code_obj.patch_yum_yum_crash_fix()
    
    def mumbos_mountain_honeycomb_flags(self):
        '''
        Pass
        '''
        pass

    ####################################
    ##### QUALITY OF LIFE FEATURES #####
    ####################################
    
    def boot_to_file_select(self):
        '''
        Upon powering the game or saving & quitting,
        the player will skip the RARE & concert cutscenes.
        '''
        file_select_map_id:int = 0x91
        self._c_libraries_code_obj.booting_up_map(file_select_map_id)
        self._game_engine_code_obj.booting_up_map(file_select_map_id)
    
    def skippable_cutscenes(self):
        '''
        Pass
        '''
        self._game_engine_code_obj.skippable_cutscenes()

    def new_game_start_area(self, map_id:int, entry_id:int):
        '''
        Pass
        '''
        self._game_engine_code_obj.new_game_start_map(map_id, entry_id)
    
    def enable_exit_to_witchs_lair(self, level_start:bool=False):
        '''
        Pass
        '''
        self._game_engine_code_obj.enable_exit_to_witchs_lair()
        self._game_engine_data_obj.adjust_menu_for_witchs_lair()
        if(level_start):
            self._game_engine_code_obj.transform_witchs_lair_to_level_start()
            self._game_engine_data_obj.transform_witchs_lair_to_level_start()
        
    def all_transformations_can_learn_moves(self):
        '''
        Pass
        '''
        self._game_engine_code_obj.all_transformations_can_learn_moves()
    
    def all_transformations_can_enter_crypt(self):
        '''
        Pass
        '''
        self._game_engine_code_obj.all_transformations_crypt_warps()

    def _remove_termite_exclusivity(self):
        '''
        Pass
        '''
        self._mumbos_mountain_code_obj.all_transformations_conga_text()
        self._game_engine_code_obj.all_transformations_cool_shorts_text()
    
    def _remove_crocodile_exclusivity(self):
        '''
        Pass
        '''
        self._game_engine_code_obj.all_transformations_turbo_trainers()
        self._game_engine_code_obj.all_transformations_mr_vile_warps()

    def _remove_walrus_exclusivity(self):
        '''
        Pass
        '''
        self._freezeezy_peak_code_obj.all_transformations_boggy_2()
        self._freezeezy_peak_code_obj.all_transformations_race_sled()
        self._freezeezy_peak_code_obj.all_transformations_wozza()
        self._game_engine_code_obj.all_transformations_lose_boggy_race()
        self._game_engine_code_obj.all_transformations_in_water()

    def _remove_pumpkin_exclusivity(self):
        '''
        Pass
        '''
        self._mad_monster_mansion_code_obj.all_transformations_loggo_pumpkin_dialog()
        self._mad_monster_mansion_code_obj.all_transformations_loggo_flush()
        self._game_engine_code_obj.all_transformations_pumpkin_honeycomb()
        self._game_engine_code_obj.all_transformations_rain_barrel_warp()
        self._game_engine_code_obj.all_transformations_loggo_spin_animation()
        self._game_engine_code_obj.all_transformations_crypt_warps()
        self._game_engine_code_obj.all_transformations_well_warps()
        self._game_engine_code_obj.all_transformations_loggo_warps()

    def _remove_bee_exclusivity(self):
        '''
        Pass
        '''
        self._click_clock_wood_code_obj.all_transformations_snarebear_collision_off()
        self._game_engine_code_obj.all_transformations_note_door_jig()
        self._game_engine_code_obj.all_transformations_non_hostile_bee_swarm()
        self._game_engine_code_obj.all_transformations_zubba_hive_warp()

    def remove_all_transformation_exclusivity(self):
        '''
        Replaces all significant instances of "get transformation"
        with a function that returns a boolean for whether the
        player is Banjo or Wishywashy (func_8028F0D4)
        Needs Testing
        src/core2/code_7060.c#L589
        '''
        self._remove_termite_exclusivity()
        self._remove_crocodile_exclusivity()
        self._remove_walrus_exclusivity()
        self._remove_pumpkin_exclusivity()
        self._remove_bee_exclusivity()

    def remove_tutorial_option(self):
        '''
        Pass
        '''
        pass

    def enable_fallproof(self):
        '''
        Pass
        '''
        self._game_engine_code_obj.enable_fallproof()

    def mr_vile_only_one_round(self):
        '''
        Pass
        '''
        pass

    def rusty_bucket_bay_forgiving_engine_room(self):
        '''
        Pass
        '''
        pass

    def unlimited_illegal_cheat_codes(self):
        '''
        Pass
        '''
        pass

    def skip_jiggy_jig(self):
        '''
        Pass
        '''
        self._game_engine_code_obj.skip_jiggy_jig()
    
    def disable_world_reset_on_death(self):
        '''
        Disables a check for whether the level should reset.
        Resetting will still occur on leaving the level.
        '''
        self._game_engine_code_obj.disable_world_reset_on_death()
    
    def unlimited_time_bottles_bonus(self):
        '''
        Makes the bottles bonus not losable.
        May crash the game if playing too long.
        '''
        self._game_engine_code_obj.unlimited_time_bottles_bonus()
    
    def bottles_bonus_codes_always_activatable(self):
        '''
        Pass
        '''
        self._game_engine_code_obj.bottles_bonus_codes_always_activatable()
    
    ######################
    ##### DIFFICULTY #####
    ######################

    def starting_inventory_counts(self,
            blue_egg_count:int=0,
            red_feather_count:int=0,
            gold_feather_count:int=0):
        '''
        Pass
        '''
        self._game_engine_code_obj.starting_inventory_counts(
            blue_egg_count,
            red_feather_count,
            gold_feather_count,
        )
    
    def egg_firing_item_requirement(self, item_enum:int):
        '''
        Pass
        '''
        self._game_engine_code_obj.egg_firing_item_requirement(item_enum)
    
    def flight_item_requirement(self, item_enum:int):
        '''
        Pass
        '''
        self._game_engine_code_obj.flight_item_requirement(item_enum)
    
    def wonderwing_item_requirement(self, item_enum:int):
        '''
        Pass
        '''
        self._game_engine_code_obj.wonderwing_item_requirement(item_enum)

    def carrying_capacity(self, carrying_capacity:dict):
        '''
        Pass
        '''
        pass

    def respawnable_sprite_collectables(self):
        '''
        Pass
        '''
        self._game_engine_code_obj.respawnable_sprite_collectables()

    def starting_lives(self, starting_life_count:int):
        '''
        Pass
        '''
        pass

    def starting_max_health(self):
        '''
        Pass
        '''
        pass

    def empty_honeycombs_for_extra_health(self, empty_honeycomb_count:int):
        '''
        Pass
        '''
        pass

    def modify_collision_markers(self, collision_marker_dict:dict):
        '''
        Pass
        '''
        pass

    def log_collision_markers(self):
        '''
        Pass
        '''
        marker_collision_dict:dict = self._game_engine_data_obj.get_marker_collision_table()
        marker_collision_pandas_dict:dict = {}
        table_count:int = 0xBB
        for item_count in range(table_count):
            for parameter in PARAMETERS_ENUM:
                if(parameter == PARAMETERS_ENUM.marker_id):
                    key_value:int = marker_collision_dict[item_count][parameter]
                    key_hex_str:str = "0x" + str(hex(key_value))[2:].upper()
                    key_translation:str = MARKER_ID_ENUMS.get_marker_name(key_value)
                    key:str = f"{key_hex_str}: {key_translation}"
                    marker_collision_pandas_dict[key] = {}
                    continue
                parameter_name:str = PARAMETERS_ENUM.get_marker_name(parameter)
                collision_str:str = ""
                for collision in COLLISION_ENUMS:
                    collision_value:int = marker_collision_dict[item_count][parameter][collision]
                    if(collision is COLLISION_ENUMS.bk_effect):
                        bk_effect:str = BK_EFFECT_ENUMS.get_effect_name(collision_value)
                        collision_value:str = f"{bk_effect}"
                    elif(collision is COLLISION_ENUMS.entity_next_state):
                        next_state_name:str = ENTITY_NEXT_STATE_ENUM.get_state_name(collision_value)
                        collision_value:str = f"{next_state_name}"
                    elif(collision is COLLISION_ENUMS.collision_sfx):
                        collision_value:str = COLLISION_SFX_ENUM.get_sfx_name(collision_value)
                    elif(collision is COLLISION_ENUMS.bk_damage):
                        collision_value:str = f"BK_Damage:_{collision_value}"
                    elif(collision is COLLISION_ENUMS.hits_to_trigger):
                        collision_value:str = f"Trigger_Hits:_{collision_value}"
                    elif(collision is COLLISION_ENUMS.item_drop_slot):
                        collision_value:str = f"Item_Drop_Slot:_{collision_value}"
                    collision_str += f"{collision_value:-^30} "
                marker_collision_pandas_dict[key][parameter_name] = collision_str[:-2]
        df = pd.DataFrame(marker_collision_pandas_dict).transpose()
        for parameter in PARAMETERS_ENUM:
            if(parameter is PARAMETERS_ENUM.marker_id):
                continue
            parameter_name:str = PARAMETERS_ENUM.get_marker_name(parameter)
            df[parameter_name] = df[parameter_name].str.wrap(30)
        df.to_excel("C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/Breakdown_Notes/collisions.xlsx")

    def gobis_valley_randomize_matching_puzzle(self):
        '''
        Pass
        '''
        pass

    def mad_monster_mansion_randomize_motzands_song(self):
        '''
        Pass
        '''
        pass

    def mad_monster_mansion_shuffle_tumblars_tiles(self):
        '''
        Pass
        '''
        pass

    def geoguesser_furnace_fun(self, geoguesser_map_camera_list:list):
        '''
        Pass
        '''
        print("Geoguesser Furnace Fun Questions")
        picture_question_dict:dict = self._gruntildas_lair_data_obj._get_picture_question_dict()
        for question_count in picture_question_dict:
            map_id:int = geoguesser_map_camera_list[question_count][0]
            camera_id:int = geoguesser_map_camera_list[question_count][1]
            print(hex(map_id), hex(camera_id))
            picture_question_dict[question_count][STR_CONST.map_enum] = map_id
            picture_question_dict[question_count][STR_CONST.camera_id] = camera_id
        self._gruntildas_lair_data_obj._set_picture_question_dict(picture_question_dict)
        # self._gruntildas_lair_code_obj.furnace_fun_picture_questions_extend()
        # self._game_engine_code_obj.set_furnace_fun_question_assets_id(
        #     picture_start_id=0x12DB, picture_end_id=0x128A)
        print("Geoguesser Furnace Fun BK, Sound, Minigame, Gruntilda -> Picture Questions")
        furnace_fun_board_dict:dict = self._gruntildas_lair_data_obj.get_furnace_fun_board_dict()
        for tile_count in furnace_fun_board_dict:
            current_type_type:int = furnace_fun_board_dict[tile_count][STR_CONST.tile_type]
            if(current_type_type in [FF_TT_ENUMS.banjo_kazooie, FF_TT_ENUMS.sound,
                                     FF_TT_ENUMS.minigame, FF_TT_ENUMS.gruntilda]):
                furnace_fun_board_dict[tile_count][STR_CONST.tile_type] = FF_TT_ENUMS.picture
        self._gruntildas_lair_data_obj.set_furnace_fun_board_dict(furnace_fun_board_dict)
        print("Geoguesser Furnace Fun Joker, Skull -> Picture Questions")
        self._gruntildas_lair_code_obj._set_rng_tile_to_one_type(FF_QT_ENUMS.picture)
    
    def extra_fast_buzzbomb(self, speed_multiplier:float=1):
        '''
        Pass
        '''
        self._game_engine_code_obj.extra_fast_buzzbomb(speed_multiplier)
    
    def modify_sir_slush_spawn(self, actor_id:int):
        '''
        Pass
        '''
        self._game_engine_code_obj.modify_sir_slush_spawn(actor_id)
    
    def extra_fast_bigbutt(self):
        '''
        Pass
        '''
        self._game_engine_code_obj.extra_fast_bigbutt()
    
    def agro_conga(self):
        '''
        Pass
        '''
        self._mumbos_mountain_code_obj.agro_conga()

    def the_floor_is_lava(self, time_to_take_damage:int=4):
        '''
        Pass
        '''
        self._game_engine_code_obj.the_floor_is_lava(time_to_take_damage)

    ##############################
    ##### COSMETICS & SOUNDS #####
    ##############################

    def replace_player_models(self, starting_asset_id:int):
        '''
        Must go in the order:
        Termite, Pumpkin, Crocodile, Walrus, Bee, Wishywashy, BK Models
        '''
        self._game_engine_code_obj.replace_transformation_models(starting_asset_id)
        self._game_engine_code_obj.replace_banjo_kazooie_models(starting_asset_id + 5)
        self._game_engine_code_obj.adjust_player_eye_model_eyes(starting_asset_id)
        self._game_engine_code_obj.spawn_appendages()
        self._game_engine_code_obj.adjust_player_model_collisions(starting_asset_id)
    
    def level_dynamic_banjo_kazooie_model(self, starting_asset_id:int):
        '''
        Pass
        '''
        self._game_engine_code_obj.level_dynamic_banjo_kazooie_model(starting_asset_id)
    
    def bk_model_dynamic_coloring(self):
        '''
        Pass
        '''
        self._game_engine_code_obj.bk_model_dynamic_coloring()

    def replace_game_engine_models_with_assets(self, asset_id_dict:dict):
        '''
        Pass
        '''
        for model_id in asset_id_dict:
            asset_id:int = asset_id_dict[model_id]
            # Replace Model

    def set_skybox_and_clouds(self):
        '''
        Pass
        '''
        pass

    def randomize_skybox_and_clouds(self):
        '''
        Pass
        '''
        pass

    def randomize_music(self):
        '''
        Pass
        '''
        pass

    def mute_all_music(self):
        '''
        Pass
        '''
        self._c_libraries_code_obj.mute_all_music()

    #################
    ##### LOGIC #####
    #################
    
    def bottles_tutorial_moves(self,
            ability_enum_list:list,
            blue_egg_count:int=50,
            red_feather_count:int=25,
            gold_feather_count:int=5,
            mumbo_token_count:int=0,
            ):
        '''
        Pass
        '''
        self._game_engine_code_obj.spiral_mountain_auto_complete_bridge()
        self._spiral_mountain_code_obj.bottles_tutorial_moves(ability_enum_list)
        self._spiral_mountain_code_obj.bottles_tutorial_items(
            blue_egg_count, red_feather_count,
            gold_feather_count, mumbo_token_count
        )

    # def set_alternate_win_conditions(self,
    #         possible_win_condition_list:list):
    #     '''
    #     Pass
    #     '''
    #     # random.seed(a=seed_val)
    #     # random.shuffle(possible_win_condition_list)
    #     win_condition_list:list = []
    #     branch_count:int = 4
    #     for item_enum, level_enum, item_val in possible_win_condition_list:
    #         if(level_enum is not None):
    #             command_function = WIN_CONDITION_FUNCTION_DICT[STR_CONST.level_count][item_enum]
    #             command_list:list = \
    #                 WIN_CONDITION_COMMANDS_DICT[STR_CONST.level_count](command_function, level_enum, item_val, branch_count)
    #             branch_count += 5
    #         elif((type(item_val) == JIGGY_ENUMS) or
    #              (type(item_val) == EMPTY_HONEYCOMB_ENUMS)):
    #             command_function = WIN_CONDITION_FUNCTION_DICT[STR_CONST.item_enum][item_enum]
    #             command_list:list = \
    #                 WIN_CONDITION_COMMANDS_DICT[STR_CONST.item_enum](command_function, item_val, branch_count)
    #             branch_count += 4
    #         else:
    #             command_function = WIN_CONDITION_FUNCTION_DICT[STR_CONST.total_count][item_enum]
    #             command_list:list = \
    #                 WIN_CONDITION_COMMANDS_DICT[STR_CONST.total_count](command_function, item_val, branch_count)
    #             branch_count += 5
    #         if(branch_count > 0x98):
    #             break
    #         else:
    #             win_condition_list.insert(0, command_list)
    #     self._game_engine_code_obj.set_alternate_win_conditions(win_condition_list)

    def set_note_door_values(self,
            note_door_list:list=[
                50, 180, 260, 350, 450, 640,
                765, 810, 828, 846, 864, 882]):
        '''
        Pass
        '''
        self._gruntildas_lair_data_obj.set_note_door_values(note_door_list)

    def set_jigsaw_puzzle_costs(self,
            jigsaw_puzzle_list:list=[
                1, 2, 5, 7, 8, 9,
                10, 12, 15, 25, 4]):
        '''
        Pass
        '''
        self._gruntildas_lair_data_obj.set_jigsaw_puzzle_costs(jigsaw_puzzle_list)

    def set_transformation_costs(self,
            transformation_costs_dict:dict=[5, 10, 15, 20, 25]):
        '''
        Pass
        '''
        self._game_engine_code_obj.set_transformation_costs(transformation_costs_dict)

    def new_game_moves(self):
        '''
        Pass
        '''
        pass

    def adjust_kill_drops(self):
        '''
        Pass
        '''
        pass

    def increase_note_pickup_count(self, note_pickup_count:int):
        '''
        Pass
        '''
        pass

    def set_note_door_criteria(self, note_door_item_requirement:str):
        '''
        Pass
        '''
        mips_hex_code:int = 0x0C0D1BBB # itemscore_noteScores_getTotal()
        if(note_door_item_requirement == STR_CONST.note):
            mips_hex_code:int = 0x0C0D1BBB # itemscore_noteScores_getTotal()
        elif(note_door_item_requirement == STR_CONST.jiggy):
            mips_hex_code:int = 0x0C0C848F # jiggyscore_total()
        elif(note_door_item_requirement == STR_CONST.empty_honeycomb):
            mips_hex_code:int = 0x0C0C8527 # honeycombscore_get_total()
        elif(note_door_item_requirement == STR_CONST.mumbo_token):
            mips_hex_code:int = 0x0C0C8599 # mumboscore_get_total()
        self._gruntildas_lair_code_obj.note_door_item_requirement(mips_hex_code)

    def set_jigsaw_puzzle_criteria(self):
        '''
        Pass
        '''
        pass
        
    def set_transformation_criteria(self):
        '''
        Pass
        '''
        pass

    def set_jiggy_win_condition(self):
        '''
        Pass
        '''
        pass

    def set_note_win_condition(self):
        '''
        Pass
        '''
        pass

    def scale_banjo_walking_speed(self):
        '''
        Pass
        '''
        pass

    def scale_talon_trot_speed(self):
        '''
        Pass
        '''
        pass

    def scale_swimming_speeds(self):
        '''
        Pass
        '''
        pass

    def scale_transformation_speeds(self):
        '''
        Pass
        '''
        pass

    def remove_slope_slide_timer(self):
        '''
        Pass
        '''
        pass

    def mad_monster_mansion_anyones_honeycomb(self):
        '''
        Pass
        '''
        pass

    def replace_moves_cheat_codes(self):
        '''
        Pass
        '''
        pass

    def gruntildas_lair_set_water_level(self, water_level:int=0):
        '''
        Pass
        '''
        pass

    def treasure_trove_cove_raise_sharkfood_island(self):
        '''
        Pass
        '''
        pass

    def shock_jump_pad_anywhere(self):
        '''
        Pass
        '''
        self._game_engine_code_obj.shock_jump_pad_anywhere()
    
    def modify_cauldron_warps(self):
        '''
        Pass
        '''
        cauldron_dict = self._gruntildas_lair_data_obj.get_cauldron_dict()
        warp_info = WARP_ENTRY_DICT[STR_CONST.treasure_trove_cove_nippers_shell_from_main]
        cauldron_dict[4][STR_CONST.map_enum] = warp_info[0]
        cauldron_dict[4][STR_CONST.entry_point] = warp_info[1]
        self._gruntildas_lair_data_obj.set_cauldron_dict(cauldron_dict)
'''
Purpose:
* Modifies code written for the game engine
'''

###################
##### IMPORTS #####
###################

from randomizer.generic_bin_file_class import Generic_Bin_File_Class

from randomizer.constants.str_values.string_constants import STRING_CONSTANTS as STR_CONST

#############################
##### C LIBRARIES CLASS #####
#############################

class GAME_ENGINE_CODE_CLASS(Generic_Bin_File_Class):
    '''
    Class for modifying code written for the game engine
    '''
    def __init__(self, file_name:str):
        '''
        Constructor
        '''
        file_path:str = STR_CONST.extracted_files_dir + file_name + STR_CONST.decompressed_bin_extension
        super().__init__(file_path)
    
    #################
    ##### WARPS #####
    #################
    
    def booting_up_map(self, map_id:int):
        '''
        When loading the game, this is the location the player boots up at
        Typically used to skip the Rareware & N64 logo cutscene and the concert
        Decomp:
        * code_14420.c#L271
        * code_956B0.c#L67
        '''
        self._write_bytes_from_int(0x1467F, map_id, byte_count=1)
        self._write_bytes_from_int(0x9580B, map_id, byte_count=1)
    
    def new_game_start_map(self, map_id:int, entry_id:int):
        '''
        ch/gameSelect.c
        code_956B0.c
        '''
        # Cutscene (MAP_85_CS_SPIRAL_MOUNTAIN_3)
        self._write_bytes_from_int(0x3E17A, map_id, byte_count=2)
        self._write_bytes_from_int(0x3E180, 0x24070000 + entry_id, byte_count=4)
        # Warps (0x112 -> MAP_1_SM_SPIRAL_MOUNTAIN + Entry 18)
        self._write_bytes_from_int(0x986FA, map_id, byte_count=1)
        self._write_bytes_from_int(0x986FB, entry_id, byte_count=1)
    
    def reassign_warp(self, start_index_list:list, map_id:int, exit_id:int):
        '''
        Pass
        '''
        warp_id = map_id * 0x100 + exit_id
        for start_index in start_index_list:
            self._write_bytes_from_int(start_index, warp_id, byte_count=2)
    
    #####################
    ##### CUTSCENES #####
    #####################
    
    def skippable_cutscenes(self):
        '''
        Allows the player to skip the intro, lair, and
        game over cutscenes.
        Decomp: code_956B0.c#L44
        '''
        # Intro And Lair Cutscenes
        # Always Return True
        self._write_bytes_from_int(0x9573C, 0x24020001, byte_count=4)
        # Game Over Cutscene
        # Always Set fileProgressFlag_set(0xE1, 1);
        self._write_bytes_from_int(0x95770, 0x00000000, byte_count=4)
    
    def skip_jiggy_jig(self):
        '''
        Treats all instances of touching the Jiggy as if
        the player was underwater/in air/a transformation.
        '''
        # Skips Triggers For Jiggy Count < 3
        self._write_bytes_from_int(0x5780, 0x28410000, byte_count=4)
        # Skips Triggers For Collecting All Jinjos
        self._write_bytes_from_int(0x579C, 0x10000004, byte_count=4)
        # Always Runs Jiggy Jig Function For Transformations/Flying/Swimming
        self._write_bytes_from_int(0xF020, 0x00000000, byte_count=4)
    
    ###############################
    ##### CARRYING CAPACITIES #####
    ###############################
    
    def starting_inventory_counts(self,
            blue_egg_count:int=0,
            red_feather_count:int=0,
            gold_feather_count:int=0):
        '''
        Allows the player to start a new save file with
        0-255 blue eggs, red feathers, or gold feathers.
        Decomp: code_BEF20.c#L175
        '''
        # Set Air & Blue Egg Value
        self._write_bytes_from_int(0xBF51C, 0x2419, byte_count=2)
        self._write_bytes_from_int(0xBF520, 0xAC59005C, byte_count=4) # Set Air
        if(blue_egg_count == 0):
            self._write_bytes_from_int(0xBF51E, 0xE10, byte_count=2) # Air Is Normally 3600
            self._write_bytes_from_int(0xBF524, 0xAC400034, byte_count=4) # Set Blue Eggs To Zero
        else:
            self._write_bytes_from_int(0xBF51E, blue_egg_count, byte_count=2)
            self._write_bytes_from_int(0xBF524, 0xAC590034, byte_count=4) # Set Blue Eggs
        # Red Feather Value
        self._write_bytes_from_int(0xBF528, 0x2419, byte_count=2)
        self._write_bytes_from_int(0xBF52A, red_feather_count, byte_count=2)
        self._write_bytes_from_int(0xBF538, 0xAC59003C, byte_count=4)
        # Gold Feather Value
        self._write_bytes_from_int(0xBF53C, 0x2419, byte_count=2)
        self._write_bytes_from_int(0xBF53E, gold_feather_count, byte_count=2)
        self._write_bytes_from_int(0xBF540, 0xAC590040, byte_count=4)

    def bottles_tutorial_gifted_counts(self,
            blue_egg_count:int=50,
            red_feather_count:int=25,
            gold_feather_count:int=5):
        '''
        Modifies how many items Bottles gives the
        player during their respective tutorials.
        '''
        self._write_bytes_from_int(0x52987, blue_egg_count, byte_count=1)
        self._write_bytes_from_int(0x5299B, red_feather_count, byte_count=1)
        self._write_bytes_from_int(0x529AF, gold_feather_count, byte_count=1)

    def cheato_carrying_capacities(self,
            blue_egg_before_val:int=100, blue_egg_after_val:int=200,
            red_feather_before_val:int=50, red_feather_after_val:int=100,
            gold_feather_before_val:int=10, gold_feather_after_val:int=20):
        '''
        Modifies the number of items a player can hold
        before and after talking to Cheato.
        '''
        self._write_bytes_from_int(0xBF21F, blue_egg_before_val, byte_count=1)
        self._write_bytes_from_int(0xBF217, blue_egg_after_val, byte_count=1)
        self._write_bytes_from_int(0xBF23F, red_feather_before_val, byte_count=1)
        self._write_bytes_from_int(0xBF237, red_feather_after_val, byte_count=1)
        self._write_bytes_from_int(0xBF25B, gold_feather_before_val, byte_count=1)
        self._write_bytes_from_int(0xBF257, gold_feather_after_val, byte_count=1)
    
    def egg_firing_item_requirement(self, item_enum:int):
        '''
        Pass
        '''
        # Egg Ass
        self._write_bytes_from_int(0x1B2CA, item_enum, byte_count=2)
        # Egg Head
        self._write_bytes_from_int(0x1B53A, item_enum, byte_count=2)
        # Poop Egg
        self._write_bytes_from_int(0x26DFE, item_enum, byte_count=2)
        # Shoot Egg
        self._write_bytes_from_int(0x26E22, item_enum, byte_count=2)
        # has_eggs = (item_empty(ITEM_D_EGGS) == 0);
        self._write_bytes_from_int(0x1B282, item_enum, byte_count=2)
        # Item Dec
        self._write_bytes_from_int(0x1B31A, item_enum, byte_count=2)
    
    def flight_item_requirement(self, item_enum:int):
        '''
        Pass
        '''
        # Flying Higher
        self._write_bytes_from_int(0x1CBAA, item_enum, byte_count=2)
        # Beak Bomb
        self._write_bytes_from_int(0x1CF82, item_enum, byte_count=2)
    
    def wonderwing_item_requirement(self, item_enum:int):
        '''
        Pass
        '''
        # Keeping Wonderwing
        self._write_bytes_from_int(0x2363A, item_enum, byte_count=2)
        # Start Wonderwing
        self._write_bytes_from_int(0x26DCE, item_enum, byte_count=2)
    
    def respawnable_sprite_collectables(self):
        '''
        Treat sprite collectables as if they are always in the final battle area
        Decomp: https://gitlab.com/banjo.decomp/banjo-kazooie/-/blob/master/src/core2/ch/collectible.c
        '''
        # Uses the branch for blue eggs instead of red feathers
        self._write_bytes_from_int(0x51D2C, 0x13010006, byte_count=4)
        # MAP_90_GL_BATTLEMENTS -> 0
        self._write_bytes_from_int(0x520E4, 0x300E0000, byte_count=4)

    #############################
    ##### HEALTH AND LIVES ######
    #############################
    
    def player_health(self,
            starting_health_val:int=5, default_health_cap:int=8,
            empty_honeycomb_for_health:int=6):
        '''
        Sets the player's starting health and how many
        empty honeycombs it takes to reach the health cap.
        '''
        ##########################
        # Change Starting Health #
        ##########################
            # D_80385F30[ITEM_14_HEALTH] = D_80385F30[ITEM_15_HEALTH_TOTAL] = start_health_val;
        self._write_bytes_from_int(0xBF517, starting_health_val, byte_count=1)
            # D_80385F30[ITEM_15_HEALTH_TOTAL] =  start_health_val + MIN(8 - start_health_val, (honeycombscore_get_total() / eh_val));
        self._write_bytes_from_int(0xC096B, 17 - starting_health_val, byte_count=1) # Adjusts MIN function itself
        self._write_bytes_from_int(0xC097B, 16 - starting_health_val, byte_count=1) # Adjusts parameter within MIN function
        self._write_bytes_from_int(0xC097F, starting_health_val, byte_count=1)

        #####################################
        # Remove Game Select Health Display #
        #####################################
        self._write_bytes_from_int(0xBF763, starting_health_val, byte_count=1)

        ##############
        # Health Cap #
        ##############
            # D_80385F30[ITEM_15_HEALTH_TOTAL] = 8;
        self._write_bytes_from_int(0xC099F, default_health_cap, byte_count=1)
            # sp34 = ((fileProgressFlag_get(FILEPROG_B9_DOUBLE_HEALTH))? 2 : 1);
        if(default_health_cap > 8):
            self._write_bytes_from_int(0xBF14F, 2, byte_count=1)
        
        ####################
        # Empty Honeycombs #
        ####################
            # Disables Pausing To Not Interrupt Next Step
            # If interrupted, the player won't receive the updated health until warp
            # if(!(item_getCount(ITEM_13_EMPTY_HONEYCOMB) < 6))
        self._write_bytes_from_int(0x5863, empty_honeycomb_for_health, byte_count=1)
        
        # Health Upgrade Animation & Updating Health
            # if(eh_val <= D_803815D4...
        byte_list = self._write_bytes_from_float(empty_honeycomb_for_health)
        self._write_bytes_from_int(0x77AC6, byte_list[0], byte_count=1)
        self._write_bytes_from_int(0x77AC7, byte_list[1], byte_count=1)

        # Removes Current Empty Honeycomb Count
            # func_803463D4(ITEM_13_EMPTY_HONEYCOMB, -empty_honeycomb_for_health);
        self._write_bytes_from_int(0x77C9A, 0x8000 - empty_honeycomb_for_health, byte_count=2)
        
        # Total Health Calculation (Loading Game/Zone)
            # D_80385F30[ITEM_13_EMPTY_HONEYCOMB] = honeycombscore_get_total() % eh_val;
        self._write_bytes_from_int(0xC091F, empty_honeycomb_for_health, byte_count=1)
            # D_80385F30[ITEM_15_HEALTH_TOTAL] =  start_health + MIN(8 - start_val, (honeycombscore_get_total() / eh_val));
        self._write_bytes_from_int(0xC095F, empty_honeycomb_for_health, byte_count=1)
    
    def player_lives(self, starting_life_count:int=3, infinite_lives:bool=False):
        '''
        Sets the player life count and/or makes the player's lives infinite.
        '''
        # Removes the life count decrease function upon death
        if(infinite_lives):
            self._write_bytes_from_int(0xBF72C, 0x00000000, byte_count=4)
            self._write_bytes_from_int(0xBF730, 0x00000000, byte_count=4)
            return
        # Modifies the player's starting life count,
        # and lives upon re-entering the game
        self._write_bytes_from_int(0xBF51B, starting_life_count, byte_count=1)

    def enable_fallproof(self):
        '''
        Player will not receive fall damage when in tumble state.
        '''
        self._write_bytes_from_int(0x2D69C, 0x00000000, byte_count=4)
        self._write_bytes_from_int(0x2D6A0, 0x00000000, byte_count=4)
    
    ##################
    ##### MODELS #####
    ##################
    
    # 8037D234 0001
    # 8037D236 0001
    # 8037D238 0001
    # 812986BA 035D
    # 812986BE 035D
    # 8129DD86 035D

    def replace_transformation_models(self, starting_asset_id:int):
        '''
        Replaces the transformation models with another asset.
        '''
        # core2/code_11660.c#L9
        wishywashy_model_id:int = starting_asset_id
        termite_bk_model_id:int = starting_asset_id + 1
        crocodile_bk_model_id:int = starting_asset_id + 2
        walrus_bk_model_id:int = starting_asset_id + 3
        pumpkin_bk_model_id:int = starting_asset_id + 4
        bee_bk_model_id:int = starting_asset_id + 5
        self._write_bytes_from_int(0x1169A, termite_bk_model_id, byte_count=2)
        self._write_bytes_from_int(0x116A2, walrus_bk_model_id, byte_count=2)
        self._write_bytes_from_int(0x116AA, pumpkin_bk_model_id, byte_count=2)
        self._write_bytes_from_int(0x116B2, crocodile_bk_model_id, byte_count=2)
        self._write_bytes_from_int(0x116BA, bee_bk_model_id, byte_count=2)
        self._write_bytes_from_int(0x116C2, wishywashy_model_id, byte_count=2)
    
    def replace_banjo_kazooie_models(self, starting_asset_id:int):
        '''
        Replaces the Banjo-Kazooie low and high poly models with
        another asset.
        '''
        # Decomp: core2/code_11660.c#L27
        self._write_bytes_from_int(0x116C4, 0x0C0C8640, byte_count=4) # level_get()
        self._write_bytes_from_int(0x116C8, 0x00000000, byte_count=4) # SLL 0, 0, 0
        self._write_bytes_from_int(0x116CC, 0x24420000 + starting_asset_id, byte_count=4) # Level Id + Starting Asset Id
        self._write_bytes_from_int(0x116D0, 0x8FBF0014, byte_count=4) # LW 1F, 14(1D)
        self._write_bytes_from_int(0x116D4, 0x27BD0018, byte_count=4) # ADDIU 1D, 1D, 18
        self._write_bytes_from_int(0x116D8, 0x03E00008, byte_count=4) # JR 1F
        self._write_bytes_from_int(0x116DC, 0x00000000, byte_count=4) # SLL 0, 0, 0
    
    def adjust_player_eye_model_eyes(self, starting_asset_id:int):
        '''
        Decomp: core2/ba/model.c#L300
        '''
        # Decomp: core2/code_16C60.c#L27
        negative_starting_asset_id:int = 0x10000 - starting_asset_id
        self._write_bytes_from_int(0x16C70, 0x244E0000 + negative_starting_asset_id, byte_count=4) # ADDIU $t6 $v0 negative_starting_asset_id
        self._write_bytes_from_int(0x16C74, 0x2DC10006, byte_count=4) # SLTIU $at $t6 0x0006
        self._write_bytes_from_int(0x16C78, 0x10200006, byte_count=4) # BEQ $at $zero 0x0006 -> BK Model
        self._write_bytes_from_int(0x16C7C, 0x000E7080, byte_count=4) # SLL $t6 $t6 0x02
        self._write_bytes_from_int(0x16C80, 0x24010000, byte_count=4) # ADDIU $at $zero 0x0 -> Wishywashy
        self._write_bytes_from_int(0x16C84, 0x10220045, byte_count=4) # BEQ $at $v0 0x0045
        self._write_bytes_from_int(0x16C88, 0x00000000, byte_count=4) # SLL 0, 0, 0
        self._write_bytes_from_int(0x16C8C, 0x1020002A, byte_count=4) # BEQ $zero $zero 0x002A -> Assume Transformation
        self._write_bytes_from_int(0x16C90, 0x00000000, byte_count=4) # SLL 0, 0, 0

    def spawn_appendages(self):
        '''
        Decomp: core2/code_16C60.c#L60
        '''
        # Decomp: core2/code_16C60.c#L60
        self._write_bytes_from_int(0x16DEC, 0x0C0A39F3, byte_count=4) # player_getTransformation()
        self._write_bytes_from_int(0x16DF4, 0x24010001, byte_count=4) # TRANSFORM_1_BANJO
        self._write_bytes_from_int(0x16E00, 0x24010001, byte_count=4) # TRANSFORM_1_BANJO
        self._write_bytes_from_int(0x16E08, 0x24010004, byte_count=4) # TRANSFORM_4_WALRUS
        self._write_bytes_from_int(0x16E14, 0x24010005, byte_count=4) # TRANSFORM_5_CROC

    def adjust_player_model_collisions(self, starting_asset_id:int):
        '''
        Decomp: core2/ba/model.c#L300
        '''
        negative_starting_asset_id:int = 0x10000 - starting_asset_id
        self._write_bytes_from_int(0xB334, 0x24480000 + negative_starting_asset_id, byte_count=4)
        self._write_bytes_from_int(0xB338, 0x2D010013, byte_count=4) # SLTIU $at $t0 0x0013
        self._write_bytes_from_int(0xB33C, 0x1020004C, byte_count=4) # BEQ $at $zero 0x004C -> Non-Player Model
        self._write_bytes_from_int(0xB340, 0x00084080, byte_count=4) # SLL $t0 $t0 0x02
        self._write_bytes_from_int(0xB344, 0x00000000, byte_count=4) # BEQ $zero $zero 0x004 -> Player Model
        self._write_bytes_from_int(0xB348, 0x00000000, byte_count=4) # SLL $zero $zero 0x0
        self._write_bytes_from_int(0xB34C, 0x00000000, byte_count=4) # SLL $zero $zero 0x0
        self._write_bytes_from_int(0xB350, 0x00000000, byte_count=4) # SLL $zero $zero 0x0
        self._write_bytes_from_int(0xB354, 0x00000000, byte_count=4) # SLL $zero $zero 0x0
    
    def replace_game_engine_models_with_assets(self, index_list:list, new_asset_id:list):
        '''
        Replaces an asset id located in the game engine
        code with another asset id.
        '''
        for index_start in index_list:
            self._write_bytes_from_int(index_start, new_asset_id, byte_count=2)

    def transparent_bk(self, alpha_val:int=0xFF):
        '''
        Decomp: ba/model.c#L130
        '''
        # baModelEnvAlpha = 0xFF;
        self._write_bytes_from_int(0xADEB, alpha_val, byte_count=1)

    ######################
    ##### PAUSE MENU #####
    ######################
    
    def enable_exit_to_witchs_lair(self):
        '''
        Allows players to exit the level by selecting
        'Exit To Witch's Lair' in the pause menu.
        '''
        # Disable Exit To Witch's Lair From TRUE to FALSE
        self._write_bytes_from_int(0x8BBF8, 0x00001025, byte_count=4)
        # Disable Debug Byte
        self._write_bytes_from_int(0x8BCE7, 0x00, byte_count=1)
    
    def transform_witchs_lair_to_level_start(self):
        '''
        Changes 'Exit To Witch's Lair' to use death warp
        locations instead of level exit locations.

        Glitch: Continues to play Pause Menu music once selected.
        Work Around: Pause and Unpause to stop the music.
        '''
        self._write_bytes_from_int(0x8C9B8, 0x0C0A7182, byte_count=4) # update_void_return_Location()
        self._write_bytes_from_int(0x8C9BC, 0x00000000, byte_count=4)
        self._write_bytes_from_int(0x8C9C0, 0x0C0A6DBC, byte_count=4) # func_8029B6F0() // Void Out Function
        self._write_bytes_from_int(0x8C9C4, 0x00000000, byte_count=4)
        self._write_bytes_from_int(0x8C9C8, 0x10000003, byte_count=4) # BEQ 0, 0, 3
        self._write_bytes_from_int(0x8C9CC, 0x00000000, byte_count=4)
        self._write_bytes_from_int(0x8C9D0, 0x00000000, byte_count=4)
        self._write_bytes_from_int(0x8C9D4, 0x00000000, byte_count=4)
    
    ####################################
    ##### ALTERNATE WIN CONDITIONS #####
    ####################################

    def _hijack_jiggy_increment(self):
        '''
        Replaces instances of the Jiggy count incrementing
        with a function that increments the Jiggy count and
        does other functions.
        '''
        # 15D94 \\ 0C0D17C9 \\ JAL D17C9 // item_inc()
        # 15D98 \\ 2404000E \\ ADDIU 4, 0, E // ITEM_E_JIGGY
        self._write_bytes_from_int(0x15D94, 0x0C0B64FB, byte_count=4) # func_802D93EC()
        # 15E18 \\ 0C0D17C9 \\ JAL D17C9 // item_inc()
        # 15E1C \\ 2404000E \\ ADDIU 4, 0, E // ITEM_E_JIGGY
        self._write_bytes_from_int(0x15E18, 0x0C0B64FB, byte_count=4) # func_802D93EC()
        # 29DC8 \\ 0C0D17C9 \\ JAL D17C9 // item_inc()
        # 29DCC \\ 2404000E \\ ADDIU 4, 0, E // ITEM_E_JIGGY
        self._write_bytes_from_int(0x29DC8, 0x0C0B64FB, byte_count=4) # func_802D93EC()
    
    def _hijack_note_increment(self):
        '''
        Replaces instances of the Note count incrementing
        with a function that increments the Note count and
        does other functions.
        '''
        # 4AB4 \\ 2404000C \\ ADDIU 4, 0, C // ITEM_C_NOTE
        # 4AB8 \\ 0C0D17C9 \\ JAL D17C9 // item_inc()
        # 4ABC \\ 2404000C \\ ADDIU 4, 0, C // ITEM_C_NOTE
        self._write_bytes_from_int(0x4AB4, 0x2404000C, byte_count=4) # ITEM_C_NOTE
        self._write_bytes_from_int(0x4AB8, 0x0C0B64FB, byte_count=4) # func_802D93EC()
        self._write_bytes_from_int(0x4ABC, 0x2404000C, byte_count=4) # ITEM_C_NOTE
        # 4AC0 \\ 10000003 \\ BEQ 0, 0, 3
        # 4AC4 \\ 00000000 \\ SLL 0, 0, 0
        # 4AC8 \\ 0C0D18FD \\ JAL D18FD // func_803463F4 (Diff Function, No Hub)
        # 4ACC \\ 24050001 \\ ADDIU 5, 0, 1 // 1
        self._write_bytes_from_int(0x4AC8, 0x0C0B64FB, byte_count=4) # func_802D93EC()
        self._write_bytes_from_int(0x4ACC, 0x2404000C, byte_count=4) # ITEM_C_NOTE
    
    def _hijack_empty_honeycomb_increment(self):
        '''
        Replaces instances of the Empty Honeycomb count incrementing
        with a function that increments the Empty Honeycomb count and
        does other functions.
        '''
        # 5850 \\ 0C0D17C9 \\ JAL D17C9 // item_inc()
        # 5854 \\ 24040013 \\ ADDIU 4, 0, 13 // ITEM_13_EMPTY_HONEYCOMB
        self._write_bytes_from_int(0x5850, 0x0C0B64FB, byte_count=4) # func_802D93EC()

    def _hijack_mumbo_token_increment(self):
        '''
        Replaces instances of the Mumbo Token count incrementing
        with a function that increments the Mumbo Token count and
        does other functions.
        '''
        # 59AE0 \\ 0C0D17C9 \\ JAL D17C9 // item_inc()
        # 59AE4 \\ 2404001C \\ ADDIU 4, 0, 1C // ITEM_1C_MUMBO_TOKEN
        self._write_bytes_from_int(0x59AE0, 0x0C0B64FB, byte_count=4) # func_802D93EC()

    def set_alternate_win_conditions(self, win_condition_list:list):
        '''
        Replaces the Bottles Bridge Speech Check function with a list of
        conditions, where if all are completed, the player will be warped
        to the beach credits cutscene. Hijacks the functions for incrementing
        the player's note, jiggy, empty honeycomb, and mumbo token scores.
        Win conditions are more explained in other win condition files.
        Decomp: ch/mole.c#L92
        '''
        # Ask For Memory
        self._write_bytes_from_int(0x5245C, 0x27BDFFE8, byte_count=4) # ADDIU 1D, 1D, 7FE8
        self._write_bytes_from_int(0x52460, 0xAFBF0014, byte_count=4) # SW 1F, 14(1D)
        # Increase Item Count For Enum
        self._write_bytes_from_int(0x52464, 0x0C0D18F5, byte_count=4) # JAL D18F5 // func_803463D4(item_id, item_diff)
        self._write_bytes_from_int(0x52468, 0x24050001, byte_count=4) # ADDIU 5, 0, 1
        # Check Each Item
        curr_index:int = 0x5246C
        for win_condition_item in win_condition_list:
            for win_condition_line in win_condition_item:
                self._write_bytes_from_int(curr_index, win_condition_line, byte_count=4)
                curr_index += 0x4
        # Verify
        if(curr_index > 0x52504):
            error_message:str = f"ERROR: set_alternate_win_conditions: Function surpassed allowed index 0x{self._convert_int_to_hex_str(curr_index, 3)}"
            print(error_message)
            raise Exception(error_message)
        # Send Player To Beach Credits
        self._write_bytes_from_int(curr_index + 0x00, 0x24040096, byte_count=4) # MAP_96_CS_END_BEACH_1
        self._write_bytes_from_int(curr_index + 0x04, 0x00002825, byte_count=4) # OR A, 0, 0
        self._write_bytes_from_int(curr_index + 0x08, 0x0C0B901E, byte_count=4) # func_802E4078() // Warp To Map
        self._write_bytes_from_int(curr_index + 0x0C, 0x24060001, byte_count=4) # ADDIU 6, 0, 1
        # Return Memory
        self._write_bytes_from_int(curr_index + 0x10, 0x8FBF0014, byte_count=4) # LW 1F, 14(1D)
        self._write_bytes_from_int(curr_index + 0x14, 0x27BD0018, byte_count=4) # ADDIU 1D, 1D, 18
        # Return Null
        self._write_bytes_from_int(curr_index + 0x18, 0x03E00008, byte_count=4) # JR 1F
        self._write_bytes_from_int(curr_index + 0x1C, 0x00000000, byte_count=4) # SLL 0, 0, 0
        # Replace func_802D93EC() -> Set to False
        self._write_bytes_from_int(0x527DC, 0x24030000, byte_count=4) # Set To False
        # Link Increment Functions
        self._hijack_jiggy_increment()
        self._hijack_note_increment()
        self._hijack_empty_honeycomb_increment()
        self._hijack_mumbo_token_increment()

    #####################
    ##### ABILITIES #####
    #####################
    
    def spiral_mountain_auto_complete_bridge(self):
        '''
        Skips the check for knowing Spiral Mountain moves in order
        to complete the bridge in Spiral Mountain.
        Decomp: ch/mole.c#L443
        '''
        # Skips Checks For Knowing SM Moves: func_802DA498()
        self._write_bytes_from_int(0xDC598, 0x14400000, byte_count=4)
        self._write_bytes_from_int(0xDC5D4, 0x50400000, byte_count=4)
    
    def learned_moves_in_world_texts(self):
        '''
        Modifies the Bottles speeches when you learn all of the moves
        in a level or forget a learnable move in a level and exit to
        the lair.
        Decomp: ch/mole.c#L47
        '''
        pass

    def shock_jump_pad_anywhere(self):
        '''
        Acts as though the floor is always a shock jump pad.
        Still requires high jump/dropdown to perform.
        '''
        # 8037C1D2 0001
        # miscflag_isTrue(0x2) -> Always 1
        self._write_bytes_from_int(0x2A1B0, 0x24020001, byte_count=4)
        self._write_bytes_from_int(0x2A1B4, 0x24020001, byte_count=4)
    
    ###########################
    ##### TRANSFORMATIONS #####
    ###########################
    
    def set_transformation_costs(self,
            transformation_costs_dict:dict=[5, 10, 15, 20, 25]):
        '''
        Pass
        '''
        self._write_bytes_from_int(0x4A7E6, transformation_costs_dict[STR_CONST.termite_transformation_cost], byte_count=2)
        self._write_bytes_from_int(0x4A7EE, transformation_costs_dict[STR_CONST.crocodile_transformation_cost], byte_count=2)
        self._write_bytes_from_int(0x4A7F6, transformation_costs_dict[STR_CONST.walrus_transformation_cost], byte_count=2)
        self._write_bytes_from_int(0x4A7FE, transformation_costs_dict[STR_CONST.pumpkin_transformation_cost], byte_count=2)
        self._write_bytes_from_int(0x4A806, transformation_costs_dict[STR_CONST.bee_transformation_cost], byte_count=2)

    ### Termite

    def all_transformations_cool_shorts_text(self):
        '''
        Pass
        '''
        # Checks If You Are Banjo Or Wishywashy
        self._write_bytes_from_int(0xD7A20, 0x0C0A3C35, byte_count=4)
        # Set Comparison To 0 (False)
        self._write_bytes_from_int(0xD7A28, 0x24010000, byte_count=4)
    
    def all_transformations_pumpkin_honeycomb(self):
        '''
        src/core2/ba/marker.c#L559
        '''
        # Checks If You Are Banjo Or Wishywashy
        self._write_bytes_from_int(0x5810, 0x0C0A3C35, byte_count=4)
        # Set Comparison To 0 (False)
        self._write_bytes_from_int(0x5818, 0x24010000, byte_count=4)
    
    ### Crocodile
    
    def all_transformations_turbo_trainers(self):
        '''
        Allows all transformations to use Turbo Trainers
        src/core2/ba/marker.c#L759
        '''
        # You are always Banjo
        self._write_bytes_from_int(0x5FC4, 0x10420003, byte_count=4)
    
    def all_transformations_mr_vile_warps(self):
        '''
        Enter Vile Warp: src/core2/code_956B0.c#L574
        Exit Vile Warp Already Allow Anything
        '''
        # Checks If You Are Banjo Or Wishywashy
        self._write_bytes_from_int(0x96D08, 0x0C0A3C35, byte_count=4)
        # Set Comparison To 0 (False)
        self._write_bytes_from_int(0x96D10, 0x24010000, byte_count=4)
    
    ### Walrus

    def all_transformations_lose_boggy_race(self):
        '''
        src/core2/code_14420.c#L871
        '''
        # Checks If You Are Banjo Or Wishywashy
        self._write_bytes_from_int(0xFC5C, 0x0C0A3C35, byte_count=4)
        # Set Comparison To 0 (False)
        self._write_bytes_from_int(0xFC64, 0x24010000, byte_count=4)
    
    def all_transformations_in_water(self):
        '''
        src/core2/code_9450.c#L94
        '''
        # Checks If You Are Banjo Or Wishywashy
        self._write_bytes_from_int(0x9770, 0x0C0A3C35, byte_count=4)
        # Set Comparison To 0 (False)
        self._write_bytes_from_int(0x9778, 0x24010000, byte_count=4)
    
    ### Pumpkin

    def all_transformations_rain_barrel_warp(self):
        '''
        src/core2/code_956B0.c#L550
        '''
        # Checks If You Are Banjo Or Wishywashy
        self._write_bytes_from_int(0x96C28, 0x0C0A3C35, byte_count=4)
        # Set Comparison To 0 (False)
        self._write_bytes_from_int(0x96C30, 0x24010000, byte_count=4)
    
    def all_transformations_loggo_spin_animation(self):
        '''
        src/core2/code_956B0.c#L562
        '''
        # Checks If You Are Banjo Or Wishywashy
        self._write_bytes_from_int(0x96C8C, 0x0C0A3C35, byte_count=4)
        # Set Comparison To 0 (False)
        self._write_bytes_from_int(0x96C94, 0x24010000, byte_count=4)
    
    def all_transformations_crypt_warps(self):
        '''
        Checks If You Are Banjo Or Wishywashy
        Set Comparison To 0 (False)
        src/core2/code_956B0.c#L1189
        '''
        # Enter Crypt
        self._write_bytes_from_int(0x982D8, 0x0C0A3C35, byte_count=4)
        self._write_bytes_from_int(0x982E0, 0x24010000, byte_count=4)
        # Leave Crypt
        self._write_bytes_from_int(0x98310, 0x0C0A3C35, byte_count=4)
        self._write_bytes_from_int(0x98318, 0x24010000, byte_count=4)
    
    def all_transformations_well_warps(self):
        '''
        src/core2/code_956B0.c#L1324
        src/core2/code_956B0.c#L1330
        '''
        # Enter Well
        # Checks If You Are Banjo Or Wishywashy
        self._write_bytes_from_int(0x987A8, 0x0C0A3C35, byte_count=4)
        # Set Comparison To 0 (False)
        self._write_bytes_from_int(0x987B0, 0x24010000, byte_count=4)
        # Leave Well
        # Checks If You Are Banjo Or Wishywashy
        self._write_bytes_from_int(0x987E0, 0x0C0A3C35, byte_count=4)
        # Set Comparison To 0 (False)
        self._write_bytes_from_int(0x987E8, 0x24010000, byte_count=4)
    
    def all_transformations_loggo_warps(self):
        '''
        src/core2/code_956B0.c#L1336
        src/core2/code_956B0.c#L1342
        '''
        # Enter Loggo
        # Checks If You Are Banjo Or Wishywashy
        self._write_bytes_from_int(0x98818, 0x0C0A3C35, byte_count=4)
        # Set Comparison To 0 (False)
        self._write_bytes_from_int(0x98820, 0x24010000, byte_count=4)
        # Leave Loggo
        # Checks If You Are Banjo Or Wishywashy
        self._write_bytes_from_int(0x98850, 0x0C0A3C35, byte_count=4)
        # Set Comparison To 0 (False)
        self._write_bytes_from_int(0x98858, 0x24010000, byte_count=4)
    
    ### Bee
    
    def all_transformations_note_door_jig(self):
        '''
        src/core2/code_14420.c#L856
        '''
        # Checks If You Are Banjo Or Wishywashy
        self._write_bytes_from_int(0x15B40, 0x0C0A3C35, byte_count=4)
        # Set Comparison To 0 (False)
        self._write_bytes_from_int(0x15B48, 0x24010000, byte_count=4)
    
    def all_transformations_non_hostile_bee_swarm(self):
        '''
        src/core2/code_47BD0.c#L251
        '''
        # Checks If You Are Banjo Or Wishywashy
        self._write_bytes_from_int(0x485C0, 0x0C0A3C35, byte_count=4)
        # Set Comparison To 0 (False)
        self._write_bytes_from_int(0x485C8, 0x24010000, byte_count=4)
    
    def all_transformations_zubba_hive_warp(self):
        '''
        src/core2/code_956B0.c#L1261
        '''
        # Checks If You Are Banjo Or Wishywashy
        self._write_bytes_from_int(0x98564, 0x0C0A3C35, byte_count=4)
        # Set Comparison To 0 (False)
        self._write_bytes_from_int(0x9856C, 0x24010000, byte_count=4)

    #######################
    ##### FURNACE FUN #####
    #######################
    # core2/code_91E10.c
    
    def set_furnace_fun_question_assets_id(self,
            picture_start_id:int=0x12DB, picture_end_id:int=0x12EE,
            sound_start_id:int=0x13A3, sound_end_id:int=0x13D6,
            grunty_start_id:int=0x1407, grunty_end_id:int=0x1425,
            default_start_id:int=0x1213, default_end_id:int=0x1277):
        '''
        Pass
        '''
        # Start Ids
        self._write_bytes_from_int(0x91F60, 0x24020000 + default_start_id, byte_count=4)
        self._write_bytes_from_int(0x91F70, 0x24020000 + picture_start_id, byte_count=4)
        self._write_bytes_from_int(0x91F78, 0x24020000 + sound_start_id, byte_count=4)
        self._write_bytes_from_int(0x91F80, 0x24020000 + grunty_start_id, byte_count=4)
        # End Ids
        self._write_bytes_from_int(0x91FA4, 0x24020000 + default_end_id, byte_count=4)
        self._write_bytes_from_int(0x91FB4, 0x24020000 + picture_end_id, byte_count=4)
        self._write_bytes_from_int(0x91FBC, 0x24020000 + sound_end_id, byte_count=4)
        self._write_bytes_from_int(0x91FC4, 0x24020000 + grunty_end_id, byte_count=4)
    
    ###########################
    ##### QUALITY OF LIFE #####
    ###########################
    # core2/code_9A740.c

    def disable_world_reset_on_death(self):
        '''
        Disables a check for whether the level should reset.
        Resetting will still occur on leaving the level.
        '''
        self._write_bytes_from_int(0x5C964, 0x24040001, byte_count=4)
    
    def all_transformations_can_learn_moves(self):
        '''
        Removes the transformation check for learning Bottles moves
        '''
        self._write_bytes_from_int(0x53018, 0x24020045, byte_count=4)
    
    def unlimited_time_bottles_bonus(self):
        '''
        Pass
        '''
        self._write_bytes_from_int(0x579EC, 0x10000009, byte_count=4)
    
    def bottles_bonus_codes_always_activatable(self):
        '''
        Pass
        '''
        command_list:list = [
            0x24040001,
            0x3C018038,
            # 0xA020DCC0,
            0xA024DCC0,
            0x3C018038,
            # 0xA020DCC1,
            0xA024DCC1,
            0x3C018038,
            0x3C0E8038,
            # 0xA020DCC2,
            0xA024DCC2,
            0x24020003,
            0x25CEDCC0,
            0x004E1821,
            # 0xA0600001,
            0xA0640001,
            # 0xA0600002,
            0xA0640002,
            # 0xA0600003,
            0xA0640003,
            0xA0600000,
            0x3C018038,
            # 0xA020DCC7,
            0xA024DCC7,
            0x3C018038,
            # 0xA020DCC8,
            0xA024DCC8,
            0x3C018038,
            0xA020DCC9,
            0x3C018038,
            # 0xA020DCCA,
            0xA024DCCA,
            0x3C018038,
            # 0xA020DCCB,
            0xA024DCCB,
            0x3C018038,
            # 0xA020DCCC,
            0xA024DCCC,
            0x3C018038,
            0x03E00008,
            # 0xAC20DF68,
            0xAC24DF68,
            0x00000000,
        ]
        index_start:int = 0x57BF0
        max_index:int = 0x57C6C
        self._write_bytes_from_hex_assembly(index_start, command_list, max_index)
    
    ###########################
    ##### ENEMY FUNCTIONS #####
    ###########################

    def extra_fast_buzzbomb(self, speed_multiplier:float=1):
        '''
        Decomp: core2/code_45310.c#L399
        '''
        # sp30 = 1 * spB8;
        # Replacing 1.0f
        new_speed:int = self._convert_bfloat_to_hex(speed_multiplier)
        self._write_bytes_from_int(0x4617A, new_speed, byte_count=2)
    
    def modify_sir_slush_spawn(self, actor_id:int=0x0125):
        '''
        Pass
        '''
        self._write_bytes_from_int(0x5ABAE, actor_id, byte_count=2)
    
    def extra_fast_bigbutt(self):
        '''
        Pass
        '''
        self._write_bytes_from_int(0x3FE40, 0x3C014000, byte_count=4)
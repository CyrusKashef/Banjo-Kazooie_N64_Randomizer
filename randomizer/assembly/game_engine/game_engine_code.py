'''
Purpose:
* Modifies code written for the game engine
'''

###################
##### IMPORTS #####
###################

from randomizer.generic_bin_file_class import Generic_Bin_File_Class

from randomizer.contants.variables.assembly_variables import \
    EXTRACTED_FILES_DIR, DECOMPRESSED_BIN_EXTENSION

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
        file_path:str = EXTRACTED_FILES_DIR + file_name + DECOMPRESSED_BIN_EXTENSION
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
            self._write_bytes_from_int(0xBF72C, 0x0000000000000000, byte_count=8)
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
    
    def replace_banjo_kazooie_models(self,
            low_poly_model:int=0x34D, high_poly_model:int=0x34E):
        '''
        Replaces the Banjo-Kazooie low and high poly models with
        another asset.
        '''
        # Low Poly Model
        self._write_bytes_from_int(0x11722, low_poly_model, byte_count=2)
        self._write_bytes_from_int(0x1172A, low_poly_model, byte_count=2)
        # High Poly Model
        self._write_bytes_from_int(0x1172E, high_poly_model, byte_count=2)
    
    def replace_game_engine_models_with_assets(self, index_list:list, new_asset_id:list):
        '''
        Replaces an asset id located in the game engine
        code with another asset id.
        '''
        for index_start in index_list:
            self._write_bytes_from_int(index_start, new_asset_id, byte_count=2)
    
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
    
    ####################################
    ##### ALTERNATE WIN CONDITIONS #####
    ####################################
    
    def remove_defeating_gruntilda_check(self):
        '''
        Removes all instance of requiring the player to beat
        gruntilda to warp to the beach cutscene. 
        '''
        # fileProgressFlag_get(FILEPROG_FC_DEFEAT_GRUNTY)
        # Instance
        self._write_bytes_from_int(0x15C94, 0x00000000, byte_count=4)
        self._write_bytes_from_int(0x15C98, 0x00000000, byte_count=4)
        self._write_bytes_from_int(0x15C9C, 0x00000000, byte_count=4)
        # Instance
        self._write_bytes_from_int(0x15D00, 0x00000000, byte_count=4)
        self._write_bytes_from_int(0x15D04, 0x00000000, byte_count=4)
        self._write_bytes_from_int(0x15D08, 0x00000000, byte_count=4)
        # Instance
        self._write_bytes_from_int(0x15DB0, 0x00000000, byte_count=4)
        self._write_bytes_from_int(0x15DB4, 0x00000000, byte_count=4)
        self._write_bytes_from_int(0x15DB8, 0x00000000, byte_count=4)
        # Instance
        self._write_bytes_from_int(0x29E28, 0x00000000, byte_count=4)
        self._write_bytes_from_int(0x29E2C, 0x00000000, byte_count=4)
        self._write_bytes_from_int(0x29E30, 0x00000000, byte_count=4)
        # Instance
        self._write_bytes_from_int(0x29FB8, 0x00000000, byte_count=4)
        self._write_bytes_from_int(0x29FBC, 0x00000000, byte_count=4)
        self._write_bytes_from_int(0x29FC0, 0x00000000, byte_count=4)
        # Instance
        self._write_bytes_from_int(0x98B34, 0x00000000, byte_count=4)
        self._write_bytes_from_int(0x98B38, 0x00000000, byte_count=4)
        self._write_bytes_from_int(0x98B3C, 0x00000000, byte_count=4)

    def jiggy_count_win_condition(self, item_count:int):
        '''
        Modifies the number of Jiggies required to warp the player to the
        Beach 100 Jiggies cutscene. Typically used with 'Remove Defeated
        Gruntilda Check' function.
        '''
        # jiggyscore_total() == 100
        # Instance
        self._write_bytes_from_int(0x15C8B, item_count, byte_count=1)
        # Instance
        self._write_bytes_from_int(0x15CF7, item_count, byte_count=1)
        # Instance
        self._write_bytes_from_int(0x15DA7, item_count, byte_count=1)
        # Instance
        self._write_bytes_from_int(0x29E1F, item_count, byte_count=1)
        # Instance
        self._write_bytes_from_int(0x29FAF, item_count, byte_count=1)
        # Instance
        self._write_bytes_from_int(0x98B4F, item_count, byte_count=1)
    
    def note_count_win_condition(self, item_count):
        '''
        Replaces the Jiggy count that warps the player to the Beach 100
        Jiggies cutscene with a Note count.
        Decomp: code_BEF20.c#L388
        '''
        ########################
        ### Note Requirement ###
        ########################
        ### (level_get() == LEVEL_1_MUMBOS_MOUNTAIN) && (note_count == 50)
        ### ->
        ### itemscore_noteScores_getTotal() == item_count
        # itemscore_noteScores_getTotal()
        self._write_bytes_from_int(0xBFE70, 0x0C0D1BBB, byte_count=4)
         # item_count
        self._write_bytes_from_int(0xBFE78, 0x2401, byte_count=2)
        self._write_bytes_from_int(0xBFE7A, item_count, byte_count=2)
        # BNE
        # self._write_bytes_from_int(0xBFE7C, 0x1441000A, byte_count=4)
        # note_count == 50 -> Removed
        self._write_bytes_from_int(0xBFE80, 0x00000000, byte_count=4)
        self._write_bytes_from_int(0xBFE84, 0x00000000, byte_count=4)
        self._write_bytes_from_int(0xBFE88, 0x00000000, byte_count=4)
        ################
        ### Cutscene ###
        ################
        ### func_80311480(0xF74, 4, NULL, NULL, NULL, NULL);
        ### ->
        ### func_802E4078(MAP_95_CS_END_ALL_100, 0, 1);
        # 2 (Might not be needed? Idk...)
        self._write_bytes_from_int(0xBFE8C, 0x24040002, byte_count=4)
        # MAP_95_CS_END_ALL_100
        self._write_bytes_from_int(0xBFE90, 0x24040095, byte_count=4)
        # 0
        self._write_bytes_from_int(0xBFE94, 0x00002825, byte_count=4)
        # func_802E4078()
        self._write_bytes_from_int(0xBFE98, 0x0C0B901E, byte_count=4)
        # 1
        self._write_bytes_from_int(0xBFE9C, 0x24060001, byte_count=4)
        # Is This Needed? func_8029CBC4
        self._write_bytes_from_int(0xBFEA0, 0x0C0A6299, byte_count=4)
    
    def collectathon_win_condition(self,
            jiggy_score:int=0x7FFF,
            note_score:int=0x7FFF,
            empty_honeycomb_score:int=0x7FFF,
            mumbo_token_score:int=0x7FFF):
        '''
        ACCIDENTALLY WROTE THIS IN SPIRAL MOUNTAIN CODE
        GOTTA FIGURE OUT A PLACE FOR GAME ENGINE/C LIBRARIES
        '''
        # 0C0D17E8 -> item_getCount()
        # 0C0C848F -> jiggyscore_total()
        # 0C0D1BBB -> itemscore_noteScores_getTotal()
        # 0C0C8527 -> honeycombscore_get_total()
        # 0C0C8599 -> mumboscore_get_total()
        # Jiggies
        self._write_bytes_from_int(0x0, 0x0C0C848F, byte_count=4) # jiggyscore_total()
        self._write_bytes_from_int(0x0, 0x00000000, byte_count=4) # null
        self._write_bytes_from_int(0x0, 0x2404,     byte_count=2) # ADDIU 4, 0, jiggy_score
        self._write_bytes_from_int(0x0, jiggy_score, byte_count=2)
        self._write_bytes_from_int(0x0, 0x2C830001, byte_count=4) # SLTI 3, 2, 4
        self._write_bytes_from_int(0x0, 0x50600011, byte_count=4) # BEQL 3, 0, 11
        # Notes
        self._write_bytes_from_int(0x0, 0x0C0D1BBB, byte_count=4) # itemscore_noteScores_getTotal()
        self._write_bytes_from_int(0x0, 0x00000000, byte_count=4) # null
        self._write_bytes_from_int(0x0, 0x2404,     byte_count=2) # ADDIU 4, 0, note_score
        self._write_bytes_from_int(0x0, note_score, byte_count=2)
        self._write_bytes_from_int(0x0, 0x2C830001, byte_count=4) # SLTI 3, 2, 4
        self._write_bytes_from_int(0x0, 0x5060000C, byte_count=4) # BEQL 3, 0, C
        # Empty Honeycombs
        self._write_bytes_from_int(0x0, 0x0C0C8527, byte_count=4) # honeycombscore_get_total()
        self._write_bytes_from_int(0x0, 0x00000000, byte_count=4) # null
        self._write_bytes_from_int(0x0, 0x2404,     byte_count=2) # ADDIU 4, 0, empty_honeycomb_score
        self._write_bytes_from_int(0x0, empty_honeycomb_score, byte_count=2)
        self._write_bytes_from_int(0x0, 0x2C830001, byte_count=4) # SLTI 3, 2, 4
        self._write_bytes_from_int(0x0, 0x50600007, byte_count=4) # BEQL 3, 0, 7
        # Mumbo Tokens
        self._write_bytes_from_int(0x0, 0x0C0C8599, byte_count=4) # mumboscore_get_total()
        self._write_bytes_from_int(0x0, 0x00000000, byte_count=4) # null
        self._write_bytes_from_int(0x0, 0x2404,     byte_count=2) # ADDIU 4, 0, mumbo_token_score
        self._write_bytes_from_int(0x0, mumbo_token_score, byte_count=2)
        self._write_bytes_from_int(0x0, 0x2C830001, byte_count=4) # SLTI 3, 2, 4
        self._write_bytes_from_int(0x0, 0x50600002, byte_count=4) # BEQL 3, 0, 2
        # Return True
        self._write_bytes_from_int(0x0, 0x03E00008, byte_count=4) # return
        self._write_bytes_from_int(0x0, 0x24020001, byte_count=4) # 1
        # Return False
        self._write_bytes_from_int(0x0, 0x03E00008, byte_count=4) # return
        self._write_bytes_from_int(0x0, 0x00001025, byte_count=4) # 0
        # Return Null (Shouldn't Ever Happen)
        # self._write_bytes_from_int(0x2AB8, 0x03E00008, byte_count=4) # return
        # self._write_bytes_from_int(0x2ABC, 0x00000000, byte_count=4) # null

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
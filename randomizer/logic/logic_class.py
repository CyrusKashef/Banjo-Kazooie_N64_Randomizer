###################
##### IMPORTS #####
###################

from randomizer.constants.int_values.transformation_enums import TRANSFORMATION_ENUMS as TRANSFORMATION
from randomizer.constants.int_values.ability_enums import ABILITY_ENUMS as ABILITY
from randomizer.constants.int_values.location_enums import LOCATION_ENUMS as LOCATION
from randomizer.constants.int_values.region_enums import REGION_ENUMS as REGION
from randomizer.constants.int_values.level_enums import LEVEL_ID_ENUMS as LEVEL
from randomizer.constants.int_values.warp_enums import WARP_ENUMS as WARP
from randomizer.constants.int_values.map_enums import MAP_ENUMS as MAP
from randomizer.constants.int_values.logic_difficulty_enums import LOGIC_DIFFICULTY_ENUMS as DIFFICULTY
from randomizer.constants.int_values.jiggy_enums import JIGGY_ENUMS as JIGGY
from randomizer.constants.int_values.empty_honeycomb_enums import EMPTY_HONEYCOMB_ENUMS as EMPTY_HONEYCOMB
# from randomizer.constants.int_values.mumbo_token_enums import MUMBO_TOKEN_ENUMS as MUMBO_TOKEN
from randomizer.constants.int_values.item_type_enums import ITEM_TYPE_ENUMS as ITEM_TYPE

from randomizer.logic.location_class import LOCATION_CLASS
from randomizer.logic.warp_class import WARP_CLASS
from randomizer.logic.region_class import REGION_CLASS
from randomizer.logic.level_class import LEVEL_CLASS

from randomizer.constants.logic_objects.spiral_mountain_level import SPIRAL_MOUNTAIN_LEVEL
from randomizer.constants.logic_objects.mumbos_mountain_level import MUMBOS_MOUNTAIN_LEVEL
from randomizer.constants.logic_objects.gruntildas_lair_level import GRUNTILDAS_LAIR_LEVEL

#######################
##### LOGIC CLASS #####
#######################

class LOGIC_CLASS():
    def __init__(self,
            seed_val:int,
            game_start_region:REGION,
            difficulty_val:DIFFICULTY,
            win_condition:function):
        # CONSTANTS
        self.world_dict:dict = {
            LEVEL.spiral_mountain: SPIRAL_MOUNTAIN_LEVEL,
            LEVEL.mumbos_mountain: MUMBOS_MOUNTAIN_LEVEL,
            LEVEL.gruntildas_lair: GRUNTILDAS_LAIR_LEVEL,
        }
        # VARIABLES
        self.seed_val:int = seed_val
        self.game_start_region:REGION = game_start_region
        self.win_condition = win_condition
        # Setup
        self.item_dict:dict = {}
        self.settings_dict:dict = {}
        self.item_count:dict = {}
        self.setup_item_dict()
        self.setup_item_count_dict()
        self.setup_settings_dict(difficulty_val)
    
    #################
    ##### SETUP #####
    #################

    def setup_item_dict(self):
        '''
        Pass
        '''
        for curr_transformation in TRANSFORMATION:
            self.item_dict[curr_transformation] = False
        for curr_ability in ABILITY:
            self.item_dict[curr_ability] = False
        for curr_jiggy in JIGGY:
            self.item_dict[curr_jiggy] = False
        for curr_empty_honeycomb in EMPTY_HONEYCOMB:
            self.item_dict[curr_empty_honeycomb] = False
        # for curr_mumbo_token in MUMBO_TOKEN:
        #     self.item_dict[curr_mumbo_token] = False

    def setup_item_count_dict(self):
        '''
        Pass
        '''
        for curr_item_type in ITEM_TYPE:
            for curr_level in LEVEL:
                self.item_count[curr_level][curr_item_type] = 0
    
    def setup_settings_dict(self, difficulty_val:DIFFICULTY):
        '''
        Pass
        '''
        for curr_difficulty in DIFFICULTY:
            self.settings_dict[curr_difficulty] = False
            if(curr_difficulty <= difficulty_val):
                self.settings_dict[curr_difficulty] = True

    ##################
    ##### TOTALS #####
    ##################

    def get_current_level_item_counts(self, curr_level:LEVEL):
        '''
        Pass
        '''
        curr_note_count:int = 0
        jiggy_id_list:list = []
        empty_honeycomb_id_list:list = []
        ##### OBTAIN ITEMS #####
        curr_jiggy_count:int = len(set(jiggy_id_list))
        curr_empty_honeycomb_count:int = len(set(empty_honeycomb_id_list))
        return curr_note_count, curr_jiggy_count, curr_empty_honeycomb_count

    def get_previous_level_item_counts(self, curr_level:LEVEL):
        '''
        Pass
        '''
        prev_note_count:int = self.item_count[curr_level][ITEM_TYPE.musical_note]
        prev_jiggy_count:int = self.item_count[curr_level][ITEM_TYPE.jiggy]
        prev_empty_honeycomb_count:int = self.item_count[curr_level][ITEM_TYPE.empty_honeycomb]
        return prev_note_count, prev_jiggy_count, prev_empty_honeycomb_count

    def check_counts_for_change(self,
            curr_note_count:int, curr_jiggy_count:int, curr_empty_honeycomb_count:int,
            prev_note_count:int, prev_jiggy_count:int, prev_empty_honeycomb_count:int
            ):
        '''
        Pass
        '''
        note_count_changed:bool = (curr_note_count != prev_note_count)
        jiggy_count_changed:bool = (curr_jiggy_count != prev_jiggy_count)
        empty_honeycomb_count_changed:bool = (curr_empty_honeycomb_count != prev_empty_honeycomb_count)
        count_change_found:bool = note_count_changed or jiggy_count_changed or empty_honeycomb_count_changed
        return count_change_found

    def update_game_totals_items_count(self):
        '''
        Pass
        '''
        change_found:bool = False
        for curr_level in LEVEL:
            # Get Current Counts
            curr_note_count, curr_jiggy_count, curr_empty_honeycomb_count = \
                self.get_current_level_item_counts(curr_level)
            # Get Previous Counts
            prev_note_count, prev_jiggy_count, prev_empty_honeycomb_count = \
                self.get_previous_level_item_counts(curr_level)
            # Check For Change
            level_change_found:bool = self.check_counts_for_change(
                curr_note_count, curr_jiggy_count, curr_empty_honeycomb_count,
                prev_note_count, prev_jiggy_count, prev_empty_honeycomb_count)
            if(level_change_found):
                change_found:bool = True
            # Update Counts
            self.item_count[curr_level][ITEM_TYPE.musical_note] = curr_note_count
            self.item_count[curr_level][ITEM_TYPE.jiggy] = curr_jiggy_count
            self.item_count[curr_level][ITEM_TYPE.empty_honeycomb] = curr_empty_honeycomb_count
        return change_found

    #####################
    ##### SOMETHING #####
    #####################

    def logic_loop(self):
        '''
        Pass
        '''
        change_is_made:bool = True
        win_condition_met:bool = False
        while(change_is_made and not win_condition_met):
            # Update Current Reachable Locations
            # Update Current Obtainable Items
            # Update Current Totals
            # Check Win Condition
            pass

    def check_win_condition_met(self):
        '''
        Pass
        '''
        return self.win_condition(self.item_dict, self.item_count)

################
##### MAIN #####
################

if __name__ == '__main__':
    # Trotless % = 100% Spiral Mountain + 100% Mumbos Mountain
    trotless_win_condition = (lambda item_dict, item_count:
            (item_count[LEVEL.spiral_mountain][ITEM_TYPE.empty_honeycomb] == 6) and
            (item_count[LEVEL.mumbos_mountain][ITEM_TYPE.jiggy] == 10) and
            (item_count[LEVEL.mumbos_mountain][ITEM_TYPE.empty_honeycomb] == 2) and
            (item_count[LEVEL.mumbos_mountain][ITEM_TYPE.musical_note] == 100) and
            item_dict[JIGGY.gruntildas_lair_1st_jiggy] and
            item_dict[JIGGY.gruntildas_lair_mumbos_mountain_witch_switch]
        )
    game_region_start = REGION.Spiral_Mountain_Main
    difficulty_val = DIFFICULTY.casual
    logic_obj = LOGIC_CLASS(
        seed_val=69420,
        game_start_region=game_region_start,
        difficulty_val=difficulty_val,
        win_condition=trotless_win_condition
    )
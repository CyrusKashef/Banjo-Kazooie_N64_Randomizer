###################
##### IMPORTS #####
###################

import random

from randomizer.constants.int_values.logic_difficulty_enums import LOGIC_DIFFICULTY_ENUMS as DIFFICULTY
from randomizer.constants.int_values.transformation_enums import TRANSFORMATION_ENUMS as TRANSFORMATION
from randomizer.constants.int_values.ability_enums import ABILITY_ENUMS as ABILITY
from randomizer.constants.int_values.location_enums import LOCATION_ENUMS as LOCATION
from randomizer.constants.int_values.region_enums import REGION_ENUMS as REGION
from randomizer.constants.int_values.level_enums import LEVEL_ID_ENUMS as LEVEL
from randomizer.constants.int_values.warp_enums import WARP_ENUMS as WARP
from randomizer.constants.int_values.map_enums import MAP_ENUMS as MAP

from randomizer.constants.int_values.item_type_enums import ITEM_TYPE_ENUMS as ITEM_TYPE
from randomizer.constants.int_values.jiggy_enums import JIGGY_ENUMS as JIGGY
from randomizer.constants.int_values.empty_honeycomb_enums import EMPTY_HONEYCOMB_ENUMS as EMPTY_HONEYCOMB
from randomizer.constants.int_values.mumbo_token_enums import MUMBO_TOKEN_ENUMS as MUMBO_TOKEN
from randomizer.constants.int_values.logic_item_enums import LOGIC_ITEM_ENUMS as LOGIC_ITEM

from randomizer.constants.logic_values.allowed_item_types import ALLOWED_ITEM_TYPE

from randomizer.logic.location_class import LOCATION_CLASS
from randomizer.logic.warp_class import WARP_CLASS
from randomizer.logic.region_class import REGION_CLASS
from randomizer.logic.level_class import LEVEL_CLASS
from randomizer.logic.item_class import ITEM_CLASS

from randomizer.constants.logic_values.spiral_mountain.spiral_mountain_level import SPIRAL_MOUNTAIN_LEVEL
# from randomizer.constants.logic_objects.mumbos_mountain_level import MUMBOS_MOUNTAIN_LEVEL
# from randomizer.constants.logic_objects.gruntildas_lair_level import GRUNTILDAS_LAIR_LEVEL

from randomizer.constants.logic_values.logic_items import ABILITY_ITEMS_LIST
from randomizer.constants.logic_values.spiral_mountain.spiral_mountain_items import SPIRAL_MOUNTAIN_ITEMS

#######################
##### LOGIC CLASS #####
#######################

class LOGIC_CLASS():
    def __init__(self,
            seed_value:int,
            jigsaw_puzzle_costs:dict,
            transformation_costs:dict,
            note_door_costs:dict,
            win_condition:list,
            game_start_region:REGION,
            seed_difficulty:DIFFICULTY,
            starting_game_items:list):
        '''
        Pass
        '''
        # CONSTANT PRIOR TO LOGIC
        self.initial_seed_value:int = seed_value
        self.jigsaw_puzzle_costs:dict = jigsaw_puzzle_costs
        self.transformation_costs:dict = transformation_costs
        self.note_door_costs:dict = note_door_costs
        self.win_condition:list = win_condition
        self.game_start_region:REGION = game_start_region
        self.seed_difficulty:DIFFICULTY = seed_difficulty
        self.starting_game_items:list = starting_game_items
        # SET, BUT MUTABLE
        self.levels:dict = {
            LEVEL.spiral_mountain: SPIRAL_MOUNTAIN_LEVEL,
        }
        self.world_items:dict = {
            LEVEL.spiral_mountain: SPIRAL_MOUNTAIN_ITEMS,
        }
        self.items:dict = {}
        self.seed_increment_value:int = 0
        self.restart_seed_count:int = 0
    
    ###################
    ##### GETTERS #####
    ###################

    def calculate_reachable_regions(self):
        '''
        Pass
        '''
        pass

    def calculate_obtainable_items(self):
        '''
        Pass
        '''
        pass

    def calculate_progression_items(self):
        '''
        Pass
        '''
        pass

    ###################
    ##### SETTERS #####
    ###################

    def reset_items(self):
        '''
        Pass
        '''
        for current_item in ABILITY_ITEMS_LIST:
            current_item.reset_item()
            item_enum:LOGIC_ITEM = current_item.get_item_enum()
            self.items[item_enum] = current_item
        for current_item in SPIRAL_MOUNTAIN_ITEMS:
            current_item.reset_item()
            item_enum:LOGIC_ITEM = current_item.get_item_enum()
            self.items[item_enum] = current_item
    
    def set_starting_game_items(self):
        '''
        Pass
        '''
        for current_item_enum in self.starting_game_items:
            current_item:ITEM_CLASS = self.items[current_item_enum]
            current_item.set_item_as_obtained()
    
    def set_starting_region(self):
        '''
        Pass
        '''
        start_region_found:bool = False
        for level_enum in self.levels:
            level:LEVEL_CLASS = self.levels[level_enum]
            level_regions:dict = level.get_level_regions()
            if(self.game_start_region in level_regions):
                start_region:REGION_CLASS = level_regions[self.game_start_region]
                start_region.add_accessible_transformation(TRANSFORMATION.banjo_kazooie)
                start_region_found:bool = True
        if(not start_region_found):
            print("Cannot Find Start Region")
            exit(0)

    def allocate_warps(self):
        '''
        Pass
        '''
        pass

    def allocate_items(self):
        '''
        Pass
        '''
        pass

    ###################
    ##### UTILITY #####
    ###################

    def _select_random_from_list(self, select_list:list):
        '''
        Pass
        '''
        random.seed(a=(self.seed_value + self.seed_increment_value))
        random_choice = random.choice(select_list)
        self.seed_increment_value += 1
        return random_choice

    def _shuffle_list(self, select_list:list):
        '''
        Pass
        '''
        random.seed(a=(self.initial_seed_value + self.seed_increment_value))
        random.shuffle(select_list)
        self.seed_increment_value += 1
        return select_list

    def _requirements_met(self, requirements:list):
        '''
        Checks each requirement in the requirements list
        to see if the player has reached that requirement.
        If the requirement is a tuple itself, perform recursive.

        Returns whether the player has met enough requirements.
        '''
        for requirement in requirements:
            if(isinstance(requirement, tuple)):
                tuple_requirements_met:bool = \
                    self._requirements_met(requirement)
                if(tuple_requirements_met is False):
                    return False
                continue
            curr_item:ITEM_CLASS = self.items[requirement]
            item_obtained:bool = curr_item.is_item_obtained()
            if(item_obtained is False):
                return False
        return True

    def check_win_condition_met(self):
        '''
        Pass
        '''
        win_condition_met:bool = self._requirements_met(self.win_condition)
        return win_condition_met
    
    def check_all_worlds_accessible(self):
        '''
        Pass
        '''
        # For SM Testing
        return True
        all_worlds_accessible:bool = (
            self.items[LOGIC_ITEM.gruntildas_lair_open_first_world] and
            self.items[LOGIC_ITEM.gruntildas_lair_open_second_world] and
            self.items[LOGIC_ITEM.gruntildas_lair_open_third_world] and
            self.items[LOGIC_ITEM.gruntildas_lair_open_fourth_world] and
            self.items[LOGIC_ITEM.gruntildas_lair_open_fifth_world] and
            self.items[LOGIC_ITEM.gruntildas_lair_open_sixth_world] and
            self.items[LOGIC_ITEM.gruntildas_lair_open_seventh_world] and
            self.items[LOGIC_ITEM.gruntildas_lair_open_eighth_world] and
            self.items[LOGIC_ITEM.gruntildas_lair_open_ninth_world] and
            self.items[LOGIC_ITEM.gruntildas_lair_open_final_battle])
        return all_worlds_accessible

    def get_items_count(self):
        '''
        Pass
        '''
        items_count:int = 0
        for item in self.items:
            if(self.items[item]):
                items_count += 1
        return items_count

    ###############
    ##### RUN #####
    ###############

    def connecting_region_logic(self):
        '''
        Pass
        '''
        change_was_made:bool = False
        for level_enum in self.levels:
            level:LEVEL_CLASS = self.levels[level_enum]
            level_regions:dict = level.get_level_regions()
            for region_enum in level_regions:
                current_region:REGION_CLASS = level_regions[region_enum]
                region_accessible:bool = (len(current_region.get_accessed_transformations()) > 0)
                if(not region_accessible):
                    continue
                connected_non_warp_regions:dict = current_region.get_connected_non_warp_regions()
                for connected_non_warp_region_enum in connected_non_warp_regions:
                    connected_region:REGION_CLASS = level_regions[connected_non_warp_region_enum]
                    for transformation in current_region.get_accessed_transformations():
                        if(connected_region.can_transformation_already_access_region(transformation)):
                            continue
                        transformation_can_access:bool = \
                            current_region.can_transformation_access_connected_region(
                                connected_region=connected_non_warp_region_enum,
                                transformation=transformation,
                                items=self.items
                            )
                        if(transformation_can_access):
                            connected_region.add_accessible_transformation(transformation)
                            change_was_made = True
        if(change_was_made):
            self.connecting_region_logic()

    def warp_assignment_logic(self):
        '''
        Pass
        '''
        pass

    def progression_item_logic(self):
        '''
        Pass
        '''
        # Calculate Required Items For Next World
        # Place Required Items
        # Record New Obtainable Items
        pass
    
    def _filter_remaining_items(self, level_enum:LEVEL, item_type:ALLOWED_ITEM_TYPE):
        '''
        Pass
        '''
        item_list:list = []
        level_items:list = self.world_items[level_enum]
        for current_item in level_items:
            already_accounted_for:bool = (current_item.is_item_placed() or current_item.is_item_obtained())
            if(already_accounted_for):
                continue
            if(current_item.get_item_type() in item_type.value):
                item_list.append(current_item)
        return item_list

    def _filter_remaining_regions(self, level_enum:LEVEL, item_type_list:ALLOWED_ITEM_TYPE):
        '''
        Pass
        '''
        region_list:list = []
        level:LEVEL_CLASS = self.levels[level_enum]
        for region_enum in level.get_level_regions():
            region:REGION_CLASS = level.get_level_region(region_enum)
            for location_enum in region.get_region_locations():
                location:LOCATION_CLASS = region.get_region_location(location_enum)
                if(location.get_set_item() is not None):
                    continue
                location_allowed_item_types:list = location.get_allowed_item_types()
                incompatible_type_found:bool = False
                for item_type in location_allowed_item_types.value:
                    if(item_type not in item_type_list.value):
                        incompatible_type_found:bool = True 
                        break
                if(incompatible_type_found is False):
                    region_list.append(region_enum)
                    break
        return region_list

    def _set_items_in_item_type(self, level_enum:LEVEL, item_list:list, region_list:list):
        '''
        Pass
        '''
        level:LEVEL_CLASS = self.levels[level_enum]
        for region_enum in level.get_level_regions():
            region:REGION_CLASS = level.get_level_region(region_enum)
            for location_enum in region.get_region_locations():
                location:LOCATION_CLASS = region.get_region_location(location_enum)
                if(location.get_set_item() is not None):
                    continue
                for current_item in item_list:
                    already_accounted_for:bool = (current_item.is_item_placed() or current_item.is_item_obtained())
                    if(already_accounted_for):
                        continue

    def remaining_item_logic(self):
        '''
        Pass
        '''
        print("Placing Remaining Items")
        # Select Locations By Restrictiveness
        # Filter Items
        # Randomly Select Item
        for level_enum in self.levels:
            for item_type in ALLOWED_ITEM_TYPE:
                print(f"\nItem Type: '{item_type}'")
                item_list:list = self._filter_remaining_items(level_enum, item_type)
                no_item_of_this_type_left:bool = (len(item_list) == 0)
                if(no_item_of_this_type_left):
                    continue
                region_list:list = self._filter_remaining_regions(level_enum, item_type)
                no_locations_of_this_type_left:bool = (len(region_list) == 0)
                if(no_locations_of_this_type_left):
                    continue
                item_list:list = self._shuffle_list(item_list)
                region_list:list = self._shuffle_list(region_list)
                self._set_items_in_item_type(item_list, region_list)
        # Place General Items

    def check_event_items(self):
        '''
        Pass
        '''
        pass

    def set_starting_logic(self):
        '''
        Pass
        '''
        self.reset_items()
        self.set_starting_game_items()
        self.set_starting_region()

    def start_logic(self):
        '''
        Pass
        '''
        print("Start Logic")
        self.set_starting_logic()
        items_count:int = self.get_items_count()
        while(not self.check_win_condition_met() and
              # not self.check_all_worlds_accessible() and
              (self.restart_seed_count < 1)):
            self.connecting_region_logic()
            self.warp_assignment_logic()
            self.progression_item_logic()
            new_items_count:int = self.get_items_count()
            if(items_count == new_items_count):
                self.restart_seed_count += 1
                print(f"Restarting Seed; Count {self.restart_seed_count}")
                self.start_logic()
        if(self.restart_seed_count > 0):
            # print("Seed Generation Failed")
            # exit(0)
            pass
        self.remaining_item_logic()
        if(not self.check_win_condition_met()):
            print("Seed Generation Failed")
            exit(0)
        print("End Logic")

################
##### MAIN #####
################

if __name__ == '__main__':
    ##################
    ### SEED VALUE ###
    ##################
    seed_value:int = 42069
    ###########################
    ### JIGSAW PUZZLE COSTS ###
    ###########################
    jigsaw_puzzle_costs:dict = {
        LOGIC_ITEM.gruntildas_lair_open_first_world: 1,
        LOGIC_ITEM.gruntildas_lair_open_second_world: 2,
        LOGIC_ITEM.gruntildas_lair_open_third_world: 5,
        LOGIC_ITEM.gruntildas_lair_open_fourth_world: 7,
        LOGIC_ITEM.gruntildas_lair_open_fifth_world: 8,
        LOGIC_ITEM.gruntildas_lair_open_sixth_world: 9,
        LOGIC_ITEM.gruntildas_lair_open_seventh_world: 10,
        LOGIC_ITEM.gruntildas_lair_open_eighth_world: 12,
        LOGIC_ITEM.gruntildas_lair_open_ninth_world: 15,
        LOGIC_ITEM.gruntildas_lair_open_final_battle: 25,
    }
    ############################
    ### TRANSFORMATION COSTS ###
    ############################
    transformation_costs:dict = {
        LOGIC_ITEM.transformation_termite: 5,
        LOGIC_ITEM.transformation_crocodile: 10,
        LOGIC_ITEM.transformation_walrus: 15,
        LOGIC_ITEM.transformation_pumpkin: 20,
        LOGIC_ITEM.transformation_bee: 25,
    }
    #######################
    ### NOTE DOOR COSTS ###
    #######################
    note_door_costs:dict = {
        LOGIC_ITEM.gruntildas_lair_open_first_note_door: 50,
        LOGIC_ITEM.gruntildas_lair_open_second_note_door: 180,
        LOGIC_ITEM.gruntildas_lair_open_third_note_door: 270,
        LOGIC_ITEM.gruntildas_lair_open_fourth_note_door: 350,
        LOGIC_ITEM.gruntildas_lair_open_fifth_note_door: 450,
        LOGIC_ITEM.gruntildas_lair_open_sixth_note_door: 640,
        LOGIC_ITEM.gruntildas_lair_open_seventh_note_door: 765,
        LOGIC_ITEM.gruntildas_lair_open_eighth_note_door: 810,
        LOGIC_ITEM.gruntildas_lair_open_ninth_note_door: 0,
        LOGIC_ITEM.gruntildas_lair_open_tenth_note_door: 0,
        LOGIC_ITEM.gruntildas_lair_open_eleventh_note_door: 0,
        LOGIC_ITEM.gruntildas_lair_open_twelfth_note_door: 0,
    }
    #####################
    ### WIN CONDITION ###
    #####################
    win_condition = [
        LOGIC_ITEM.spiral_mountain_empty_honeycomb_atop_tree,
        LOGIC_ITEM.spiral_mountain_empty_honeycomb_colliwobble,
        LOGIC_ITEM.spiral_mountain_empty_honeycomb_quarries,
        LOGIC_ITEM.spiral_mountain_empty_honeycomb_stump,
        LOGIC_ITEM.spiral_mountain_empty_honeycomb_underwater,
        LOGIC_ITEM.spiral_mountain_empty_honeycomb_waterfall,
    ]
    #############
    ### LOGIC ###
    #############
    logic_obj:LOGIC_CLASS = LOGIC_CLASS(
        seed_value=42069,
        jigsaw_puzzle_costs=jigsaw_puzzle_costs,
        transformation_costs=transformation_costs,
        note_door_costs=note_door_costs,
        win_condition=win_condition,
        game_start_region=REGION.Spiral_Mountain_Main,
        seed_difficulty=DIFFICULTY.beginner,
        starting_game_items=[]
    )
    logic_obj.start_logic()
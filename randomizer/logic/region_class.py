###################
##### IMPORTS #####
###################

# Enums

from randomizer.constants.int_values.region_enums import REGION_ENUMS as REGION
from randomizer.constants.int_values.warp_enums import WARP_ENUMS as WARP
from randomizer.constants.int_values.location_enums import LOCATION_ENUMS as LOCATION

from randomizer.constants.int_values.transformation_enums import TRANSFORMATION_ENUMS as TRANSFORMATION
from randomizer.constants.int_values.item_type_enums import ITEM_TYPE_ENUMS as EVENT
from randomizer.constants.int_values.level_enums import LEVEL_ID_ENUMS as LEVEL
from randomizer.constants.int_values.jiggy_enums import JIGGY_ENUMS as JIGGY
from randomizer.constants.int_values.empty_honeycomb_enums import EMPTY_HONEYCOMB_ENUMS as EMPTY_HONEYCOMB
from randomizer.constants.int_values.mumbo_token_enums import MUMBO_TOKEN_ENUMS as MUMBO_TOKEN
from randomizer.constants.int_values.item_type_enums import ITEM_TYPE_ENUMS as ITEM_TYPE
from randomizer.constants.int_values.logic_difficulty_enums import LOGIC_DIFFICULTY_ENUMS as DIFFICULTY

# Classes

from randomizer.logic.location_class import LOCATION_CLASS
from randomizer.logic.item_class import ITEM_CLASS
from randomizer.logic.warp_class import WARP_CLASS

########################
##### REGION CLASS #####
########################

class REGION_CLASS():
    def __init__(self,
            debug_name:str,
            region_enum:REGION,
            allowed_transformations:list,
            required_transformation_access:list,
            transformation_pad:TRANSFORMATION|None,
            detransformation_zone:bool,
            connected_non_warp_regions:dict,
            locations:dict,
            warp_exits:dict):
        '''
        Pass
        '''
        # DEVELOPER VALUES
        self.debug_name:str = debug_name
        self.region_enum:int = region_enum
        # ACCESS/OBTAIN REQUIREMENTS
        self.allowed_transformations:list = allowed_transformations
        self.required_transformation_access:list = required_transformation_access
        # CONSTANT PRIOR TO LOGIC
        self.transformation_pad:TRANSFORMATION|None = transformation_pad
        self.detransformation_zone:bool = detransformation_zone
        self.connected_non_warp_regions:dict = connected_non_warp_regions
        # SET, BUT MUTABLE
        self.locations:dict = locations
        self.warp_exits:dict = warp_exits
        # SET DURING LOGIC
        self.accessed_transformations:list = []
    
    ###################
    ##### GETTERS #####
    ###################

    def get_debug_name(self):
        '''
        Pass
        '''
        return self.debug_name

    def get_region_enum(self):
        '''
        Pass
        '''
        return self.region_enum

    def get_allowed_transformations(self):
        '''
        Pass
        '''
        return self.allowed_transformationsl

    def get_required_transformation_access(self):
        '''
        Pass
        '''
        return self.required_transformation_access

    def get_transformation_pad(self):
        '''
        Pass
        '''
        return self.transformation_pad

    def is_detransformation_zone(self):
        '''
        Pass
        '''
        return self.detransformation_zone
    
    def get_connected_non_warp_regions(self):
        '''
        Pass
        '''
        return self.connected_non_warp_regions

    def get_accessed_transformations(self):
        '''
        Pass
        '''
        return self.accessed_transformations
    
    def can_transformation_already_access_region(self, transformation:TRANSFORMATION):
        '''
        Pass
        '''
        return (transformation in self.get_accessed_transformations())

    def get_region_location(self, location_enum:LOCATION_CLASS):
        '''
        Pass
        '''
        return self.locations[location_enum]

    def get_region_locations(self):
        '''
        Pass
        '''
        return self.locations

    ###################
    ##### SETTERS #####
    ###################

    def reset_region(self):
        '''
        Pass
        '''
        self.accessed_transformations:list = []

    # Accessibility

    def add_accessible_transformation(self, transformation:TRANSFORMATION):
        '''
        Pass
        '''
        if(transformation not in self.get_accessed_transformations()):
            self.accessed_transformations.append(transformation)

    # Locations & Items

    def set_selected_item_to_location(self, location_enum:LOCATION, item:ITEM_CLASS):
        '''
        Pass
        '''
        location:LOCATION_CLASS = self.locations[location_enum]
        location.set_specifed_item(item)

    def set_default_item_to_location(self, location_enum:LOCATION):
        '''
        Pass
        '''
        location:LOCATION_CLASS = self.locations[location_enum]
        location.set_default_item()

    # Warps

    def set_warp_to_selected_region(self, warp_enum:WARP, to_region:REGION):
        '''
        Pass
        '''
        warp:WARP_CLASS = self.warp_exits[warp_enum]
        warp.set_to_selected_region(to_region)

    def set_warp_to_default_region(self, warp_enum:WARP):
        '''
        Pass
        '''
        warp:WARP_CLASS = self.warp_exits[warp_enum]
        warp.set_to_default_region()

    ###################
    ##### UTILITY #####
    ###################

    def would_set_item_be_obtainable(self,
            location_enum:LOCATION,
            item_object:ITEM_CLASS,
            items:dict):
        '''
        Pass
        '''
        location:LOCATION_CLASS = self.locations[location_enum]
        for transformation in self.accessed_transformations:
            location_is_reachable:bool = location.is_location_reachable(transformation, items)
            item_is_obtainable:bool = item_object.is_item_obtainable(transformation, items)
            if(location_is_reachable and item_is_obtainable):
                return True
        return False

    def calculate_obtainable_items(self,
            items:dict,
            difficulty:DIFFICULTY):
        '''
        Pass
        '''
        pass

    def _requirements_met(self,
            requirements:tuple,
            items:dict):
        '''
        Checks each requirement in the requirements list
        to see if the player has reached that requirement.
        If the requirement is a tuple itself, perform recursive.

        Returns whether the player has met enough requirements.
        '''
        for requirement in requirements:
            if(isinstance(requirement, tuple)):
                tuple_requirements_met:bool = \
                    self._requirements_met(requirement, items)
                if(tuple_requirements_met is False):
                    return False
                continue
            curr_item:ITEM_CLASS = items[requirement]
            item_obtained:bool = curr_item.is_item_obtained()
            if(item_obtained is False):
                return False
        return True
    
    def can_transformation_access_connected_region(self,
            connected_region:REGION,
            transformation:TRANSFORMATION,
            items:dict):
        '''
        Pass
        '''
        transformation_requirements = self.connected_non_warp_regions[connected_region][transformation]
        transformation_can_access:bool = self._requirements_met(transformation_requirements, items)
        return transformation_can_access
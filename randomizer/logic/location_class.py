###################
##### IMPORTS #####
###################

# Enums

from randomizer.constants.int_values.transformation_enums import TRANSFORMATION_ENUMS as TRANSFORMATION
from randomizer.constants.int_values.location_enums import LOCATION_ENUMS as LOCATION
from randomizer.constants.int_values.item_type_enums import ITEM_TYPE_ENUMS as ITEM_TYPE
from randomizer.constants.int_values.logic_difficulty_enums import LOGIC_DIFFICULTY_ENUMS as DIFFICULTY

# Classes

from randomizer.logic.item_class import ITEM_CLASS

##########################
##### LOCATION CLASS #####
##########################

class LOCATION_CLASS():
    def __init__(self,
            debug_name:str,
            location_enum:LOCATION,
            reach_requirements:dict,
            default_item:ITEM_CLASS,
            keep_as_default:bool,
            allowed_item_types:list):
        '''
        Pass
        '''
        # DEVELOPER VALUES
        self.debug_name:str = debug_name
        self.location_enum:LOCATION = location_enum
        # ACCESS/OBTAIN REQUIREMENTS
        self.reach_requirements:dict = reach_requirements
        # CONSTANT PRIOR TO LOGIC
        self.default_item:ITEM_CLASS = default_item
        self.keep_as_default:bool = keep_as_default
        self.allowed_item_types:list = allowed_item_types
        # SET, BUT MUTABLE
        self.item_is_obtainable:bool = False
        # SET DURING LOGIC
        self.set_item:ITEM_CLASS = None

    ###################
    ##### GETTERS #####
    ###################

    def get_debug_name(self):
        '''
        Pass
        '''
        return self.debug_name

    def get_location_enum(self):
        '''
        Pass
        '''
        return self.location_enum

    def get_reach_requirements(self):
        '''
        Pass
        '''
        return self.reach_requirements
    
    def get_default_type(self):
        '''
        Pass
        '''
        return self.default_item_type

    def get_default_flag(self):
        '''
        Pass
        '''
        return self.default_item_flag

    def get_allowed_item_types(self):
        '''
        Pass
        '''
        return self.allowed_item_types

    def get_set_item(self):
        '''
        Pass
        '''
        return self.set_item

    ###################
    ##### SETTERS #####
    ###################

    def reset_location(self):
        '''
        Pass
        '''
        self.item_is_obtainable:bool = False
        self.set_item:ITEM_CLASS = None

    def set_specifed_item(self, item:ITEM_CLASS):
        '''
        Pass
        '''
        self.set_item:ITEM_CLASS = item

    def set_default_item(self):
        '''
        Pass
        '''
        self.set_item:ITEM_CLASS = self.default_item

    ###################
    ##### UTILITY #####
    ###################

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

    def is_location_reachable(self,
            transformation:TRANSFORMATION,
            items:dict):
        '''
        Pass
        '''
        transformation_reach_requirement:tuple = self.reach_requirements[transformation]
        is_location_reachable:bool = self._requirements_met(transformation_reach_requirement, items)
        return is_location_reachable

    def is_item_obtainable(self, items:dict):
        '''
        Pass
        '''
        if(self.item_is_obtainable):
            return True
        elif(self.set_item is None):
            return False
        for transformation in self.accessed_transformations:
            location_requirements_met:bool = self.is_location_reachable(transformation, items)
            item_requirements_met:bool = self.set_item.is_item_obtainable(transformation, items)
            set_item_is_obtainable:bool = (location_requirements_met and item_requirements_met)
            if(set_item_is_obtainable):
                return True
        return False
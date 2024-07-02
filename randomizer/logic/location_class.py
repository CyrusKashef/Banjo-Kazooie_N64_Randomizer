###################
##### IMPORTS #####
###################

from randomizer.constants.int_values.transformation_enums import TRANSFORMATION_ENUMS as TRANSFORMATION
from randomizer.constants.int_values.location_enums import LOCATION_ENUMS
from randomizer.constants.int_values.item_type_enums import ITEM_TYPE_ENUMS
from randomizer.logic.item_class import ITEM_CLASS

#################
##### CLASS #####
#################

class LOCATION_CLASS():
    def __init__(self,
            debug_name:str,
            location_enum:LOCATION_ENUMS,
            reach_requirement_dict:dict,
            guaranteed_item:ITEM_TYPE_ENUMS|None=None):
        '''
        Debug Name:
          * Name given to the location for debugging purposes
        Location Enum:
          * Arbitrary value to make location distinct
        Reach Requirement Dict:
          * Dictionary of Transformations (key) and lambdas (values) for reaching the location
        '''
        # Variables
        self.debug_name:str = debug_name
        self.location_enum:LOCATION_ENUMS = location_enum
        self.reach_requirement_dict:dict = reach_requirement_dict
        self.guaranteed_item:ITEM_CLASS|None = guaranteed_item
        # Setup
        self.location_item:ITEM_CLASS|None = None
        if(self.guaranteed_item is not None):
            self.location_item:ITEM_CLASS|None = self.guaranteed_item
        self.item_obtainable:bool = False

    def check_if_item_is_placeable(self,
            curr_item:ITEM_CLASS,
            item_dict:dict, settings_dict:dict):
        '''
        Pass
        '''
        obtain_requirement_dict:dict = curr_item.get_obtain_requirement_dict()
        for curr_transformation in TRANSFORMATION:
            if((curr_transformation not in self.reach_requirement_dict) or
               (curr_transformation not in obtain_requirement_dict)):
                continue
            can_reach:bool = (self.reach_requirement_dict[curr_transformation])(item_dict, settings_dict)
            can_obtain:bool = (obtain_requirement_dict[curr_transformation])(item_dict, settings_dict)
            if(can_reach and can_obtain):
                return True
        return False

    def check_if_item_is_obtainable(self,
            curr_transformation:TRANSFORMATION,
            item_dict:dict, settings_dict:dict):
        '''
        Pass
        '''
        if(self.location_item is None):
            return None
        elif(self.item_obtainable):
            return self.location_item
        can_reach:bool = (self.reach_requirement_dict[curr_transformation])(item_dict, settings_dict)
        can_obtain:bool = self.location_item.check_if_item_is_obtainable()
        if(can_reach and can_obtain):
            self.item_obtainable:bool = True
            return self.location_item
        return None
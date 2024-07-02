###################
##### IMPORTS #####
###################

from randomizer.constants.int_values.transformation_enums import TRANSFORMATION_ENUMS as TRANSFORMATION
from randomizer.constants.int_values.item_type_enums import ITEM_TYPE_ENUMS

#################
##### CLASS #####
#################

class ITEM_CLASS():
    def __init__(self,
            debug_name:str,
            item_type:ITEM_TYPE_ENUMS,
            item_enum:int|None,
            obtain_requirement_dict:dict):
        self.debug_name:str = debug_name
        self.item_type:ITEM_TYPE_ENUMS = item_type
        self.item_enum:int = item_enum
        self.obtain_requirement_dict:dict = obtain_requirement_dict
    
    def get_item_type(self):
        '''
        Pass
        '''
        return self.item_type
    
    def get_item_enum(self):
        '''
        Pass
        '''
        return self.item_enum
    
    def get_obtain_requirement_dict(self):
        '''
        Pass
        '''
        return self.obtain_requirement_dict

    def check_if_item_is_obtainable(self,
            curr_transformation:TRANSFORMATION,
            item_dict:dict, settings_dict:dict):
        '''
        Pass
        '''
        can_obtain:bool = (self.obtain_requirement_dict[curr_transformation])(item_dict, settings_dict)
        return can_obtain
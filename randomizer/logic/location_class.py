###################
##### IMPORTS #####
###################

from randomizer.constants.int_values.transformation_enums import TRANSFORMATION_ENUMS as TRANSFORMATION
from randomizer.constants.int_values.location_enums import LOCATION_ENUMS
from randomizer.constants.int_values.other_item_enums import OTHER_ITEM_ENUMS

#################
##### CLASS #####
#################

class LOCATION_CLASS():
    def __init__(self,
            debug_name:str,
            location_enum:LOCATION_ENUMS,
            reach_requirement_dict:dict,
            guaranteed_item:OTHER_ITEM_ENUMS|None=None):
        '''
        Debug Name:
          * Name given to the location for debugging purposes
        Location Enum:
          * Arbitrary value to make location distinct
        Reach Requirement Dict:
          * Dictionary of Transformations (key) and lambdas (values) for reaching the location
        '''
        self.debug_name:str = debug_name
        self.location_enum:LOCATION_ENUMS = location_enum
        self.reach_requirement_dict:dict = reach_requirement_dict
        self.guaranteed_item:OTHER_ITEM_ENUMS|None = guaranteed_item
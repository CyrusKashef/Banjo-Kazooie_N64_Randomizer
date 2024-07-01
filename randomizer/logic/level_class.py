###################
##### IMPORTS #####
###################

from randomizer.constants.int_values.region_enums import REGION_ENUMS
from randomizer.constants.int_values.level_enums import LEVEL_ID_ENUMS

#################
##### CLASS #####
#################

class LEVEL_CLASS():
    def __init__(self,
            debug_name:str,
            level_enum:LEVEL_ID_ENUMS,
            level_start_region_enum:REGION_ENUMS,
            region_dict:dict):
        self.debug_name:str = debug_name
        self.level_enum:LEVEL_ID_ENUMS = level_enum
        self.level_start_region_enum:REGION_ENUMS = level_start_region_enum
        self.region_dict:dict = region_dict
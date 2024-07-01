###################
##### IMPORTS #####
###################

from randomizer.constants.int_values.warp_enums import WARP_ENUMS
from randomizer.constants.int_values.region_enums import REGION_ENUMS
from randomizer.constants.int_values.map_enums import MAP_ENUMS

#################
##### CLASS #####
#################

class WARP_CLASS():
    def __init__(self,
            debug_name:str,
            warp_enum:WARP_ENUMS,
            default_region_enum:REGION_ENUMS,
            default_warp_to_map:MAP_ENUMS,
            default_warp_to_entry:int,
            allowed_transformations:list):
        self.debug_name:str = debug_name
        self.warp_enum:WARP_ENUMS = warp_enum
        self.default_region_enum:REGION_ENUMS = default_region_enum
        self.default_warp_to_map:MAP_ENUMS = default_warp_to_map
        self.default_warp_to_entry:int = default_warp_to_entry
        self.allowed_transformations:list = allowed_transformations
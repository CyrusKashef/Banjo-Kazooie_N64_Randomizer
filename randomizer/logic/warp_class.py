###################
##### IMPORTS #####
###################

from randomizer.constants.int_values.warp_enums import WARP_ENUMS as WARP
from randomizer.constants.int_values.region_enums import REGION_ENUMS as REGION
from randomizer.constants.int_values.map_enums import MAP_ENUMS as MAP

######################
##### WARP CLASS #####
######################

class WARP_CLASS():
    def __init__(self,
            debug_name:str,
            warp_enum:WARP,
            allowed_transformations:list,
            default_to_region:REGION,
            one_way_warp:bool):
        '''
        Pass
        '''
        # DEVELOPER VALUES
        self.debug_name:str = debug_name
        self.warp_enum:WARP = warp_enum
        # ACCESS/OBTAIN REQUIREMENTS
        self.allowed_transformations:list = allowed_transformations
        # CONSTANT PRIOR TO LOGIC
        self.default_to_region:REGION = default_to_region
        self.one_way_warp:bool = one_way_warp
        # SET, BUT MUTABLE
        # SET DURING LOGIC
        self.set_to_region:REGION = None

    ###################
    ##### GETTERS #####
    ###################

    def get_debug_name(self):
        '''
        Pass
        '''
        return self.debug_name

    def get_warp_enum(self):
        '''
        Pass
        '''
        return self.warp_enum

    def get_allowed_transformations(self):
        '''
        Pass
        '''
        return self.allowed_transformations

    ###################
    ##### SETTERS #####
    ###################

    def set_to_selected_region(self, region:REGION):
        '''
        Pass
        '''
        self.set_to_region:REGION = region

    def set_to_default_region(self):
        '''
        Pass
        '''
        self.set_to_region:REGION = self.default_to_region

    ###################
    ##### UTILITY #####
    ###################
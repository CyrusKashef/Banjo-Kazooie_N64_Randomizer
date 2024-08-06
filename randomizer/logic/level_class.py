###################
##### IMPORTS #####
###################

from randomizer.constants.int_values.region_enums import REGION_ENUMS
from randomizer.constants.int_values.level_enums import LEVEL_ID_ENUMS as LEVEL

#######################
##### LEVEL CLASS #####
#######################

class LEVEL_CLASS():
    def __init__(self,
            debug_name:str,
            level_enum:LEVEL,
            default_start_region:REGION_ENUMS,
            level_regions:dict):
        '''
        Pass
        '''
        # DEVELOPER VALUES
        self.debug_name:str = debug_name
        self.level_enum:LEVEL = level_enum
        # ACCESS/OBTAIN REQUIREMENTS
        # CONSTANT PRIOR TO LOGIC
        self.level_start_region_enum:REGION_ENUMS = default_start_region
        # SET, BUT MUTABLE
        self.level_regions:dict = level_regions
        # SET DURING LOGIC
        self.level_start_region:REGION_ENUMS = None

    ###################
    ##### GETTERS #####
    ###################

    def get_debug_name(self):
        '''
        Pass
        '''
        return self.debug_name

    def get_level_enum(self):
        '''
        Pass
        '''
        return self.level_enum

    def get_level_region(self, region_enum:REGION_ENUMS):
        '''
        Pass
        '''
        return self.level_regions[region_enum]

    def get_level_regions(self):
        '''
        Pass
        '''
        return self.level_regions

    ###################
    ##### SETTERS #####
    ###################

    def set_start_region(self):
        '''
        Pass
        '''
        pass

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

    #####################
    ##### UTILITIES #####
    #####################

    def check_connected_regions(self):
        '''
        Pass
        '''
        pass

    def calculate_obtainable_items(self):
        '''
        Pass
        '''
        pass
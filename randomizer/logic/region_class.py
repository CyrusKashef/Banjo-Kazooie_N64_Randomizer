###################
##### IMPORTS #####
###################

from randomizer.constants.int_values.transformation_enums import TRANSFORMATION_ENUMS
from randomizer.constants.int_values.region_enums import REGION_ENUMS

#################
##### CLASS #####
#################

class REGION_CLASS():
    def __init__(self,
            debug_name:str,
            region_enum:REGION_ENUMS,
            transformation_pad:TRANSFORMATION_ENUMS|None,
            detransformation_zone:bool,
            allowed_transformations:list,
            required_transformation_access:list,
            location_dict:dict,
            connected_non_warp_regions_dict:dict,
            exit_region:dict):
        self.debug_name:str = debug_name
        self.region_enum:int = region_enum
        self.transformation_pad:TRANSFORMATION_ENUMS|None = transformation_pad
        self.detransformation_zone:bool = detransformation_zone
        self.allowed_transformations:list = allowed_transformations
        self.required_transformation_access:list = required_transformation_access
        self.location_dict:dict = location_dict
        self.connected_non_warp_regions_dict:dict = connected_non_warp_regions_dict
        self.exit_region_dict:dict = exit_region
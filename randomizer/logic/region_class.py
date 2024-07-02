###################
##### IMPORTS #####
###################

from randomizer.constants.int_values.transformation_enums import TRANSFORMATION_ENUMS
from randomizer.constants.int_values.region_enums import REGION_ENUMS
from randomizer.constants.int_values.item_type_enums import ITEM_TYPE_ENUMS as ITEM_TYPE
from randomizer.constants.int_values.level_enums import LEVEL_ID_ENUMS as LEVEL
from randomizer.constants.int_values.jiggy_enums import JIGGY_ENUMS as JIGGY
from randomizer.constants.int_values.empty_honeycomb_enums import EMPTY_HONEYCOMB_ENUMS as EMPTY_HONEYCOMB
# from randomizer.constants.int_values.mumbo_token_enums import MUMBO_TOKEN_ENUMS as MUMBO_TOKEN
from randomizer.logic.item_class import ITEM_CLASS

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
    
    def get_region_item_counts(self):
        '''
        Pass
        '''
        curr_note_count:int = 0
        jiggy_id_list:list = []
        empty_honeycomb_id_list:list = []
        for curr_location in self.location_dict:
            location_item:ITEM_CLASS|None = curr_location.check_if_item_is_obtainable()
            if(location_item is None):
                continue
            curr_item_type:ITEM_TYPE = location_item.get_item_type()
            if(curr_item_type is ITEM_TYPE.musical_note):
                curr_note_count += 1
            elif(curr_item_type is ITEM_TYPE.jiggy):
                jiggy_id:JIGGY = location_item.get_item_enum()
                jiggy_id_list.append(jiggy_id)
            elif(curr_item_type is ITEM_TYPE.empty_honeycomb):
                empty_honeycomb_id:EMPTY_HONEYCOMB = location_item.get_item_enum()
                empty_honeycomb_id_list.append(empty_honeycomb_id)
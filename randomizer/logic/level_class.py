###################
##### IMPORTS #####
###################

from randomizer.constants.int_values.region_enums import REGION_ENUMS
from randomizer.constants.int_values.level_enums import LEVEL_ID_ENUMS as LEVEL

#################
##### CLASS #####
#################

class LEVEL_CLASS():
    def __init__(self,
            debug_name:str,
            level_enum:LEVEL,
            level_start_region_enum:REGION_ENUMS,
            region_dict:dict):
        self.debug_name:str = debug_name
        self.level_enum:LEVEL = level_enum
        self.level_start_region_enum:REGION_ENUMS = level_start_region_enum
        self.region_dict:dict = region_dict
    
    def get_level_item_counts(self):
        '''
        Pass
        '''
        for curr_region in self.region_dict:
            curr_region

    def level_specific_items(self, item_dict:dict):
        '''
        Pass
        '''
        if(self.level_enum is LEVEL.spiral_mountain):
            pass
        elif(self.level_enum is LEVEL.mumbos_mountain):
            pass
        elif(self.level_enum is LEVEL.treasure_trove_cove):
            pass
        elif(self.level_enum is LEVEL.clankers_cavern):
            pass
        elif(self.level_enum is LEVEL.bubblegloop_swamp):
            pass
        elif(self.level_enum is LEVEL.freezeezy_peak):
            pass
        elif(self.level_enum is LEVEL.gobis_valley):
            pass
        elif(self.level_enum is LEVEL.mad_monster_mansion):
            pass
        elif(self.level_enum is LEVEL.rusty_bucket_bay):
            pass
        elif(self.level_enum is LEVEL.click_clock_wood):
            pass
        elif(self.level_enum is LEVEL.gruntildas_lair):
            pass
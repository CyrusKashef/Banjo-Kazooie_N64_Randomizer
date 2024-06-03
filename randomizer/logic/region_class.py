from randomizer.constants.int_values.level_enums import LEVEL_ID_ENUMS as LEVEL
from randomizer.constants.int_values.map_enums import MAP_ENUMS as MAP
from randomizer.constants.int_values.region_enums import REGION_ENUMS as REGION
from randomizer.constants.int_values.transformation_enums import TRANSFORMATION_ENUMS as TRANSFORMATION

class Region_Class():
    def __init__(self,
                name:str, hint_name:str, level:LEVEL, location_list:list=[],
                transformation_pad:TRANSFORMATION|None=None, event_list:list=[], exit_list:list=[],
                death_warp_possible:bool=False, death_warp_region:REGION=-1,
                exit_to_witchs_lair_active:bool=False, exit_to_witchs_lair_region:REGION=-1):
        self.debug_name:str = name                                          # Debug name of the region
        self.hint_name:str = hint_name                                      # What a hint would refer to this region as
        self.level:LEVEL = level                                            # What level is this region associated with
        self.location_list:list = location_list                             # List of locations within the room
        self.transformation_pad:TRANSFORMATION|None = transformation_pad    # If there's a transformation pad here, what does it turn you into?
        self.event_list:list = event_list                                   # What triggers can happen here?
        self.exit_list:list = exit_list                                     # What rooms can you have exit to?
        self.death_warp_possible:bool = death_warp_possible                 # Can you death warp in this room without enemies? Ex: Fires, Pitfalls, etc
        self.death_warp_region:REGION = death_warp_region                   # Where dying takes you
        self.exit_to_witchs_lair_active:bool = exit_to_witchs_lair_active   # Whether the feature 'Exit To Witch's Lair' is active
        self.exit_to_witchs_lair_region:REGION = exit_to_witchs_lair_region # If feature 'Exit To Witch's Lair' is active, where would it take you

    def get_base_game_deathwarp_region(self):
        '''
        Get the default deathwarp depending on the region's level.
        '''
        if(self.level == LEVEL.spiral_mountain):
            return REGION.Spiral_Mountain_Main
        elif(self.level == LEVEL.mumbos_mountain):
            return REGION.Mumbos_Mountain_Main
        elif(self.level == LEVEL.treasure_trove_cove):
            return REGION.Treasure_Trove_Cove_Main
        elif(self.level == LEVEL.clankers_cavern):
            return REGION.Clankers_Cavern_Level_Entry
        elif(self.level == LEVEL.bubblegloop_swamp):
            return REGION.Bubblegloop_Swamp_Main
        elif(self.level == LEVEL.freezeezy_peak):
            return REGION.Freezeezy_Peak_Igloo_Exterior
        elif(self.level == LEVEL.gobis_valley):
            return REGION.Gobis_Valley_Level_Entry
        elif(self.level == LEVEL.mad_monster_mansion):
            return REGION.Mad_Monster_Mansion_Floor_1_Exterior
        elif(self.level == LEVEL.rusty_bucket_bay):
            return REGION.Rusty_Bucket_Bay_Level_Entry
        elif(self.level == LEVEL.click_clock_wood):
            return REGION.Click_Clock_Wood_Lobby
        return -1

    def get_base_game_exit_to_witchs_lair_region(self):
        '''
        Get the default exit to witch's lair location depending on the region's level.
        '''
        if(self.level == LEVEL.spiral_mountain):
            return REGION.Gruntildas_Lair_Mumbos_Mountain_Floor
        elif(self.level == LEVEL.mumbos_mountain):
            return REGION.Gruntildas_Lair_Mumbos_Mountain_Floor
        elif(self.level == LEVEL.treasure_trove_cove):
            return REGION.Gruntildas_Lair_Treasure_Trove_Cove_Floor
        elif(self.level == LEVEL.clankers_cavern):
            return REGION.Gruntildas_Lair_Clankers_Cavern_World_Entrance
        elif(self.level == LEVEL.bubblegloop_swamp):
            return REGION.Gruntildas_Lair_Bubblegloop_Swamp_Floor_Entrance
        elif(self.level == LEVEL.freezeezy_peak):
            return REGION.Gruntildas_Lair_Freezeezy_Peak_Floor
        elif(self.level == LEVEL.gobis_valley):
            return REGION.Gruntildas_Lair_Gobis_Valley_Entrance
        elif(self.level == LEVEL.mad_monster_mansion):
            return REGION.Gruntildas_Lair_Mad_Monster_Mansion_Entrance
        elif(self.level == LEVEL.rusty_bucket_bay):
            return REGION.Gruntildas_Lair_Rusty_Bucket_Bay_Entrance_Level_2
        elif(self.level == LEVEL.click_clock_wood):
            return REGION.Gruntildas_Lair_Click_Clock_Wood_Entrance
        return -1
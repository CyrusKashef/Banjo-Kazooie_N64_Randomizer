'''
Shoutouts to the DK64 Randomizer team for sharing their logic <3
Enumerators from the following class are arbitrary values used to make each instance unique.

A region is a section of a map that a player can either:
1) 1 & Separate From Other Warps
  - Example: Starting Pad, Room Warps
2) 2
  - Example: Rusty Bucket Bay Level Entry vs Atop Water
3) Contains A Forced Detransform
  - Example: Freezeezy Peak's Entrance <-> Webbed Flying Pad
'''

###################
##### IMPORTS #####
###################

from enum import IntEnum, auto

########################
##### REGION ENUMS #####
########################

class REGION_ENUMS(IntEnum):
    # Spiral Mountain Regions
    Spiral_Mountain_Main = auto() # 1
    Spiral_Mountain_Lair_Entrance = auto() # 1
    Spiral_Mountain_House_Interior = auto() # 1

    # Mumbo's Mountain Regions
    Mumbos_Mountain_Main = auto() # 1
    Mumbos_Mountain_Mumbos_Interior = auto() # 1
    Mumbos_Mountain_Ticker_Interior_Bottom_Entrance = auto() # 1
    Mumbos_Mountain_Ticker_Interior_Upper_Floors = auto() # 1
    Mumbos_Mountain_Atop_Of_Ticker = auto() # 1

    # Treasure Trove Cove Regions
    # Note: These will have to be redone. Assume no jump down logic for now
    # * Each treetop will need to be a region (assume climb)
    # * Each ledge will need to be a region (assume jump from)
    Treasure_Trove_Cove_Main = auto() # 1
    Treasure_Trove_Cove_Stairs_Alcove = auto() # 1
    Treasure_Trove_Cove_Atop_Mountain_Entrance = auto() # 1
    Treasure_Trove_Cove_Floor_Near_Lighthouse = auto() # 1
    Treasure_Trove_Cove_Atop_Lighthouse = auto() # 1
    Treasure_Trove_Cove_Atop_Mountain_Ledges = auto() # 2
    Treasure_Trove_Cove_Mountain_Tree_Ledge = auto() # 2
    Treasure_Trove_Cove_Salty_Hippo_Interior_Lower_Entrance = auto() # 1
    Treasure_Trove_Cove_Salty_Hippo_Interior_Upper_Entrance = auto() # 1
    Treasure_Trove_Cove_Nipper_Interior = auto() # 1
    Treasure_Trove_Cove_Sandcastle_Interior = auto() # 1
    Treasure_Trove_Cove_Sharkfood_Island_Interior = auto() # 1

    # Clanker's Cavern Regions
    Clankers_Cavern_Level_Entry_Pipe = auto() # 1
    Clankers_Cavern_Level_Entry_Floor = auto() # 2
    Clankers_Cavern_Level_Entry_Atop_Flammable_Container = auto() # 2
    Clankers_Cavern_Level_Entry_Pipe_Walkway = auto() # 2
    Clankers_Cavern_Atop_Water_Near_Clanker = auto() # 1, Via Gills
    Clankers_Cavern_Blowhole_Interior = auto() # 1
    Clankers_Cavern_Mouth_Interior = auto() # 1
    Clankers_Cavern_Belly_Interior = auto() # 1
    Clankers_Cavern_Wonderwing_Room = auto() # 1

    # Bubblegloop Swamp Regions
    Bubblegloop_Swamp_Main = auto() # 1
    Bubblegloop_Swamp_Mumbos_Exterior = auto() # 1
    Bubblegloop_Swamp_Tanktup_Interior = auto() # 1
    Bubblegloop_Swamp_Mumbos_Interior = auto() # 1
    Bubblegloop_Swamp_Vile_Interior = auto() # 1

    # Freezeezy Peak Regions
    Freezeezy_Peak_Main_Lower_Floor = auto() # 2
    Freezeezy_Peak_Mumbos_Exterior = auto() # 1
    Freezeezy_Peak_Christmas_Tree_Pot = auto() # 1
    Freezeezy_Peak_Wozza_Cave_Exterior = auto() # 1
    Freezeezy_Peak_Igloo_Exterior = auto() # 1
    Freezeezy_Peak_Mumbos_Interior = auto() # 1
    Freezeezy_Peak_Christmas_Tree_Interior = auto() # 1
    Freezeezy_Peak_Wozza_Cave_Interior = auto() # 1
    Freezeezy_Peak_Igloo_Interior = auto() # 1

    # Gobi's Valley Regions
    Gobis_Valley_Level_1_Entry = auto() # 1
    Gobis_Valley_Level_2_Jinxy_Entrance_Exterior = auto() # 1
    Gobis_Valley_Level_3_King_Sandybutt_Entrance_Exterior = auto() # 1
    Gobis_Valley_Grabba = auto() # 2
    Gobis_Valley_Level_3_Around_Grabba = auto() # 2
    Gobis_Valley_Level_3_Matching_Puzzle_Exterior = auto() # 1
    Gobis_Valley_Jinxy_Entrance_Interior = auto() # 1
    Gobis_Valley_King_Sandybutt_Entrance_Interior = auto() # 1
    Gobis_Valley_SNS_Entrance_Interior = auto() # 1
    Gobis_Valley_Water_Pyramid_Upper_Interior = auto() # 1
    Gobis_Valley_Water_Pyramid_Lower_Interior = auto() # 1
    Gobis_Valley_Matching_Puzzle_Interior = auto() # 1

    # Mad Monster Mansion Regions
    Mad_Monster_Mansion_Floor_1_Exterior = auto() # 1
    Mad_Monster_Mansion_Floor_2_Exterior = auto() # 1
    Mad_Monster_Mansion_Floor_3_Exterior = auto() # 1
    Mad_Monster_Mansion_Graveyard = auto() # 1
    Mad_Monster_Mansion_Church_Roof_Lower = auto() # 1
    Mad_Monster_Mansion_Church_Roof_Upper = auto() # 1
    Mad_Monster_Mansion_Mumbos_Exterior = auto() # 1
    Mad_Monster_Mansion_Blue_Egg_Room = auto() # 1
    Mad_Monster_Mansion_Red_Feather_Room = auto() # 1
    Mad_Monster_Mansion_Honeycomb_Room = auto() # 1
    Mad_Monster_Mansion_Restroom = auto() # 1
    Mad_Monster_Mansion_Note_Room = auto() # 1
    Mad_Monster_Mansion_Bedroom = auto() # 1
    Mad_Monster_Mansion_Dining_Room_Floor = auto() # 1
    Mad_Monster_Mansion_Dining_Room_Fireplace = auto() # 1
    Mad_Monster_Mansion_Well_Ropes_Entrance = auto() # 1
    Mad_Monster_Mansion_Well_Underwater = auto() # 1
    Mad_Monster_Mansion_Tumblar_Interior = auto() # 1
    Mad_Monster_Mansion_Church_Nave = auto() # 1
    Mad_Monster_Mansion_Church_Secret_Room = auto() # 1
    Mad_Monster_Mansion_Mumbos_Interior = auto() # 1
    Mad_Monster_Mansion_Cellar = auto() # 1
    Mad_Monster_Mansion_Loggo_Interior = auto() # 1
    Mad_Monster_Mansion_Drainpipe_Lower_Interior = auto() # 1
    Mad_Monster_Mansion_Drainpipe_Upper_Interior = auto() # 1

    # Rusty Bucket Bay Regions
    Rusty_Bucket_Bay_Level_Entry = auto() # 1
    Rusty_Bucket_Bay_Grated_Floor = auto() # 2
    Rusty_Bucket_Bay_Warehouse_Window_And_Ledges = auto() # 2
    Rusty_Bucket_Bay_Acid_Pool = auto() # 2
    Rusty_Bucket_Bay_Crane_Up_Grated_Ledge = auto() # 2
    Rusty_Bucket_Bay_Crane_Up_Button_Ledge = auto() # 2
    Rusty_Bucket_Bay_Atop_Crane_Up = auto() # 2
    Rusty_Bucket_Bay_Crane_Down_Grated_Ledge = auto() # 2
    Rusty_Bucket_Bay_Crane_Down_Button_Ledge = auto() # 2
    Rusty_Bucket_Bay_Atop_Crane_Down = auto() # 2
    Rusty_Bucket_Bay_Main_On_Water = auto() # 2
    Rusty_Bucket_Bay_Main_Under_Water = auto() # 2
    Rusty_Bucket_Bay_Anchor_Room = auto() # 1
    Rusty_Bucket_Bay_Engine_Room_Entrance = auto() # 1
    Rusty_Bucket_Bay_Engine_Room_Control_Area = auto() # 1
    Rusty_Bucket_Bay_Warehouse_Water_Surface = auto() # 1
    Rusty_Bucket_Bay_Warehouse_Window_Plank = auto() # 1
    Rusty_Bucket_Bay_Boat_Room = auto() # 1
    Rusty_Bucket_Bay_Chompa_Container = auto() # 1
    Rusty_Bucket_Bay_Boom_Box_Container = auto() # 1
    Rusty_Bucket_Bay_Seaman_Grublin_Container = auto() # 1
    Rusty_Bucket_Bay_Cabin_Room = auto() # 1
    Rusty_Bucket_Bay_Captains_Room = auto() # 1
    Rusty_Bucket_Bay_Navigation_Room = auto() # 1
    Rusty_Bucket_Bay_Boom_Box_Pipe = auto() # 1
    Rusty_Bucket_Bay_Kitchen = auto() # 1
    Rusty_Bucket_Bay_Boss_Boom_Box = auto() # 1

    # Click Clock Wood Regions

    Click_Clock_Wood_Lobby = auto() # 1

    Click_Clock_Wood_Spring_Entrance = auto() # 1
    Click_Clock_Wood_Spring_Lake_Island = auto() # 2
    Click_Clock_Wood_Spring_Mumbos_Exterior = auto() # 1
    Click_Clock_Wood_Spring_Lower_Branches = auto() # 2
    Click_Clock_Wood_Spring_Zubba_Exterior = auto() # 1
    Click_Clock_Wood_Spring_Treehouse = auto() # 2
    Click_Clock_Wood_Spring_Nabnut_Exterior = auto() # 1
    Click_Clock_Wood_Spring_Eyrie = auto() # 2
    Click_Clock_Wood_Spring_Whipcrack_Exterior = auto() # 1
    Click_Clock_Wood_Spring_Mumbos_Interior = auto() # 1
    Click_Clock_Wood_Spring_Zubba_Interior = auto() # 1
    Click_Clock_Wood_Spring_Nabnut_Interior = auto() # 1
    Click_Clock_Wood_Spring_Whipcrack_Interior = auto() # 1

    Click_Clock_Wood_Summer_Entrance = auto() # 1
    Click_Clock_Wood_Summer_Lake_Island = auto() # 2
    Click_Clock_Wood_Summer_Mumbos_Exterior = auto() # 1
    Click_Clock_Wood_Summer_Lower_Branches = auto() # 2
    Click_Clock_Wood_Summer_Zubba_Exterior = auto() # 1
    Click_Clock_Wood_Summer_Treehouse = auto() # 2
    Click_Clock_Wood_Summer_Nabnut_Exterior = auto() # 1
    Click_Clock_Wood_Summer_Eyrie = auto() # 2
    Click_Clock_Wood_Summer_Whipcrack_Exterior = auto() # 1
    Click_Clock_Wood_Summer_Mumbos_Interior = auto() # 1
    Click_Clock_Wood_Summer_Zubba_Interior = auto() # 1
    Click_Clock_Wood_Summer_Nabnut_Interior = auto() # 1
    Click_Clock_Wood_Summer_Whipcrack_Interior = auto() # 1

    Click_Clock_Wood_Autumn_Entrance = auto() # 1
    Click_Clock_Wood_Autumn_Lake_Island = auto() # 2
    Click_Clock_Wood_Autumn_Mumbos_Exterior = auto() # 1
    Click_Clock_Wood_Autumn_Lower_Branches = auto() # 2
    Click_Clock_Wood_Autumn_Zubba_Exterior = auto() # 1
    Click_Clock_Wood_Autumn_Treehouse = auto() # 2
    Click_Clock_Wood_Autumn_Nabnut_Exterior = auto() # 1
    Click_Clock_Wood_Autumn_Eyrie = auto() # 2
    Click_Clock_Wood_Autumn_Whipcrack_Exterior = auto() # 1
    Click_Clock_Wood_Autumn_Mumbos_Interior = auto() # 1
    Click_Clock_Wood_Autumn_Zubba_Interior = auto() # 1
    Click_Clock_Wood_Autumn_Nabnut_Interior = auto() # 1
    Click_Clock_Wood_Autumn_Flooded_Room = auto() # 1
    Click_Clock_Wood_Autumn_Whipcrack_Interior = auto() # 1

    Click_Clock_Wood_Winter_Entrance = auto() # 1
    Click_Clock_Wood_Winter_Lake_Island = auto() # 2
    Click_Clock_Wood_Winter_Lower_Branches = auto() # 2
    Click_Clock_Wood_Winter_Zubba_Exterior = auto() # 2
    Click_Clock_Wood_Winter_Treehouse = auto() # 2
    Click_Clock_Wood_Winter_Nabnut_Exterior = auto() # 1
    Click_Clock_Wood_Winter_Eyrie = auto() # 2
    Click_Clock_Wood_Winter_Whipcrack_Exterior = auto() # 1
    Click_Clock_Wood_Winter_Mumbos_Interior = auto() # 1
    Click_Clock_Wood_Winter_Nabnut_Interior = auto() # 1
    Click_Clock_Wood_Winter_Flooded_Room = auto() # 1
    Click_Clock_Wood_Winter_Acorn_Storage = auto() # 1
    Click_Clock_Wood_Winter_Whipcrack_Interior = auto() # 1

    # Grunty's Lair Regions
    Gruntildas_Lair_Spiral_Mountain_Entrance = auto()
    Gruntildas_Lair_Termite_Detransformation_Zone = auto()
    Gruntildas_Lair_Mumbos_Mountain_Entrance = auto()
    Gruntildas_Lair_50_Note_Door = auto()

    Gruntildas_Lair_Treasure_Trove_Cove_Clankers_Cavern_Puzzles = auto()

    Gruntildas_Lair_Floor_3_Upper = auto()
    Gruntildas_Lair_Floor_3_Lower = auto()
    Gruntildas_Lair_180_Note_Door = auto()
    Gruntildas_Lair_To_Clankers_Cavern_Pipe = auto()

    Gruntildas_Lair_Pipe_Pink_Cauldron_Room = auto()

    Gruntildas_Lair_Treasure_Trove_Cove_Entrance = auto()

    Gruntildas_Lair_Clankers_Cavern_Room_Entrance = auto()
    Gruntildas_Lair_Clankers_Cavern_World_Entrance = auto()

    Gruntildas_Lair_Pointing_Gruntilda_Statue_Main_Entrance = auto()
    Gruntildas_Lair_Pointing_Gruntilda_Statue_Pipe_Entrance = auto()
    Gruntildas_Lair_260_Note_Door = auto()

    Gruntildas_Lair_Bubblegloop_Swamp_Room_Entrance = auto()
    Gruntildas_Lair_Crocodile_Detransformation_Zone = auto()
    Gruntildas_Lair_Bubblegloop_Swamp_Entrance = auto()

    Gruntildas_Lair_Gobis_Valley_Vase_Area = auto()
    Gruntildas_Lair_Gobis_Valley_Entrance = auto()

    Gruntildas_Lair_Gruntilda_Head_Area = auto()
    Gruntildas_Lair_Gruntilda_Head_Pink_Cauldron_Area = auto()
    Gruntildas_Lair_Gruntilda_Head_Teal_Cauldron_Area = auto()
    Gruntildas_Lair_Freezeezy_Peak_Entrance = auto()
    Gruntildas_Lair_Walrus_Detransformation_Zone = auto()

    Gruntildas_Lair_Lava_Room_Main_Entrance = auto()
    Gruntildas_Lair_Pumpkin_Detransformation_Zone = auto()
    Gruntildas_Lair_Lava_Room_Brentilda_Area = auto()

    Gruntildas_Lair_Mad_Monster_Mansion_Entrance = auto()
    Gruntildas_Lair_Crypt_Entrance = auto()

    Gruntildas_Lair_Water_Switch_Room_Underwater = auto()
    Gruntildas_Lair_Water_Switch_Room_Level_1_Entrance = auto()
    Gruntildas_Lair_640_Note_Door = auto()
    Gruntildas_Lair_Water_Switch_Room_Mumbo_Token_Entrance = auto()

    Gruntildas_Lair_Rusty_Bucket_Bay_Entrance_Level_1_Underwater = auto()
    Gruntildas_Lair_Rusty_Bucket_Bay_Entrance_Level_1_Above_Water = auto()
    Gruntildas_Lair_Rusty_Bucket_Bay_Entrance_Level_2_Above_Water = auto()
    Gruntildas_Lair_Rusty_Bucket_Bay_Entrance_Level_3_Above_Water = auto()

    Gruntildas_Lair_Mad_Monster_Mansion_Puzzle_Level_1_Underwater = auto()
    Gruntildas_Lair_Mad_Monster_Mansion_Puzzle_Level_1_Above_Water = auto()
    Gruntildas_Lair_Mad_Monster_Mansion_Puzzle_Alcoves = auto()
    Gruntildas_Lair_Rusty_Bucket_Bay_Puzzle_Tunnel = auto()

    Gruntildas_Lair_Crypt = auto()

    Gruntildas_Lair_Click_Clock_Wood_Whipcrack_Entrance = auto()
    Gruntildas_Lair_Click_Clock_Wood_Whipcrack_Tunnel = auto()
    Gruntildas_Lair_Click_Clock_Wood_Token_Tunnel = auto()
    Gruntildas_Lair_Click_Clock_Wood_Amber_Cauldron_Tunnel = auto()
    Gruntildas_Lair_Click_Clock_Wood_Amber_Cauldron = auto()
    Gruntildas_Lair_Click_Clock_Wood_Level_Entrance = auto()
    Gruntildas_Lair_765_Note_Door_Floor = auto()

    Gruntildas_Lair_Furnace_Fun_Tunnel = auto()

    Gruntildas_Lair_Furnace_Fun = auto()

    Gruntildas_Lair_810_Note_Door = auto()
    Gruntildas_Lair_Final_Battle_Puzzle = auto()
    Gruntildas_Lair_Dingpot = auto()
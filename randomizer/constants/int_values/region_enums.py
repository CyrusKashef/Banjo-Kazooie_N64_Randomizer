'''
Shoutouts to the DK64 Randomizer team for sharing their logic <3

A region is a section of a map that a player can either:
1) Warp To
  - Example: Starting Pad, Room Warps
2) Reach Only After Triggering An Event
  - Example: Chimpy's Cliff
3) Reachable Area But Not Return Back Without Meeting A Requirement
  - Example: Rusty Bucket Bay Level Entry vs Atop Water
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
    Spiral_Mountain_Main = auto() # Warp To
    Spiral_Mountain_Lair_Entrance = auto() # Warp To, Bridge Incomplete
    Spiral_Mountain_House_Interior = auto() # Warp To

    # Mumbo's Mountain Regions
    Mumbos_Mountain_Main = auto() # Warp To
    Mumbos_Mountain_Chimpy_Cliff = auto() # Reach Only After Triggering An Event
    Mumbos_Mountain_Mumbos_Interior = auto() # Warp To
    Mumbos_Mountain_Ticker_Interior_Bottom_Entrance = auto() # Warp To
    Mumbos_Mountain_Ticker_Interior_Top_Entrance = auto() # Warp To
    Mumbos_Mountain_Atop_Of_Ticker = auto() # Warp To

    # Treasure Trove Cove Regions
    Treasure_Trove_Cove_Main = auto() # Warp To
    Treasure_Trove_Cove_Stairs_Alcove = auto() # Warp To
    Treasure_Trove_Cove_Atop_Mountain_Entrance = auto() # Warp To
    Treasure_Trove_Cove_Floor_Near_Lighthouse = auto() # Warp To
    Treasure_Trove_Cove_Atop_Lighthouse = auto() # Warp To
    Treasure_Trove_Cove_Salty_Hippo_Interior_Lower_Entrance = auto() # Warp To
    Treasure_Trove_Cove_Salty_Hippo_Interior_Upper_Entrance = auto() # Warp To
    Treasure_Trove_Cove_Nipper_Interior = auto() # Warp To
    Treasure_Trove_Cove_Sandcastle_Interior = auto() # Warp To
    Treasure_Trove_Cove_Sharkfood_Island_Interior = auto() # Warp To

    # Clanker's Cavern Regions
    Clankers_Cavern_Level_Entry_Pipe = auto() # Warp To
    Clankers_Cavern_Level_Entry_Floor = auto() # Reachable Area But Not Return Back Without Meeting A Requirement
    Clankers_Cavern_Level_Entry_Atop_Flammable_Container = auto() # Reachable Area But Not Return Back Without Meeting A Requirement
    Clankers_Cavern_Level_Entry_Pipe_Walkway = auto() # Reachable Area But Not Return Back Without Meeting A Requirement
    Clankers_Cavern_Atop_Water_Near_Clanker = auto() # Warp To
    Clankers_Cavern_Atop_Clanker = auto() # Reach Only After Triggering An Event
    Clankers_Cavern_Blowhole_Interior = auto() # Warp To
    Clankers_Cavern_Mouth_Interior = auto() # Warp To, Belly Needs Dive
    Clankers_Cavern_Belly_Interior = auto() # Warp To, Mouth Needs Dive
    Clankers_Cavern_Wonderwing_Room = auto() # Warp To

    # Bubblegloop Swamp Regions
    Bubblegloop_Swamp_Main = auto() # Warp To
    Bubblegloop_Swamp_Mumbos_Exterior = auto() # Warp To, May Require Health Or Transformation
    Bubblegloop_Swamp_Tanktup_Exterior = auto() # Warp To, May Require Health Or Transformation
    Bubblegloop_Swamp_Vile_Exterior = auto() # Warp To, May Require Health Or Transformation
    Bubblegloop_Swamp_Tanktup_Interior = auto() # Warp To
    Bubblegloop_Swamp_Mumbos_Interior = auto() # Warp To
    Bubblegloop_Swamp_Vile_Interior = auto() # Warp To

    # Freezeezy Peak Regions
    Freezeezy_Peak_Main_Lower_Floor = auto() # Reachable Area But Not Return Back Without Meeting A Requirement
    Freezeezy_Peak_Mumbos_Exterior = auto() # Warp To, May Require Health Or Transformation
    Freezeezy_Peak_Tree_Pot = auto() # Warp To, Cannot Re-Enter Without Climb
    Freezeezy_Peak_Wozza_Exterior = auto() # Warp To, Cannot Exit Without Wozza
    Freezeezy_Peak_Igloo_Exterior = auto() # Warp To
    Freezeezy_Peak_Mumbos_Interior = auto() # Warp To
    Freezeezy_Peak_Tree_Interior = auto() # Warp To
    Freezeezy_Peak_Wozza_Interior = auto() # Warp To
    Freezeezy_Peak_Igloo_Interior = auto() # Warp To

    # Gobi's Valley Regions
    Gobis_Valley_Level_1_Entry = auto() # Warp To
    Gobis_Valley_Level_2_Jinxy_Entrance_Exterior = auto() # Warp To, Cannot Re-Enter/Re-Reach Easily
    Gobis_Valley_Level_3_King_Sandybutt_Entrance_Exterior = auto() # Warp To, Cannot Reach Without Jump
    Gobis_Valley_Grabba = auto() # Reachable Area But Not Return Back Without Meeting A Requirement
    Gobis_Valley_Level_3_Around_Grabba = auto() # Reachable Area But Not Return Back Without Meeting A Requirement
    Gobis_Valley_Level_3_Matching_Puzzle_Exterior = auto() # Warp To
    Gobis_Valley_Jinxy_Entrance_Interior = auto() # Warp To
    Gobis_Valley_King_Sandybutt_Entrance_Interior = auto() # Warp To
    Gobis_Valley_SNS_Entrance_Interior = auto() # Warp To
    Gobis_Valley_Water_Pyramid_Upper_Interior = auto() # Warp To
    Gobis_Valley_Water_Pyramid_Lower_Interior = auto() # Warp To
    Gobis_Valley_Matching_Puzzle_Interior = auto() # Warp To

    # Mad Monster Mansion Regions
    Mad_Monster_Mansion_Floor_1_Exterior = auto() # Warp To
    Mad_Monster_Mansion_Floor_2_Exterior = auto() # Warp To
    Mad_Monster_Mansion_Floor_3_Exterior = auto() # Warp To
    Mad_Monster_Mansion_Graveyard = auto() # Warp To, Needs Moves To Escape
    Mad_Monster_Mansion_Church_Roof_Lower = auto() # Warp To, Cannot Re-Enter/Re-Reach Easily
    Mad_Monster_Mansion_Church_Roof_Upper = auto() # Warp To
    Mad_Monster_Mansion_Mumbos_Exterior = auto() # Warp To
    Mad_Monster_Mansion_Blue_Egg_Room = auto() # Warp To
    Mad_Monster_Mansion_Red_Feather_Room = auto() # Warp To
    Mad_Monster_Mansion_Honeycomb_Room = auto() # Warp To
    Mad_Monster_Mansion_Restroom = auto() # Warp To
    Mad_Monster_Mansion_Note_Room = auto() # Warp To
    Mad_Monster_Mansion_Bedroom = auto() # Warp To
    Mad_Monster_Mansion_Dining_Room_Floor = auto() # Warp To
    Mad_Monster_Mansion_Dining_Room_Fireplace = auto() # Warp To
    Mad_Monster_Mansion_Well_Ropes_Entrance = auto() # Warp To
    Mad_Monster_Mansion_Well_Underwater = auto() # Warp To
    Mad_Monster_Mansion_Tumblar_Interior = auto() # Warp To
    Mad_Monster_Mansion_Church_Nave = auto() # Warp To
    Mad_Monster_Mansion_Church_Secret_Room = auto() # Warp To
    Mad_Monster_Mansion_Mumbos_Interior = auto() # Warp To
    Mad_Monster_Mansion_Cellar = auto() # Warp To
    Mad_Monster_Mansion_Loggo_Interior = auto() # Warp To
    Mad_Monster_Mansion_Drainpipe_Lower_Interior = auto() # Warp To
    Mad_Monster_Mansion_Drainpipe_Upper_Interior = auto() # Warp To

    # Rusty Bucket Bay Regions
    Rusty_Bucket_Bay_Level_Entry = auto() # Warp To
    Rusty_Bucket_Bay_Grated_Floor = auto() # Reachable Area But Not Return Back Without Meeting A Requirement
    Rusty_Bucket_Bay_Toll_2 = auto() # Reach Only After Triggering An Event
    Rusty_Bucket_Bay_Warehouse_Window_And_Ledges = auto() # Reachable Area But Not Return Back Without Meeting A Requirement
    Rusty_Bucket_Bay_Acid_Pool = auto() # Reachable Area But Not Return Back Without Meeting A Requirement
    Rusty_Bucket_Bay_Crane_Up = auto() # Reachable Area But Not Return Back Without Meeting A Requirement
    Rusty_Bucket_Bay_Toll_4 = auto() # Reach Only After Triggering An Event
    Rusty_Bucket_Bay_Containers_Exterior_Floor = auto() # Reachable Area But Not Return Back Without Meeting A Requirement
    Rusty_Bucket_Bay_Containers_Exterior_Atop = auto() # Warp To
    Rusty_Bucket_Bay_Toll_6 = auto() # Reach Only After Triggering An Event
    Rusty_Bucket_Bay_Crane_Down = auto() # Reachable Area But Not Return Back Without Meeting A Requirement
    Rusty_Bucket_Bay_Toll_8 = auto() # Reach Only After Triggering An Event
    Rusty_Bucket_Bay_Orange_Jinjo = auto() # Reach Only After Triggering An Event Or Exploits
    Rusty_Bucket_Bay_Bow = auto()
    Rusty_Bucket_Bay_Bow_Lifeboats = auto()
    Rusty_Bucket_Bay_Stern = auto()
    Rusty_Bucket_Bay_Stern_Lifeboat = auto()
    Rusty_Bucket_Bay_On_Main_Water = auto()
    Rusty_Bucket_Bay_Under_Main_Water = auto()
    Rusty_Bucket_Bay_On_Snacker_Water = auto()
    Rusty_Bucket_Bay_Under_Snacker_Water = auto()
    Rusty_Bucket_Bay_Behind_Propellers = auto()
    Rusty_Bucket_Bay_Anchor_Room_Button = auto()
    Rusty_Bucket_Bay_Anchor_Room_Underwater = auto()
    Rusty_Bucket_Bay_Engine_Room_Entrance = auto()
    Rusty_Bucket_Bay_Engine_Room_Entrance_Floor = auto()
    Rusty_Bucket_Bay_Engine_Room_Safe_Intersection = auto()
    Rusty_Bucket_Bay_Engine_Room_Button_Right = auto()
    Rusty_Bucket_Bay_Engine_Room_Button_Left = auto()
    Rusty_Bucket_Bay_Engine_Room_Jiggy = auto()
    Rusty_Bucket_Bay_Engine_Control_Room = auto()
    Rusty_Bucket_Bay_Warehouse_Water_Surface = auto()
    Rusty_Bucket_Bay_Warehouse_Stone_Floor = auto()
    Rusty_Bucket_Bay_Warehouse_Lower_Boxes = auto()
    Rusty_Bucket_Bay_Warehouse_Window_Plank = auto()
    Rusty_Bucket_Bay_Warehouse_Top_Boxes = auto()
    Rusty_Bucket_Bay_Boat_Room_Underwater = auto()
    Rusty_Bucket_Bay_Boat_Room_Stone_Floor = auto()
    Rusty_Bucket_Bay_Chompa_Container = auto()
    Rusty_Bucket_Bay_Boom_Box_Container = auto()
    Rusty_Bucket_Bay_Seaman_Grublin_Container = auto()
    Rusty_Bucket_Bay_Cabin_Room = auto()
    Rusty_Bucket_Bay_Captains_Room = auto()
    Rusty_Bucket_Bay_Navigation_Room = auto()
    Rusty_Bucket_Bay_Boom_Box_Pipe = auto()
    Rusty_Bucket_Bay_Kitchen = auto()
    Rusty_Bucket_Bay_Boss_Boom_Box = auto()

    # Click Clock Wood Regions

    Click_Clock_Wood_Lobby = auto()

    Click_Clock_Wood_Spring_Entrance = auto()
    Click_Clock_Wood_Spring_Underwater = auto()
    Click_Clock_Wood_Spring_Lake_Island = auto()
    Click_Clock_Wood_Spring_Flower = auto()
    Click_Clock_Wood_Spring_Lonely_Snarebear = auto()
    Click_Clock_Wood_Spring_Mumbos_Exterior = auto()
    Click_Clock_Wood_Spring_Tree_Rim = auto()
    Click_Clock_Wood_Spring_Lower_Branches = auto()
    Click_Clock_Wood_Spring_Zubba_Exterior = auto()
    Click_Clock_Wood_Spring_Treehouse = auto()
    Click_Clock_Wood_Spring_Nabnut_Exterior = auto()
    Click_Clock_Wood_Spring_Eyrie = auto()
    Click_Clock_Wood_Spring_Whipcrack_Exterior = auto()
    Click_Clock_Wood_Spring_Top_Of_Tree = auto()
    Click_Clock_Wood_Spring_Mumbos_Interior = auto()
    Click_Clock_Wood_Spring_Zubba_Interior = auto()
    Click_Clock_Wood_Spring_Nabnut_Interior = auto()
    Click_Clock_Wood_Spring_Whipcrack_Interior = auto()

    Click_Clock_Wood_Summer_Entrance = auto()
    Click_Clock_Wood_Summer_Dried_Lake = auto()
    Click_Clock_Wood_Summer_Lake_Island = auto()
    Click_Clock_Wood_Summer_Flower = auto()
    Click_Clock_Wood_Summer_Lonely_Snarebear = auto()
    Click_Clock_Wood_Summer_Mumbos_Exterior = auto()
    Click_Clock_Wood_Summer_Tree_Rim = auto()
    Click_Clock_Wood_Summer_Lower_Branches = auto()
    Click_Clock_Wood_Summer_Zubba_Exterior = auto()
    Click_Clock_Wood_Summer_Treehouse = auto()
    Click_Clock_Wood_Summer_Nabnut_Exterior = auto()
    Click_Clock_Wood_Summer_Eyrie = auto()
    Click_Clock_Wood_Summer_Whipcrack_Exterior = auto()
    Click_Clock_Wood_Summer_Top_Of_Tree = auto()
    Click_Clock_Wood_Summer_Mumbos_Interior = auto()
    Click_Clock_Wood_Summer_Zubba_Interior = auto()
    Click_Clock_Wood_Summer_Nabnut_Interior = auto()
    Click_Clock_Wood_Summer_Whipcrack_Interior = auto()

    Click_Clock_Wood_Autumn_Entrance = auto()
    Click_Clock_Wood_Autumn_Underwater = auto()
    Click_Clock_Wood_Autumn_Lake_Island = auto()
    Click_Clock_Wood_Autumn_Gnawty_Home = auto()
    Click_Clock_Wood_Autumn_Flower = auto()
    Click_Clock_Wood_Autumn_Lonely_Snarebear = auto()
    Click_Clock_Wood_Autumn_Mumbos_Exterior = auto()
    Click_Clock_Wood_Autumn_Tree_Rim = auto()
    Click_Clock_Wood_Autumn_Lower_Branches = auto()
    Click_Clock_Wood_Autumn_Zubba_Exterior = auto()
    Click_Clock_Wood_Autumn_Treehouse = auto()
    Click_Clock_Wood_Autumn_Nabnut_Exterior = auto()
    Click_Clock_Wood_Autumn_Eyrie = auto()
    Click_Clock_Wood_Autumn_Whipcrack_Exterior = auto()
    Click_Clock_Wood_Autumn_Top_Of_Tree = auto()
    Click_Clock_Wood_Autumn_Mumbos_Interior = auto()
    Click_Clock_Wood_Autumn_Zubba_Interior = auto()
    Click_Clock_Wood_Autumn_Nabnut_Interior = auto()
    Click_Clock_Wood_Autumn_Flooded_Room = auto()
    Click_Clock_Wood_Autumn_Whipcrack_Interior = auto()

    Click_Clock_Wood_Winter_Entrance = auto()
    Click_Clock_Wood_Winter_Atop_Ice_Water = auto()
    Click_Clock_Wood_Winter_Underwater = auto()
    Click_Clock_Wood_Winter_Lake_Island = auto()
    Click_Clock_Wood_Winter_Gnawty_Home = auto()
    Click_Clock_Wood_Winter_Flower = auto()
    Click_Clock_Wood_Winter_Lonely_Snarebear = auto()
    Click_Clock_Wood_Winter_Mumbos_Exterior = auto()
    Click_Clock_Wood_Winter_Tree_Rim = auto()
    Click_Clock_Wood_Winter_Lower_Branches = auto()
    Click_Clock_Wood_Winter_Zubba_Exterior = auto()
    Click_Clock_Wood_Winter_Treehouse = auto()
    Click_Clock_Wood_Winter_Nabnut_Exterior = auto()
    Click_Clock_Wood_Winter_Eyrie = auto()
    Click_Clock_Wood_Winter_Whipcrack_Exterior = auto()
    Click_Clock_Wood_Winter_Top_Of_Tree = auto()
    Click_Clock_Wood_Winter_Mumbos_Interior = auto()
    Click_Clock_Wood_Winter_Nabnut_Interior = auto()
    Click_Clock_Wood_Winter_Flooded_Room = auto()
    Click_Clock_Wood_Winter_Acorn_Storage = auto()
    Click_Clock_Wood_Winter_Whipcrack_Interior = auto()

    # Grunty's Lair Regions

    Gruntildas_Lair_Mumbos_Mountain_Floor = auto()
    Gruntildas_Lair_Atop_Mumbos_Mountain_Entrance = auto()
    Gruntildas_Lair_50_Note_Door = auto()

    Gruntildas_Lair_Treasure_Trove_Cove_Puzzle = auto()
    Gruntildas_Lair_Clankers_Cavern_Puzzle = auto()

    Gruntildas_Lair_Floor_3_Main = auto()
    Gruntildas_Lair_Floor_3_Lower = auto()
    Gruntildas_Lair_Floor_3_Lower_Underwater = auto()
    Gruntildas_Lair_Click_Clock_Wood_Puzzle = auto()
    Gruntildas_Lair_180_Note_Door = auto()

    Gruntildas_Lair_Pipe_Pink_Cauldron = auto()

    Gruntildas_Lair_Treasure_Trove_Cove_Floor = auto()
    Gruntildas_Lair_Treasure_Trove_Cove_Cannon = auto()
    Gruntildas_Lair_Treasure_Trove_Cove_Jiggy = auto()

    Gruntildas_Lair_Clankers_Cavern_Floor_Entrance = auto()
    Gruntildas_Lair_Clankers_Cavern_World_Entrance = auto()
    Gruntildas_Lair_Clankers_Cavern_Floor_Underwater = auto()
    Gruntildas_Lair_Clankers_Cavern_Brentilda = auto()
    Gruntildas_Lair_Bubblegloop_Swamp_Puzzle = auto()

    Gruntildas_Lair_Floor_4_Main = auto()
    Gruntildas_Lair_Floor_4_Inside_Statue = auto()
    Gruntildas_Lair_Floor_4_Pipe = auto()
    Gruntildas_Lair_Floor_4_Underwater = auto()
    Gruntildas_Lair_260_Note_Door = auto()

    Gruntildas_Lair_Bubblegloop_Swamp_Floor_Entrance = auto()
    Gruntildas_Lair_Freezeezy_Peak_Puzzle = auto()
    Gruntildas_Lair_Crocodile_Cheato = auto()

    Gruntildas_Lair_Floor_5_Main = auto()
    Gruntildas_Lair_Floor_5_Wading_Boots = auto()
    Gruntildas_Lair_Shock_Jump_Switch = auto()
    Gruntildas_Lair_Sarcophogus = auto()
    Gruntildas_Lair_Gobis_Valley_Entrance = auto()

    Gruntildas_Lair_Freezeezy_Peak_Floor = auto()
    Gruntildas_Lair_Temporary_Flight_Pad = auto()
    Gruntildas_Lair_Floor_6_Pink_Cauldron = auto()
    Gruntildas_Lair_Floor_6_Teal_Cauldron = auto()
    Gruntildas_Lair_Advent_Calendar_Jiggy = auto()
    Gruntildas_Lair_Flight_Tunnel = auto()
    Gruntildas_Lair_Atop_Gruntys_Hat = auto()
    Gruntildas_Lair_Eyeball_Jiggy = auto()

    Gruntildas_Lair_Gobis_Valley_Puzzle = auto()
    Gruntildas_Lair_Pumpkin_Cheato = auto()

    Gruntildas_Lair_Mad_Monster_Mansion_Entrance = auto()
    Gruntildas_Lair_Crypt_Entrance = auto()

    Gruntildas_Lair_Water_Switch_Room_Underwater = auto()
    Gruntildas_Lair_Water_Switch_Room_Level_1 = auto()
    Gruntildas_Lair_Water_Switch_Room_Level_2 = auto()
    Gruntildas_Lair_Rusty_Bucket_Bay_Witch_Switch_Jiggy = auto()

    Gruntildas_Lair_Rusty_Bucket_Bay_Entrance_Level_1 = auto()
    Gruntildas_Lair_Rusty_Bucket_Bay_Entrance_Level_2 = auto()
    Gruntildas_Lair_Rusty_Bucket_Bay_Entrance_Level_3 = auto()

    Gruntildas_Lair_Mad_Monster_Mansion_Puzzle_Alcoves = auto()
    Gruntildas_Lair_Mad_Monster_Mansion_Puzzle_Underwater = auto()
    Gruntildas_Lair_Rusty_Bucket_Bay_Puzzle_Tunnel = auto()
    Gruntildas_Lair_Rusty_Bucket_Bay_Puzzle_Room = auto()

    Gruntildas_Lair_Crypt = auto()

    Gruntildas_Lair_Floor_7_Main = auto()
    Gruntildas_Lair_Click_Clock_Wood_Entrance = auto()
    Gruntildas_Lair_Click_Clock_Wood_Puzzle_Switch = auto()

    Gruntildas_Lair_Furnace_Fun_Tunnel = auto()

    Gruntildas_Lair_Furnace_Fun = auto()

    Gruntildas_Lair_Finale_Gold_Cauldron = auto()
    Gruntildas_Lair_Beauty_Machines = auto()
    Gruntildas_Lair_Dingpot = auto()
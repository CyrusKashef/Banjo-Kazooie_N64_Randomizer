###################
##### IMPORTS #####
###################

from enum import IntEnum, auto

##########################
##### LOCATION ENUMS #####
##########################

class LOCATION_ENUMS(IntEnum):
    ###########################
    ##### SPIRAL MOUNTAIN #####
    ###########################
    # Notes
    # Blue Eggs
    # Red Feathers
    # Gold Feathers
    # Jiggies
    # Empty Honeycombs
    spiral_mountain_stump = auto()
    spiral_mountain_ledges = auto()
    spiral_mountain_atop_tree = auto()
    spiral_mountain_underwater = auto()
    spiral_mountain_quarries = auto()
    spiral_mountain_colliwobble = auto()
    # Mumbo Tokens
    # Extra Lives
    spiral_mountain_atop_banjos_house = auto()
    spiral_mountain_behind_waterfall = auto()
    # Jinjos
    # Bottles Molehills
    spiral_mountain_bottles_climb = auto()
    spiral_mountain_bottles_jump = auto()
    spiral_mountain_bottles_attack = auto()
    spiral_mountain_bottles_dive = auto()
    # Other Items
    # Custom Locations
    ###########################
    ##### MUMBOS MOUNTAIN #####
    ###########################
    # Notes
    mumbos_mountain_bridge_note_1 = auto()
    mumbos_mountain_bridge_note_2 = auto()
    mumbos_mountain_bridge_note_3 = auto()
    mumbos_mountain_bridge_note_4 = auto()
    mumbos_mountain_bridge_note_5 = auto()
    mumbos_mountain_bridge_note_6 = auto()
    mumbos_mountain_bridge_note_7 = auto()
    mumbos_mountain_grass_slope_note_1 = auto()
    mumbos_mountain_grass_slope_note_2 = auto()
    mumbos_mountain_grass_slope_note_3 = auto()
    mumbos_mountain_grass_slope_note_4 = auto()
    mumbos_mountain_grass_slope_note_5 = auto()
    mumbos_mountain_grass_slope_note_6 = auto()
    mumbos_mountain_grass_slope_note_7 = auto()
    mumbos_mountain_grass_slope_note_8 = auto()
    mumbos_mountain_grass_slope_note_9 = auto()
    mumbos_mountain_grass_slope_note_10 = auto()
    mumbos_mountain_grass_slope_note_11 = auto()
    mumbos_mountain_grass_slope_note_12 = auto()
    mumbos_mountain_grass_slope_note_13 = auto()
    mumbos_mountain_grass_slope_note_14 = auto()
    mumbos_mountain_grass_slope_note_15 = auto()
    mumbos_mountain_grass_slope_note_16 = auto()
    mumbos_mountain_grass_slope_note_17 = auto()
    mumbos_mountain_grass_slope_note_18 = auto()
    mumbos_mountain_dirt_slope_note_1 = auto()
    mumbos_mountain_dirt_slope_note_2 = auto()
    mumbos_mountain_dirt_slope_note_3 = auto()
    mumbos_mountain_dirt_slope_note_4 = auto()
    mumbos_mountain_dirt_slope_note_5 = auto()
    mumbos_mountain_dirt_slope_note_6 = auto()
    mumbos_mountain_dirt_slope_note_7 = auto()
    mumbos_mountain_dirt_slope_note_8 = auto()
    mumbos_mountain_dirt_slope_note_9 = auto()
    mumbos_mountain_dirt_slope_note_10 = auto()
    mumbos_mountain_dirt_slope_note_11 = auto()
    mumbos_mountain_dirt_slope_note_12 = auto()
    mumbos_mountain_dirt_slope_note_13 = auto()
    mumbos_mountain_dirt_slope_note_14 = auto()
    mumbos_mountain_dirt_slope_note_15 = auto()
    mumbos_mountain_dirt_slope_note_16 = auto()
    mumbos_mountain_dirt_slope_note_17 = auto()
    mumbos_mountain_dirt_slope_note_18 = auto()
    mumbos_mountain_dirt_slope_note_19 = auto()
    mumbos_mountain_dirt_slope_note_20 = auto()
    mumbos_mountain_dirt_slope_note_21 = auto()
    mumbos_mountain_long_stairs_note_1 = auto()
    mumbos_mountain_long_stairs_note_2 = auto()
    mumbos_mountain_long_stairs_note_3 = auto()
    mumbos_mountain_long_stairs_note_4 = auto()
    mumbos_mountain_long_stairs_note_5 = auto()
    mumbos_mountain_long_stairs_note_6 = auto()
    mumbos_mountain_long_stairs_note_7 = auto()
    mumbos_mountain_long_stairs_note_8 = auto()
    mumbos_mountain_long_stairs_note_9 = auto()
    mumbos_mountain_short_stairs_note_1 = auto()
    mumbos_mountain_short_stairs_note_2 = auto()
    mumbos_mountain_short_stairs_note_3 = auto()
    mumbos_mountain_short_stairs_note_4 = auto()
    mumbos_mountain_stonehenge_note_1 = auto()
    mumbos_mountain_stonehenge_note_2 = auto()
    mumbos_mountain_stonehenge_note_3 = auto()
    mumbos_mountain_stonehenge_note_4 = auto()
    mumbos_mountain_stonehenge_note_5 = auto()
    mumbos_mountain_stonehenge_note_6 = auto()
    mumbos_mountain_stonehenge_note_7 = auto()
    mumbos_mountain_stonehenge_note_8 = auto()
    mumbos_mountain_stonehenge_note_9 = auto()
    mumbos_mountain_stonehenge_note_10 = auto()
    mumbos_mountain_stonehenge_note_11 = auto()
    mumbos_mountain_stonehenge_note_12 = auto()
    mumbos_mountain_stonehenge_note_13 = auto()
    mumbos_mountain_stonehenge_note_14 = auto()
    mumbos_mountain_atop_huts_note_1 = auto()
    mumbos_mountain_atop_huts_note_2 = auto()
    mumbos_mountain_atop_huts_note_3 = auto()
    mumbos_mountain_atop_huts_note_4 = auto()
    mumbos_mountain_atop_huts_note_5 = auto()
    mumbos_mountain_atop_huts_note_6 = auto()
    mumbos_mountain_underwater_note_1 = auto()
    mumbos_mountain_underwater_note_2 = auto()
    mumbos_mountain_underwater_note_3 = auto()
    mumbos_mountain_underwater_note_4 = auto()
    mumbos_mountain_underwater_note_5 = auto()
    mumbos_mountain_underwater_note_6 = auto()
    mumbos_mountain_tickers_tower_note_1 = auto()
    mumbos_mountain_tickers_tower_note_2 = auto()
    mumbos_mountain_tickers_tower_note_3 = auto()
    mumbos_mountain_tickers_tower_note_4 = auto()
    mumbos_mountain_tickers_tower_note_5 = auto()
    mumbos_mountain_tickers_tower_note_6 = auto()
    mumbos_mountain_mumbos_skull_note_1 = auto()
    mumbos_mountain_mumbos_skull_note_2 = auto()
    mumbos_mountain_mumbos_skull_note_3 = auto()
    mumbos_mountain_mumbos_skull_note_4 = auto()
    # Blue Eggs
    mumbos_mountain_stonehenge_egg_1 = auto()
    mumbos_mountain_stonehenge_egg_2 = auto()
    mumbos_mountain_stonehenge_egg_3 = auto()
    mumbos_mountain_stonehenge_egg_4 = auto()
    mumbos_mountain_stonehenge_egg_5 = auto()
    mumbos_mountain_tickers_tower_egg_1 = auto()
    mumbos_mountain_tickers_tower_egg_2 = auto()
    mumbos_mountain_tickers_tower_egg_3 = auto()
    mumbos_mountain_tickers_tower_egg_4 = auto()
    mumbos_mountain_tickers_tower_egg_5 = auto()
    mumbos_mountain_tickers_tower_egg_6 = auto()
    mumbos_mountain_mumbos_skull_egg_1 = auto()
    mumbos_mountain_mumbos_skull_egg_2 = auto()
    mumbos_mountain_mumbos_skull_egg_3 = auto()
    mumbos_mountain_mumbos_skull_egg_4 = auto()
    mumbos_mountain_mumbos_skull_egg_5 = auto()
    mumbos_mountain_mumbos_skull_egg_6 = auto()
    mumbos_mountain_mumbos_skull_egg_7 = auto()
    mumbos_mountain_mumbos_skull_egg_8 = auto()
    mumbos_mountain_mumbos_skull_egg_9 = auto()
    mumbos_mountain_mumbos_skull_egg_10 = auto()
    mumbos_mountain_mumbos_skull_egg_11 = auto()
    mumbos_mountain_mumbos_skull_egg_12 = auto()
    # Red Feathers
    # Gold Feathers
    # Jiggies
    mumbos_mountain_inside_mumbos_skull_eye = auto()
    mumbos_mountain_green_slope_jiggy = auto()
    mumbos_mountain_stonehenge_jiggy = auto()
    mumbos_mountain_atop_tickers_tower_jiggy = auto()
    # Empty Honeycombs
    mumbos_mountain_above_juju = auto()
    mumbos_mountain_alcove = auto()
    # Mumbo Tokens
    mumbos_mountain_mumbos_bridge_token = auto()
    mumbos_mountain_near_pink_jinjo_token = auto()
    mumbos_mountain_stonehenge_token = auto()
    mumbos_mountain_conga_token = auto()
    mumbos_mountain_tickers_tower_token = auto()
    # Extra Lives
    mumbos_mountain_atop_tickers_tower_life = auto()
    # Jinjos
    mumbos_mountain_pink_jinjo_platform = auto()
    mumbos_mountain_blue_jinjo_island = auto()
    mumbos_mountain_yellow_jinjo_ledge = auto()
    mumbos_mountain_orange_jinjo_stonehenge = auto()
    # Bottles Molehills
    mumbos_mountain_bottles_beak_buster = auto()
    mumbos_mountain_bottles_talon_trot = auto()
    mumbos_mountain_bottles_egg_firing = auto()
    # Events
    mumbos_mountain_conga = auto()
    mumbos_mountain_chimpy = auto()
    mumbos_mountain_juju = auto()
    mumbos_mountain_orange_pads = auto()
    mumbos_mountain_huts = auto()
    # Other Items
    mumbos_mountain_below_conga = auto()
    # Custom Locations
    ###############################
    ##### TREASURE TROVE COVE #####
    ###############################
    # Notes
    # Blue Eggs
    # Red Feathers
    # Gold Feathers
    # Jiggies
    # Empty Honeycombs
    # Mumbo Tokens
    # Extra Lives
    # Jinjos
    # Bottles Molehills
    # Other Items
    # Custom Locations
    ###########################
    ##### CLANKERS CAVERN #####
    ###########################
    # Notes
    # Blue Eggs
    # Red Feathers
    # Gold Feathers
    # Jiggies
    # Empty Honeycombs
    # Mumbo Tokens
    # Extra Lives
    # Jinjos
    # Bottles Molehills
    # Other Items
    # Custom Locations
    #############################
    ##### BUBBLEGLOOP SWAMP #####
    #############################
    # Notes
    # Blue Eggs
    # Red Feathers
    # Gold Feathers
    # Jiggies
    # Empty Honeycombs
    # Mumbo Tokens
    # Extra Lives
    # Jinjos
    # Bottles Molehills
    # Other Items
    # Custom Locations
    ##########################
    ##### FREEZEEZY PEAK #####
    ##########################
    # Notes
    # Blue Eggs
    # Red Feathers
    # Gold Feathers
    # Jiggies
    # Empty Honeycombs
    # Mumbo Tokens
    # Extra Lives
    # Jinjos
    # Bottles Molehills
    # Other Items
    # Custom Locations
    ########################
    ##### GOBIS VALLEY #####
    ########################
    # Notes
    # Blue Eggs
    # Red Feathers
    # Gold Feathers
    # Jiggies
    # Empty Honeycombs
    # Mumbo Tokens
    # Extra Lives
    # Jinjos
    # Bottles Molehills
    # Other Items
    # Custom Locations
    ###############################
    ##### MAD MONSTER MANSION #####
    ###############################
    # Notes
    # Blue Eggs
    # Red Feathers
    # Gold Feathers
    # Jiggies
    # Empty Honeycombs
    # Mumbo Tokens
    # Extra Lives
    # Jinjos
    # Bottles Molehills
    # Other Items
    # Custom Locations
    ############################
    ##### RUSTY BUCKET BAY #####
    ############################
    # Notes
    # Blue Eggs
    # Red Feathers
    # Gold Feathers
    # Jiggies
    # Empty Honeycombs
    # Mumbo Tokens
    # Extra Lives
    # Jinjos
    # Bottles Molehills
    # Other Items
    # Custom Locations
    ############################
    ##### CLICK CLOCK WOOD #####
    ############################
    # Notes
    # Blue Eggs
    # Red Feathers
    # Gold Feathers
    # Jiggies
    # Empty Honeycombs
    # Mumbo Tokens
    # Extra Lives
    # Jinjos
    # Bottles Molehills
    # Other Items
    # Custom Locations
    ###########################
    ##### GRUNTILDAS LAIR #####
    ###########################
    # Notes
    # Blue Eggs
    # Red Feathers
    # Gold Feathers
    # Jiggies
    gruntildas_lair_first_jiggy = auto()
    gruntildas_lair_mumbos_mountain_witch_switch_jiggy = auto()
    # Empty Honeycombs
    # Mumbo Tokens
    # Extra Lives
    # Jinjos
    # Bottles Molehills
    # Other Items
    # Custom Locations
    # Custom Gruntildas Lair Locations
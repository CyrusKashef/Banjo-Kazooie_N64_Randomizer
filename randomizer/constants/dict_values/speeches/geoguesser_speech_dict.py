###################
##### IMPORTS #####
###################

from randomizer.constants.str_values.string_constants import STRING_CONSTANTS as STR_CONST
from randomizer.constants.int_values.map_setup_asset_ids import MAP_SETUP_ASSET_ID
from randomizer.constants.int_values.map_enums import MAP_ENUMS
from randomizer.constants.int_values.speech_constants import SPEECH_CONSTANTS

#####################
##### CONSTANTS #####
#####################

MUMBOS_MOUNTAIN_ANSWER:str = "ýlMUMBO'S MOUNTAIN"
TREASURE_TROVE_COVE_ANSWER:str = "ýlTREASURE TROVE COVE"
CLANKERS_CAVERN_ANSWER:str = "ýlCLANKER'S CAVERN"
BUBBLEGLOOP_SWAMP_ANSWER:str = "ýlBUBBLEGLOOP SWAMP"
FREEZEEZY_PEAK_ANSWER:str = "ýlFREEZEEZY PEAK"
GOBIS_VALLEY_ANSWER:str = "ýlGOBI'S VALLEY"
MAD_MONSTER_MANSION_ANSWER:str = "ýlMAD MONSTER MANSION"
RUSTY_BUCKET_BAY_ANSWER:str = "ýlRUSTY BUCKET BAY"
CLICK_CLOCK_WOOD_ANSWER:str = "ýlCLICK CLOCK WOOD"
GRUNTILDAS_LAIR_ANSWER:str = "ýlGRUNTILDA'S LAIR"
SPIRAL_MOUNTAIN_ANSWER:str = "ýlSPIRAL MOUNTAIN"

##################################################
##### GEOGUESSER LEVEL SPECIFIC PROMPTS LIST #####
##################################################

GEOGUESSER_LEVEL_SPECIFIC_PROMPTS_LIST:tuple = (
    {
        0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
        1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: MUMBOS_MOUNTAIN_ANSWER},
        2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
        3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
    },
    {
        0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
        1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: TREASURE_TROVE_COVE_ANSWER},
        2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: GOBIS_VALLEY_ANSWER},
        3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
    },
    {
        0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
        1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: CLANKERS_CAVERN_ANSWER},
        2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
        3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
    },
    {
        0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
        1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: BUBBLEGLOOP_SWAMP_ANSWER},
        2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: MAD_MONSTER_MANSION_ANSWER},
        3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
    },
    {
        0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
        1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: FREEZEEZY_PEAK_ANSWER},
        2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
        3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
    },
    {
        0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
        1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: GOBIS_VALLEY_ANSWER},
        2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: TREASURE_TROVE_COVE_ANSWER},
        3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
    },
    {
        0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
        1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: MAD_MONSTER_MANSION_ANSWER},
        2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
        3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
    },
    {
        0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
        1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
        2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: CLANKERS_CAVERN_ANSWER},
        3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
    },
    {
        0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
        1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
        2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: MUMBOS_MOUNTAIN_ANSWER},
        3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
    },
)

####################################################
##### GEOGUESSER LEVEL SPECIFIC QUESTIONS LIST #####
####################################################

GEOGUESSER_LEVEL_SPECIFIC_QUESTIONS_DICT:dict = {
    ###########################
    ##### MUMBOS MOUNTAIN #####
    ###########################
    STR_CONST.mumbos_mountain: (
        {
            STR_CONST.question_dict: { # WALL NEAR JUJU - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: MUMBOS_MOUNTAIN_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.mumbos_mountain_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 3944.305,
                STR_CONST.y_position: 3049.49,
                STR_CONST.z_position: -2741.394,
                STR_CONST.pitch: 358,
                STR_CONST.yaw: 350.75,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # AREA BEHIND MUMBO'S SKULL - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: MUMBOS_MOUNTAIN_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.mumbos_mountain_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 5875.312,
                STR_CONST.y_position: 2475.648,
                STR_CONST.z_position: -3284.654,
                STR_CONST.pitch: 344.5,
                STR_CONST.yaw: 137.5,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # WOOD/STONE WALL TRANSITION - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: MUMBOS_MOUNTAIN_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.mumbos_mountain_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -5054.876,
                STR_CONST.y_position: 758.7698,
                STR_CONST.z_position: 3992.216,
                STR_CONST.pitch: 352,
                STR_CONST.yaw: 97.75,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # GREEN SLIPPERY HILL - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: MUMBOS_MOUNTAIN_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.mumbos_mountain_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 4839.801,
                STR_CONST.y_position: 1055.967,
                STR_CONST.z_position: 1719.067,
                STR_CONST.pitch: 318.75,
                STR_CONST.yaw: 376,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # BROWN SLIPPERY HILL - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: MUMBOS_MOUNTAIN_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.mumbos_mountain_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -1915.028,
                STR_CONST.y_position: 2220.212,
                STR_CONST.z_position: 588.1013,
                STR_CONST.pitch: 323.5,
                STR_CONST.yaw: 381.5,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # TICKER'S TOWER OUTSIDE - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: MUMBOS_MOUNTAIN_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.mumbos_mountain_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -325.0688,
                STR_CONST.y_position: 2314.078,
                STR_CONST.z_position: -1778.104,
                STR_CONST.pitch: 5,
                STR_CONST.yaw: 574.5,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # TALON TROT MOLEHILL - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "THAT DUMB MOLE I DO QUITE SPURN, WHICH MOVE HERE DID YOU LEARN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: "ýlTALON TROT"},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: "ýlBEAK BUSTER"},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: "ýlTURBO TALON TROT"},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.mumbos_mountain_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -2550,
                STR_CONST.y_position: 2500,
                STR_CONST.z_position: -1217,
                STR_CONST.pitch: 270,
                STR_CONST.yaw: 600,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # BEAK BUSTER MOLEHILL - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "THAT DUMB MOLE I DO QUITE SPURN, WHICH MOVE HERE DID YOU LEARN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: "ýlBEAK BUSTER"},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: "ýlTALON TROT"},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: "ýlEGG FIRING"},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.mumbos_mountain_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 3943,
                STR_CONST.y_position: 2450,
                STR_CONST.z_position: -3422,
                STR_CONST.pitch: 270,
                STR_CONST.yaw: 890,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # PATH NEAR JUJU - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: MUMBOS_MOUNTAIN_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.mumbos_mountain_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 4394.735,
                STR_CONST.y_position: 2847.34,
                STR_CONST.z_position: -633.0239,
                STR_CONST.pitch: 270,
                STR_CONST.yaw: 178.5,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # STAIRS TO LEVEL EXIT - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: MUMBOS_MOUNTAIN_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.mumbos_mountain_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 4862.719,
                STR_CONST.y_position: 630.7415,
                STR_CONST.z_position: 4565.066,
                STR_CONST.pitch: 303,
                STR_CONST.yaw: 247.75,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # TICKER'S TOWER GREEN WALL - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: MUMBOS_MOUNTAIN_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.mumbos_mountain_tickers_tower,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -41.9609,
                STR_CONST.y_position: 2478.65,
                STR_CONST.z_position: 315.7167,
                STR_CONST.pitch: 10.5,
                STR_CONST.yaw: 173.25,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # TICKER'S TOWER CEILING - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: MUMBOS_MOUNTAIN_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.mumbos_mountain_tickers_tower,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -23.68592,
                STR_CONST.y_position: 2027.844,
                STR_CONST.z_position: -96.86076,
                STR_CONST.pitch: 90,
                STR_CONST.yaw: 27.75,
                STR_CONST.roll: 0,
            },
        },
    ),
    ###############################
    ##### TREASURE TROVE COVE #####
    ###############################
    STR_CONST.treasure_trove_cove: (
        {
            STR_CONST.question_dict: { # SHOCK JUMP ALCOVE - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: TREASURE_TROVE_COVE_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: SPIRAL_MOUNTAIN_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.treasure_trove_cove_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 3357.357,
                STR_CONST.y_position: 2338.568,
                STR_CONST.z_position: -1500.783,
                STR_CONST.pitch: 18,
                STR_CONST.yaw: 61.75,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # GREEN BRICK WALL - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: TREASURE_TROVE_COVE_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: FREEZEEZY_PEAK_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.treasure_trove_cove_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -5034.56,
                STR_CONST.y_position: 2335.474,
                STR_CONST.z_position: -5796.993,
                STR_CONST.pitch: 0,
                STR_CONST.yaw: 219.5,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # VINE SLOPE NEAR POOLS - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: TREASURE_TROVE_COVE_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: FREEZEEZY_PEAK_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.treasure_trove_cove_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -3727.016,
                STR_CONST.y_position: 1413.319,
                STR_CONST.z_position: 699.9492,
                STR_CONST.pitch: 5.75,
                STR_CONST.yaw: 356.5,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # INSIDE POOL - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: TREASURE_TROVE_COVE_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: FREEZEEZY_PEAK_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.treasure_trove_cove_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -2488.807,
                STR_CONST.y_position: 2667.149,
                STR_CONST.z_position: -4594.222,
                STR_CONST.pitch: 349.5,
                STR_CONST.yaw: 63.75,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # SALTY HIPPO SIGN - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: TREASURE_TROVE_COVE_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: FREEZEEZY_PEAK_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.treasure_trove_cove_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 1568.298,
                STR_CONST.y_position: 1140.217,
                STR_CONST.z_position: 1340.438,
                STR_CONST.pitch: 348.5,
                STR_CONST.yaw: 436,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # SHOCK JUMP PAD NEAR NIPPER - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: TREASURE_TROVE_COVE_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: FREEZEEZY_PEAK_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.treasure_trove_cove_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -3855.651,
                STR_CONST.y_position: 1028.082,
                STR_CONST.z_position: 2754.164,
                STR_CONST.pitch: 270,
                STR_CONST.yaw: 361,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # EXTRA LIFE WATER LEDGE - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: TREASURE_TROVE_COVE_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: FREEZEEZY_PEAK_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.treasure_trove_cove_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -3135.711,
                STR_CONST.y_position: 3560.417,
                STR_CONST.z_position: -1876.887,
                STR_CONST.pitch: 333,
                STR_CONST.yaw: 256.5,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # LIGHTHOUSE LADDER - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: TREASURE_TROVE_COVE_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: FREEZEEZY_PEAK_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.treasure_trove_cove_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 500.6864,
                STR_CONST.y_position: 8372.813,
                STR_CONST.z_position: -2725.929,
                STR_CONST.pitch: 273,
                STR_CONST.yaw: 122.5,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # SALTY HIPPO SIDE CLOSED - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: TREASURE_TROVE_COVE_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: FREEZEEZY_PEAK_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.treasure_trove_cove_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -370.0996,
                STR_CONST.y_position: 434.6263,
                STR_CONST.z_position: 1547.228,
                STR_CONST.pitch: 7.25,
                STR_CONST.yaw: -11.75,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # SAND IN FRONT OF NIPPER - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: TREASURE_TROVE_COVE_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: FREEZEEZY_PEAK_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.treasure_trove_cove_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -4675.352,
                STR_CONST.y_position: 1476.336,
                STR_CONST.z_position: 4084.48,
                STR_CONST.pitch: 270,
                STR_CONST.yaw: 94.75,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # LIGHTHOUSE GRASS TO WALL - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: TREASURE_TROVE_COVE_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: MUMBOS_MOUNTAIN_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.treasure_trove_cove_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -858.6091,
                STR_CONST.y_position: 5688.453,
                STR_CONST.z_position: -1939.85,
                STR_CONST.pitch: 323.75,
                STR_CONST.yaw: 302.5,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # INSIDE NIPPER - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: TREASURE_TROVE_COVE_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: FREEZEEZY_PEAK_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.treasure_trove_cove_nippers_shell,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 716.5,
                STR_CONST.y_position: 158.299,
                STR_CONST.z_position: -380.7033,
                STR_CONST.pitch: 0,
                STR_CONST.yaw: 288,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # INSIDE BLUBBER'S SHIP, WALL - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: TREASURE_TROVE_COVE_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: FREEZEEZY_PEAK_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.treasure_trove_cove_blubbers_ship,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -408.8959,
                STR_CONST.y_position: -297.491,
                STR_CONST.z_position: 13.43445,
                STR_CONST.pitch: 1.75,
                STR_CONST.yaw: 447.5,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # INSIDE SANDCASTLE, EGG DECOR - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: TREASURE_TROVE_COVE_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: FREEZEEZY_PEAK_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.treasure_trove_cove_sandcastle,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 369.7462,
                STR_CONST.y_position: 89.61766,
                STR_CONST.z_position: 802.8957,
                STR_CONST.pitch: 359,
                STR_CONST.yaw: 180.25,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # SHARKFOOD ISLAND - Verified (Shows SnS Egg)
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: TREASURE_TROVE_COVE_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: FREEZEEZY_PEAK_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.treasure_trove_cove_sharkfood_island,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -6.163025,
                STR_CONST.y_position: 3030.83,
                STR_CONST.z_position: 9.063196,
                STR_CONST.pitch: 270,
                STR_CONST.yaw: 134.25,
                STR_CONST.roll: 0,
            },
        },
    ),
    ###########################
    ##### CLANKERS CAVERN #####
    ###########################
    STR_CONST.clankers_cavern: (
        {
            STR_CONST.question_dict: { # GRATED VENT EXTRA LIFE - Verified (No Extra Life)
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: CLANKERS_CAVERN_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.clankers_cavern_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 7306.225,
                STR_CONST.y_position: 3971.166,
                STR_CONST.z_position: 2284.982,
                STR_CONST.pitch: 90,
                STR_CONST.yaw: 202.75,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # MAIN WALL - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: CLANKERS_CAVERN_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.clankers_cavern_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 6004.75,
                STR_CONST.y_position: 2449.571,
                STR_CONST.z_position: 1275.663,
                STR_CONST.pitch: 0,
                STR_CONST.yaw: 186.25,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # MUTIE-SNIPPETS - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: CLANKERS_CAVERN_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: BUBBLEGLOOP_SWAMP_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.clankers_cavern_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 13780,
                STR_CONST.y_position: 3960,
                STR_CONST.z_position: -11,
                STR_CONST.pitch: 90,
                STR_CONST.yaw: 85.25,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # RANDOM DRAIN PIPE - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: CLANKERS_CAVERN_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.clankers_cavern_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -4435.541,
                STR_CONST.y_position: 5524.033,
                STR_CONST.z_position: 499.1089,
                STR_CONST.pitch: 360,
                STR_CONST.yaw: 180,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # MOUTH ROOF - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: CLANKERS_CAVERN_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.clankers_cavern_mouth_belly,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -24.97535,
                STR_CONST.y_position: 1205.94,
                STR_CONST.z_position: 6202.556,
                STR_CONST.pitch: 90,
                STR_CONST.yaw: 0,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # TEETH SIDEWAYS - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: CLANKERS_CAVERN_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.clankers_cavern_mouth_belly,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 32.99876,
                STR_CONST.y_position: 1573.285,
                STR_CONST.z_position: 6700.35,
                STR_CONST.pitch: 0,
                STR_CONST.yaw: 185,
                STR_CONST.roll: 90,
            },
        },
        {
            STR_CONST.question_dict: { # BLOWHOLE ENTRANCE BELLY - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: CLANKERS_CAVERN_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.clankers_cavern_mouth_belly,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -2.15465,
                STR_CONST.y_position: 1980.159,
                STR_CONST.z_position: 2822.181,
                STR_CONST.pitch: 90,
                STR_CONST.yaw: 180,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # BLOWHOLE ENTRANCE MOUTH - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: CLANKERS_CAVERN_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.clankers_cavern_mouth_belly,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 2.245174,
                STR_CONST.y_position: 1992.006,
                STR_CONST.z_position: 5713.401,
                STR_CONST.pitch: 49.25,
                STR_CONST.yaw: 0,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # BELLY TO WONDERWING - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: CLANKERS_CAVERN_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.clankers_cavern_mouth_belly,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -4.619799,
                STR_CONST.y_position: 1803.375,
                STR_CONST.z_position: -2967.287,
                STR_CONST.pitch: 0,
                STR_CONST.yaw: 0,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # BLOWHOLE EXIT TUNNEL - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: CLANKERS_CAVERN_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.clankers_cavern_blowhole,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 0,
                STR_CONST.y_position: -277.7022,
                STR_CONST.z_position: 2197.081,
                STR_CONST.pitch: 0,
                STR_CONST.yaw: 180,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # BLOWHOLE BACKGROUND - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: CLANKERS_CAVERN_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.clankers_cavern_blowhole,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -14.33859,
                STR_CONST.y_position: 523.7628,
                STR_CONST.z_position: -2235.67,
                STR_CONST.pitch: 0,
                STR_CONST.yaw: 0,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # WONDERWING BACKGROUND - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: CLANKERS_CAVERN_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.clankers_cavern_wonderwing,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -1.979507,
                STR_CONST.y_position: 606.3477,
                STR_CONST.z_position: 1888.292,
                STR_CONST.pitch: 345.5,
                STR_CONST.yaw: 180,
                STR_CONST.roll: 0,
            },
        },
    ),
    #############################
    ##### BUBBLEGLOOP SWAMP #####
    #############################
    STR_CONST.bubblegloop_swamp: (
        {
            STR_CONST.question_dict: { # CROCTUS ALCOVE - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: BUBBLEGLOOP_SWAMP_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: MUMBOS_MOUNTAIN_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: TREASURE_TROVE_COVE_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.bubblegloop_swamp_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 1696.633,
                STR_CONST.y_position: 1424.555,
                STR_CONST.z_position: -2921.663,
                STR_CONST.pitch: 21.5,
                STR_CONST.yaw: 1.25,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # SWAMP - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: BUBBLEGLOOP_SWAMP_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: MUMBOS_MOUNTAIN_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: TREASURE_TROVE_COVE_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.bubblegloop_swamp_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -4572.669,
                STR_CONST.y_position: 1235.22,
                STR_CONST.z_position: -7985.53,
                STR_CONST.pitch: 270,
                STR_CONST.yaw: 234.75,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # MAZE WALL - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: BUBBLEGLOOP_SWAMP_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: MUMBOS_MOUNTAIN_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: TREASURE_TROVE_COVE_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.bubblegloop_swamp_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -5819.403,
                STR_CONST.y_position: 1362.346,
                STR_CONST.z_position: -4573.093,
                STR_CONST.pitch: 0,
                STR_CONST.yaw: 180,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # GREEN VINEY WALL NEAR MAZE - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: BUBBLEGLOOP_SWAMP_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: MUMBOS_MOUNTAIN_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: TREASURE_TROVE_COVE_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.bubblegloop_swamp_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -6617.026,
                STR_CONST.y_position: 628.9435,
                STR_CONST.z_position: -6400.8,
                STR_CONST.pitch: 1.5,
                STR_CONST.yaw: 25.5,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # DIRT WALL NEAR MAZE - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: BUBBLEGLOOP_SWAMP_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: MUMBOS_MOUNTAIN_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: TREASURE_TROVE_COVE_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.bubblegloop_swamp_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -3097.467,
                STR_CONST.y_position: 642.2558,
                STR_CONST.z_position: -6481.685,
                STR_CONST.pitch: 3,
                STR_CONST.yaw: 313,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # GREEN TREE WALL NEAR MAZE - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: BUBBLEGLOOP_SWAMP_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: MUMBOS_MOUNTAIN_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: TREASURE_TROVE_COVE_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.bubblegloop_swamp_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -3615.164,
                STR_CONST.y_position: 2262.298,
                STR_CONST.z_position: -9206.062,
                STR_CONST.pitch: 0,
                STR_CONST.yaw: 355.75,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # BROWN WOODS WALL NEAR MAZE - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: BUBBLEGLOOP_SWAMP_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: MUMBOS_MOUNTAIN_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: TREASURE_TROVE_COVE_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.bubblegloop_swamp_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -3786.955,
                STR_CONST.y_position: 2153.943,
                STR_CONST.z_position: -8896.935,
                STR_CONST.pitch: 0,
                STR_CONST.yaw: 422.25,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # MAIN FLOOR - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: BUBBLEGLOOP_SWAMP_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: MUMBOS_MOUNTAIN_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: TREASURE_TROVE_COVE_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.bubblegloop_swamp_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 84.87136,
                STR_CONST.y_position: 731.7421,
                STR_CONST.z_position: 1892.981,
                STR_CONST.pitch: 270,
                STR_CONST.yaw: 520.25,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # CROCODILE - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: BUBBLEGLOOP_SWAMP_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: MUMBOS_MOUNTAIN_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: TREASURE_TROVE_COVE_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.bubblegloop_swamp_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -2950.111,
                STR_CONST.y_position: 963.5966,
                STR_CONST.z_position: -4727.99,
                STR_CONST.pitch: 317.25,
                STR_CONST.yaw: 597.75,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # VILE FLOOR - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: BUBBLEGLOOP_SWAMP_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: MUMBOS_MOUNTAIN_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: TREASURE_TROVE_COVE_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.bubblegloop_swamp_mr_vile,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 190.9366,
                STR_CONST.y_position: 465.6641,
                STR_CONST.z_position: -627.4702,
                STR_CONST.pitch: 270,
                STR_CONST.yaw: 182,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # VILE WALL - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: BUBBLEGLOOP_SWAMP_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: MUMBOS_MOUNTAIN_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: TREASURE_TROVE_COVE_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.bubblegloop_swamp_mr_vile,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -22.68349,
                STR_CONST.y_position: 509.142,
                STR_CONST.z_position: -222.8491,
                STR_CONST.pitch: 10,
                STR_CONST.yaw: 180,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # TANKTUP WALL - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: BUBBLEGLOOP_SWAMP_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: MUMBOS_MOUNTAIN_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: TREASURE_TROVE_COVE_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.bubblegloop_swamp_tip_tup_chior,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 197.5894,
                STR_CONST.y_position: 285.3244,
                STR_CONST.z_position: 6.829033,
                STR_CONST.pitch: 35.5,
                STR_CONST.yaw: 269,
                STR_CONST.roll: 0,
            },
        },
    ),
    ##########################
    ##### FREEZEEZY PEAK #####
    ##########################
    STR_CONST.freezeezy_peak: (
        {
            STR_CONST.question_dict: { # SNOWMAN'S HAT HOLE - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: FREEZEEZY_PEAK_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.freezeezy_peak_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -465.6506,
                STR_CONST.y_position: 7178.462,
                STR_CONST.z_position: 1506.529,
                STR_CONST.pitch: 45.25,
                STR_CONST.yaw: 376,
                STR_CONST.roll: 180,
            },
        },
        {
            STR_CONST.question_dict: { # SNOWMAN'S BROOM - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: FREEZEEZY_PEAK_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.freezeezy_peak_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -3216.458,
                STR_CONST.y_position: 5382.728,
                STR_CONST.z_position: -241.0887,
                STR_CONST.pitch: 1.5,
                STR_CONST.yaw: 605.75,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # SNOWMAN'S SCARF - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: FREEZEEZY_PEAK_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.freezeezy_peak_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -1408.161,
                STR_CONST.y_position: 5150.373,
                STR_CONST.z_position: -936.9828,
                STR_CONST.pitch: 27,
                STR_CONST.yaw: 572.5,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # BIG SLIPPERY ICE - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: FREEZEEZY_PEAK_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.freezeezy_peak_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -684.2966,
                STR_CONST.y_position: 1871.414,
                STR_CONST.z_position: -3886.432,
                STR_CONST.pitch: 302.25,
                STR_CONST.yaw: 359.25,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # MUMBO ICE WATER SHORE - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: FREEZEEZY_PEAK_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.freezeezy_peak_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 5929.298,
                STR_CONST.y_position: 1557.376,
                STR_CONST.z_position: -2552.312,
                STR_CONST.pitch: 270,
                STR_CONST.yaw: 298,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # UNDER CHRISTMAS TREE BRIDGE - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: FREEZEEZY_PEAK_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.freezeezy_peak_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -4497.768,
                STR_CONST.y_position: 3.059343,
                STR_CONST.z_position: 5854.513,
                STR_CONST.pitch: 69.5,
                STR_CONST.yaw: 345.25,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # SNOWMAN'S EYEBALL - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: FREEZEEZY_PEAK_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.freezeezy_peak_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -865.8077,
                STR_CONST.y_position: 6833.189,
                STR_CONST.z_position: 1275.459,
                STR_CONST.pitch: 346.5,
                STR_CONST.yaw: 354.75,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # SKYBOX
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: FREEZEEZY_PEAK_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.freezeezy_peak_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 1418.606,
                STR_CONST.y_position: 4729.076,
                STR_CONST.z_position: 351.7776,
                STR_CONST.pitch: 32.25,
                STR_CONST.yaw: 264.75,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # BOGGY'S IGLOO ROOF - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: FREEZEEZY_PEAK_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.freezeezy_peak_igloo,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 24.99312,
                STR_CONST.y_position: 158.7766,
                STR_CONST.z_position: 408.869,
                STR_CONST.pitch: 47.5,
                STR_CONST.yaw: 3.75,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # CHRISTMAS TOP STEM - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: FREEZEEZY_PEAK_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.freezeezy_peak_christmas_tree,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 0,
                STR_CONST.y_position: 2525,
                STR_CONST.z_position: 0,
                STR_CONST.pitch: 90,
                STR_CONST.yaw: 0,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # CHRISTMAS TREE STAR - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: FREEZEEZY_PEAK_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.freezeezy_peak_christmas_tree,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -1026.883,
                STR_CONST.y_position: 228.2184,
                STR_CONST.z_position: -39.27332,
                STR_CONST.pitch: 9.75,
                STR_CONST.yaw: 88.25,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # WOZZA CAVE STALACTITE - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: FREEZEEZY_PEAK_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.freezeezy_peak_wozzas_cave,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -1015.267,
                STR_CONST.y_position: 989.2142,
                STR_CONST.z_position: -201.3457,
                STR_CONST.pitch: 344,
                STR_CONST.yaw: -212,
                STR_CONST.roll: 0,
            },
        },
    ),
    ########################
    ##### GOBIS VALLEY #####
    ########################
    STR_CONST.gobis_valley: (
        {
            STR_CONST.question_dict: { # UPPER MOAT WALL - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: GOBIS_VALLEY_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.gobis_valley_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -1282.561,
                STR_CONST.y_position: 2107.692,
                STR_CONST.z_position: -868.9236,
                STR_CONST.pitch: 0,
                STR_CONST.yaw: -134.5,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # TRUNKER MOAT
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: GOBIS_VALLEY_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.gobis_valley_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 1010.907,
                STR_CONST.y_position: 315.0595,
                STR_CONST.z_position: 9435.213,
                STR_CONST.pitch: 309.25,
                STR_CONST.yaw: 153.5,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # TRUNKER LONELY ISLAND - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: GOBIS_VALLEY_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.gobis_valley_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 1175.878,
                STR_CONST.y_position: 1003.308,
                STR_CONST.z_position: 8866.885,
                STR_CONST.pitch: 270,
                STR_CONST.yaw: 355.25,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # GREEN JINJO ALCOVE - Verified (Jinjo Is Present)
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: GOBIS_VALLEY_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.gobis_valley_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 5281.177,
                STR_CONST.y_position: 2653.665,
                STR_CONST.z_position: 445.939,
                STR_CONST.pitch: 1,
                STR_CONST.yaw: 90.5,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # JINXY'S EYES - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: GOBIS_VALLEY_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.gobis_valley_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -2822.178,
                STR_CONST.y_position: 3152.207,
                STR_CONST.z_position: 5907.742,
                STR_CONST.pitch: 313.75,
                STR_CONST.yaw: 448.5,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # TARGET - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: GOBIS_VALLEY_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.gobis_valley_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -3961.476,
                STR_CONST.y_position: 4482.903,
                STR_CONST.z_position: 357.4252,
                STR_CONST.pitch: 358,
                STR_CONST.yaw: 357.25,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # SKYBOX - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: GOBIS_VALLEY_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.gobis_valley_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 4128.637,
                STR_CONST.y_position: 5460.396,
                STR_CONST.z_position: 2655.496,
                STR_CONST.pitch: 359,
                STR_CONST.yaw: 228,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # GOBI'S VALLEY KING SANDYBUTT'S MAZE WALL BANJO - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "BE SURE NOT TO DROP YOUR CROWN, WHERE'S THIS PICTURE I HAVE UPSIDE DOWN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: GOBIS_VALLEY_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.gobis_valley_king_sandybutts_tomb,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -1019.474,
                STR_CONST.y_position: 225.1346,
                STR_CONST.z_position: -1837.127,
                STR_CONST.pitch: 2.25,
                STR_CONST.yaw: 179.5,
                STR_CONST.roll: 180,
            },
        },
        {
            STR_CONST.question_dict: { # GOBI'S VALLEY KING SANDYBUTT'S MAZE OUTER WALL - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: GOBIS_VALLEY_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.gobis_valley_king_sandybutts_tomb,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -1159.364,
                STR_CONST.y_position: 812.8812,
                STR_CONST.z_position: -1040.058,
                STR_CONST.pitch: 339,
                STR_CONST.yaw: 89.75,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # GOBI'S VALLEY KING SANDYBUTT'S TOMB CEILING - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: GOBIS_VALLEY_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.gobis_valley_king_sandybutts_tomb,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -4977.362,
                STR_CONST.y_position: 310.397,
                STR_CONST.z_position: 647.7031,
                STR_CONST.pitch: 36.5,
                STR_CONST.yaw: 359.25,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # GOBI'S VALLEY KING SANDYBUTT'S TOMB WALL - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: GOBIS_VALLEY_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.gobis_valley_king_sandybutts_tomb,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -4789.376,
                STR_CONST.y_position: 259.0181,
                STR_CONST.z_position: -269.65,
                STR_CONST.pitch: 353.75,
                STR_CONST.yaw: 336.25,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # SNS CEILING
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: GOBIS_VALLEY_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.gobis_valley_stop_n_swap_egg,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -2.829065,
                STR_CONST.y_position: 754.7567,
                STR_CONST.z_position: -3260.488,
                STR_CONST.pitch: 42.5,
                STR_CONST.yaw: 0.25,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # SNS HALLWAY - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: GOBIS_VALLEY_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.gobis_valley_stop_n_swap_egg,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -9.089915,
                STR_CONST.y_position: 935.5681,
                STR_CONST.z_position: -3695.213,
                STR_CONST.pitch: 345.5,
                STR_CONST.yaw: 184,
                STR_CONST.roll: 0,
            },
        },
    ),
    ###############################
    ##### MAD MONSTER MANSION #####
    ###############################
    STR_CONST.mad_monster_mansion: (
        {
            STR_CONST.question_dict: { # SECOND STORY BROKEN WINDOW - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: MAD_MONSTER_MANSION_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.mad_monster_mansion_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 1992.993,
                STR_CONST.y_position: 1365.756,
                STR_CONST.z_position: 258.102,
                STR_CONST.pitch: 357.75,
                STR_CONST.yaw: 88,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # BEHIND ENTRANCE - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: MAD_MONSTER_MANSION_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.mad_monster_mansion_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 995.2186,
                STR_CONST.y_position: 179.208,
                STR_CONST.z_position: 3597.368,
                STR_CONST.pitch: 0.75,
                STR_CONST.yaw: 182.25,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # MAZE HEDGE WALL - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: MAD_MONSTER_MANSION_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: MUMBOS_MOUNTAIN_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.mad_monster_mansion_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -324.8374,
                STR_CONST.y_position: 259.9305,
                STR_CONST.z_position: -583.9254,
                STR_CONST.pitch: 0,
                STR_CONST.yaw: 96,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # WELL SWAMPY AREA - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: MAD_MONSTER_MANSION_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.mad_monster_mansion_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 6566.775,
                STR_CONST.y_position: 348.8464,
                STR_CONST.z_position: -2835.071,
                STR_CONST.pitch: 270,
                STR_CONST.yaw: 0,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # GREEN POOL - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: MAD_MONSTER_MANSION_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.mad_monster_mansion_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 5910.052,
                STR_CONST.y_position: 223.506,
                STR_CONST.z_position: 1291.208,
                STR_CONST.pitch: 270,
                STR_CONST.yaw: 0,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # GRAVEYARD GRASS - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: MAD_MONSTER_MANSION_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.mad_monster_mansion_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -1122.222,
                STR_CONST.y_position: 501.9447,
                STR_CONST.z_position: -3291.818,
                STR_CONST.pitch: 314.5,
                STR_CONST.yaw: 74.75,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # CHURCH OUTER BRICKS - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: MAD_MONSTER_MANSION_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.mad_monster_mansion_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -1984.714,
                STR_CONST.y_position: 783.8168,
                STR_CONST.z_position: -1598.433,
                STR_CONST.pitch: 0,
                STR_CONST.yaw: 90,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # TALL GRASS - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: MAD_MONSTER_MANSION_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.mad_monster_mansion_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 2080.958,
                STR_CONST.y_position: 545.2666,
                STR_CONST.z_position: -1736.126,
                STR_CONST.pitch: 318.75,
                STR_CONST.yaw: -5,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # ROOF - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: MAD_MONSTER_MANSION_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.mad_monster_mansion_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 963.5428,
                STR_CONST.y_position: 1234.517,
                STR_CONST.z_position: -1471.681,
                STR_CONST.pitch: 320.25,
                STR_CONST.yaw: 180.5,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # BRICK WALL ABOVE CELLAR - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: MAD_MONSTER_MANSION_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.mad_monster_mansion_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -651.3209,
                STR_CONST.y_position: 391.7985,
                STR_CONST.z_position: -245.786,
                STR_CONST.pitch: 0,
                STR_CONST.yaw: 180,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # RED BRICK WALL NEAR MUMBO'S SKULL - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: MAD_MONSTER_MANSION_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.mad_monster_mansion_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -1038.741,
                STR_CONST.y_position: 439.0536,
                STR_CONST.z_position: -4462.667,
                STR_CONST.pitch: 357.5,
                STR_CONST.yaw: 146.25,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # TUMBLAR'S SHED - Verified (hard)
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: MAD_MONSTER_MANSION_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.mad_monster_mansion_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 2042.015,
                STR_CONST.y_position: 580.8999,
                STR_CONST.z_position: -5221.22,
                STR_CONST.pitch: 0,
                STR_CONST.yaw: 180,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # INSIDE LOGGO WALL - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: MAD_MONSTER_MANSION_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.mad_monster_mansion_inside_loggo,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 37.00111,
                STR_CONST.y_position: 482.477,
                STR_CONST.z_position: -219.8717,
                STR_CONST.pitch: 0,
                STR_CONST.yaw: 180,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # INSIDE LOGGO CEILING
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: MAD_MONSTER_MANSION_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.mad_monster_mansion_inside_loggo,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -2.20474,
                STR_CONST.y_position: 327.1584,
                STR_CONST.z_position: 57.22723,
                STR_CONST.pitch: 90,
                STR_CONST.yaw: 6.75,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # INSIDE CHURCH BRICK WALL - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: MAD_MONSTER_MANSION_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.mad_monster_mansion_church_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -60.20097,
                STR_CONST.y_position: 2326.999,
                STR_CONST.z_position: 589.6569,
                STR_CONST.pitch: 3.75,
                STR_CONST.yaw: -180.75,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # INSIDE CHURCH PIANO SIDE NOTES
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: MAD_MONSTER_MANSION_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.mad_monster_mansion_church_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -2279.277,
                STR_CONST.y_position: 483.2618,
                STR_CONST.z_position: -2781.837,
                STR_CONST.pitch: 0,
                STR_CONST.yaw: -90,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # INSIDE CHURCH STONE FLOOR
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: MAD_MONSTER_MANSION_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.mad_monster_mansion_church_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -1452.715,
                STR_CONST.y_position: 1747.367,
                STR_CONST.z_position: 3239.045,
                STR_CONST.pitch: 270,
                STR_CONST.yaw: 0,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # INSIDE CHURCH RUG - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: MAD_MONSTER_MANSION_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.mad_monster_mansion_church_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -860.2027,
                STR_CONST.y_position: 1009.819,
                STR_CONST.z_position: -1135.755,
                STR_CONST.pitch: 270,
                STR_CONST.yaw: 0,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # CELLAR WINE RACK - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: MAD_MONSTER_MANSION_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.mad_monster_mansion_cellar,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -15.46668,
                STR_CONST.y_position: 145.2814,
                STR_CONST.z_position: 921.9053,
                STR_CONST.pitch: 0,
                STR_CONST.yaw: 180,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # CELLAR CEILING - Verified (Looks like two boxes lmao)
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: MAD_MONSTER_MANSION_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.mad_monster_mansion_cellar,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 0,
                STR_CONST.y_position: 100,
                STR_CONST.z_position: 0,
                STR_CONST.pitch: 90,
                STR_CONST.yaw: 90,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # CELLAR RIPPED WALLPAPER - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: MAD_MONSTER_MANSION_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.mad_monster_mansion_cellar,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 350.2066,
                STR_CONST.y_position: 199.3553,
                STR_CONST.z_position: -728.6328,
                STR_CONST.pitch: 2,
                STR_CONST.yaw: -4.25,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # DINING ROOM PURPLE RUG - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: MAD_MONSTER_MANSION_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.mad_monster_mansion_dining_room,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 7.823772,
                STR_CONST.y_position: 542.2625,
                STR_CONST.z_position: 2134.485,
                STR_CONST.pitch: 270,
                STR_CONST.yaw: 0,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # DINING ROOM UGLY ASS WALLPAPER LMAO
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: MAD_MONSTER_MANSION_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.mad_monster_mansion_dining_room,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -20.96531,
                STR_CONST.y_position: 896.8608,
                STR_CONST.z_position: 1078.573,
                STR_CONST.pitch: 0,
                STR_CONST.yaw: 180,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # DINING ROOM UP CHIMNEY - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: MAD_MONSTER_MANSION_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.mad_monster_mansion_dining_room,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 5.137066,
                STR_CONST.y_position: 299.9282,
                STR_CONST.z_position: -2759.191,
                STR_CONST.pitch: 90,
                STR_CONST.yaw: 180,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # BEDROOM BEDFRAME - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: MAD_MONSTER_MANSION_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.mad_monster_mansion_bedroom,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -451.1894,
                STR_CONST.y_position: 300.5799,
                STR_CONST.z_position: 299.4879,
                STR_CONST.pitch: 0,
                STR_CONST.yaw: 90,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # DRAINPIPE ROOF
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: MAD_MONSTER_MANSION_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.mad_monster_mansion_drainpipe,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 11.08807,
                STR_CONST.y_position: 491.8031,
                STR_CONST.z_position: -11.61693,
                STR_CONST.pitch: 90,
                STR_CONST.yaw: 270,
                STR_CONST.roll: 0,
            },
        },
    ),
    ############################
    ##### RUSTY BUCKET BAY #####
    ############################
    STR_CONST.rusty_bucket_bay: (
        {
            STR_CONST.question_dict: { # TOXIC WASTE AREA - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: CLANKERS_CAVERN_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.rusty_bucket_bay_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -7886.307,
                STR_CONST.y_position: -1605.14,
                STR_CONST.z_position: -3256.356,
                STR_CONST.pitch: 340,
                STR_CONST.yaw: 143.5,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # RANDOM HOLE IN THE WALL - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: CLANKERS_CAVERN_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.rusty_bucket_bay_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 8163.528,
                STR_CONST.y_position: -380.8172,
                STR_CONST.z_position: 3559.135,
                STR_CONST.pitch: 0,
                STR_CONST.yaw: 270,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # GARAGE BEHIND LEVEL ENTRANCE - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: CLANKERS_CAVERN_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.rusty_bucket_bay_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 1011.278,
                STR_CONST.y_position: -320.2595,
                STR_CONST.z_position: 4863.44,
                STR_CONST.pitch: 0,
                STR_CONST.yaw: 180,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # LARGE BOAT DOORS - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: CLANKERS_CAVERN_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.rusty_bucket_bay_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 9334.849,
                STR_CONST.y_position: -1935.297,
                STR_CONST.z_position: 11.75977,
                STR_CONST.pitch: 0,
                STR_CONST.yaw: 270,
                STR_CONST.roll: 0,
            },
        },
        # {
        #     STR_CONST.question_dict: { # BROWN BRICK WALL - Verified
        #         SPEECH_CONSTANTS.full_screen: {
        #             0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
        #             1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
        #             2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
        #             3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: CLANKERS_CAVERN_ANSWER},
        #         },
        #     },
        #     STR_CONST.map_enum: MAP_ENUMS.rusty_bucket_bay_main,
        #     STR_CONST.camera_dict: {
        #         STR_CONST.camera_type: 2,
        #         STR_CONST.x_position: -6991.774,
        #         STR_CONST.y_position: 1596.689,
        #         STR_CONST.z_position: -4576.076,
        #         STR_CONST.pitch: 0,
        #         STR_CONST.yaw: 270,
        #         STR_CONST.roll: 0,
        #     },
        # },
        {
            STR_CONST.question_dict: { # BROWN BRICK WALL
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: CLANKERS_CAVERN_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.rusty_bucket_bay_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -7402.445,
                STR_CONST.y_position: 1753.976,
                STR_CONST.z_position: -4604.167,
                STR_CONST.pitch: 0,
                STR_CONST.yaw: 270,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # VINEY BRICK WALL - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: CLANKERS_CAVERN_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.rusty_bucket_bay_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 6560.099,
                STR_CONST.y_position: -1947.452,
                STR_CONST.z_position: 1780.343,
                STR_CONST.pitch: 0,
                STR_CONST.yaw: 180,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # ANCHOR ROOM BLUE WALL - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: CLANKERS_CAVERN_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.rusty_bucket_bay_anchor_room,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 3988.985,
                STR_CONST.y_position: 1006.562,
                STR_CONST.z_position: 27.66792,
                STR_CONST.pitch: 0,
                STR_CONST.yaw: 0,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # ENGINE ROOM LARGE RANDOM PIPE - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: CLANKERS_CAVERN_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.rusty_bucket_bay_anchor_room,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -1504.4,
                STR_CONST.y_position: 1558.744,
                STR_CONST.z_position: 53.95737,
                STR_CONST.pitch: 0,
                STR_CONST.yaw: 90,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # CHUMP WAREHOUSE FLOOR - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: CLANKERS_CAVERN_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.rusty_bucket_bay_chump_warehouse,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 780.3677,
                STR_CONST.y_position: -583.9476,
                STR_CONST.z_position: -86.18205,
                STR_CONST.pitch: 318,
                STR_CONST.yaw: 94,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # HE TOUCHED THE BUTT - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: CLANKERS_CAVERN_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.rusty_bucket_bay_boat_room,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -17.93646,
                STR_CONST.y_position: -430.7504,
                STR_CONST.z_position: 56.09351,
                STR_CONST.pitch: 84,
                STR_CONST.yaw: 0.25,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # CLOSED TOP - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: CLANKERS_CAVERN_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.rusty_bucket_bay_boom_box_container,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -50.0836,
                STR_CONST.y_position: 229.5067,
                STR_CONST.z_position: -357.7157,
                STR_CONST.pitch: 90,
                STR_CONST.yaw: 270,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # BLUE BED - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: CLANKERS_CAVERN_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.rusty_bucket_bay_cabin_window,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -363.0436,
                STR_CONST.y_position: 227.4341,
                STR_CONST.z_position: 362.6899,
                STR_CONST.pitch: 313,
                STR_CONST.yaw: 90,
                STR_CONST.roll: 0,
            },
        },
    ),
    ############################
    ##### CLICK CLOCK WOOD #####
    ############################
    STR_CONST.click_clock_wood: (
        {
            STR_CONST.question_dict: { # UNDER A BRIDGE - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: MUMBOS_MOUNTAIN_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.click_clock_wood_main_hub,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -1288.207,
                STR_CONST.y_position: -17.91627,
                STR_CONST.z_position: 8.312572,
                STR_CONST.pitch: 4.75,
                STR_CONST.yaw: 88.5,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # HUB SPRING AREA - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: MUMBOS_MOUNTAIN_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.click_clock_wood_main_hub,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 533.0525,
                STR_CONST.y_position: 649.8201,
                STR_CONST.z_position: 2394.224,
                STR_CONST.pitch: 271.25,
                STR_CONST.yaw: 182,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # HUB SKYBOX - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: MUMBOS_MOUNTAIN_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.click_clock_wood_main_hub,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 418.9485,
                STR_CONST.y_position: 1496.504,
                STR_CONST.z_position: 708.952,
                STR_CONST.pitch: 61.25,
                STR_CONST.yaw: 232.75,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # JUNGLE TREES - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: MUMBOS_MOUNTAIN_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.click_clock_wood_spring_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 4772.215,
                STR_CONST.y_position: 5450.205,
                STR_CONST.z_position: -50.39964,
                STR_CONST.pitch: 350.5,
                STR_CONST.yaw: 280,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # SUMMER WALL - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: MUMBOS_MOUNTAIN_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.click_clock_wood_summer_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 3414.092,
                STR_CONST.y_position: 58.20487,
                STR_CONST.z_position: 1748.724,
                STR_CONST.pitch: 357.75,
                STR_CONST.yaw: 101.5,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # SUMMER TREE LEAVES - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: MUMBOS_MOUNTAIN_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.click_clock_wood_summer_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -286.1222,
                STR_CONST.y_position: 4781.244,
                STR_CONST.z_position: -4608.238,
                STR_CONST.pitch: 3.25,
                STR_CONST.yaw: 31.5,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # EYRIE'S NEST
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: MUMBOS_MOUNTAIN_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.click_clock_wood_winter_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -3868.462,
                STR_CONST.y_position: 3530.367,
                STR_CONST.z_position: 43.04758,
                STR_CONST.pitch: 55.5,
                STR_CONST.yaw: 90.5,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # WINTER SNOWY HILLS
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: MUMBOS_MOUNTAIN_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.click_clock_wood_winter_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -5446.411,
                STR_CONST.y_position: 891.1115,
                STR_CONST.z_position: 1072.035,
                STR_CONST.pitch: 335.75,
                STR_CONST.yaw: 245,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # TEAL TREE SIDE
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: MUMBOS_MOUNTAIN_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.click_clock_wood_winter_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 3435.918,
                STR_CONST.y_position: 1963.641,
                STR_CONST.z_position: -1694.236,
                STR_CONST.pitch: 0,
                STR_CONST.yaw: 115.5,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # FROZEN BEEHIVE - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: MUMBOS_MOUNTAIN_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.click_clock_wood_winter_main,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 70.02638,
                STR_CONST.y_position: 3362.301,
                STR_CONST.z_position: -4577.728,
                STR_CONST.pitch: 351.5,
                STR_CONST.yaw: 180.25,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # NABNUT ACORN STORAGE VINES - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: MUMBOS_MOUNTAIN_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.click_clock_wood_winter_acorn_attic,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: 132.788,
                STR_CONST.y_position: 895.5581,
                STR_CONST.z_position: -174.8974,
                STR_CONST.pitch: 359.5,
                STR_CONST.yaw: 265.75,
                STR_CONST.roll: 0,
            },
        },
        {
            STR_CONST.question_dict: { # WHIPCRACK ROOM VINES - Verified
                SPEECH_CONSTANTS.full_screen: {
                    0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                    1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
                    2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: MUMBOS_MOUNTAIN_ANSWER},
                    3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                },
            },
            STR_CONST.map_enum: MAP_ENUMS.click_clock_wood_spring_whipcracks,
            STR_CONST.camera_dict: {
                STR_CONST.camera_type: 2,
                STR_CONST.x_position: -392.0549,
                STR_CONST.y_position: 385.5459,
                STR_CONST.z_position: -104.5909,
                STR_CONST.pitch: 1.75,
                STR_CONST.yaw: 67,
                STR_CONST.roll: 0,
            },
        },
    ),
}

#############################################
##### GEOGUESSER GENERAL QUESTIONS LIST #####
#############################################

GEOGUESSER_GENERAL_SPEECH_DICT:dict = (
    ###########################
    ##### MUMBOS MOUNTAIN #####
    ###########################
    ###############################
    ##### TREASURE TROVE COVE #####
    ###############################
    # {
    #     STR_CONST.question_dict: { # INSIDE SANDCASTLE, KAZOOIE WITH SHELLS - Verified
    #         SPEECH_CONSTANTS.full_screen: {
    #             0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SOLVED THIS PUZZLE WITH GOOD FACING, BUT WHICH DIRECTION IS THIS FACING?"},
    #             1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: "ýlRIGHT OF THE ENTRANCE"},
    #             2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: "ýlLEFT OF THE ENTRANCE"},
    #             3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: "ýlON THE CEILING"},
    #         },
    #     },
    #     STR_CONST.map_enum: MAP_ENUMS.treasure_trove_cove_sandcastle,
    #     STR_CONST.camera_dict: {
    #         STR_CONST.camera_type: 2,
    #         STR_CONST.x_position: 414.2784,
    #         STR_CONST.y_position: 240.6057,
    #         STR_CONST.z_position: 136.5121,
    #         STR_CONST.pitch: 1.5,
    #         STR_CONST.yaw: 268.75,
    #         STR_CONST.roll: 0,
    #     },
    # },
    # {
    #     STR_CONST.question_dict: { # INSIDE SANDCASTLE, KAZOOIE WITHOUT SHELLS - Verified
    #         SPEECH_CONSTANTS.full_screen: {
    #             0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SOLVED THIS PUZZLE WITH GOOD FACING, BUT WHICH DIRECTION IS THIS FACING?"},
    #             1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: "ýlLEFT OF THE ENTRANCE"},
    #             2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: "ýlRIGHT OF THE ENTRANCE"},
    #             3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: "ýlON THE CEILING"},
    #         },
    #     },
    #     STR_CONST.map_enum: MAP_ENUMS.treasure_trove_cove_sandcastle,
    #     STR_CONST.camera_dict: {
    #         STR_CONST.camera_type: 2,
    #         STR_CONST.x_position: -382.6091,
    #         STR_CONST.y_position: 230.8376,
    #         STR_CONST.z_position: -135.725,
    #         STR_CONST.pitch: 5.75,
    #         STR_CONST.yaw: 446.75,
    #         STR_CONST.roll: 0,
    #     },
    # },
    ###########################
    ##### CLANKERS CAVERN #####
    ###########################
    # {
    #     STR_CONST.question_dict: { # GOLDEN SHORT PIPE - Verified
    #         SPEECH_CONSTANTS.full_screen: {
    #             0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SURELY ITEMS YOU WOULDN'T NEGLECT, WHICH ONE HERE DO YOU COLLECT?"},
    #             1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: "ýlMUMBO TOKEN"},
    #             2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: "ýlEMPTY HONEYCOMB"},
    #             3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: "ýlEXTRA LIFE"},
    #         },
    #     },
    #     STR_CONST.map_enum: MAP_ENUMS.clankers_cavern_main,
    #     STR_CONST.camera_dict: {
    #         STR_CONST.camera_type: 2,
    #         STR_CONST.x_position: 925.5875,
    #         STR_CONST.y_position: 2294.469,
    #         STR_CONST.z_position: -2630.054,
    #         STR_CONST.pitch: 15,
    #         STR_CONST.yaw: 365,
    #         STR_CONST.roll: 0,
    #     },
    # },
    # {
    #     STR_CONST.question_dict: { # BLOWHOLE TO MOUTH - Verified
    #         SPEECH_CONSTANTS.full_screen: {
    #             0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "PASSED THIS TUNNEL AT BLAZING SPEED, GOING THROUGH IT, WHERE DOES IT LEAD?"},
    #             1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: "ýlYOU CAN'T GO IN THIS DIRECTION"},
    #             2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: "ýlWONDERWING BOTTLES TUNNEL"},
    #             3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: "ýlOUT CLANKER'S RIGHT GILL"},
    #         },
    #     },
    #     STR_CONST.map_enum: MAP_ENUMS.clankers_cavern_mouth_belly,
    #     STR_CONST.camera_dict: {
    #         STR_CONST.camera_type: 2,
    #         STR_CONST.x_position: 1,
    #         STR_CONST.y_position: 1727.161,
    #         STR_CONST.z_position: 5988.179,
    #         STR_CONST.pitch: 45.5,
    #         STR_CONST.yaw: 359.5,
    #         STR_CONST.roll: 0,
    #     },
    # },
    #############################
    ##### BUBBLEGLOOP SWAMP #####
    #############################
    # {
    #     STR_CONST.question_dict: { # ATOP CROCODILE - Verified
    #         SPEECH_CONSTANTS.full_screen: {
    #             0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "WE KNOW THE LEVEL, BUT I WON'T STOP, WHAT WOULD YOU BE STANDING ON TOP?"},
    #             1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: "ýlA CROCODILE"},
    #             2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: "ýlA HUT"},
    #             3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: "ýlA CATTAIL"},
    #         },
    #     },
    #     STR_CONST.map_enum: MAP_ENUMS.bubblegloop_swamp_main,
    #     STR_CONST.camera_dict: {
    #         STR_CONST.camera_type: 2,
    #         STR_CONST.x_position: -1764.15,
    #         STR_CONST.y_position: 1465.964,
    #         STR_CONST.z_position: -4184.32,
    #         STR_CONST.pitch: 353.25,
    #         STR_CONST.yaw: 232,
    #         STR_CONST.roll: 0,
    #     },
    # },
    # {
    #     STR_CONST.question_dict: { # ATOP HUT - Verified
    #         SPEECH_CONSTANTS.full_screen: {
    #             0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "WE KNOW THE LEVEL, BUT I WON'T STOP, WHAT WOULD YOU BE STANDING ON TOP?"},
    #             1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: "ýlA HUT"},
    #             2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: "ýlA CROCODILE"},
    #             3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: "ýlA CATTAIL"},
    #         },
    #     },
    #     STR_CONST.map_enum: MAP_ENUMS.bubblegloop_swamp_main,
    #     STR_CONST.camera_dict: {
    #         STR_CONST.camera_type: 2,
    #         STR_CONST.x_position: 4905.651,
    #         STR_CONST.y_position: 1521.388,
    #         STR_CONST.z_position: -4358.437,
    #         STR_CONST.pitch: 355.25,
    #         STR_CONST.yaw: 136.5,
    #         STR_CONST.roll: 0,
    #     },
    # },
    ##########################
    ##### FREEZEEZY PEAK #####
    ##########################
    # {
    #     STR_CONST.question_dict: { # HOVERED ABOVE PRESENTS - Verified
    #         SPEECH_CONSTANTS.full_screen: {
    #             0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "FREEZEEZY PEAK WE KNOW SO WELL, BUT WHERE IS THIS, CAN YOU TELL?"},
    #             1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: "ýlNEAR A STACK OF PRESENTS"},
    #             2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: "ýlBEHIND THE CHRISTMAS TREE"},
    #             3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: "ýlINSIDE WOZZA'S CAVE"},
    #         },
    #     },
    #     STR_CONST.map_enum: MAP_ENUMS.freezeezy_peak_main,
    #     STR_CONST.camera_dict: {
    #         STR_CONST.camera_type: 2,
    #         STR_CONST.x_position: -5442.054,
    #         STR_CONST.y_position: 2337.45,
    #         STR_CONST.z_position: 1194,
    #         STR_CONST.pitch: 354.25,
    #         STR_CONST.yaw: 446.5,
    #         STR_CONST.roll: 0,
    #     },
    # },
    ########################
    ##### GOBIS VALLEY #####
    ########################
    ###############################
    ##### MAD MONSTER MANSION #####
    ###############################
    ############################
    ##### RUSTY BUCKET BAY #####
    ############################
    # {
    #     STR_CONST.question_dict: { # RAREWARE YELLOW CONTAINER ON BOAT - Verified
    #         SPEECH_CONSTANTS.full_screen: {
    #             0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "RUSTY BUCKET HAS A LOT OF WARES, BUT THIS ONE IS CONSIDERED RARE'S!"},
    #             1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: "ýlON THE DECK OF THE BOAT"},
    #             2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: "ýlIN ONE OF THE BLUE CONTAINERS"},
    #             3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: "ýlIN THE WAREHOUSE WITH A CHUMP"},
    #         },
    #     },
    #     STR_CONST.map_enum: MAP_ENUMS.rusty_bucket_bay_main,
    #     STR_CONST.camera_dict: {
    #         STR_CONST.camera_type: 2,
    #         STR_CONST.x_position: 4647.633,
    #         STR_CONST.y_position: 43.98711,
    #         STR_CONST.z_position: 1404.164,
    #         STR_CONST.pitch: 0.5,
    #         STR_CONST.yaw: -0.25,
    #         STR_CONST.roll: 0,
    #     },
    # },
    # {
    #     STR_CONST.question_dict: { # NAVIGATION ROOM MAP - Verified
    #         SPEECH_CONSTANTS.full_screen: {
    #             0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "RUSTY BUCKET BAY IS FULL OF DETAIL, BUT WHICH AREA DOES THIS ENTAIL?"},
    #             1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: "ýlNAVIGATION ROOM"},
    #             2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: "ýlKITCHEN"},
    #             3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: "ýlCAPTAIN'S BEDROOM"},
    #         },
    #     },
    #     STR_CONST.map_enum: MAP_ENUMS.rusty_bucket_bay_navigation_window,
    #     STR_CONST.camera_dict: {
    #         STR_CONST.camera_type: 2,
    #         STR_CONST.x_position: 89.59196,
    #         STR_CONST.y_position: 367.8279,
    #         STR_CONST.z_position: -688.2775,
    #         STR_CONST.pitch: 2.75,
    #         STR_CONST.yaw: 362,
    #         STR_CONST.roll: 0,
    #     },
    # },
    # {
    #     STR_CONST.question_dict: { # CABIN ROOM WINDOW - Verified
    #         SPEECH_CONSTANTS.full_screen: {
    #             0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "THE SHIP HAS WINDOWS YOU WENT THROUGH, WHICH ROOM WOULD HAVE THIS LOVELY VIEW?"},
    #             1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: "ýlSEAMAN GRUBLIN CABINS"},
    #             2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: "ýlNAVIGATION ROOM"},
    #             3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: "ýlCAPTAIN'S BEDROOM"},
    #         },
    #     },
    #     STR_CONST.map_enum: MAP_ENUMS.rusty_bucket_bay_cabin_window,
    #     STR_CONST.camera_dict: {
    #         STR_CONST.camera_type: 2,
    #         STR_CONST.x_position: 4.449204,
    #         STR_CONST.y_position: 280.84,
    #         STR_CONST.z_position: -260.0715,
    #         STR_CONST.pitch: 355,
    #         STR_CONST.yaw: 0.75,
    #         STR_CONST.roll: 0,
    #     },
    # },
    ############################
    ##### CLICK CLOCK WOOD #####
    ############################
    ###########################
    ##### SPIRAL MOUNTAIN #####
    ###########################
    {
        STR_CONST.question_dict: { # UNDER GRUNTILDA HEAD - Verified
            SPEECH_CONSTANTS.full_screen: {
                0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: SPIRAL_MOUNTAIN_ANSWER},
                2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
            },
        },
        STR_CONST.map_enum: MAP_ENUMS.spiral_mountain_main,
        STR_CONST.camera_dict: {
            STR_CONST.camera_type: 2,
            STR_CONST.x_position: -51.64992,
            STR_CONST.y_position: 824.8796,
            STR_CONST.z_position: -3242.825,
            STR_CONST.pitch: 82,
            STR_CONST.yaw: 1.75,
            STR_CONST.roll: 0,
        },
    },
    {
        STR_CONST.question_dict: { # LAKE - Verified
            SPEECH_CONSTANTS.full_screen: {
                0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: SPIRAL_MOUNTAIN_ANSWER},
                2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: MUMBOS_MOUNTAIN_ANSWER},
            },
        },
        STR_CONST.map_enum: MAP_ENUMS.spiral_mountain_main,
        STR_CONST.camera_dict: {
            STR_CONST.camera_type: 2,
            STR_CONST.x_position: -6005.871,
            STR_CONST.y_position: 317.8342,
            STR_CONST.z_position: -1182.092,
            STR_CONST.pitch: 344.75,
            STR_CONST.yaw: 267.5,
            STR_CONST.roll: 0,
        },
    },
    ############################
    ##### GRUNTILDA'S LAIR #####
    ############################
    {
        STR_CONST.question_dict: { # CLOUD AT MUMBO'S MOUNTAIN ENTRANCE - Verified
            SPEECH_CONSTANTS.full_screen: {
                0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: MUMBOS_MOUNTAIN_ANSWER},
                3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
            },
        },
        STR_CONST.map_enum: MAP_ENUMS.gruntildas_lair_mumbos_mountain_entrance,
        STR_CONST.camera_dict: {
            STR_CONST.camera_type: 2,
            STR_CONST.x_position: 3498.595,
            STR_CONST.y_position: 1102.637,
            STR_CONST.z_position: -1809.923,
            STR_CONST.pitch: 3,
            STR_CONST.yaw: 68.5,
            STR_CONST.roll: 0,
        },
    },
    {
        STR_CONST.question_dict: { # HALLWAY TO MUMBO'S MOUNTAIN PUZZLE - Verified
            SPEECH_CONSTANTS.full_screen: {
                0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: MUMBOS_MOUNTAIN_ANSWER},
                3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
            },
        },
        STR_CONST.map_enum: MAP_ENUMS.gruntildas_lair_mumbos_mountain_entrance,
        STR_CONST.camera_dict: {
            STR_CONST.camera_type: 2,
            STR_CONST.x_position: 3424.183,
            STR_CONST.y_position: 107.8559,
            STR_CONST.z_position: -1037.881,
            STR_CONST.pitch: 41.75,
            STR_CONST.yaw: 221.25,
            STR_CONST.roll: 0,
        },
    },
    {
        STR_CONST.question_dict: { # LIGHT ABOVE TTC/CC PUZZLES - Verified
            SPEECH_CONSTANTS.full_screen: {
                0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: BUBBLEGLOOP_SWAMP_ANSWER},
                3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: MAD_MONSTER_MANSION_ANSWER},
            },
        },
        STR_CONST.map_enum: MAP_ENUMS.gruntildas_lair_treasure_trove_cove_clankers_cavern_puzzles,
        STR_CONST.camera_dict: {
            STR_CONST.camera_type: 2,
            STR_CONST.x_position: 430.1624,
            STR_CONST.y_position: 112.9697,
            STR_CONST.z_position: 895.9904,
            STR_CONST.pitch: 58.25,
            STR_CONST.yaw: 26.5,
            STR_CONST.roll: 0,
        },
    },
    {
        STR_CONST.question_dict: { # CEILING ABOVE PINK CAULDRON - Verified
            SPEECH_CONSTANTS.full_screen: {
                0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: BUBBLEGLOOP_SWAMP_ANSWER},
                3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: MAD_MONSTER_MANSION_ANSWER},
            },
        },
        STR_CONST.map_enum: MAP_ENUMS.gruntildas_lair_treasure_trove_cove_clankers_cavern_puzzles,
        STR_CONST.camera_dict: {
            STR_CONST.camera_type: 2,
            STR_CONST.x_position: -1109.441,
            STR_CONST.y_position: -600.4733,
            STR_CONST.z_position: 3334.131,
            STR_CONST.pitch: 50.25,
            STR_CONST.yaw: 228.75,
            STR_CONST.roll: 0,
        },
    },
    {
        STR_CONST.question_dict: { # WALL BELOW CLANKER'S CAVERN PUZZLE
            SPEECH_CONSTANTS.full_screen: {
                0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: CLANKERS_CAVERN_ANSWER},
                3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
            },
        },
        STR_CONST.map_enum: MAP_ENUMS.gruntildas_lair_treasure_trove_cove_clankers_cavern_puzzles,
        STR_CONST.camera_dict: {
            STR_CONST.camera_type: 2,
            STR_CONST.x_position: -1075.489,
            STR_CONST.y_position: 417.0432,
            STR_CONST.z_position: -500.3755,
            STR_CONST.pitch: 4.25,
            STR_CONST.yaw: 57.75,
            STR_CONST.roll: 0,
        },
    },
    {
        STR_CONST.question_dict: { # WALL ABOVE 50 NOTE DOOR EXIT
            SPEECH_CONSTANTS.full_screen: {
                0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: TREASURE_TROVE_COVE_ANSWER},
                3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GOBIS_VALLEY_ANSWER},
            },
        },
        STR_CONST.map_enum: MAP_ENUMS.gruntildas_lair_treasure_trove_cove_clankers_cavern_puzzles,
        STR_CONST.camera_dict: {
            STR_CONST.camera_type: 2,
            STR_CONST.x_position: 390.0092,
            STR_CONST.y_position: 844.2415,
            STR_CONST.z_position: 817.8067,
            STR_CONST.pitch: 1.5,
            STR_CONST.yaw: 215.25,
            STR_CONST.roll: 0,
        },
    },
    # {
    #     STR_CONST.question_dict: { # ABOVE UNDERWATER CCW PUZZLE ENTRANCE - Verified
    #         SPEECH_CONSTANTS.full_screen: {
    #             0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
    #             1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
    #             2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: MUMBOS_MOUNTAIN_ANSWER},
    #             3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
    #         },
    #     },
    #     STR_CONST.map_enum: MAP_ENUMS.gruntildas_lair_click_clock_wood_puzzle,
    #     STR_CONST.camera_dict: {
    #         STR_CONST.camera_type: 2,
    #         STR_CONST.x_position: 4870.958,
    #         STR_CONST.y_position: 396.9359,
    #         STR_CONST.z_position: 1847.595,
    #         STR_CONST.pitch: 5,
    #         STR_CONST.yaw: 403,
    #         STR_CONST.roll: 0,
    #     },
    # },
    {
        STR_CONST.question_dict: { # YUM-YUM PICTURE
            SPEECH_CONSTANTS.full_screen: {
                0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: TREASURE_TROVE_COVE_ANSWER},
                3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GOBIS_VALLEY_ANSWER},
            },
        },
        STR_CONST.map_enum: MAP_ENUMS.gruntildas_lair_click_clock_wood_puzzle,
        STR_CONST.camera_dict: {
            STR_CONST.camera_type: 2,
            STR_CONST.x_position: 828.8434,
            STR_CONST.y_position: 218.8694,
            STR_CONST.z_position: -215.7536,
            STR_CONST.pitch: 356,
            STR_CONST.yaw: 328,
            STR_CONST.roll: 0,
        },
    },
    # {
    #     STR_CONST.question_dict: { # ABOVE 180 NOTE DOOR ENTRANCE - Verified
    #         SPEECH_CONSTANTS.full_screen: {
    #             0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
    #             1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
    #             2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: BUBBLEGLOOP_SWAMP_ANSWER},
    #             3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: MAD_MONSTER_MANSION_ANSWER},
    #         },
    #     },
    #     STR_CONST.map_enum: MAP_ENUMS.gruntildas_lair_pointing_grunty_statue,
    #     STR_CONST.camera_dict: {
    #         STR_CONST.camera_type: 2,
    #         STR_CONST.x_position: 69.63149,
    #         STR_CONST.y_position: 866.5637,
    #         STR_CONST.z_position: 1661.445,
    #         STR_CONST.pitch: 43.25,
    #         STR_CONST.yaw: 180.5,
    #         STR_CONST.roll: 0,
    #     },
    # },
    # {
    #     STR_CONST.question_dict: { # FREEZEEZY PEAK CAVE WALL PAINTING - Verified
    #         SPEECH_CONSTANTS.full_screen: {
    #             0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
    #             1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
    #             2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: FREEZEEZY_PEAK_ANSWER},
    #             3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
    #         },
    #     },
    #     STR_CONST.map_enum: MAP_ENUMS.gruntildas_lair_freezeezy_peak_entrance,
    #     STR_CONST.camera_dict: {
    #         STR_CONST.camera_type: 2,
    #         STR_CONST.x_position: 3319.205,
    #         STR_CONST.y_position: 877.7614,
    #         STR_CONST.z_position: 6906.147,
    #         STR_CONST.pitch: 1.5,
    #         STR_CONST.yaw: 98.25,
    #         STR_CONST.roll: 0,
    #     },
    # },
    {
        STR_CONST.question_dict: { # GRUNTY HEAD STATUE CEILING - Verified
            SPEECH_CONSTANTS.full_screen: {
                0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: MUMBOS_MOUNTAIN_ANSWER},
                3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
            },
        },
        STR_CONST.map_enum: MAP_ENUMS.gruntildas_lair_freezeezy_peak_entrance,
        STR_CONST.camera_dict: {
            STR_CONST.camera_type: 2,
            STR_CONST.x_position: -671.5924,
            STR_CONST.y_position: 1970.571,
            STR_CONST.z_position: 308.6785,
            STR_CONST.pitch: 90,
            STR_CONST.yaw: -62.5,
            STR_CONST.roll: 0,
        },
    },
    {
        STR_CONST.question_dict: { # MOSSY WALKWAY/WALL - Verified
            SPEECH_CONSTANTS.full_screen: {
                0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: BUBBLEGLOOP_SWAMP_ANSWER},
                3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: MAD_MONSTER_MANSION_ANSWER},
            },
        },
        STR_CONST.map_enum: MAP_ENUMS.gruntildas_lair_freezeezy_peak_entrance,
        STR_CONST.camera_dict: {
            STR_CONST.camera_type: 2,
            STR_CONST.x_position: -1568.678,
            STR_CONST.y_position: 2057.93,
            STR_CONST.z_position: -1443.571,
            STR_CONST.pitch: 355,
            STR_CONST.yaw: 37.75,
            STR_CONST.roll: 0,
        },
    },
    {
        STR_CONST.question_dict: { # ABOVE WITCH SWITCH JIGGY HOLE, UPSIDE DOWN
            SPEECH_CONSTANTS.full_screen: {
                0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: MUMBOS_MOUNTAIN_ANSWER},
                3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
            },
        },
        STR_CONST.map_enum: MAP_ENUMS.gruntildas_lair_click_clock_wood_entrance,
        STR_CONST.camera_dict: {
            STR_CONST.camera_type: 2,
            STR_CONST.x_position: 90.08061,
            STR_CONST.y_position: 4346.932,
            STR_CONST.z_position: 607.8855,
            STR_CONST.pitch: 0,
            STR_CONST.yaw: 180,
            STR_CONST.roll: 180,
        },
    },
    {
        STR_CONST.question_dict: { # CLOUD WAVES WALLPAPER - Verified
            SPEECH_CONSTANTS.full_screen: {
                0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: TREASURE_TROVE_COVE_ANSWER},
                3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: GOBIS_VALLEY_ANSWER},
            },
        },
        STR_CONST.map_enum: MAP_ENUMS.gruntildas_lair_treasure_trove_cove_entrance,
        STR_CONST.camera_dict: {
            STR_CONST.camera_type: 2,
            STR_CONST.x_position: -263.2788,
            STR_CONST.y_position: 1161.732,
            STR_CONST.z_position: -1002.799,
            STR_CONST.pitch: 0,
            STR_CONST.yaw: 0,
            STR_CONST.roll: 0,
        },
    },
    {
        STR_CONST.question_dict: { # ABOVE BGS PUZZLE ENTRANCE
            SPEECH_CONSTANTS.full_screen: {
                0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: CLANKERS_CAVERN_ANSWER},
                3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
            },
        },
        STR_CONST.map_enum: MAP_ENUMS.gruntildas_lair_clankers_cavern_entrance,
        STR_CONST.camera_dict: {
            STR_CONST.camera_type: 2,
            STR_CONST.x_position: -2356.84,
            STR_CONST.y_position: 1032.29,
            STR_CONST.z_position: -1350.591,
            STR_CONST.pitch: 0,
            STR_CONST.yaw: 146.5,
            STR_CONST.roll: 0,
        },
    },
    {
        STR_CONST.question_dict: { # WALL NEAR BGS PUZZLE
            SPEECH_CONSTANTS.full_screen: {
                0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: BUBBLEGLOOP_SWAMP_ANSWER},
                3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: MAD_MONSTER_MANSION_ANSWER},
            },
        },
        STR_CONST.map_enum: MAP_ENUMS.gruntildas_lair_clankers_cavern_entrance,
        STR_CONST.camera_dict: {
            STR_CONST.camera_type: 2,
            STR_CONST.x_position: -6671.657,
            STR_CONST.y_position: 902.4377,
            STR_CONST.z_position: -77.75095,
            STR_CONST.pitch: 0,
            STR_CONST.yaw: 127.5,
            STR_CONST.roll: 0,
        },
    },
    # {
    #     STR_CONST.question_dict: { # CEILING ABOVE CHEATOS ENTRANCE - Verified
    #         SPEECH_CONSTANTS.full_screen: {
    #             0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
    #             1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
    #             2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: FREEZEEZY_PEAK_ANSWER},
    #             3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: CLICK_CLOCK_WOOD_ANSWER},
    #         },
    #     },
    #     STR_CONST.map_enum: MAP_ENUMS.gruntildas_lair_bubblegloop_swamp_entrance,
    #     STR_CONST.camera_dict: {
    #         STR_CONST.camera_type: 2,
    #         STR_CONST.x_position: 1849.823,
    #         STR_CONST.y_position: 401.2762,
    #         STR_CONST.z_position: -5864.296,
    #         STR_CONST.pitch: 40.75,
    #         STR_CONST.yaw: 58.5,
    #         STR_CONST.roll: 0,
    #     },
    # },
    {
        STR_CONST.question_dict: { # RUSTY BUCKET BAY PUZZLE ROOM - Verified
            SPEECH_CONSTANTS.full_screen: {
                0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SEE THE PICTURE ON MY SCREEN, DO YOU KNOW WHERE YOU HAVE BEEN?"},
                1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: GRUNTILDAS_LAIR_ANSWER},
                2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: RUSTY_BUCKET_BAY_ANSWER},
                3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: CLANKERS_CAVERN_ANSWER},
            },
        },
        STR_CONST.map_enum: MAP_ENUMS.gruntildas_lair_mad_monster_mansion_rusty_bucket_bay_puzzle,
        STR_CONST.camera_dict: {
            STR_CONST.camera_type: 2,
            STR_CONST.x_position: 7485.031,
            STR_CONST.y_position: 2105.467,
            STR_CONST.z_position: -2033.525,
            STR_CONST.pitch: 339.75,
            STR_CONST.yaw: 203.5,
            STR_CONST.roll: 0,
        },
    },
    # {
    #     STR_CONST.question_dict: { # GOBI'S VALLEY ENTRANCE TOP AREA VASE - Verified
    #         SPEECH_CONSTANTS.full_screen: {
    #             0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "HAVE YOU SEEN THIS ON YOUR STROLL, WHAT'S ON THE OTHER SIDE OF THE HOLE?"},
    #             1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: "ýlA HAT"},
    #             2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: "ýlAN EMPTY HONEYCOMB"},
    #             3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: "ýlA STOP N SWAP EGG"},
    #         },
    #     },
    #     STR_CONST.map_enum: MAP_ENUMS.gruntildas_lair_gobis_valley_entrance,
    #     STR_CONST.camera_dict: {
    #         STR_CONST.camera_type: 2,
    #         STR_CONST.x_position: -12.72085,
    #         STR_CONST.y_position: 2282.857,
    #         STR_CONST.z_position: -3.872086,
    #         STR_CONST.pitch: 270,
    #         STR_CONST.yaw: 358.75,
    #         STR_CONST.roll: 0,
    #     },
    # },
    # {
    #     STR_CONST.question_dict: { # DOUBLE HEALTH CEILING - Verified
    #         SPEECH_CONSTANTS.full_screen: {
    #             0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "THIS PICTURE LOOKS UP AT THE SKY, CAN YOU TELL ME WHAT'S NEARBY?"},
    #             1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: "ýlAN ABUSED CAULDRON"},
    #             2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: "ýlA HORDE OF ZUBBAS"},
    #             3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: "ýlA LOSER'S BED"},
    #         },
    #     },
    #     STR_CONST.map_enum: MAP_ENUMS.gruntildas_lair_final_battle_puzzle,
    #     STR_CONST.camera_dict: {
    #         STR_CONST.camera_type: 2,
    #         STR_CONST.x_position: 6354.705,
    #         STR_CONST.y_position: 477.8839,
    #         STR_CONST.z_position: -219.3746,
    #         STR_CONST.pitch: 53.25,
    #         STR_CONST.yaw: 642,
    #         STR_CONST.roll: 0,
    #     },
    # },
    # {
    #     STR_CONST.question_dict: { # MMM PUZZLE EXTRA LIFE - Verified
    #         SPEECH_CONSTANTS.full_screen: {
    #             0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "SECRETS SCATTERED ACROSS MY LAIR, WHERE COULD YOU FIND THIS IN THE AIR?"},
    #             1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: "ýlABOVE THE MAD MONSTER MANSION PUZZLE"},
    #             2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: "ýlCEILING WITH THE ACTIVATABLE FLIGHT PAD"},
    #             3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: "ýlABOVE THE BEAUTY MACHINES"},
    #         },
    #     },
    #     STR_CONST.map_enum: MAP_ENUMS.gruntildas_lair_mad_monster_mansion_rusty_bucket_bay_puzzle,
    #     STR_CONST.camera_dict: {
    #         STR_CONST.camera_type: 2,
    #         STR_CONST.x_position: -817.7502,
    #         STR_CONST.y_position: 2054.313,
    #         STR_CONST.z_position: 206.9098,
    #         STR_CONST.pitch: 2.25,
    #         STR_CONST.yaw: 177.5,
    #         STR_CONST.roll: 0,
    #     },
    # },
    # {
    #     STR_CONST.question_dict: { # PIPE ROOM GOLD FEATHER - Verified (No Gold Feather, Can Hear Gruntling)
    #         SPEECH_CONSTANTS.full_screen: {
    #             0: {SPEECH_CONSTANTS.sprite: 0x80, SPEECH_CONSTANTS.speech: "THIS ONE'S TRICKY AND WILL SPELL YOUR DOOM, WHERE IS THIS IN THE ROOM?"},
    #             1: {SPEECH_CONSTANTS.sprite: 0x81, SPEECH_CONSTANTS.speech: "ýlNEAR A PIPE"},
    #             2: {SPEECH_CONSTANTS.sprite: 0x82, SPEECH_CONSTANTS.speech: "ýlUNDERNEATH THE BUBBLEGLOOP SWAMP MAZE"},
    #             3: {SPEECH_CONSTANTS.sprite: 0x83, SPEECH_CONSTANTS.speech: "ýlON THE EDGE OF A GIANT TREE"},
    #         },
    #     },
    #     STR_CONST.map_enum: MAP_ENUMS.gruntildas_lair_cauldron_pipe_room,
    #     STR_CONST.camera_dict: {
    #         STR_CONST.camera_type: 2,
    #         STR_CONST.x_position: 274.5542,
    #         STR_CONST.y_position: 773.0818,
    #         STR_CONST.z_position: 433.1332,
    #         STR_CONST.pitch: 357.25,
    #         STR_CONST.yaw: 180.25,
    #         STR_CONST.roll: 180,
    #     },
    # }
)

if __name__ == '__main__':
    for level_name in GEOGUESSER_LEVEL_SPECIFIC_QUESTIONS_DICT:
        level_question_count:int = len(GEOGUESSER_LEVEL_SPECIFIC_QUESTIONS_DICT[level_name])
        print(f"{level_name}: {level_question_count}")
    print(f"Generic Count: {len(GEOGUESSER_GENERAL_SPEECH_DICT)}")
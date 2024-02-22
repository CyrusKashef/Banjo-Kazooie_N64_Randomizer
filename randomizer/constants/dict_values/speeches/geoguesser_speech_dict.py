###################
##### IMPORTS #####
###################

from randomizer.constants.str_values.string_constants import STRING_CONSTANTS as STR_CONST
from randomizer.constants.int_values.map_setup_asset_ids import MAP_SETUP_ASSET_ID
from randomizer.constants.int_values.map_enums import MAP_ENUMS

##################################
##### GEOGUESSER SPEECH LIST #####
##################################
    # {
    #     STR_CONST.question_dict: { # SECOND STORY WINDOW
    #         4: {
    #             0: {7: 0x80, 8: ""},
    #             1: {7: 0x81, 8: "ýl"},
    #             2: {7: 0x82, 8: "ýl"},
    #             3: {7: 0x83, 8: "ýl"},
    #         },
    #     },
    #     STR_CONST.map_enum: MAP_ENUMS.DUMMY,
    #     STR_CONST.camera_dict: {
    #         STR_CONST.camera_type: 2,
    #         STR_CONST.x_position: 0000,
    #         STR_CONST.y_position: 0000,
    #         STR_CONST.z_position: 0000,
    #         STR_CONST.pitch: 0000,
    #         STR_CONST.yaw: 0000,
    #         STR_CONST.roll: 0000,
    #     },
    # },

GEOGUESSER_SPEECH_MEDIUM_LIST:tuple = (
    ###########################
    ##### SPIRAL MOUNTAIN #####
    ###########################
    {
        STR_CONST.question_dict: { # UNDER GRUNTILDA HEAD
            4: {
                0: {7: 0x80, 8: ""},
                1: {7: 0x81, 8: "ýlSPIRAL MOUNTAIN"},
                2: {7: 0x82, 8: "ýlGRUNTILDA'S LAIR"},
                3: {7: 0x83, 8: "ýlCLICK CLOCK WOOD"},
            },
        },
        STR_CONST.map_enum: MAP_ENUMS.spiral_mountain_main,
        STR_CONST.camera_dict: {
            STR_CONST.camera_type: 2,
            STR_CONST.x_position: -51.64992,
            STR_CONST.y_position: 824.8796,
            STR_CONST.z_position: 3242.825,
            STR_CONST.pitch: 82,
            STR_CONST.yaw: 1.75,
            STR_CONST.roll: 0,
        },
    },
    {
        STR_CONST.question_dict: { # LAKE
            4: {
                0: {7: 0x80, 8: ""},
                1: {7: 0x81, 8: "ýlSPIRAL MOUNTAIN"},
                2: {7: 0x82, 8: "ýlGRUNTILDA'S LAIR"},
                3: {7: 0x83, 8: "ýlMUMBO'S MOUNTAIN"},
            },
        },
        STR_CONST.map_enum: MAP_ENUMS.gruntildas_lair_final_battle_puzzle,
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
    {
        STR_CONST.question_dict: { # GRUNTILDA HOLE
            4: {
                0: {7: 0x80, 8: ""},
                1: {7: 0x81, 8: "ýlSPIRAL MOUNTAIN"},
                2: {7: 0x82, 8: "ýlMUMBO'S MOUNTAIN"},
                3: {7: 0x83, 8: "ýlCLICK CLOCK WOOD"},
            },
        },
        STR_CONST.map_enum: MAP_ENUMS.gruntildas_lair_final_battle_puzzle,
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
    ##### MUMBO'S MOUNTAIN #####
    ############################

    ###############################
    ##### TREASURE TROVE COVE #####
    ###############################
    {
        STR_CONST.question_dict: { # SHOCK JUMP ALCOVE
            4: {
                0: {7: 0x80, 8: ""},
                1: {7: 0x81, 8: "ýlTREASURE TROVE COVE"},
                2: {7: 0x82, 8: "ýlSPIRAL MOUNTAIN"},
                3: {7: 0x83, 8: "ýlCLICK CLOCK WOOD"},
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
        STR_CONST.question_dict: { # INSIDE NIPPER
            4: {
                0: {7: 0x80, 8: ""},
                1: {7: 0x81, 8: "ýl"},
                2: {7: 0x82, 8: "ýl"},
                3: {7: 0x83, 8: "ýl"},
            },
        },
        STR_CONST.map_enum: MAP_ENUMS.treasure_trove_cove_nippers_shell,
        STR_CONST.camera_dict: {
            STR_CONST.camera_type: 2,
            STR_CONST.x_position: 79.07181,
            STR_CONST.y_position: 195.99,
            STR_CONST.z_position: 140.9551,
            STR_CONST.pitch: 357,
            STR_CONST.yaw: 194.75,
            STR_CONST.roll: 0,
        },
    },
    ############################
    ##### CLANKER'S CAVERN #####
    ############################
    {
        STR_CONST.question_dict: { # GRATED VENT EXTRA LIFE
            4: {
                0: {7: 0x80, 8: ""},
                1: {7: 0x81, 8: "ýlCLANKER'S CAVERN"},
                2: {7: 0x82, 8: "ýl"},
                3: {7: 0x83, 8: "ýl"},
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
        STR_CONST.question_dict: { # GOLDEN SHORT PIPE
            4: {
                0: {7: 0x80, 8: ""},
                1: {7: 0x81, 8: "ýlMUMBO TOKEN"},
                2: {7: 0x82, 8: "ýlEMPTY HONEYCOMB"},
                3: {7: 0x83, 8: "ýlEXTRA LIFE"},
            },
        },
        STR_CONST.map_enum: MAP_ENUMS.clankers_cavern_main,
        STR_CONST.camera_dict: {
            STR_CONST.camera_type: 2,
            STR_CONST.x_position: 925.5875,
            STR_CONST.y_position: 2294.469,
            STR_CONST.z_position: -2630.054,
            STR_CONST.pitch: 15,
            STR_CONST.yaw: 365,
            STR_CONST.roll: 0,
        },
    },
    {
        STR_CONST.question_dict: { # BLOWHOLE TO MOUTH
            4: {
                0: {7: 0x80, 8: "PASSED THIS TUNNEL AT BLAZING SPEED, GOING THROUGH IT, WHERE DOES IT LEAD?"},
                1: {7: 0x81, 8: "ýlYOU CAN'T GO IN THIS DIRECTION"},
                2: {7: 0x82, 8: "ýlWONDERWING BOTTLES TUNNEL"},
                3: {7: 0x83, 8: "ýlOUT CLANKER'S RIGHT GILL"},
            },
        },
        STR_CONST.map_enum: MAP_ENUMS.clankers_cavern_main,
        STR_CONST.camera_dict: {
            STR_CONST.camera_type: 2,
            STR_CONST.x_position: 1,
            STR_CONST.y_position: 1727.161,
            STR_CONST.z_position: 5988.179,
            STR_CONST.pitch: 45.5,
            STR_CONST.yaw: 359.5,
            STR_CONST.roll: 0,
        },
    },
    ##############################
    ##### BLUBBLEGLOOP SWAMP #####
    ##############################
    {
        STR_CONST.question_dict: { # ATOP CROCODILE
            4: {
                0: {7: 0x80, 8: "WE KNOW THE LEVEL, BUT I WON'T STOP, WHAT WOULD YOU BE STANDING ON TOP?"},
                1: {7: 0x81, 8: "ýlA CROCODILE"},
                2: {7: 0x82, 8: "ýlA HUT"},
                3: {7: 0x83, 8: "ýlA CATTAIL"},
            },
        },
        STR_CONST.map_enum: MAP_ENUMS.bubblegloop_swamp_main,
        STR_CONST.camera_dict: {
            STR_CONST.camera_type: 2,
            STR_CONST.x_position: -1764.15,
            STR_CONST.y_position: 1465.964,
            STR_CONST.z_position: -4184.32,
            STR_CONST.pitch: 353.25,
            STR_CONST.yaw: 232,
            STR_CONST.roll: 0,
        },
    },
    {
        STR_CONST.question_dict: { # ATOP HUT
            4: {
                0: {7: 0x80, 8: "WE KNOW THE LEVEL, BUT I WON'T STOP, WHAT WOULD YOU BE STANDING ON TOP?"},
                1: {7: 0x81, 8: "ýlA HUT"},
                2: {7: 0x82, 8: "ýlA CROCODILE"},
                3: {7: 0x83, 8: "ýlA CATTAIL"},
            },
        },
        STR_CONST.map_enum: MAP_ENUMS.bubblegloop_swamp_main,
        STR_CONST.camera_dict: {
            STR_CONST.camera_type: 2,
            STR_CONST.x_position: 4905.651,
            STR_CONST.y_position: 1521.388,
            STR_CONST.z_position: -4358.437,
            STR_CONST.pitch: 355.25,
            STR_CONST.yaw: 136.5,
            STR_CONST.roll: 0,
        },
    },
    ##########################
    ##### FREEZEEZY PEAK #####
    ##########################
    {
        STR_CONST.question_dict: { # HOVERED ABOVE PRESENTS
            4: {
                0: {7: 0x80, 8: ""},
                1: {7: 0x81, 8: "ýlNEAR A STACK OF PRESENTS"},
                2: {7: 0x82, 8: "ýlBEHIND THE CHRISTMAS TREE"},
                3: {7: 0x83, 8: "ýlINSIDE WOZZA'S CAVE"},
            },
        },
        STR_CONST.map_enum: MAP_ENUMS.freezeezy_peak_main,
        STR_CONST.camera_dict: {
            STR_CONST.camera_type: 2,
            STR_CONST.x_position: -5442.054,
            STR_CONST.y_position: 2337.45,
            STR_CONST.z_position: 1194,
            STR_CONST.pitch: 354.25,
            STR_CONST.yaw: 446.5,
            STR_CONST.roll: 0,
        },
    },
    #########################
    ##### GOBI'S VALLEY #####
    #########################
    {
        STR_CONST.question_dict: { # GOBI'S VALLEY KING SANDYBUTT'S MAZE
            4: {
                0: {7: 0x80, 8: "BE SURE NOT TO DROP YOUR CROWN, WHERE'S THIS PICTURE I HAVE UPSIDE DOWN?"},
                1: {7: 0x81, 8: "ýlGOBI'S VALLEY"},
                2: {7: 0x82, 8: "ýlGRUNTILDA'S LAIR"},
                3: {7: 0x83, 8: "ýlCLICK CLOCK WOOD"},
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
    ###############################
    ##### MAD MONSTER MANSION #####
    ###############################
    {
        STR_CONST.question_dict: { # SECOND STORY BROKEN WINDOW
            4: {
                0: {7: 0x80, 8: ""},
                1: {7: 0x81, 8: "ýlMAD MONSTER MANSION"},
                2: {7: 0x82, 8: "ýlRUSTY BUCKET BAY"},
                3: {7: 0x83, 8: "ýlGRUNTILDA'S LAIR"},
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
        STR_CONST.question_dict: { # BEHIND ENTRANCE
            4: {
                0: {7: 0x80, 8: ""},
                1: {7: 0x81, 8: "ýlMAD MONSTER MANSION"},
                2: {7: 0x82, 8: "ýlRUSTY BUCKET BAY"},
                3: {7: 0x83, 8: "ýlGRUNTILDA'S LAIR"},
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
        STR_CONST.question_dict: { # MAZE HEDGE WALL
            4: {
                0: {7: 0x80, 8: ""},
                1: {7: 0x81, 8: "ýlMAD MONSTER MANSION"},
                2: {7: 0x82, 8: "ýlMUMBO'S MOUNTAIN"},
                3: {7: 0x83, 8: "ýlCLICK CLOCK WOOD"},
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
        STR_CONST.question_dict: { # MUMBO'S HUT
            4: {
                0: {7: 0x80, 8: ""},
                1: {7: 0x81, 8: "ýlMAD MONSTER MANSION"},
                2: {7: 0x82, 8: "ýlCLICK CLOCK WOOD WINTER"},
                3: {7: 0x83, 8: "ýlCLICK CLOCK WOOD SUMMER"},
            },
        },
        STR_CONST.map_enum: MAP_ENUMS.mad_monster_mansion_mumbos_hut,
        STR_CONST.camera_dict: {
            STR_CONST.camera_type: 2,
            STR_CONST.x_position: -51,
            STR_CONST.y_position: 584.118,
            STR_CONST.z_position: 42.7272,
            STR_CONST.pitch: 344,
            STR_CONST.yaw: 186,
            STR_CONST.roll: 0,
        },
    },
    ############################
    ##### RUSTY BUCKET BAY #####
    ############################
    {
        STR_CONST.question_dict: { # TOXIC WASTE AREA
            4: {
                0: {7: 0x80, 8: ""},
                1: {7: 0x81, 8: "ýlRUSTY BUCKET BAY"},
                2: {7: 0x82, 8: "ýl"},
                3: {7: 0x83, 8: "ýl"},
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
        STR_CONST.question_dict: { # OUT OF BOUNDS WINDOW
            4: {
                0: {7: 0x80, 8: ""},
                1: {7: 0x81, 8: "ýlRUSTY BUCKET BAY"},
                2: {7: 0x82, 8: "ýlMAD MONSTER MANSION"},
                3: {7: 0x83, 8: "ýl"},
            },
        },
        STR_CONST.map_enum: MAP_ENUMS.rusty_bucket_bay_main,
        STR_CONST.camera_dict: {
            STR_CONST.camera_type: 2,
            STR_CONST.x_position: 10047.43,
            STR_CONST.y_position: -1105.388,
            STR_CONST.z_position: 4710.588,
            STR_CONST.pitch: 357.5,
            STR_CONST.yaw: 133.5,
            STR_CONST.roll: 0,
        },
    },
    {
        STR_CONST.question_dict: { # RAREWARE YELLOW CONTAINER ON BOAT
            4: {
                0: {7: 0x80, 8: ""},
                1: {7: 0x81, 8: "ýlON THE BOAT"},
                2: {7: 0x82, 8: "ýlIN A BLUE CONTAINER"},
                3: {7: 0x83, 8: "ýlIN THE WAREHOUSE WITH A CHUMP"},
            },
        },
        STR_CONST.map_enum: MAP_ENUMS.rusty_bucket_bay_main,
        STR_CONST.camera_dict: {
            STR_CONST.camera_type: 2,
            STR_CONST.x_position: 4647.633,
            STR_CONST.y_position: 43.98711,
            STR_CONST.z_position: 1404.164,
            STR_CONST.pitch: 0.5,
            STR_CONST.yaw: -0.25,
            STR_CONST.roll: 0,
        },
    },
    {
        STR_CONST.question_dict: { # NAVIGATION ROOM MAP
            4: {
                0: {7: 0x80, 8: ""},
                1: {7: 0x81, 8: "ýlNAVIGATION ROOM"},
                2: {7: 0x82, 8: "ýlKITCHEN"},
                3: {7: 0x83, 8: "ýlCAPTAIN'S BEDROOM"},
            },
        },
        STR_CONST.map_enum: MAP_ENUMS.rusty_bucket_bay_navigation_window,
        STR_CONST.camera_dict: {
            STR_CONST.camera_type: 2,
            STR_CONST.x_position: 89.59196,
            STR_CONST.y_position: 367.8279,
            STR_CONST.z_position: -688.2775,
            STR_CONST.pitch: 2.75,
            STR_CONST.yaw: 362,
            STR_CONST.roll: 0,
        },
    },
    {
        STR_CONST.question_dict: { # CABIN ROOM WINDOW
            4: {
                0: {7: 0x80, 8: ""},
                1: {7: 0x81, 8: "ýlSEAMAN GRUBLIN CABINS"},
                2: {7: 0x82, 8: "ýlNAVIGATION ROOM"},
                3: {7: 0x83, 8: "ýlCAPTAIN'S BEDROOM"},
            },
        },
        STR_CONST.map_enum: MAP_ENUMS.rusty_bucket_bay_cabin_window,
        STR_CONST.camera_dict: {
            STR_CONST.camera_type: 2,
            STR_CONST.x_position: 4.449204,
            STR_CONST.y_position: 280.84,
            STR_CONST.z_position: -260.0715,
            STR_CONST.pitch: 355,
            STR_CONST.yaw: 0.75,
            STR_CONST.roll: 0,
        },
    },
    ############################
    ##### CLICK CLOCK WOOD #####
    ############################
    {
        STR_CONST.question_dict: { # SUMMER MUMBO'S HUT
            4: {
                0: {7: 0x80, 8: ""},
                1: {7: 0x81, 8: "ýlCLICK CLOCK WOOD SUMMER"},
                2: {7: 0x82, 8: "ýlMAD MONSTER MANSION"},
                3: {7: 0x83, 8: "ýlCLICK CLOCK WOOD WINTER"},
            },
        },
        STR_CONST.map_enum: MAP_ENUMS.click_clock_wood_summer_mumbos_skull,
        STR_CONST.camera_dict: {
            STR_CONST.camera_type: 2,
            STR_CONST.x_position: -51,
            STR_CONST.y_position: 584.118,
            STR_CONST.z_position: 42.7272,
            STR_CONST.pitch: 344,
            STR_CONST.yaw: 186,
            STR_CONST.roll: 0,
        },
    },
    ############################
    ##### GRUNTILDA'S LAIR #####
    ############################
    {
        STR_CONST.question_dict: { # GOBI'S VALLEY ENTRANCE HALLWAY
            4: {
                0: {7: 0x80, 8: "WHERE THIS PICTURE CAN BE FOUND, WHAT OTHER THING CAN BE FOUND?"},
                1: {7: 0x81, 8: "ýlA GIANT VASE"},
                2: {7: 0x82, 8: "ýlA SPIKED CEILING"},
                3: {7: 0x83, 8: "ýlMAGIC CARPETS"},
            },
        },
        STR_CONST.map_enum: MAP_ENUMS.gruntildas_lair_gobis_valley_entrance,
        STR_CONST.camera_dict: {
            STR_CONST.camera_type: 2,
            STR_CONST.x_position: -5109.125,
            STR_CONST.y_position: 1993.17,
            STR_CONST.z_position: 1675.914,
            STR_CONST.pitch: 300.75,
            STR_CONST.yaw: 1.75,
            STR_CONST.roll: 0,
        },
    },
    {
        STR_CONST.question_dict: { # GOBI'S VALLEY ENTRANCE TOP AREA VASE
            4: {
                0: {7: 0x80, 8: "HAVE YOU SEEN THIS ON YOUR STROLL, WHAT'S ON THE OTHER SIDE OF THE HOLE?"},
                1: {7: 0x81, 8: "ýlA HAT"},
                2: {7: 0x82, 8: "ýlAN EMPTY HONEYCOMB"},
                3: {7: 0x83, 8: "ýlA STOP N SWAP EGG"},
            },
        },
        STR_CONST.map_enum: MAP_ENUMS.gruntildas_lair_gobis_valley_entrance,
        STR_CONST.camera_dict: {
            STR_CONST.camera_type: 2,
            STR_CONST.x_position: -12.72085,
            STR_CONST.y_position: 2282.857,
            STR_CONST.z_position: -3.872086,
            STR_CONST.pitch: 270,
            STR_CONST.yaw: 358.75,
            STR_CONST.roll: 0,
        },
    },
    {
        STR_CONST.question_dict: { # GRUNTILDA'S LAIR PUMPKIN
            4: {
                0: {7: 0x80, 8: ""},
                1: {7: 0x81, 8: "ýlNEAR THE BEAUTY TRANSFER MACHINES"},
                2: {7: 0x82, 8: "ýlOUTSIDE MAD MONSTER MANSION'S ENTRANCE"},
                3: {7: 0x83, 8: "ýl"},
            },
        },
        STR_CONST.map_enum: MAP_ENUMS.gruntildas_lair_final_battle_puzzle,
        STR_CONST.camera_dict: {
            STR_CONST.camera_type: 2,
            STR_CONST.x_position: -815.9854,
            STR_CONST.y_position: -152.6971,
            STR_CONST.z_position: 112.995,
            STR_CONST.pitch: 354,
            STR_CONST.yaw: 369,
            STR_CONST.roll: 0,
        },
    },
    {
        STR_CONST.question_dict: { # DOUBLE HEALTH CEILING
            4: {
                0: {7: 0x80, 8: ""},
                1: {7: 0x81, 8: "ýl"},
                2: {7: 0x82, 8: "ýl"},
                3: {7: 0x83, 8: "ýl"},
            },
        },
        STR_CONST.map_enum: MAP_ENUMS.gruntildas_lair_final_battle_puzzle,
        STR_CONST.camera_dict: {
            STR_CONST.camera_type: 2,
            STR_CONST.x_position: 6354.705,
            STR_CONST.y_position: 477.8839,
            STR_CONST.z_position: -219.3746,
            STR_CONST.pitch: 53.25,
            STR_CONST.yaw: 642,
            STR_CONST.roll: 0,
        },
    },
    {
        STR_CONST.question_dict: { # MMM PUZZLE EXTRA LIFE
            4: {
                0: {7: 0x80, 8: ""},
                1: {7: 0x81, 8: "ýlABOVE THE MAD MONSTER MANSION PUZZLE"},
                2: {7: 0x82, 8: "ýlCEILING WITH THE ACTIVATABLE FLIGHT PAD"},
                3: {7: 0x83, 8: "ýlABOVE THE BEAUTY MACHINES"},
            },
        },
        STR_CONST.map_enum: MAP_ENUMS.gruntildas_lair_mad_monster_mansion_rusty_bucket_bay_puzzle,
        STR_CONST.camera_dict: {
            STR_CONST.camera_type: 2,
            STR_CONST.x_position: -817.7502,
            STR_CONST.y_position: 2054.313,
            STR_CONST.z_position: 206.9098,
            STR_CONST.pitch: 2.25,
            STR_CONST.yaw: 177.5,
            STR_CONST.roll: 0,
        },
    },
    {
        STR_CONST.question_dict: { # PIPE ROOM GOLD FEATHER
            4: {
                0: {7: 0x80, 8: ""},
                1: {7: 0x81, 8: "ýlNEAR A BROKEN PIPE"},
                2: {7: 0x82, 8: "ýlUNDERNEATH THE BUBBLEGLOOP SWAMP MAZE"},
                3: {7: 0x83, 8: "ýlON THE EDGE OF A GIANT TREE"},
            },
        },
        STR_CONST.map_enum: MAP_ENUMS.gruntildas_lair_cauldron_pipe_room,
        STR_CONST.camera_dict: {
            STR_CONST.camera_type: 2,
            STR_CONST.x_position: 274.5542,
            STR_CONST.y_position: 773.0818,
            STR_CONST.z_position: 433.1332,
            STR_CONST.pitch: 357.25,
            STR_CONST.yaw: 180.25,
            STR_CONST.roll: 180,
        },
    },
    ########################
    ##### FINAL BATTLE #####
    ########################
    {
        STR_CONST.question_dict: { # FINAL BATTLE ENTRANCE
            4: {
                0: {7: 0x80, 8: ""},
                1: {7: 0x81, 8: "ýlNEITHER OF THE OTHER ANSWERS"},
                2: {7: 0x82, 8: "ýlCLANKER'S CAVERN"},
                3: {7: 0x83, 8: "ýlRUSTY BUCKET BAY"},
            },
        },
        STR_CONST.map_enum: MAP_ENUMS.final_battle_arena,
        STR_CONST.camera_dict: {
            STR_CONST.camera_type: 2,
            STR_CONST.x_position: -4,
            STR_CONST.y_position: 225.619,
            STR_CONST.z_position: 1047.252,
            STR_CONST.pitch: 270,
            STR_CONST.yaw: 359.75,
            STR_CONST.roll: 0,
        },
    },
    {
        STR_CONST.question_dict: { # FINAL BATTLE SIDE WALL
            4: {
                0: {7: 0x80, 8: ""},
                1: {7: 0x81, 8: "ýl"},
                2: {7: 0x82, 8: "ýl"},
                3: {7: 0x83, 8: "ýl"},
            },
        },
        STR_CONST.map_enum: MAP_ENUMS.final_battle_arena,
        STR_CONST.camera_dict: {
            STR_CONST.camera_type: 2,
            STR_CONST.x_position: 4648.346,
            STR_CONST.y_position: -1335.516,
            STR_CONST.z_position: -69.04868,
            STR_CONST.pitch: 358,
            STR_CONST.yaw: 94,
            STR_CONST.roll: 0,
        },
    },
)
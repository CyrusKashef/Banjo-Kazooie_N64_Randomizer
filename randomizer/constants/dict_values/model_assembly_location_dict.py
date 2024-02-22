'''
Purpose:
* Links the asset id with the index locations in the assembly files
'''

###################
##### IMPORTS #####
###################

from randomizer.constants.int_values.object_model_asset_ids import OBJECT_MODEL_ASSET_ID
from randomizer.constants.int_values.assembly_file_enums import ASSEMBLY_FILE_ENUMS

########################################
##### MODEL ASSEMBLY LOCATION DICT #####
########################################

MODEL_ASSEMBLY_LOCATION_DICT = {
    OBJECT_MODEL_ASSET_ID.bk_termite: {
        ASSEMBLY_FILE_ENUMS.game_engine_code: [0x1169A],
    },
    OBJECT_MODEL_ASSET_ID.bk_wishywashy: {
        ASSEMBLY_FILE_ENUMS.game_engine_code: [0x116C2],
    },
    OBJECT_MODEL_ASSET_ID.bk_walrus: {
        ASSEMBLY_FILE_ENUMS.game_engine_code: [0x116B2],
    },
    OBJECT_MODEL_ASSET_ID.bk_bee: {
        ASSEMBLY_FILE_ENUMS.game_engine_code: [0x116BA],
    },
    OBJECT_MODEL_ASSET_ID.bk_pumpkin: {
        ASSEMBLY_FILE_ENUMS.game_engine_code: [0x116A2],
    },
    OBJECT_MODEL_ASSET_ID.bk_crocodile: {
        ASSEMBLY_FILE_ENUMS.game_engine_code: [0x116AA],
    },
    0x7DC: { # Empty Honeycomb 2D
        ASSEMBLY_FILE_ENUMS.game_engine_code: [0x77A62],
    },
}
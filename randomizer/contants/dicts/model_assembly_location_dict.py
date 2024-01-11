'''
Purpose:
* Links the asset id with the index locations in the assembly files
'''

###################
##### IMPORTS #####
###################

from randomizer.contants.enums.assets_enums import ASSET_ID_ENUMS
from randomizer.contants.enums.assembly_file_enums import ASSEMBLY_FILE_ENUMS

########################################
##### MODEL ASSEMBLY LOCATION DICT #####
########################################

MODEL_ASSEMBLY_LOCATION_DICT = {
    ASSET_ID_ENUMS.bk_termite: {
        ASSEMBLY_FILE_ENUMS.game_engine_code: [0x1169A],
    },
    ASSET_ID_ENUMS.bk_wishywashy: {
        ASSEMBLY_FILE_ENUMS.game_engine_code: [0x116C2],
    },
    ASSET_ID_ENUMS.bk_walrus: {
        ASSEMBLY_FILE_ENUMS.game_engine_code: [0x116B2],
    },
    ASSET_ID_ENUMS.bk_bee: {
        ASSEMBLY_FILE_ENUMS.game_engine_code: [0x116BA],
    },
    ASSET_ID_ENUMS.bk_pumpkin: {
        ASSEMBLY_FILE_ENUMS.game_engine_code: [0x116A2],
    },
    ASSET_ID_ENUMS.bk_crocodile: {
        ASSEMBLY_FILE_ENUMS.game_engine_code: [0x116AA],
    },
}
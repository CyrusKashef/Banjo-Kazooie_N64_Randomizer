'''
Purpose:
*
'''

# core1/code_CE60.c#L195

from randomizer.constants.int_values.level_enums import LEVEL_ID_ENUMS
from randomizer.constants.int_values.music_zone_enums import MUSIC_ZONE_ENUMS

X_POSITION_INDEX_STR:str = "X Position Index"
Z_POSITION_INDEX_STR:str = "Z Position Index"
RADIUS_INDEX_STR:str = "Radius Index"

MUSIC_ZONE_DICT:dict = {
    LEVEL_ID_ENUMS.mumbos_mountain: {
        MUSIC_ZONE_ENUMS.mumbos_mountain_conga_1: {
            X_POSITION_INDEX_STR: 0x0,
            Z_POSITION_INDEX_STR: 0x0,
            RADIUS_INDEX_STR:     0x0,
        },
        MUSIC_ZONE_ENUMS.mumbos_mountain_conga_2: 0x0,
        MUSIC_ZONE_ENUMS.mumbos_mountain_juju: 0x0,
        MUSIC_ZONE_ENUMS.mumbos_mountain_tickers_tower: 0x0,
        MUSIC_ZONE_ENUMS.mumbos_mountain_underwater: 0x0,
        MUSIC_ZONE_ENUMS.mumbos_mountain_default: 0x0,
    },
}
###################
##### IMPORTS #####
###################

# Classes

from randomizer.logic.warp_class import WARP_CLASS

# Enums

from randomizer.constants.int_values.warp_enums import WARP_ENUMS as WARP
from randomizer.constants.int_values.region_enums import REGION_ENUMS as REGION
from randomizer.constants.logic_values.allowed_transformations import ALLOWED_TRANSFORMATIONS

#################
##### WARPS #####
#################

SPIRAL_MOUNTAIN_BANJOS_HOUSE_FROM_MAIN_WARP:WARP_CLASS = WARP_CLASS(
    debug_name="SM Banjos House From Main",
    warp_enum=WARP.spiral_mountain_banjos_house_from_main,
    allowed_transformations=ALLOWED_TRANSFORMATIONS.any_transformation,
    default_to_region=REGION.Spiral_Mountain_Main,
    one_way_warp=False
)

SPIRAL_MOUNTAIN_MAIN_FROM_BANJOS_HOUSE_WARP:WARP_CLASS = WARP_CLASS(
    debug_name="SM Banjos House From Main",
    warp_enum=WARP.spiral_mountain_main_from_banjos_house,
    allowed_transformations=ALLOWED_TRANSFORMATIONS.any_transformation,
    default_to_region=REGION.Spiral_Mountain_House_Interior,
    one_way_warp=False
)

GRUNTILDAS_LAIR_SPIRAL_MOUNTAIN_ENTRANCE_FROM_SPIRAL_MOUNTAIN_MAIN_WARP:WARP_CLASS = WARP_CLASS(
    debug_name="GL Spiral Mountain Entrance From SM Main",
    warp_enum=WARP.gruntildas_lair_mm_lobby_from_spiral_mountain_main,
    allowed_transformations=ALLOWED_TRANSFORMATIONS.any_transformation,
    default_to_region=REGION.Spiral_Mountain_Lair_Entrance,
    one_way_warp=False
)
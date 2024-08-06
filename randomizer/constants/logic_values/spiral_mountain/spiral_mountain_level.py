###################
##### IMPORTS #####
###################

from randomizer.logic.level_class import LEVEL_CLASS

from randomizer.constants.int_values.level_enums import LEVEL_ID_ENUMS as LEVEL
from randomizer.constants.int_values.region_enums import REGION_ENUMS as REGION

from randomizer.constants.logic_values.spiral_mountain import spiral_mountain_region

#################
##### LEVEL #####
#################

SPIRAL_MOUNTAIN_LEVEL:LEVEL_CLASS = LEVEL_CLASS(
    debug_name="Spiral Mountain",
    level_enum=LEVEL.spiral_mountain,
    default_start_region=REGION.Spiral_Mountain_Main,
    level_regions={
        REGION.Spiral_Mountain_Main: spiral_mountain_region.SPIRAL_MOUNTAIN_MAIN_REGION,
        REGION.Spiral_Mountain_House_Interior: spiral_mountain_region.SPIRAL_MOUNTAIN_INSIDE_BANJOS_HOUSE,
        REGION.Spiral_Mountain_Lair_Entrance: spiral_mountain_region.SPIRAL_MOUNTAIN_LAIR_ENTRANCE_REGION,
    }
)
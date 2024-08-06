###################
##### IMPORTS #####
###################

# Class

from randomizer.logic.region_class import REGION_CLASS

# Enum

from randomizer.constants.int_values.region_enums import REGION_ENUMS as REGION
from randomizer.constants.int_values.location_enums import LOCATION_ENUMS as LOCATION
from randomizer.constants.int_values.warp_enums import WARP_ENUMS as WARP
from randomizer.constants.int_values.transformation_enums import TRANSFORMATION_ENUMS as TRANSFORMATION
from randomizer.constants.int_values.logic_item_enums import LOGIC_ITEM_ENUMS as LOGIC_ITEM
from randomizer.constants.logic_values.allowed_transformations import ALLOWED_TRANSFORMATIONS

from randomizer.constants.logic_values.spiral_mountain import \
    spiral_mountain_locations, spiral_mountain_warps

###################
##### REGIONS #####
###################

SPIRAL_MOUNTAIN_MAIN_REGION:REGION_CLASS = REGION_CLASS(
    debug_name="Spiral Mountain Main",
    region_enum=REGION.Spiral_Mountain_Main,
    allowed_transformations=ALLOWED_TRANSFORMATIONS.any_transformation,
    required_transformation_access=None,
    transformation_pad=None,
    detransformation_zone=False,
    connected_non_warp_regions={
        REGION.Spiral_Mountain_Lair_Entrance:  {
            TRANSFORMATION.banjo_kazooie: (),
            TRANSFORMATION.termite: (),
            TRANSFORMATION.crocodile: (),
            TRANSFORMATION.walrus: (),
            TRANSFORMATION.pumpkin: (),
            TRANSFORMATION.bee: (),
        },
    },
    locations={
        # Bottles Molehills
        LOCATION.spiral_mountain_bottles_intro: spiral_mountain_locations.SPIRAL_MOUNTAIN_BOTTLES_INTRO_LOCATION,
        LOCATION.spiral_mountain_bottles_camera: spiral_mountain_locations.SPIRAL_MOUNTAIN_BOTTLES_CAMERA_LOCATION,
        LOCATION.spiral_mountain_bottles_jump: spiral_mountain_locations.SPIRAL_MOUNTAIN_BOTTLES_JUMP_LOCATION,
        LOCATION.spiral_mountain_bottles_dive: spiral_mountain_locations.SPIRAL_MOUNTAIN_BOTTLES_DIVE_LOCATION,
        LOCATION.spiral_mountain_bottles_attack: spiral_mountain_locations.SPIRAL_MOUNTAIN_BOTTLES_ATTACK_LOCATION,
        LOCATION.spiral_mountain_bottles_beak_barge: spiral_mountain_locations.SPIRAL_MOUNTAIN_BOTTLES_BEAK_BARGE_LOCATION,
        LOCATION.spiral_mountain_bottles_bridge: spiral_mountain_locations.SPIRAL_MOUNTAIN_BOTTLES_BRIDGE_LOCATION,
        # Empty Honeycombs
        LOCATION.spiral_mountain_atop_tree: spiral_mountain_locations.SPIRAL_MOUNTAIN_ATOP_TREE_LOCATION,
        LOCATION.spiral_mountain_colliwobble: spiral_mountain_locations.SPIRAL_MOUNTAIN_COLLIWOBBLE_LOCATION,
        LOCATION.spiral_mountain_ledges: spiral_mountain_locations.SPIRAL_MOUNTAIN_LEDGES_LOCATION,
        LOCATION.spiral_mountain_quarries: spiral_mountain_locations.SPIRAL_MOUNTAIN_QUARRIES_LOCATION,
        LOCATION.spiral_mountain_stump: spiral_mountain_locations.SPIRAL_MOUNTAIN_STUMP_LOCATION,
        LOCATION.spiral_mountain_underwater: spiral_mountain_locations.SPIRAL_MOUNTAIN_UNDERWATER_LOCATION,
        # Extra Lives
        LOCATION.spiral_mountain_atop_banjos_house: spiral_mountain_locations.SPIRAL_MOUNTAIN_ATOP_HOUSE_LOCATION,
        LOCATION.spiral_mountain_behind_waterfall: spiral_mountain_locations.SPIRAL_MOUNTAIN_BEHIND_WATERFALL_LOCATION,
    },
    warp_exits={
        WARP.spiral_mountain_banjos_house_from_main: spiral_mountain_warps.SPIRAL_MOUNTAIN_BANJOS_HOUSE_FROM_MAIN_WARP,
    }
)

SPIRAL_MOUNTAIN_LAIR_ENTRANCE_REGION:REGION_CLASS = REGION_CLASS(
    debug_name="Spiral Mountain Lair Entrance",
    region_enum=REGION.Spiral_Mountain_Lair_Entrance,
    allowed_transformations=ALLOWED_TRANSFORMATIONS.any_transformation,
    required_transformation_access=None,
    transformation_pad=None,
    detransformation_zone=False,
    connected_non_warp_regions={
        REGION.Spiral_Mountain_Main: {
            TRANSFORMATION.banjo_kazooie: (),
            TRANSFORMATION.termite: (),
            TRANSFORMATION.crocodile: (),
            TRANSFORMATION.walrus: (),
            TRANSFORMATION.pumpkin: (),
            TRANSFORMATION.bee: (),
        }
    },
    locations={},
    warp_exits={
        # WARP.gruntildas_lair_mm_lobby_from_spiral_mountain_main: spiral_mountain_warps.GRUNTILDAS_LAIR_SPIRAL_MOUNTAIN_ENTRANCE_FROM_SPIRAL_MOUNTAIN_MAIN_WARP,
    }
)

SPIRAL_MOUNTAIN_INSIDE_BANJOS_HOUSE:REGION_CLASS = REGION_CLASS(
    debug_name="Spiral Mountain Inside Banjos House",
    region_enum=REGION.Spiral_Mountain_House_Interior,
    allowed_transformations=ALLOWED_TRANSFORMATIONS.any_transformation,
    required_transformation_access=None,
    transformation_pad=None,
    detransformation_zone=False,
    connected_non_warp_regions={},
    locations={},
    warp_exits={
        WARP.spiral_mountain_main_from_banjos_house: spiral_mountain_warps.SPIRAL_MOUNTAIN_MAIN_FROM_BANJOS_HOUSE_WARP,
    }
)
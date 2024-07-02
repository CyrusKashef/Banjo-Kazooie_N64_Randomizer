###################
##### IMPORTS #####
###################

from randomizer.constants.int_values.transformation_enums import TRANSFORMATION_ENUMS as TRANSFORMATION
from randomizer.constants.int_values.ability_enums import ABILITY_ENUMS as ABILITY
from randomizer.constants.int_values.location_enums import LOCATION_ENUMS as LOCATION
from randomizer.constants.int_values.region_enums import REGION_ENUMS as REGION
from randomizer.constants.int_values.level_enums import LEVEL_ID_ENUMS as LEVEL
from randomizer.constants.int_values.warp_enums import WARP_ENUMS as WARP
from randomizer.constants.int_values.map_enums import MAP_ENUMS as MAP
from randomizer.constants.int_values.logic_difficulty_enums import LOGIC_DIFFICULTY_ENUMS as DIFFICULTY
from randomizer.constants.int_values.jiggy_enums import JIGGY_ENUMS as JIGGY
from randomizer.constants.int_values.empty_honeycomb_enums import EMPTY_HONEYCOMB_ENUMS as EMPTY_HONEYCOMB
# from randomizer.constants.int_values.mumbo_token_enums import MUMBO_TOKEN_ENUMS as MUMBO_TOKEN
from randomizer.constants.int_values.item_type_enums import ITEM_TYPE_ENUMS as ITEM_TYPE

from randomizer.logic.location_class import LOCATION_CLASS
from randomizer.logic.warp_class import WARP_CLASS
from randomizer.logic.region_class import REGION_CLASS
from randomizer.logic.level_class import LEVEL_CLASS

#################################
##### GRUNTILDAS LAIR LEVEL #####
#################################

GRUNTILDAS_LAIR_LEVEL = LEVEL_CLASS(
    debug_name="Gruntildas Lair",
    level_enum=LEVEL.gruntildas_lair,
    level_start_region_enum=REGION.Gruntildas_Lair_Spiral_Mountain_Entrance,
    region_dict={
        REGION.Gruntildas_Lair_Spiral_Mountain_Entrance: REGION_CLASS(
            debug_name="Gruntildas Lair Spiral Mountain Entrance",
            region_enum=REGION.Gruntildas_Lair_Spiral_Mountain_Entrance,
            transformation_pad=None,
            detransformation_zone=False,
            allowed_transformations=[
                TRANSFORMATION.banjo_kazooie,
                TRANSFORMATION.termite,
                TRANSFORMATION.crocodile,
                TRANSFORMATION.walrus,
                TRANSFORMATION.pumpkin,
                TRANSFORMATION.bee],
            required_transformation_access=[],
            location_dict={
                LOCATION.gruntildas_lair_first_jiggy: LOCATION_CLASS(
                    debug_name="GL First Jiggy",
                    location_enum=LOCATION.gruntildas_lair_first_jiggy,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                )
            },
            connected_non_warp_regions_dict={
                REGION.Gruntildas_Lair_Termite_Detransformation_Zone: {
                    TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                    TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                    TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                    TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                    TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                    TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                },
                REGION.Gruntildas_Lair_50_Note_Door: {
                    TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                        item_dict[ABILITY.talon_trot]
                    ),
                    TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                    TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                    TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                    TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                    TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                }
            },
            exit_region={
                WARP.spiral_mountain_main_from_gruntildas_lair: WARP_CLASS(
                    debug_name="SM Exiting Gruntildas Lair",
                    warp_enum=WARP.spiral_mountain_main_from_gruntildas_lair,
                    default_region_enum=REGION.Spiral_Mountain_Lair_Entrance,
                    default_warp_to_map=MAP.spiral_mountain_main,
                    default_warp_to_entry=0x13,
                    allowed_transformations=[
                        TRANSFORMATION.banjo_kazooie,
                        TRANSFORMATION.termite,
                        TRANSFORMATION.crocodile,
                        TRANSFORMATION.walrus,
                        TRANSFORMATION.pumpkin,
                        TRANSFORMATION.bee],
                )
            }
        ),
        REGION.Gruntildas_Lair_Termite_Detransformation_Zone: REGION_CLASS(
            debug_name="Gruntildas Lair Termite Detransformation Zone",
            region_enum=REGION.Gruntildas_Lair_Termite_Detransformation_Zone,
            transformation_pad=None,
            detransformation_zone=True,
            allowed_transformations=[
                TRANSFORMATION.banjo_kazooie,
                TRANSFORMATION.termite,
                TRANSFORMATION.crocodile,
                TRANSFORMATION.walrus,
                TRANSFORMATION.pumpkin,
                TRANSFORMATION.bee],
            required_transformation_access=[],
            location_dict={},
            connected_non_warp_regions_dict={
                REGION.Gruntildas_Lair_Spiral_Mountain_Entrance: {
                    TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                    TRANSFORMATION.termite: (lambda item_dict, settings_dict: False),
                    TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: False),
                    TRANSFORMATION.walrus: (lambda item_dict, settings_dict: False),
                    TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: False),
                    TRANSFORMATION.bee: (lambda item_dict, settings_dict: False)
                },
                REGION.Gruntildas_Lair_Mumbos_Mountain_Entrance: {
                    TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                    TRANSFORMATION.termite: (lambda item_dict, settings_dict: False),
                    TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: False),
                    TRANSFORMATION.walrus: (lambda item_dict, settings_dict: False),
                    TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: False),
                    TRANSFORMATION.bee: (lambda item_dict, settings_dict: False)
                }
            },
            exit_region={}
        ),
        REGION.Gruntildas_Lair_Mumbos_Mountain_Entrance: REGION_CLASS(
            debug_name="Gruntildas Lair Mumbos Mountain Entrance",
            region_enum=REGION.Gruntildas_Lair_Mumbos_Mountain_Entrance,
            transformation_pad=None,
            detransformation_zone=False,
            allowed_transformations=[
                TRANSFORMATION.banjo_kazooie,
                TRANSFORMATION.termite,
                TRANSFORMATION.crocodile,
                TRANSFORMATION.walrus,
                TRANSFORMATION.pumpkin,
                TRANSFORMATION.bee],
            required_transformation_access=[],
            location_dict={},
            connected_non_warp_regions_dict={
                REGION.Gruntildas_Lair_Termite_Detransformation_Zone: {
                    TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                    TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                    TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                    TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                    TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                    TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                }
            },
            exit_region={
                WARP.mumbos_mountain_main_from_gruntildas_lair: WARP_CLASS(
                    debug_name="MM Entering From Gruntildas Lair",
                    warp_enum=WARP.mumbos_mountain_main_from_gruntildas_lair,
                    default_region_enum=REGION.Mumbos_Mountain_Main,
                    default_warp_to_map=MAP.mumbos_mountain_main,
                    default_warp_to_entry=0x05,
                    allowed_transformations=[
                        TRANSFORMATION.banjo_kazooie,
                        TRANSFORMATION.termite,
                        TRANSFORMATION.crocodile,
                        TRANSFORMATION.walrus,
                        TRANSFORMATION.pumpkin,
                        TRANSFORMATION.bee],
                )
            }
        ),
        REGION.Gruntildas_Lair_50_Note_Door: REGION_CLASS(
            debug_name="Gruntildas Lair",
            region_enum=None,
            transformation_pad=None,
            detransformation_zone=False,
            allowed_transformations=[
                TRANSFORMATION.banjo_kazooie,
                TRANSFORMATION.termite,
                TRANSFORMATION.crocodile,
                TRANSFORMATION.walrus,
                TRANSFORMATION.pumpkin,
                TRANSFORMATION.bee],
            required_transformation_access=[],
            location_dict={},
            connected_non_warp_regions_dict={
                REGION.Gruntildas_Lair_Spiral_Mountain_Entrance: {
                    TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                    TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                    TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                    TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                    TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                    TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                }
            },
            exit_region={
                WARP.gruntildas_lair_ttc_cc_puzzles_from_mumbos_mountain_lobby: WARP_CLASS(
                    debug_name="GL TTC CC Puzzles From MM Lobby",
                    warp_enum=WARP.gruntildas_lair_ttc_cc_puzzles_from_mumbos_mountain_lobby,
                    default_region_enum=REGION.Gruntildas_Lair_Treasure_Trove_Cove_Clankers_Cavern_Puzzles,
                    default_warp_to_map=MAP.gruntildas_lair_treasure_trove_cove_clankers_cavern_puzzles,
                    default_warp_to_entry=0x01,
                    allowed_transformations=[
                        TRANSFORMATION.banjo_kazooie,
                        TRANSFORMATION.termite,
                        TRANSFORMATION.crocodile,
                        TRANSFORMATION.walrus,
                        TRANSFORMATION.pumpkin,
                        TRANSFORMATION.bee],
                )
            }
        ),
    }
)
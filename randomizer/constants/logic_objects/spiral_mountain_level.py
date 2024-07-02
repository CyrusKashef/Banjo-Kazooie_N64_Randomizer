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
##### SPIRAL MOUNTAIN LEVEL #####
#################################

SPIRAL_MOUNTAIN_LEVEL = LEVEL_CLASS(
    debug_name="Spiral Mountain",
    level_enum=LEVEL.spiral_mountain,
    level_start_region_enum=REGION.Spiral_Mountain_Main,
    region_dict={
        REGION.Spiral_Mountain_Main: REGION_CLASS(
            debug_name="Spiral Mountain Main",
            region_enum=REGION.Spiral_Mountain_Main,
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
                # Notes
                # Blue Eggs
                # Red Feathers
                # Gold Feathers
                # Jiggies
                # Empty Honeycombs
                LOCATION.spiral_mountain_stump: LOCATION_CLASS(
                    debug_name="SM Stump",
                    location_enum=LOCATION.spiral_mountain_stump,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.flap_flip]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.spiral_mountain_atop_tree: LOCATION_CLASS(
                    debug_name="SM Atop Tree",
                    location_enum=LOCATION.spiral_mountain_atop_tree,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.climb]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    },
                ),
                LOCATION.spiral_mountain_ledges: LOCATION_CLASS(
                    debug_name="SM Ledges",
                    location_enum=LOCATION.spiral_mountain_ledges,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            (item_dict[ABILITY.high_jump] and
                                (item_dict[ABILITY.feathery_flap] or
                                item_dict[ABILITY.rat_a_tat_rap])) or
                            (item_dict[ABILITY.talon_trot])
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.spiral_mountain_underwater: LOCATION_CLASS(
                    debug_name="SM Underwater",
                    location_enum=LOCATION.spiral_mountain_underwater,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.dive]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: False)
                    }
                ),
                LOCATION.spiral_mountain_colliwobble: LOCATION_CLASS(
                    debug_name="SM Colliwobble",
                    location_enum=LOCATION.spiral_mountain_colliwobble,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.rat_a_tat_rap]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: False)
                    }
                ),
                # Mumbo Tokens
                # Extra Lives
                LOCATION.spiral_mountain_atop_banjos_house: LOCATION_CLASS(
                    debug_name="SM Atop Banjo's House",
                    location_enum=LOCATION.spiral_mountain_atop_banjos_house,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.flap_flip]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.spiral_mountain_behind_waterfall: LOCATION_CLASS(
                    debug_name="SM Behind Waterfall",
                    location_enum=LOCATION.spiral_mountain_behind_waterfall,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            (item_dict[ABILITY.high_jump] and
                                (item_dict[ABILITY.feathery_flap] or
                                item_dict[ABILITY.rat_a_tat_rap])) or
                            (item_dict[ABILITY.talon_trot])
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                # Jinjos
                # Bottles Molehills
                LOCATION.spiral_mountain_bottles_climb: LOCATION_CLASS(
                    debug_name="SM Bottles Climb",
                    location_enum=LOCATION.spiral_mountain_bottles_climb,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.spiral_mountain_bottles_jump: LOCATION_CLASS(
                    debug_name="SM Bottles Jump",
                    location_enum=LOCATION.spiral_mountain_bottles_jump,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.spiral_mountain_bottles_attack: LOCATION_CLASS(
                    debug_name="SM Bottles Attack",
                    location_enum=LOCATION.spiral_mountain_bottles_attack,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.spiral_mountain_bottles_dive: LOCATION_CLASS(
                    debug_name="SM Bottles Dive",
                    location_enum=LOCATION.spiral_mountain_bottles_dive,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                # Other Items
                # Custom Locations
            },
            connected_non_warp_regions_dict={
                REGION.Spiral_Mountain_Lair_Entrance: {
                    TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                    TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                    TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                    TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                    TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                    TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                }
            },
            exit_region={
                WARP.spiral_mountain_banjos_house_from_main: WARP_CLASS(
                    debug_name="SM Into Banjo's House",
                    warp_enum=WARP.spiral_mountain_banjos_house_from_main,
                    default_region_enum=REGION.Spiral_Mountain_House_Interior,
                    default_warp_to_map=MAP.spiral_mountain_banjos_house,
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
        REGION.Spiral_Mountain_Lair_Entrance: REGION_CLASS(
            debug_name="SM Gruntilda's Lair Entrance",
            region_enum=REGION.Spiral_Mountain_Lair_Entrance,
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
                REGION.Spiral_Mountain_Main: {
                    TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                    TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                    TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                    TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                    TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                    TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                }
            },
            exit_region={
                WARP.gruntildas_lair_mm_lobby_from_spiral_mountain_main: WARP_CLASS(
                    debug_name="SM Bridge To GL MM Lobby",
                    warp_enum=WARP.gruntildas_lair_mm_lobby_from_spiral_mountain_main,
                    default_region_enum=REGION.Gruntildas_Lair_Spiral_Mountain_Entrance,
                    default_warp_to_map=MAP.gruntildas_lair_mumbos_mountain_entrance,
                    default_warp_to_entry=0x12,
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
        REGION.Spiral_Mountain_House_Interior: REGION_CLASS(
            debug_name="SM Inside Banjo's House",
            region_enum=REGION.Spiral_Mountain_House_Interior,
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
            connected_non_warp_regions_dict={},
            exit_region={
                WARP.spiral_mountain_main_from_banjos_house: WARP_CLASS(
                    debug_name="SM Banjo's House To Main",
                    warp_enum=WARP.spiral_mountain_main_from_banjos_house,
                    default_region_enum=REGION.Spiral_Mountain_Main,
                    default_warp_to_map=MAP.spiral_mountain_main,
                    default_warp_to_entry=0x12,
                    allowed_transformations=[
                        TRANSFORMATION.banjo_kazooie,
                        TRANSFORMATION.termite,
                        TRANSFORMATION.crocodile,
                        TRANSFORMATION.walrus,
                        TRANSFORMATION.pumpkin,
                        TRANSFORMATION.bee],
                )
            }
        )
    },
)



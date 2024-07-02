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
##### MUMBOS MOUNTAIN LEVEL #####
#################################

MUMBOS_MOUNTAIN_LEVEL = LEVEL_CLASS(
    debug_name="Mumbos Mountain",
    level_enum=LEVEL.mumbos_mountain,
    level_start_region_enum=REGION.Mumbos_Mountain_Main,
    region_dict={
        REGION.Mumbos_Mountain_Main: REGION_CLASS(
            debug_name="Mumbos Mountain Main",
            region_enum=REGION.Mumbos_Mountain_Main,
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
                LOCATION.mumbos_mountain_bridge_note_1: LOCATION_CLASS(
                    debug_name="MM Bridge Note 1",
                    location_enum=LOCATION.mumbos_mountain_bridge_note_1,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_bridge_note_2: LOCATION_CLASS(
                    debug_name="MM Bridge Note 2",
                    location_enum=LOCATION.mumbos_mountain_bridge_note_2,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_bridge_note_3: LOCATION_CLASS(
                    debug_name="MM Bridge Note 3",
                    location_enum=LOCATION.mumbos_mountain_bridge_note_3,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_bridge_note_4: LOCATION_CLASS(
                    debug_name="MM Bridge Note 4",
                    location_enum=LOCATION.mumbos_mountain_bridge_note_4,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_bridge_note_5: LOCATION_CLASS(
                    debug_name="MM Bridge Note 5",
                    location_enum=LOCATION.mumbos_mountain_bridge_note_5,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_bridge_note_6: LOCATION_CLASS(
                    debug_name="MM Bridge Note 6",
                    location_enum=LOCATION.mumbos_mountain_bridge_note_6,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_bridge_note_7: LOCATION_CLASS(
                    debug_name="MM Bridge Note 7",
                    location_enum=LOCATION.mumbos_mountain_bridge_note_7,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_grass_slope_note_1: LOCATION_CLASS(
                    debug_name="MM Grass Slope Note 1",
                    location_enum=LOCATION.mumbos_mountain_grass_slope_note_1,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.talon_trot]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_grass_slope_note_2: LOCATION_CLASS(
                    debug_name="MM Grass Slope Note 2",
                    location_enum=LOCATION.mumbos_mountain_grass_slope_note_2,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.talon_trot]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_grass_slope_note_3: LOCATION_CLASS(
                    debug_name="MM Grass Slope Note 3",
                    location_enum=LOCATION.mumbos_mountain_grass_slope_note_3,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.talon_trot]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_grass_slope_note_4: LOCATION_CLASS(
                    debug_name="MM Grass Slope Note 4",
                    location_enum=LOCATION.mumbos_mountain_grass_slope_note_4,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_grass_slope_note_5: LOCATION_CLASS(
                    debug_name="MM Grass Slope Note 5",
                    location_enum=LOCATION.mumbos_mountain_grass_slope_note_5,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_grass_slope_note_6: LOCATION_CLASS(
                    debug_name="MM Grass Slope Note 6",
                    location_enum=LOCATION.mumbos_mountain_grass_slope_note_6,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_grass_slope_note_7: LOCATION_CLASS(
                    debug_name="MM Grass Slope Note 7",
                    location_enum=LOCATION.mumbos_mountain_grass_slope_note_7,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_grass_slope_note_8: LOCATION_CLASS(
                    debug_name="MM Grass Slope Note 8",
                    location_enum=LOCATION.mumbos_mountain_grass_slope_note_8,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_grass_slope_note_9: LOCATION_CLASS(
                    debug_name="MM Grass Slope Note 9",
                    location_enum=LOCATION.mumbos_mountain_grass_slope_note_9,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_grass_slope_note_10: LOCATION_CLASS(
                    debug_name="MM Grass Slope Note 10",
                    location_enum=LOCATION.mumbos_mountain_grass_slope_note_10,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.talon_trot]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_grass_slope_note_11: LOCATION_CLASS(
                    debug_name="MM Grass Slope Note 11",
                    location_enum=LOCATION.mumbos_mountain_grass_slope_note_11,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.talon_trot]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_grass_slope_note_12: LOCATION_CLASS(
                    debug_name="MM Grass Slope Note 12",
                    location_enum=LOCATION.mumbos_mountain_grass_slope_note_12,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.talon_trot]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_grass_slope_note_13: LOCATION_CLASS(
                    debug_name="MM Grass Slope Note 13",
                    location_enum=LOCATION.mumbos_mountain_grass_slope_note_13,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.talon_trot]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_grass_slope_note_14: LOCATION_CLASS(
                    debug_name="MM Grass Slope Note 14",
                    location_enum=LOCATION.mumbos_mountain_grass_slope_note_14,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.talon_trot]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_grass_slope_note_15: LOCATION_CLASS(
                    debug_name="MM Grass Slope Note 15",
                    location_enum=LOCATION.mumbos_mountain_grass_slope_note_15,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.talon_trot]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_grass_slope_note_16: LOCATION_CLASS(
                    debug_name="MM Grass Slope Note 16",
                    location_enum=LOCATION.mumbos_mountain_grass_slope_note_16,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.talon_trot]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_grass_slope_note_17: LOCATION_CLASS(
                    debug_name="MM Grass Slope Note 17",
                    location_enum=LOCATION.mumbos_mountain_grass_slope_note_17,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.talon_trot]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_grass_slope_note_18: LOCATION_CLASS(
                    debug_name="MM Grass Slope Note 18",
                    location_enum=LOCATION.mumbos_mountain_grass_slope_note_18,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.talon_trot]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_dirt_slope_note_1: LOCATION_CLASS(
                    debug_name="MM Dirt Slope Note 1",
                    location_enum=LOCATION.mumbos_mountain_dirt_slope_note_1,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_dirt_slope_note_2: LOCATION_CLASS(
                    debug_name="MM Dirt Slope Note 2",
                    location_enum=LOCATION.mumbos_mountain_dirt_slope_note_2,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_dirt_slope_note_3: LOCATION_CLASS(
                    debug_name="MM Dirt Slope Note 3",
                    location_enum=LOCATION.mumbos_mountain_dirt_slope_note_3,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_dirt_slope_note_4: LOCATION_CLASS(
                    debug_name="MM Dirt Slope Note 4",
                    location_enum=LOCATION.mumbos_mountain_dirt_slope_note_4,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_dirt_slope_note_5: LOCATION_CLASS(
                    debug_name="MM Dirt Slope Note 5",
                    location_enum=LOCATION.mumbos_mountain_dirt_slope_note_5,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_dirt_slope_note_6: LOCATION_CLASS(
                    debug_name="MM Dirt Slope Note 6",
                    location_enum=LOCATION.mumbos_mountain_dirt_slope_note_6,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_dirt_slope_note_7: LOCATION_CLASS(
                    debug_name="MM Dirt Slope Note 7",
                    location_enum=LOCATION.mumbos_mountain_dirt_slope_note_7,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_dirt_slope_note_8: LOCATION_CLASS(
                    debug_name="MM Dirt Slope Note 8",
                    location_enum=LOCATION.mumbos_mountain_dirt_slope_note_8,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_dirt_slope_note_9: LOCATION_CLASS(
                    debug_name="MM Dirt Slope Note 9",
                    location_enum=LOCATION.mumbos_mountain_dirt_slope_note_9,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_dirt_slope_note_10: LOCATION_CLASS(
                    debug_name="MM Dirt Slope Note 10",
                    location_enum=LOCATION.mumbos_mountain_dirt_slope_note_10,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_dirt_slope_note_11: LOCATION_CLASS(
                    debug_name="MM Dirt Slope Note 11",
                    location_enum=LOCATION.mumbos_mountain_dirt_slope_note_11,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_dirt_slope_note_12: LOCATION_CLASS(
                    debug_name="MM Dirt Slope Note 12",
                    location_enum=LOCATION.mumbos_mountain_dirt_slope_note_12,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_dirt_slope_note_13: LOCATION_CLASS(
                    debug_name="MM Dirt Slope Note 13",
                    location_enum=LOCATION.mumbos_mountain_dirt_slope_note_13,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_dirt_slope_note_14: LOCATION_CLASS(
                    debug_name="MM Dirt Slope Note 14",
                    location_enum=LOCATION.mumbos_mountain_dirt_slope_note_14,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_dirt_slope_note_15: LOCATION_CLASS(
                    debug_name="MM Dirt Slope Note 15",
                    location_enum=LOCATION.mumbos_mountain_dirt_slope_note_15,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_dirt_slope_note_16: LOCATION_CLASS(
                    debug_name="MM Dirt Slope Note 16",
                    location_enum=LOCATION.mumbos_mountain_dirt_slope_note_16,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_dirt_slope_note_17: LOCATION_CLASS(
                    debug_name="MM Dirt Slope Note 17",
                    location_enum=LOCATION.mumbos_mountain_dirt_slope_note_17,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_dirt_slope_note_18: LOCATION_CLASS(
                    debug_name="MM Dirt Slope Note 18",
                    location_enum=LOCATION.mumbos_mountain_dirt_slope_note_18,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_dirt_slope_note_19: LOCATION_CLASS(
                    debug_name="MM Dirt Slope Note 19",
                    location_enum=LOCATION.mumbos_mountain_dirt_slope_note_19,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_dirt_slope_note_20: LOCATION_CLASS(
                    debug_name="MM Dirt Slope Note 20",
                    location_enum=LOCATION.mumbos_mountain_dirt_slope_note_20,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_dirt_slope_note_21: LOCATION_CLASS(
                    debug_name="MM Dirt Slope Note 21",
                    location_enum=LOCATION.mumbos_mountain_dirt_slope_note_21,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_long_stairs_note_1: LOCATION_CLASS(
                    debug_name="MM Long Stairs Note 1",
                    location_enum=LOCATION.mumbos_mountain_long_stairs_note_1,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_long_stairs_note_2: LOCATION_CLASS(
                    debug_name="MM Long Stairs Note 2",
                    location_enum=LOCATION.mumbos_mountain_long_stairs_note_2,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_long_stairs_note_3: LOCATION_CLASS(
                    debug_name="MM Long Stairs Note 3",
                    location_enum=LOCATION.mumbos_mountain_long_stairs_note_3,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_long_stairs_note_4: LOCATION_CLASS(
                    debug_name="MM Long Stairs Note 4",
                    location_enum=LOCATION.mumbos_mountain_long_stairs_note_4,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_long_stairs_note_5: LOCATION_CLASS(
                    debug_name="MM Long Stairs Note 5",
                    location_enum=LOCATION.mumbos_mountain_long_stairs_note_5,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_long_stairs_note_6: LOCATION_CLASS(
                    debug_name="MM Long Stairs Note 6",
                    location_enum=LOCATION.mumbos_mountain_long_stairs_note_6,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_long_stairs_note_7: LOCATION_CLASS(
                    debug_name="MM Long Stairs Note 7",
                    location_enum=LOCATION.mumbos_mountain_long_stairs_note_7,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_long_stairs_note_8: LOCATION_CLASS(
                    debug_name="MM Long Stairs Note 8",
                    location_enum=LOCATION.mumbos_mountain_long_stairs_note_8,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_long_stairs_note_9: LOCATION_CLASS(
                    debug_name="MM Long Stairs Note 9",
                    location_enum=LOCATION.mumbos_mountain_long_stairs_note_9,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_short_stairs_note_1: LOCATION_CLASS(
                    debug_name="MM Short Stairs Note 1",
                    location_enum=LOCATION.mumbos_mountain_short_stairs_note_1,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_short_stairs_note_2: LOCATION_CLASS(
                    debug_name="MM Short Stairs Note 2",
                    location_enum=LOCATION.mumbos_mountain_short_stairs_note_2,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_short_stairs_note_3: LOCATION_CLASS(
                    debug_name="MM Short Stairs Note 3",
                    location_enum=LOCATION.mumbos_mountain_short_stairs_note_3,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_short_stairs_note_4: LOCATION_CLASS(
                    debug_name="MM Short Stairs Note 4",
                    location_enum=LOCATION.mumbos_mountain_short_stairs_note_4,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_stonehenge_note_1: LOCATION_CLASS(
                    debug_name="MM Stonehenge Note 1",
                    location_enum=LOCATION.mumbos_mountain_stonehenge_note_1,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.talon_trot]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_stonehenge_note_2: LOCATION_CLASS(
                    debug_name="MM Stonehenge Note 2",
                    location_enum=LOCATION.mumbos_mountain_stonehenge_note_2,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.talon_trot]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_stonehenge_note_3: LOCATION_CLASS(
                    debug_name="MM Stonehenge Note 3",
                    location_enum=LOCATION.mumbos_mountain_stonehenge_note_3,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.talon_trot]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_stonehenge_note_4: LOCATION_CLASS(
                    debug_name="MM Stonehenge Note 4",
                    location_enum=LOCATION.mumbos_mountain_stonehenge_note_4,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.talon_trot]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_stonehenge_note_5: LOCATION_CLASS(
                    debug_name="MM Stonehenge Note 5",
                    location_enum=LOCATION.mumbos_mountain_stonehenge_note_5,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.talon_trot]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_stonehenge_note_6: LOCATION_CLASS(
                    debug_name="MM Stonehenge Note 6",
                    location_enum=LOCATION.mumbos_mountain_stonehenge_note_6,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.talon_trot]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_stonehenge_note_7: LOCATION_CLASS(
                    debug_name="MM Stonehenge Note 7",
                    location_enum=LOCATION.mumbos_mountain_stonehenge_note_7,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.talon_trot]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_stonehenge_note_8: LOCATION_CLASS(
                    debug_name="MM Stonehenge Note 8",
                    location_enum=LOCATION.mumbos_mountain_stonehenge_note_8,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.talon_trot]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_stonehenge_note_9: LOCATION_CLASS(
                    debug_name="MM Stonehenge Note 9",
                    location_enum=LOCATION.mumbos_mountain_stonehenge_note_9,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.talon_trot]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_stonehenge_note_10: LOCATION_CLASS(
                    debug_name="MM Stonehenge Note 10",
                    location_enum=LOCATION.mumbos_mountain_stonehenge_note_10,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.talon_trot]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_stonehenge_note_11: LOCATION_CLASS(
                    debug_name="MM Stonehenge Note 11",
                    location_enum=LOCATION.mumbos_mountain_stonehenge_note_11,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.talon_trot]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_stonehenge_note_12: LOCATION_CLASS(
                    debug_name="MM Stonehenge Note 12",
                    location_enum=LOCATION.mumbos_mountain_stonehenge_note_12,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.talon_trot]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_stonehenge_note_13: LOCATION_CLASS(
                    debug_name="MM Stonehenge Note 13",
                    location_enum=LOCATION.mumbos_mountain_stonehenge_note_13,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.talon_trot]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_stonehenge_note_14: LOCATION_CLASS(
                    debug_name="MM Stonehenge Note 14",
                    location_enum=LOCATION.mumbos_mountain_stonehenge_note_14,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.talon_trot]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_atop_huts_note_1: LOCATION_CLASS(
                    debug_name="MM Atop Huts Note 1",
                    location_enum=LOCATION.mumbos_mountain_atop_huts_note_1,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.high_jump] or
                            item_dict[ABILITY.flap_flip] or
                            item_dict[ABILITY.talon_trot]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_atop_huts_note_2: LOCATION_CLASS(
                    debug_name="MM Atop Huts Note 2",
                    location_enum=LOCATION.mumbos_mountain_atop_huts_note_2,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.high_jump] or
                            item_dict[ABILITY.flap_flip] or
                            item_dict[ABILITY.talon_trot]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_atop_huts_note_3: LOCATION_CLASS(
                    debug_name="MM Atop Huts Note 3",
                    location_enum=LOCATION.mumbos_mountain_atop_huts_note_3,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.high_jump] or
                            item_dict[ABILITY.flap_flip] or
                            item_dict[ABILITY.talon_trot]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_atop_huts_note_4: LOCATION_CLASS(
                    debug_name="MM Atop Huts Note 4",
                    location_enum=LOCATION.mumbos_mountain_atop_huts_note_4,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.high_jump] or
                            item_dict[ABILITY.flap_flip] or
                            item_dict[ABILITY.talon_trot]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_atop_huts_note_5: LOCATION_CLASS(
                    debug_name="MM Atop Huts Note 5",
                    location_enum=LOCATION.mumbos_mountain_atop_huts_note_5,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.high_jump] or
                            item_dict[ABILITY.flap_flip] or
                            item_dict[ABILITY.talon_trot]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_atop_huts_note_6: LOCATION_CLASS(
                    debug_name="MM Atop Huts Note 6",
                    location_enum=LOCATION.mumbos_mountain_atop_huts_note_6,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.high_jump] or
                            item_dict[ABILITY.flap_flip] or
                            item_dict[ABILITY.talon_trot]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_underwater_note_1: LOCATION_CLASS(
                    debug_name="MM Underwater Note 1",
                    location_enum=LOCATION.mumbos_mountain_underwater_note_1,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.dive]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_underwater_note_2: LOCATION_CLASS(
                    debug_name="MM Underwater Note 2",
                    location_enum=LOCATION.mumbos_mountain_underwater_note_2,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.dive]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_underwater_note_3: LOCATION_CLASS(
                    debug_name="MM Underwater Note 3",
                    location_enum=LOCATION.mumbos_mountain_underwater_note_3,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.dive]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_underwater_note_4: LOCATION_CLASS(
                    debug_name="MM Underwater Note 4",
                    location_enum=LOCATION.mumbos_mountain_underwater_note_4,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.dive]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_underwater_note_5: LOCATION_CLASS(
                    debug_name="MM Underwater Note 5",
                    location_enum=LOCATION.mumbos_mountain_underwater_note_5,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.dive]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_underwater_note_6: LOCATION_CLASS(
                    debug_name="MM Underwater Note 6",
                    location_enum=LOCATION.mumbos_mountain_underwater_note_6,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.dive]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                # Blue Eggs
                LOCATION.mumbos_mountain_stonehenge_egg_1: LOCATION_CLASS(
                    debug_name="MM Stonehenge Egg 1",
                    location_enum=LOCATION.mumbos_mountain_stonehenge_egg_1,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_stonehenge_egg_2: LOCATION_CLASS(
                    debug_name="MM Stonehenge Egg 2",
                    location_enum=LOCATION.mumbos_mountain_stonehenge_egg_2,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_stonehenge_egg_3: LOCATION_CLASS(
                    debug_name="MM Stonehenge Egg 3",
                    location_enum=LOCATION.mumbos_mountain_stonehenge_egg_3,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_stonehenge_egg_4: LOCATION_CLASS(
                    debug_name="MM Stonehenge Egg 4",
                    location_enum=LOCATION.mumbos_mountain_stonehenge_egg_4,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_stonehenge_egg_5: LOCATION_CLASS(
                    debug_name="MM Stonehenge Egg 5",
                    location_enum=LOCATION.mumbos_mountain_stonehenge_egg_5,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                # Red Feathers
                # Gold Feathers
                # Jiggies
                LOCATION.mumbos_mountain_inside_mumbos_skull_eye: LOCATION_CLASS(
                    debug_name="MM Inside Mumbos Skull Eye",
                    location_enum=LOCATION.mumbos_mountain_inside_mumbos_skull_eye,
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
                LOCATION.mumbos_mountain_green_slope_jiggy: LOCATION_CLASS(
                    debug_name="MM Green Slope Jiggy",
                    location_enum=LOCATION.mumbos_mountain_green_slope_jiggy,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_stonehenge_jiggy: LOCATION_CLASS(
                    debug_name="MM Stonehenge Jiggy",
                    location_enum=LOCATION.mumbos_mountain_stonehenge_jiggy,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: 
                            item_dict[ABILITY.talon_trot]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_atop_tickers_tower_jiggy: LOCATION_CLASS(
                    debug_name="MM Atop Tickers Tower Jiggy",
                    location_enum=LOCATION.mumbos_mountain_atop_tickers_tower_jiggy,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: 
                            item_dict[ABILITY.high_jump] or
                            item_dict[ABILITY.flap_flip] or
                            item_dict[ABILITY.talon_trot]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                # Empty Honeycombs
                LOCATION.mumbos_mountain_above_juju_empty_honeycomb: LOCATION_CLASS(
                    debug_name="MM Above Juju Empty Honeycomb",
                    location_enum=LOCATION.mumbos_mountain_above_juju_empty_honeycomb,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: 
                            item_dict[ABILITY.egg_firing] and item_dict[ABILITY.flap_flip]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: False)
                    }
                ),
                LOCATION.mumbos_mountain_alcove_empty_honeycomb: LOCATION_CLASS(
                    debug_name="MM Alcove Empty Honeycomb",
                    location_enum=LOCATION.mumbos_mountain_alcove_empty_honeycomb,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                # Mumbo Tokens
                LOCATION.mumbos_mountain_mumbos_bridge_token: LOCATION_CLASS(
                    debug_name="MM Mumbos Bridge Token",
                    location_enum=LOCATION.mumbos_mountain_mumbos_bridge_token,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_near_pink_jinjo_token: LOCATION_CLASS(
                    debug_name="MM Near Pink Jinjo Token",
                    location_enum=LOCATION.mumbos_mountain_near_pink_jinjo_token,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_stonehenge_token: LOCATION_CLASS(
                    debug_name="MM Stonehenge Token",
                    location_enum=LOCATION.mumbos_mountain_stonehenge_token,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_conga_token: LOCATION_CLASS(
                    debug_name="MM Conga Token",
                    location_enum=LOCATION.mumbos_mountain_conga_token,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: 
                            item_dict[JIGGY.mumbos_mountain_chimpy] and
                            item_dict[ABILITY.flap_flip] and
                            item_dict[ABILITY.high_jump] and
                            item_dict[ABILITY.feathery_flap]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_tickers_tower_token: LOCATION_CLASS(
                    debug_name="MM Tickers Tower Token",
                    location_enum=LOCATION.mumbos_mountain_tickers_tower_token,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: 
                            item_dict[ABILITY.flap_flip] or
                            item_dict[ABILITY.talon_trot]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                # Extra Lives
                # Jinjos
                LOCATION.mumbos_mountain_pink_jinjo_platform: LOCATION_CLASS(
                    debug_name="MM Pink Jinjo Platform",
                    location_enum=LOCATION.mumbos_mountain_pink_jinjo_platform,
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
                LOCATION.mumbos_mountain_blue_jinjo_island: LOCATION_CLASS(
                    debug_name="MM Blue Jinjo Island",
                    location_enum=LOCATION.mumbos_mountain_blue_jinjo_island,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: 
                            item_dict[ABILITY.talon_trot] or
                            (
                                item_dict[ABILITY.high_jump] and
                                item_dict[ABILITY.feathery_flap]
                            )
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_yellow_jinjo_ledge: LOCATION_CLASS(
                    debug_name="MM Yellow Jinjo Ledge",
                    location_enum=LOCATION.mumbos_mountain_yellow_jinjo_ledge,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_orange_jinjo_stonehenge: LOCATION_CLASS(
                    debug_name="MM Orange Jinjo Stonehenge",
                    location_enum=LOCATION.mumbos_mountain_orange_jinjo_stonehenge,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.talon_trot]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                # Bottles Molehills
                LOCATION.mumbos_mountain_bottles_beak_buster: LOCATION_CLASS(
                    debug_name="MM Bottles Beak Buster",
                    location_enum=LOCATION.mumbos_mountain_bottles_beak_buster,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_bottles_talon_trot: LOCATION_CLASS(
                    debug_name="MM Bottles Talon Trot",
                    location_enum=LOCATION.mumbos_mountain_bottles_talon_trot,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_bottles_egg_firing: LOCATION_CLASS(
                    debug_name="MM Bottles Egg Firing",
                    location_enum=LOCATION.mumbos_mountain_bottles_egg_firing,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[JIGGY.mumbos_mountain_chimpy] and
                            item_dict[ABILITY.flap_flip]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                # Events
                LOCATION.mumbos_mountain_conga: LOCATION_CLASS(
                    debug_name="MM Conga",
                    location_enum=LOCATION.mumbos_mountain_conga,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[JIGGY.mumbos_mountain_chimpy] and
                            item_dict[ABILITY.flap_flip] and
                            item_dict[ABILITY.egg_firing]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: False)
                    }
                ),
                LOCATION.mumbos_mountain_chimpy: LOCATION_CLASS(
                    debug_name="MM Chimpy",
                    location_enum=LOCATION.mumbos_mountain_chimpy,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ITEM_TYPE.chimpys_orange]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: False)
                    }
                ),
                LOCATION.mumbos_mountain_juju: LOCATION_CLASS(
                    debug_name="MM Juju",
                    location_enum=LOCATION.mumbos_mountain_juju,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.egg_firing]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: False)
                    }
                ),
                LOCATION.mumbos_mountain_orange_pads: LOCATION_CLASS(
                    debug_name="MM Orange Pads",
                    location_enum=LOCATION.mumbos_mountain_orange_pads,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_huts: LOCATION_CLASS(
                    debug_name="MM Huts",
                    location_enum=LOCATION.mumbos_mountain_huts,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.beak_buster] and
                            (
                                item_dict[ABILITY.high_jump] or
                                item_dict[ABILITY.flap_flip]
                            )
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: False)
                    }
                ),
                # Other Items
                LOCATION.mumbos_mountain_orange_below_conga: LOCATION_CLASS(
                    debug_name="MM Orange Below Conga",
                    location_enum=LOCATION.mumbos_mountain_orange_below_conga,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                            item_dict[ABILITY.climb]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: False),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                # Custom Locations
            },
            connected_non_warp_regions_dict={
                REGION.Mumbos_Mountain_Atop_Of_Ticker: {
                    TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: False),
                    TRANSFORMATION.termite: (lambda item_dict, settings_dict: False),
                    TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: False),
                    TRANSFORMATION.walrus: (lambda item_dict, settings_dict: False),
                    TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: False),
                    TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                }
            },
            exit_region={
                WARP.gruntildas_lair_mm_lobby_from_mumbos_mountain_main: WARP_CLASS(
                    debug_name="MM Leaving Level To Gruntildas Lair",
                    warp_enum=WARP.gruntildas_lair_mm_lobby_from_mumbos_mountain_main,
                    default_region_enum=REGION.Gruntildas_Lair_Mumbos_Mountain_Entrance,
                    default_warp_to_map=MAP.gruntildas_lair_mumbos_mountain_entrance,
                    default_warp_to_entry=0x02,
                    allowed_transformations=[
                        TRANSFORMATION.banjo_kazooie,
                        TRANSFORMATION.termite,
                        TRANSFORMATION.crocodile,
                        TRANSFORMATION.walrus,
                        TRANSFORMATION.pumpkin,
                        TRANSFORMATION.bee],
                ),
                WARP.mumbos_mountain_mumbos_hut_from_main: WARP_CLASS(
                    debug_name="MM Into Mumbos Hut",
                    warp_enum=WARP.mumbos_mountain_mumbos_hut_from_main,
                    default_region_enum=REGION.Mumbos_Mountain_Mumbos_Interior,
                    default_warp_to_map=MAP.mumbos_mountain_mumbos_hut,
                    default_warp_to_entry=0x01,
                    allowed_transformations=[
                        TRANSFORMATION.banjo_kazooie,
                        TRANSFORMATION.termite,
                        TRANSFORMATION.crocodile,
                        TRANSFORMATION.walrus,
                        TRANSFORMATION.pumpkin,
                        TRANSFORMATION.bee],
                ),
                WARP.mumbos_mountain_tickers_tower_lower_from_main: WARP_CLASS(
                    debug_name="MM Into Tickers Lower",
                    warp_enum=WARP.mumbos_mountain_tickers_tower_lower_from_main,
                    default_region_enum=REGION.Mumbos_Mountain_Ticker_Interior_Bottom_Entrance,
                    default_warp_to_map=MAP.mumbos_mountain_tickers_tower,
                    default_warp_to_entry=0x02,
                    allowed_transformations=[
                        TRANSFORMATION.banjo_kazooie,
                        TRANSFORMATION.termite,
                        TRANSFORMATION.crocodile,
                        TRANSFORMATION.walrus,
                        TRANSFORMATION.pumpkin,
                        TRANSFORMATION.bee],
                ),
            },
        ),
        REGION.Mumbos_Mountain_Mumbos_Interior: REGION_CLASS(
            debug_name="Mumbos Mountain Inside Mumbos Skull",
            region_enum=REGION.Mumbos_Mountain_Mumbos_Interior,
            transformation_pad=TRANSFORMATION.termite,
            detransformation_zone=False,
            allowed_transformations=[
                TRANSFORMATION.banjo_kazooie,
                TRANSFORMATION.termite,
                TRANSFORMATION.crocodile,
                TRANSFORMATION.walrus,
                TRANSFORMATION.pumpkin,
                TRANSFORMATION.bee],
            required_transformation_access=[
                TRANSFORMATION.banjo_kazooie,
                TRANSFORMATION.termite],
            location_dict={
                # Notes
                LOCATION.mumbos_mountain_mumbos_skull_note_1: LOCATION_CLASS(
                    debug_name="MM Mumbos Skull Note 1",
                    location_enum=LOCATION.mumbos_mountain_mumbos_skull_note_1,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_mumbos_skull_note_2: LOCATION_CLASS(
                    debug_name="MM Mumbos Skull Note 2",
                    location_enum=LOCATION.mumbos_mountain_mumbos_skull_note_2,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_mumbos_skull_note_3: LOCATION_CLASS(
                    debug_name="MM Mumbos Skull Note 3",
                    location_enum=LOCATION.mumbos_mountain_mumbos_skull_note_3,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_mumbos_skull_note_4: LOCATION_CLASS(
                    debug_name="MM Mumbos Skull Note 4",
                    location_enum=LOCATION.mumbos_mountain_mumbos_skull_note_4,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                # Blue Eggs
                LOCATION.mumbos_mountain_mumbos_skull_egg_1: LOCATION_CLASS(
                    debug_name="MM Mumbos Skull Egg 1",
                    location_enum=LOCATION.mumbos_mountain_mumbos_skull_egg_1,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: 
                            item_dict[ABILITY.flap_flip]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_mumbos_skull_egg_2: LOCATION_CLASS(
                    debug_name="MM Mumbos Skull Egg 2",
                    location_enum=LOCATION.mumbos_mountain_mumbos_skull_egg_2,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: 
                            item_dict[ABILITY.flap_flip]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_mumbos_skull_egg_3: LOCATION_CLASS(
                    debug_name="MM Mumbos Skull Egg 3",
                    location_enum=LOCATION.mumbos_mountain_mumbos_skull_egg_3,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: 
                            item_dict[ABILITY.flap_flip]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_mumbos_skull_egg_4: LOCATION_CLASS(
                    debug_name="MM Mumbos Skull Egg 4",
                    location_enum=LOCATION.mumbos_mountain_mumbos_skull_egg_4,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: 
                            item_dict[ABILITY.flap_flip]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_mumbos_skull_egg_5: LOCATION_CLASS(
                    debug_name="MM Mumbos Skull Egg 5",
                    location_enum=LOCATION.mumbos_mountain_mumbos_skull_egg_5,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: 
                            item_dict[ABILITY.flap_flip]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_mumbos_skull_egg_6: LOCATION_CLASS(
                    debug_name="MM Mumbos Skull Egg 6",
                    location_enum=LOCATION.mumbos_mountain_mumbos_skull_egg_6,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: 
                            item_dict[ABILITY.flap_flip]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_mumbos_skull_egg_7: LOCATION_CLASS(
                    debug_name="MM Mumbos Skull Egg 7",
                    location_enum=LOCATION.mumbos_mountain_mumbos_skull_egg_7,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: 
                            item_dict[ABILITY.flap_flip]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_mumbos_skull_egg_8: LOCATION_CLASS(
                    debug_name="MM Mumbos Skull Egg 8",
                    location_enum=LOCATION.mumbos_mountain_mumbos_skull_egg_8,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: 
                            item_dict[ABILITY.flap_flip]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_mumbos_skull_egg_9: LOCATION_CLASS(
                    debug_name="MM Mumbos Skull Egg 9",
                    location_enum=LOCATION.mumbos_mountain_mumbos_skull_egg_9,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: 
                            item_dict[ABILITY.flap_flip]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_mumbos_skull_egg_10: LOCATION_CLASS(
                    debug_name="MM Mumbos Skull Egg 10",
                    location_enum=LOCATION.mumbos_mountain_mumbos_skull_egg_10,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: 
                            item_dict[ABILITY.flap_flip]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_mumbos_skull_egg_11: LOCATION_CLASS(
                    debug_name="MM Mumbos Skull Egg 11",
                    location_enum=LOCATION.mumbos_mountain_mumbos_skull_egg_11,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: 
                            item_dict[ABILITY.flap_flip]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_mumbos_skull_egg_12: LOCATION_CLASS(
                    debug_name="MM Mumbos Skull Egg 12",
                    location_enum=LOCATION.mumbos_mountain_mumbos_skull_egg_12,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: 
                            item_dict[ABILITY.flap_flip]
                        ),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                # Red Feathers
                # Gold Feathers
                # Jiggies
                # Empty Honeycombs
                # Mumbo Tokens
                # Extra Lives
                # Jinjos
                # Bottles Molehills
                # Other Items
                # Custom Locations
            },
            connected_non_warp_regions_dict={},
            exit_region={
                WARP.mumbos_mountain_main_from_mumbos_hut: WARP_CLASS(
                    debug_name="MM Exiting Mumbos Skull",
                    warp_enum=WARP.mumbos_mountain_main_from_mumbos_hut,
                    default_region_enum=REGION.Mumbos_Mountain_Main,
                    default_warp_to_map=MAP.mumbos_mountain_main,
                    default_warp_to_entry=0x01,
                    allowed_transformations=[
                        TRANSFORMATION.banjo_kazooie,
                        TRANSFORMATION.termite,
                        TRANSFORMATION.crocodile,
                        TRANSFORMATION.walrus,
                        TRANSFORMATION.pumpkin,
                        TRANSFORMATION.bee],
                )
            },
        ),
        REGION.Mumbos_Mountain_Ticker_Interior_Bottom_Entrance: REGION_CLASS(
            debug_name="Mumbos Mountain Tickers Tower Bottom Entrance",
            region_enum=REGION.Mumbos_Mountain_Ticker_Interior_Bottom_Entrance,
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
                # Mumbo Tokens
                # Extra Lives
                # Jinjos
                # Bottles Molehills
                # Other Items
                # Custom Locations
            },
            connected_non_warp_regions_dict={
                REGION.Mumbos_Mountain_Ticker_Interior_Upper_Floors: {
                    TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict:
                        (
                            settings_dict[DIFFICULTY.intermediate] and
                            (
                                item_dict[ABILITY.feathery_flap] or
                                item_dict[ABILITY.rat_a_tat_rap]
                            )
                        ) or
                        (
                            settings_dict[DIFFICULTY.expert] and
                            item_dict[ABILITY.talon_trot]
                        )
                    ),
                    TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                    TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                    TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                    TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                    TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                }
            },
            exit_region={
                WARP.mumbos_mountain_main_from_tickers_tower_lower: WARP_CLASS(
                    debug_name="MM Leaving Tickers Tower Lower",
                    warp_enum=WARP.mumbos_mountain_main_from_tickers_tower_lower,
                    default_region_enum=REGION.Mumbos_Mountain_Main,
                    default_warp_to_map=MAP.mumbos_mountain_main,
                    default_warp_to_entry=0x02,
                    allowed_transformations=[
                        TRANSFORMATION.banjo_kazooie,
                        TRANSFORMATION.termite,
                        TRANSFORMATION.crocodile,
                        TRANSFORMATION.walrus,
                        TRANSFORMATION.pumpkin,
                        TRANSFORMATION.bee],
                )
            },
        ),
        REGION.Mumbos_Mountain_Ticker_Interior_Upper_Floors: REGION_CLASS(
            debug_name="Mumbos Mountain Tickers Tower Upper Floors",
            region_enum=REGION.Mumbos_Mountain_Ticker_Interior_Upper_Floors,
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
                LOCATION.mumbos_mountain_tickers_tower_note_1: LOCATION_CLASS(
                    debug_name="MM Tickers Tower Note 1",
                    location_enum=LOCATION.mumbos_mountain_tickers_tower_note_1,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_tickers_tower_note_2: LOCATION_CLASS(
                    debug_name="MM Tickers Tower Note 2",
                    location_enum=LOCATION.mumbos_mountain_tickers_tower_note_2,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_tickers_tower_note_3: LOCATION_CLASS(
                    debug_name="MM Tickers Tower Note 3",
                    location_enum=LOCATION.mumbos_mountain_tickers_tower_note_3,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_tickers_tower_note_4: LOCATION_CLASS(
                    debug_name="MM Tickers Tower Note 4",
                    location_enum=LOCATION.mumbos_mountain_tickers_tower_note_4,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_tickers_tower_note_5: LOCATION_CLASS(
                    debug_name="MM Tickers Tower Note 5",
                    location_enum=LOCATION.mumbos_mountain_tickers_tower_note_5,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_tickers_tower_note_6: LOCATION_CLASS(
                    debug_name="MM Tickers Tower Note 6",
                    location_enum=LOCATION.mumbos_mountain_tickers_tower_note_6,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                # Blue Eggs
                LOCATION.mumbos_mountain_tickers_tower_egg_1: LOCATION_CLASS(
                    debug_name="MM Tickers Tower Egg 1",
                    location_enum=LOCATION.mumbos_mountain_tickers_tower_egg_1,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_tickers_tower_egg_2: LOCATION_CLASS(
                    debug_name="MM Tickers Tower Egg 2",
                    location_enum=LOCATION.mumbos_mountain_tickers_tower_egg_2,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_tickers_tower_egg_3: LOCATION_CLASS(
                    debug_name="MM Tickers Tower Egg 3",
                    location_enum=LOCATION.mumbos_mountain_tickers_tower_egg_3,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_tickers_tower_egg_4: LOCATION_CLASS(
                    debug_name="MM Tickers Tower Egg 4",
                    location_enum=LOCATION.mumbos_mountain_tickers_tower_egg_4,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_tickers_tower_egg_5: LOCATION_CLASS(
                    debug_name="MM Tickers Tower Egg 5",
                    location_enum=LOCATION.mumbos_mountain_tickers_tower_egg_5,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                LOCATION.mumbos_mountain_tickers_tower_egg_6: LOCATION_CLASS(
                    debug_name="MM Tickers Tower Egg 6",
                    location_enum=LOCATION.mumbos_mountain_tickers_tower_egg_6,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                # Red Feathers
                # Gold Feathers
                # Jiggies
                # Empty Honeycombs
                # Mumbo Tokens
                # Extra Lives
                # Jinjos
                # Bottles Molehills
                # Other Items
                # Custom Locations
            },
            connected_non_warp_regions_dict={
                REGION.Mumbos_Mountain_Ticker_Interior_Bottom_Entrance: {
                    TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                    TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                    TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                    TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                    TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                    TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                }
            },
            exit_region={
                WARP.mumbos_mountain_main_from_tickers_tower_upper: WARP_CLASS(
                    debug_name="MM Leaving Tickers Tower Upper",
                    warp_enum=WARP.mumbos_mountain_main_from_tickers_tower_upper,
                    default_region_enum=REGION.Mumbos_Mountain_Atop_Of_Ticker,
                    default_warp_to_map=MAP.mumbos_mountain_main,
                    default_warp_to_entry=0x03,
                    allowed_transformations=[
                        TRANSFORMATION.banjo_kazooie,
                        TRANSFORMATION.termite,
                        TRANSFORMATION.crocodile,
                        TRANSFORMATION.walrus,
                        TRANSFORMATION.pumpkin,
                        TRANSFORMATION.bee],
                )
            },
        ),
        REGION.Mumbos_Mountain_Atop_Of_Ticker: REGION_CLASS(
            debug_name="Mumbos Mountain Atop Tickers Tower",
            region_enum=REGION.Mumbos_Mountain_Atop_Of_Ticker,
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
                # Mumbo Tokens
                # Extra Lives
                LOCATION.mumbos_mountain_atop_tickers_tower_life: LOCATION_CLASS(
                    debug_name="MM Atop Tickers Tower Life",
                    location_enum=LOCATION.mumbos_mountain_atop_tickers_tower_life,
                    reach_requirement_dict={
                        TRANSFORMATION.banjo_kazooie: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.termite: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.crocodile: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.walrus: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.pumpkin: (lambda item_dict, settings_dict: True),
                        TRANSFORMATION.bee: (lambda item_dict, settings_dict: True)
                    }
                ),
                # Jinjos
                # Bottles Molehills
                # Other Items
                # Custom Locations
            },
            connected_non_warp_regions_dict={},
            exit_region={},
        ),
    },
)
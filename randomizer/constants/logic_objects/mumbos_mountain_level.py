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
            exit_region={},
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
            connected_non_warp_regions_dict={},
            exit_region={},
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
            connected_non_warp_regions_dict={},
            exit_region={},
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
            connected_non_warp_regions_dict={},
            exit_region={},
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
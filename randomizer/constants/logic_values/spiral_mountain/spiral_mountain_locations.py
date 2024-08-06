###################
##### IMPORTS #####
###################

# Classes

from randomizer.logic.location_class import LOCATION_CLASS

# Enums

from randomizer.constants.int_values.location_enums import LOCATION_ENUMS as LOCATION
from randomizer.constants.int_values.logic_item_enums import LOGIC_ITEM_ENUMS as LOGIC_ITEM
from randomizer.constants.int_values.item_type_enums import ITEM_TYPE_ENUMS as ITEM_TYPE
from randomizer.constants.logic_values.allowed_item_types import ALLOWED_ITEM_TYPE
from randomizer.constants.int_values.transformation_enums import TRANSFORMATION_ENUMS as TRANSFORMATION
from randomizer.constants.int_values.logic_difficulty_enums import LOGIC_DIFFICULTY_ENUMS as DIFFICULTY
from randomizer.constants.int_values.ability_enums import ABILITY_ENUMS as ABILITY

# Objects

from randomizer.constants.logic_values import logic_items
from randomizer.constants.logic_values.spiral_mountain import spiral_mountain_items

#####################
##### LOCATIONS #####
#####################

# Bottles Molehills

SPIRAL_MOUNTAIN_BOTTLES_INTRO_LOCATION = LOCATION_CLASS(
    debug_name="Spiral Mountain Bottles Intro",
    location_enum=LOCATION.spiral_mountain_bottles_intro,
    reach_requirements={
        TRANSFORMATION.banjo_kazooie: (),
        TRANSFORMATION.termite: (),
        TRANSFORMATION.crocodile: (),
        TRANSFORMATION.walrus: (),
        TRANSFORMATION.pumpkin: (),
        TRANSFORMATION.bee: (),
    },
    default_item=None,
    keep_as_default=False,
    allowed_item_types=ALLOWED_ITEM_TYPE.complex_objects,
)

SPIRAL_MOUNTAIN_BOTTLES_CAMERA_LOCATION = LOCATION_CLASS(
    debug_name="Spiral Mountain Bottles Camera",
    location_enum=LOCATION.spiral_mountain_bottles_camera,
    reach_requirements={
        TRANSFORMATION.banjo_kazooie: (),
        TRANSFORMATION.termite: (),
        TRANSFORMATION.crocodile: (),
        TRANSFORMATION.walrus: (),
        TRANSFORMATION.pumpkin: (),
        TRANSFORMATION.bee: (),
    },
    default_item=None,
    keep_as_default=False,
    allowed_item_types=ALLOWED_ITEM_TYPE.complex_objects,
)

SPIRAL_MOUNTAIN_BOTTLES_CLIMB_LOCATION = LOCATION_CLASS(
    debug_name="Spiral Mountain Bottles Climb",
    location_enum=LOCATION.spiral_mountain_bottles_climb,
    reach_requirements={
        TRANSFORMATION.banjo_kazooie: (),
        TRANSFORMATION.termite: (),
        TRANSFORMATION.crocodile: (),
        TRANSFORMATION.walrus: (),
        TRANSFORMATION.pumpkin: (),
        TRANSFORMATION.bee: (),
    },
    default_item=logic_items.ABILITY_CLIMB_ITEM,
    keep_as_default=False,
    allowed_item_types=ALLOWED_ITEM_TYPE.complex_objects,
)

SPIRAL_MOUNTAIN_BOTTLES_DIVE_LOCATION = LOCATION_CLASS(
    debug_name="Spiral Mountain Bottles Dive",
    location_enum=LOCATION.spiral_mountain_bottles_dive,
    reach_requirements={
        TRANSFORMATION.banjo_kazooie: (),
        TRANSFORMATION.termite: (),
        TRANSFORMATION.crocodile: (),
        TRANSFORMATION.walrus: (),
        TRANSFORMATION.pumpkin: (),
        TRANSFORMATION.bee: (),
    },
    default_item=logic_items.ABILITY_DIVE_ITEM,
    keep_as_default=False,
    allowed_item_types=ALLOWED_ITEM_TYPE.complex_objects,
)

SPIRAL_MOUNTAIN_BOTTLES_ATTACK_LOCATION = LOCATION_CLASS(
    debug_name="Spiral Mountain Bottles Attack",
    location_enum=LOCATION.spiral_mountain_bottles_attack,
    reach_requirements={
        TRANSFORMATION.banjo_kazooie: (),
        TRANSFORMATION.termite: (),
        TRANSFORMATION.crocodile: (),
        TRANSFORMATION.walrus: (),
        TRANSFORMATION.pumpkin: (),
        TRANSFORMATION.bee: (),
    },
    default_item=spiral_mountain_items.ATTACK_TUTORIAL_ITEM,
    keep_as_default=False,
    allowed_item_types=ALLOWED_ITEM_TYPE.complex_objects,
)

SPIRAL_MOUNTAIN_BOTTLES_JUMP_LOCATION = LOCATION_CLASS(
    debug_name="Spiral Mountain Bottles Jump",
    location_enum=LOCATION.spiral_mountain_bottles_jump,
    reach_requirements={
        TRANSFORMATION.banjo_kazooie: (),
        TRANSFORMATION.termite: (),
        TRANSFORMATION.crocodile: (),
        TRANSFORMATION.walrus: (),
        TRANSFORMATION.pumpkin: (),
        TRANSFORMATION.bee: (),
    },
    default_item=spiral_mountain_items.JUMP_TUTORIAL_ITEM,
    keep_as_default=False,
    allowed_item_types=ALLOWED_ITEM_TYPE.complex_objects,
)

SPIRAL_MOUNTAIN_BOTTLES_BEAK_BARGE_LOCATION = LOCATION_CLASS(
    debug_name="Spiral Mountain Bottles Beak Barge",
    location_enum=LOCATION.spiral_mountain_bottles_beak_barge,
    reach_requirements={
        TRANSFORMATION.banjo_kazooie: (),
        TRANSFORMATION.termite: (),
        TRANSFORMATION.crocodile: (),
        TRANSFORMATION.walrus: (),
        TRANSFORMATION.pumpkin: (),
        TRANSFORMATION.bee: (),
    },
    default_item=logic_items.ABILITY_BEAK_BARGE_ITEM,
    keep_as_default=False,
    allowed_item_types=ALLOWED_ITEM_TYPE.complex_objects,
)

SPIRAL_MOUNTAIN_BOTTLES_BRIDGE_LOCATION = LOCATION_CLASS(
    debug_name="Spiral Mountain Bottles Bridge",
    location_enum=LOCATION.spiral_mountain_bottles_bridge,
    reach_requirements={
        TRANSFORMATION.banjo_kazooie: (),
        TRANSFORMATION.termite: (),
        TRANSFORMATION.crocodile: (),
        TRANSFORMATION.walrus: (),
        TRANSFORMATION.pumpkin: (),
        TRANSFORMATION.bee: (),
    },
    default_item=None,
    keep_as_default=False,
    allowed_item_types=ALLOWED_ITEM_TYPE.complex_objects,
)

# Empty Honeycomb

SPIRAL_MOUNTAIN_ATOP_TREE_LOCATION:LOCATION_CLASS = LOCATION_CLASS(
    debug_name="Spiral Mountain Atop Tree",
    location_enum=LOCATION.spiral_mountain_atop_tree,
    reach_requirements={
        TRANSFORMATION.banjo_kazooie: (LOGIC_ITEM.ability_climb,),
        TRANSFORMATION.bee: (),
    },
    default_item=spiral_mountain_items.EMPTY_HONEYCOMB_SM_ATOP_TREE_ITEM,
    keep_as_default=False,
    allowed_item_types=ALLOWED_ITEM_TYPE.floating_complex_objects,
)

SPIRAL_MOUNTAIN_LEDGES_LOCATION:LOCATION_CLASS = LOCATION_CLASS(
    debug_name="Spiral Mountain Ledges",
    location_enum=LOCATION.spiral_mountain_ledges,
    reach_requirements={
        TRANSFORMATION.banjo_kazooie: (
            (
                LOGIC_ITEM.ability_high_jump,
                (
                    (LOGIC_ITEM.ability_feathery_flap,),
                    (LOGIC_ITEM.ability_rat_a_tat_rap,)
                ),
            ),
            (LOGIC_ITEM.ability_talon_trot,),
        ),
        TRANSFORMATION.termite: (),
        TRANSFORMATION.crocodile: (),
        TRANSFORMATION.walrus: (),
        TRANSFORMATION.pumpkin: (),
        TRANSFORMATION.bee: (),
    },
    default_item=spiral_mountain_items.EMPTY_HONEYCOMB_SM_WATERFALL_ITEM,
    keep_as_default=False,
    allowed_item_types=ALLOWED_ITEM_TYPE.complex_objects,
)

SPIRAL_MOUNTAIN_STUMP_LOCATION:LOCATION_CLASS = LOCATION_CLASS(
    debug_name="Spiral Mountain Stump",
    location_enum=LOCATION.spiral_mountain_stump,
    reach_requirements={
        TRANSFORMATION.banjo_kazooie: (LOGIC_ITEM.ability_flap_flip,),
        TRANSFORMATION.termite: (),
        TRANSFORMATION.crocodile: (),
        TRANSFORMATION.walrus: (),
        TRANSFORMATION.pumpkin: (),
        TRANSFORMATION.bee: (),
    },
    default_item=spiral_mountain_items.EMPTY_HONEYCOMB_SM_STUMP_ITEM,
    keep_as_default=False,
    allowed_item_types=ALLOWED_ITEM_TYPE.complex_objects,
)

SPIRAL_MOUNTAIN_UNDERWATER_LOCATION:LOCATION_CLASS = LOCATION_CLASS(
    debug_name="Spiral Mountain Underwater",
    location_enum=LOCATION.spiral_mountain_underwater,
    reach_requirements={
        TRANSFORMATION.banjo_kazooie: (LOGIC_ITEM.ability_dive,),
        TRANSFORMATION.termite: (),
        TRANSFORMATION.crocodile: (),
        TRANSFORMATION.walrus: (),
        TRANSFORMATION.pumpkin: (),
        TRANSFORMATION.bee: (lambda items, difficulty:
            difficulty >= DIFFICULTY.intermediate
        ),
    },
    default_item=spiral_mountain_items.EMPTY_HONEYCOMB_SM_UNDERWATER_ITEM,
    keep_as_default=False,
    allowed_item_types=ALLOWED_ITEM_TYPE.floating_complex_objects,
)

SPIRAL_MOUNTAIN_QUARRIES_LOCATION:LOCATION_CLASS = LOCATION_CLASS(
    debug_name="Spiral Mountain Quarries",
    location_enum=LOCATION.spiral_mountain_quarries,
    reach_requirements={
        TRANSFORMATION.banjo_kazooie: (LOGIC_ITEM.ability_beak_barge,),
    },
    default_item=spiral_mountain_items.EMPTY_HONEYCOMB_SM_QUARRIES_ITEM,
    keep_as_default=True,
    allowed_item_types=ALLOWED_ITEM_TYPE.empty_honeycomb_only,
)

SPIRAL_MOUNTAIN_COLLIWOBBLE_LOCATION:LOCATION_CLASS = LOCATION_CLASS(
    debug_name="Spiral Mountain Colliwobble",
    location_enum=LOCATION.spiral_mountain_colliwobble,
    reach_requirements={
        TRANSFORMATION.banjo_kazooie: (LOGIC_ITEM.ability_rat_a_tat_rap,),
    },
    default_item=spiral_mountain_items.EMPTY_HONEYCOMB_SM_COLLIWOBBLE_ITEM,
    keep_as_default=True,
    allowed_item_types=ALLOWED_ITEM_TYPE.empty_honeycomb_only,
)

# Extra Lives

SPIRAL_MOUNTAIN_ATOP_HOUSE_LOCATION:LOCATION_CLASS = LOCATION_CLASS(
    debug_name="Spiral Mountain Atop House",
    location_enum=LOCATION.spiral_mountain_atop_banjos_house,
    reach_requirements={
        TRANSFORMATION.banjo_kazooie: (LOGIC_ITEM.ability_flap_flip,),
        TRANSFORMATION.termite: (),
        TRANSFORMATION.crocodile: (),
        TRANSFORMATION.walrus: (),
        TRANSFORMATION.pumpkin: (),
        TRANSFORMATION.bee: (),
    },
    default_item=logic_items.EXTRA_LIFE_ITEM,
    keep_as_default=False,
    allowed_item_types=ALLOWED_ITEM_TYPE.complex_objects,
)

SPIRAL_MOUNTAIN_BEHIND_WATERFALL_LOCATION:LOCATION_CLASS = LOCATION_CLASS(
    debug_name="Spiral Mountain Behind Waterfall",
    location_enum=LOCATION.spiral_mountain_behind_waterfall,
    reach_requirements={
        TRANSFORMATION.banjo_kazooie: (
            (
                LOGIC_ITEM.ability_high_jump,
                (
                    (LOGIC_ITEM.ability_feathery_flap,),
                    (LOGIC_ITEM.ability_rat_a_tat_rap,)
                ),
            ),
            (LOGIC_ITEM.ability_talon_trot,),
        ),
        TRANSFORMATION.termite: (),
        TRANSFORMATION.crocodile: (),
        TRANSFORMATION.walrus: (),
        TRANSFORMATION.pumpkin: (),
        TRANSFORMATION.bee: (),
    },
    default_item=logic_items.EXTRA_LIFE_ITEM,
    keep_as_default=False,
    allowed_item_types=ALLOWED_ITEM_TYPE.complex_objects,
)
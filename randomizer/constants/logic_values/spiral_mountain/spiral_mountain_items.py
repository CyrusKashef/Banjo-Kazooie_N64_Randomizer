###################
##### IMPORTS #####
###################

from randomizer.logic.item_class import ITEM_CLASS

from randomizer.constants.int_values.transformation_enums import TRANSFORMATION_ENUMS as TRANSFORMATION
from randomizer.constants.int_values.logic_item_enums import LOGIC_ITEM_ENUMS as LOGIC_ITEM
from randomizer.constants.int_values.item_type_enums import ITEM_TYPE_ENUMS as ITEM_TYPE
from randomizer.constants.int_values.empty_honeycomb_enums import EMPTY_HONEYCOMB_ENUMS as EMPTY_HONEYCOMB

from randomizer.constants.logic_values import logic_items

#############################
##### ABILITY TUTORIALS #####
#############################
# Might not use these if moves are split

JUMP_TUTORIAL_ITEM:ITEM_CLASS = ITEM_CLASS(
    debug_name="Jump Tutorial",
    item_enum=LOGIC_ITEM.spiral_mountain_jump_tutorial,
    obtain_requirements={
        TRANSFORMATION.banjo_kazooie: (),
    },
    item_type=ITEM_TYPE.bottles_molehill,
    item_flag=None
)

ATTACK_TUTORIAL_ITEM:ITEM_CLASS = ITEM_CLASS(
    debug_name="Attack Tutorial",
    item_enum=LOGIC_ITEM.spiral_mountain_attack_tutorial,
    obtain_requirements={
        TRANSFORMATION.banjo_kazooie: (),
    },
    item_type=ITEM_TYPE.bottles_molehill,
    item_flag=None
)



############################
##### EMPTY HONEYCOMBS #####
############################

EMPTY_HONEYCOMB_SM_STUMP_ITEM:ITEM_CLASS = ITEM_CLASS(
    debug_name="Empty Honeycomb Stump",
    item_enum=LOGIC_ITEM.spiral_mountain_empty_honeycomb_stump,
    obtain_requirements={
        TRANSFORMATION.banjo_kazooie: (),
        TRANSFORMATION.termite: (),
        TRANSFORMATION.crocodile: (),
        TRANSFORMATION.walrus: (),
        TRANSFORMATION.pumpkin: (),
        TRANSFORMATION.bee: (),
    },
    item_type=ITEM_TYPE.empty_honeycomb,
    item_flag=EMPTY_HONEYCOMB.spiral_mountain_stump
)

EMPTY_HONEYCOMB_SM_ATOP_TREE_ITEM:ITEM_CLASS = ITEM_CLASS(
    debug_name="Empty Honeycomb Atop Tree",
    item_enum=LOGIC_ITEM.spiral_mountain_empty_honeycomb_atop_tree,
    obtain_requirements={
        TRANSFORMATION.banjo_kazooie: (),
        TRANSFORMATION.termite: (),
        TRANSFORMATION.crocodile: (),
        TRANSFORMATION.walrus: (),
        TRANSFORMATION.pumpkin: (),
        TRANSFORMATION.bee: (),
    },
    item_type=ITEM_TYPE.empty_honeycomb,
    item_flag=EMPTY_HONEYCOMB.spiral_mountain_atop_tree
)

EMPTY_HONEYCOMB_SM_UNDERWATER_ITEM:ITEM_CLASS = ITEM_CLASS(
    debug_name="Empty Honeycomb Underwater",
    item_enum=LOGIC_ITEM.spiral_mountain_empty_honeycomb_underwater,
    obtain_requirements={
        TRANSFORMATION.banjo_kazooie: (),
        TRANSFORMATION.termite: (),
        TRANSFORMATION.crocodile: (),
        TRANSFORMATION.walrus: (),
        TRANSFORMATION.pumpkin: (),
        TRANSFORMATION.bee: (),
    },
    item_type=ITEM_TYPE.empty_honeycomb,
    item_flag=EMPTY_HONEYCOMB.spiral_mountain_underwater
)

EMPTY_HONEYCOMB_SM_WATERFALL_ITEM:ITEM_CLASS = ITEM_CLASS(
    debug_name="Empty Honeycomb Waterfall",
    item_enum=LOGIC_ITEM.spiral_mountain_empty_honeycomb_waterfall,
    obtain_requirements={
        TRANSFORMATION.banjo_kazooie: (),
        TRANSFORMATION.termite: (),
        TRANSFORMATION.crocodile: (),
        TRANSFORMATION.walrus: (),
        TRANSFORMATION.pumpkin: (),
        TRANSFORMATION.bee: (),
    },
    item_type=ITEM_TYPE.empty_honeycomb,
    item_flag=EMPTY_HONEYCOMB.spiral_mountain_waterfall
)

EMPTY_HONEYCOMB_SM_QUARRIES_ITEM:ITEM_CLASS = ITEM_CLASS(
    debug_name="Empty Honeycomb Quarries",
    item_enum=LOGIC_ITEM.spiral_mountain_empty_honeycomb_quarries,
    obtain_requirements={
        TRANSFORMATION.banjo_kazooie: (),
        TRANSFORMATION.termite: (),
        TRANSFORMATION.crocodile: (),
        TRANSFORMATION.walrus: (),
        TRANSFORMATION.pumpkin: (),
        TRANSFORMATION.bee: (),
    },
    item_type=ITEM_TYPE.empty_honeycomb,
    item_flag=EMPTY_HONEYCOMB.spiral_mountain_quarries
)

EMPTY_HONEYCOMB_SM_COLLIWOBBLE_ITEM:ITEM_CLASS = ITEM_CLASS(
    debug_name="Empty Honeycomb Colliwobble",
    item_enum=LOGIC_ITEM.spiral_mountain_empty_honeycomb_colliwobble,
    obtain_requirements={
        TRANSFORMATION.banjo_kazooie: (),
        TRANSFORMATION.termite: (),
        TRANSFORMATION.crocodile: (),
        TRANSFORMATION.walrus: (),
        TRANSFORMATION.pumpkin: (),
        TRANSFORMATION.bee: (),
    },
    item_type=ITEM_TYPE.empty_honeycomb,
    item_flag=EMPTY_HONEYCOMB.spiral_mountain_colliwobble
)

#####################
##### ITEM LIST #####
#####################

SPIRAL_MOUNTAIN_ITEMS:list = [
    # Empty Honeycombs
    EMPTY_HONEYCOMB_SM_STUMP_ITEM,
    EMPTY_HONEYCOMB_SM_ATOP_TREE_ITEM,
    EMPTY_HONEYCOMB_SM_UNDERWATER_ITEM,
    EMPTY_HONEYCOMB_SM_WATERFALL_ITEM,
    EMPTY_HONEYCOMB_SM_QUARRIES_ITEM,
    EMPTY_HONEYCOMB_SM_COLLIWOBBLE_ITEM,
]

# Extra Lives
extra_lives_list:list = [logic_items.EXTRA_LIFE_ITEM] * 2

# Final List
SPIRAL_MOUNTAIN_ITEMS.extend(extra_lives_list)
###################
##### IMPORTS #####
###################

from randomizer.logic.item_class import ITEM_CLASS
from randomizer.constants.int_values.item_type_enums import ITEM_TYPE_ENUMS as ITEM_TYPE
from randomizer.constants.int_values.logic_item_enums import LOGIC_ITEM_ENUMS as LOGIC_ITEM
from randomizer.constants.int_values.transformation_enums import TRANSFORMATION_ENUMS as TRANSFORMATION
from randomizer.constants.int_values.logic_difficulty_enums import LOGIC_DIFFICULTY_ENUMS as DIFFICULTY
from randomizer.constants.int_values.ability_enums import ABILITY_ENUMS as ABILITY

#########################
##### ABILITY ITEMS #####
#########################

ABILITY_BEAK_BARGE_ITEM:ITEM_CLASS = ITEM_CLASS(
    debug_name="Ability Beak Barge",
    item_enum=LOGIC_ITEM.ability_beak_barge,
    obtain_requirements={
        TRANSFORMATION.banjo_kazooie: [],
    },
    item_type=ITEM_TYPE.bottles_molehill,
    item_flag=ABILITY.beak_barge
)

ABILITY_BEAK_BOMB_ITEM:ITEM_CLASS = ITEM_CLASS(
    debug_name="Ability Beak Bomb",
    item_enum=LOGIC_ITEM.ability_beak_bomb,
    obtain_requirements={
        TRANSFORMATION.banjo_kazooie: [],
    },
    item_type=ITEM_TYPE.bottles_molehill,
    item_flag=ABILITY.beak_bomb
)

ABILITY_BEAK_BUSTER_ITEM:ITEM_CLASS = ITEM_CLASS(
    debug_name="Ability Beak Buster",
    item_enum=LOGIC_ITEM.ability_beak_buster,
    obtain_requirements={
        TRANSFORMATION.banjo_kazooie: [],
    },
    item_type=ITEM_TYPE.bottles_molehill,
    item_flag=ABILITY.beak_buster
)

ABILITY_CLAW_SWIPE_ITEM:ITEM_CLASS = ITEM_CLASS(
    debug_name="Ability Claw Swipe",
    item_enum=LOGIC_ITEM.ability_claw_swipe,
    obtain_requirements={
        TRANSFORMATION.banjo_kazooie: [],
    },
    item_type=ITEM_TYPE.bottles_molehill,
    item_flag=ABILITY.claw_swipe
)

ABILITY_CLIMB_ITEM:ITEM_CLASS = ITEM_CLASS(
    debug_name="Ability Climb",
    item_enum=LOGIC_ITEM.ability_climb,
    obtain_requirements={
        TRANSFORMATION.banjo_kazooie: [],
    },
    item_type=ITEM_TYPE.bottles_molehill,
    item_flag=ABILITY.climb
)

ABILITY_EGG_FIRING_ITEM:ITEM_CLASS = ITEM_CLASS(
    debug_name="Ability Egg Firing",
    item_enum=LOGIC_ITEM.ability_egg_firing,
    obtain_requirements={
        TRANSFORMATION.banjo_kazooie: [],
    },
    item_type=ITEM_TYPE.bottles_molehill,
    item_flag=ABILITY.egg_firing
)

ABILITY_FEATHERY_FLAP_ITEM:ITEM_CLASS = ITEM_CLASS(
    debug_name="Ability Feathery Flap",
    item_enum=LOGIC_ITEM.ability_feathery_flap,
    obtain_requirements={
        TRANSFORMATION.banjo_kazooie: [],
    },
    item_type=ITEM_TYPE.bottles_molehill,
    item_flag=ABILITY.feathery_flap
)

ABILITY_FLAP_FLIP_ITEM:ITEM_CLASS = ITEM_CLASS(
    debug_name="Ability Flap Flip",
    item_enum=LOGIC_ITEM.ability_flap_flip,
    obtain_requirements={
        TRANSFORMATION.banjo_kazooie: [],
    },
    item_type=ITEM_TYPE.bottles_molehill,
    item_flag=ABILITY.flap_flip
)

ABILITY_FLIGHT_ITEM:ITEM_CLASS = ITEM_CLASS(
    debug_name="Ability Flight",
    item_enum=LOGIC_ITEM.ability_flight,
    obtain_requirements={
        TRANSFORMATION.banjo_kazooie: [],
    },
    item_type=ITEM_TYPE.bottles_molehill,
    item_flag=ABILITY.flight
)

ABILITY_HIGH_JUMP_ITEM:ITEM_CLASS = ITEM_CLASS(
    debug_name="Ability High Jump",
    item_enum=LOGIC_ITEM.ability_high_jump,
    obtain_requirements={
        TRANSFORMATION.banjo_kazooie: [],
    },
    item_type=ITEM_TYPE.bottles_molehill,
    item_flag=ABILITY.high_jump
)

ABILITY_RAT_A_TAT_RAP_ITEM:ITEM_CLASS = ITEM_CLASS(
    debug_name="Ability Rat-A-Tat Rap",
    item_enum=LOGIC_ITEM.ability_rat_a_tat_rap,
    obtain_requirements={
        TRANSFORMATION.banjo_kazooie: [],
    },
    item_type=ITEM_TYPE.bottles_molehill,
    item_flag=ABILITY.rat_a_tat_rap
)

ABILITY_ROLL_ITEM:ITEM_CLASS = ITEM_CLASS(
    debug_name="Ability Roll",
    item_enum=LOGIC_ITEM.ability_roll,
    obtain_requirements={
        TRANSFORMATION.banjo_kazooie: [],
    },
    item_type=ITEM_TYPE.bottles_molehill,
    item_flag=ABILITY.roll
)

ABILITY_SHOCK_JUMP_ITEM:ITEM_CLASS = ITEM_CLASS(
    debug_name="Ability Shock Jump",
    item_enum=LOGIC_ITEM.ability_shock_jump,
    obtain_requirements={
        TRANSFORMATION.banjo_kazooie: [],
    },
    item_type=ITEM_TYPE.bottles_molehill,
    item_flag=ABILITY.shock_jump
)

ABILITY_STILT_STRIDE_ITEM:ITEM_CLASS = ITEM_CLASS(
    debug_name="Ability Stilt Stride",
    item_enum=LOGIC_ITEM.ability_stilt_stride,
    obtain_requirements={
        TRANSFORMATION.banjo_kazooie: [],
    },
    item_type=ITEM_TYPE.bottles_molehill,
    item_flag=ABILITY.stilt_stride
)

ABILITY_DIVE_ITEM:ITEM_CLASS = ITEM_CLASS(
    debug_name="Ability Dive",
    item_enum=LOGIC_ITEM.ability_dive,
    obtain_requirements={
        TRANSFORMATION.banjo_kazooie: [],
    },
    item_type=ITEM_TYPE.bottles_molehill,
    item_flag=ABILITY.dive
)

ABILITY_TALON_TROT_ITEM:ITEM_CLASS = ITEM_CLASS(
    debug_name="Ability Talon Trot",
    item_enum=LOGIC_ITEM.ability_talon_trot,
    obtain_requirements={
        TRANSFORMATION.banjo_kazooie: [],
    },
    item_type=ITEM_TYPE.bottles_molehill,
    item_flag=ABILITY.talon_trot
)

ABILITY_TURBO_TALON_TROT_ITEM:ITEM_CLASS = ITEM_CLASS(
    debug_name="Ability Turbo Talon Trot",
    item_enum=LOGIC_ITEM.ability_turbo_talon_trot,
    obtain_requirements={
        TRANSFORMATION.banjo_kazooie: [],
    },
    item_type=ITEM_TYPE.bottles_molehill,
    item_flag=ABILITY.turbo_talon_trot
)

ABILITY_WONDERWING_ITEM:ITEM_CLASS = ITEM_CLASS(
    debug_name="Ability Wonderwing",
    item_enum=LOGIC_ITEM.ability_wonderwing,
    obtain_requirements={
        TRANSFORMATION.banjo_kazooie: [],
    },
    item_type=ITEM_TYPE.bottles_molehill,
    item_flag=ABILITY.wonderwing
)

ABILITY_NOTE_DOOR_ITEM:ITEM_CLASS = ITEM_CLASS(
    debug_name="Ability Note Door",
    item_enum=LOGIC_ITEM.ability_note_door,
    obtain_requirements={
        TRANSFORMATION.banjo_kazooie: [],
    },
    item_type=ITEM_TYPE.bottles_molehill,
    item_flag=ABILITY.note_door
)

##############################
##### ABILITY ITEMS LIST #####
##############################

ABILITY_ITEMS_LIST:list = [
    ABILITY_BEAK_BARGE_ITEM,
    ABILITY_BEAK_BOMB_ITEM,
    ABILITY_BEAK_BUSTER_ITEM,
    ABILITY_CLAW_SWIPE_ITEM,
    ABILITY_CLIMB_ITEM,
    ABILITY_EGG_FIRING_ITEM,
    ABILITY_FEATHERY_FLAP_ITEM,
    ABILITY_FLAP_FLIP_ITEM,
    ABILITY_FLIGHT_ITEM,
    ABILITY_HIGH_JUMP_ITEM,
    ABILITY_RAT_A_TAT_RAP_ITEM,
    ABILITY_ROLL_ITEM,
    ABILITY_SHOCK_JUMP_ITEM,
    ABILITY_STILT_STRIDE_ITEM,
    ABILITY_DIVE_ITEM,
    ABILITY_TALON_TROT_ITEM,
    ABILITY_TURBO_TALON_TROT_ITEM,
    ABILITY_WONDERWING_ITEM,
]

##########################
##### NON ENUM ITEMS #####
##########################

BLUE_EGG_ITEM = ITEM_CLASS(
    debug_name="Blue Egg",
    item_enum=None,
    obtain_requirements={
        TRANSFORMATION.banjo_kazooie: [],
        TRANSFORMATION.termite: [],
        TRANSFORMATION.crocodile: [],
        TRANSFORMATION.walrus: [],
        TRANSFORMATION.pumpkin: [],
        TRANSFORMATION.bee: [],
    },
    item_type=ITEM_TYPE.blue_egg,
    item_flag=None
)

RED_FEATHER_ITEM = ITEM_CLASS(
    debug_name="Red Feathers",
    item_enum=None,
    obtain_requirements={
        TRANSFORMATION.banjo_kazooie: [],
        TRANSFORMATION.termite: [],
        TRANSFORMATION.crocodile: [],
        TRANSFORMATION.walrus: [],
        TRANSFORMATION.pumpkin: [],
        TRANSFORMATION.bee: [],
    },
    item_type=ITEM_TYPE.red_feather,
    item_flag=None
)

GOLD_FEATHER_ITEM = ITEM_CLASS(
    debug_name="Gold Feathers",
    item_enum=None,
    obtain_requirements={
        TRANSFORMATION.banjo_kazooie: [],
        TRANSFORMATION.termite: [],
        TRANSFORMATION.crocodile: [],
        TRANSFORMATION.walrus: [],
        TRANSFORMATION.pumpkin: [],
        TRANSFORMATION.bee: [],
    },
    item_type=ITEM_TYPE.gold_feather,
    item_flag=None
)

EXTRA_LIFE_ITEM = ITEM_CLASS(
    debug_name="Extra Life",
    item_enum=None,
    obtain_requirements={
        TRANSFORMATION.banjo_kazooie: [],
        TRANSFORMATION.termite: [],
        TRANSFORMATION.crocodile: [],
        TRANSFORMATION.walrus: [],
        TRANSFORMATION.pumpkin: [],
        TRANSFORMATION.bee: [],
    },
    item_type=ITEM_TYPE.extra_life,
    item_flag=None
)
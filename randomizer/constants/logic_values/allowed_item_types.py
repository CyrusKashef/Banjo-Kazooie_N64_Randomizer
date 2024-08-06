###################
##### IMPORTS #####
###################

from enum import Enum

from randomizer.constants.int_values.item_type_enums import ITEM_TYPE_ENUMS as ITEM_TYPE

##############################
##### ALLOWED ITEM TYPES #####
##############################

class ALLOWED_ITEM_TYPE(Enum):
    # Only One Type
    jiggy_only = [
        ITEM_TYPE.jiggy]
    empty_honeycomb_only = [
        ITEM_TYPE.empty_honeycomb]
    mumbo_token_only = [
        ITEM_TYPE.mumbo_token]
    # Multiple Types
    simple_objects = [
        ITEM_TYPE.musical_note,
        ITEM_TYPE.blue_egg,
        ITEM_TYPE.red_feather,
        ITEM_TYPE.gold_feather]
    complex_objects = [
        ITEM_TYPE.jiggy,
        ITEM_TYPE.empty_honeycomb,
        ITEM_TYPE.mumbo_token,
        ITEM_TYPE.jinjo,
        ITEM_TYPE.bottles_molehill,
        ITEM_TYPE.extra_life,
        ITEM_TYPE.chimpys_orange,
        ITEM_TYPE.blubbers_gold,
        ITEM_TYPE.red_present,
        ITEM_TYPE.blue_present,
        ITEM_TYPE.green_present,
        ITEM_TYPE.flower_pot,
        ITEM_TYPE.nubnuts_acorn,
        ITEM_TYPE.eyries_caterpillar]
    floating_complex_objects = [
        ITEM_TYPE.jiggy,
        ITEM_TYPE.empty_honeycomb,
        ITEM_TYPE.mumbo_token,
        ITEM_TYPE.jinjo,
        ITEM_TYPE.extra_life,
        ITEM_TYPE.chimpys_orange,
        ITEM_TYPE.blubbers_gold,
        ITEM_TYPE.red_present,
        ITEM_TYPE.blue_present,
        ITEM_TYPE.green_present,
        ITEM_TYPE.nubnuts_acorn]

if __name__ == '__main__':
    for item in ALLOWED_ITEM_TYPE:
        print(item.get_value())
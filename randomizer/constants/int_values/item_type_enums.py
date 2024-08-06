'''
Enumerators from the following class are arbitrary values used to make each instance unique.

The items in the class are sorted by importance for placing.
Static item types are placed at the bottom.
'''

###################
##### IMPORTS #####
###################

from enum import IntEnum, auto

###########################
##### ITEM TYPE ENUMS #####
###########################

class ITEM_TYPE_ENUMS(IntEnum):
    #####################
    ### Complex Items ###
    #####################
    # Soft Lock Potential
    bottles_molehill = auto()
    jiggy = auto()
    # Used To Acquire Access
    mumbo_token = auto()
    # Used To Acquire Jiggies
    jinjo = auto()
    chimpys_orange = auto()
    blubbers_gold = auto()
    red_present = auto()
    blue_present = auto()
    green_present = auto()
    flower_pot = auto()
    nubnuts_acorn = auto()
    eyries_caterpillar = auto()
    # Good To Have
    empty_honeycomb = auto()
    # Other Complex Items
    extra_life = auto()
    ####################
    ### Simple Items ###
    ####################
    # Soft Lock Potential Simple Items
    musical_note = auto()
    # Other Simple Items
    blue_egg = auto()
    red_feather = auto()
    gold_feather = auto()
    ####################
    ### Static Items ###
    ####################
    event = auto()
    switch = auto()
    flight_pad = auto()
    treasure_hunt_x = auto()
    transformation = auto()
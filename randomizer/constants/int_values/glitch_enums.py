'''
Enumerators from the following class are arbitrary values used to make each instance unique.

Glitch Explanations:
* Simple Slope Abuse:
  - Easy jumping, rolling, or button mashing to climb slope
* Beak Buster iFrames:
  - Using Beak Buster to avoid damage from height or an attack
* Beak Bomb Grabba:
  - Using Beak Bomb to obtain Grabba's Jiggy
* Prolonged Slope Abuse:
  - Slope abusing along a ledge to get to a certain location
* Tickers Tower Termiteless:
  - Slope abusing up Ticker's Tower
* Mumbos Mountain Witch Switch Termiteless:
  - Slope abusing up Mumbo's Mountain's entrance
* Engine Room iFrame Abuse:
  - Hitting the Engine Room blades to take damage and using iFrames to pass through
* Treehouse Hitbox Extend:
  - Using Egg Firing to extend the player's hitbox to collect the item in the Treehouse
* Sarchophagus Hitbox Extend:
  - Using Egg Firing or Roll to extend the player's hitbox to collect the item in the Sarchophagus
* Clankers Cavern Blades Gold Feather-less:
  - Navigating through Clanker's blades in the Wonderwing Room without Gold Feathers or taking damage
* Wozzas Cave Backside As Banjo:
  - Quick Diving to the back of Wozza's Cave to collect any items in the back
* Lighthouse Early:
  - Slope abusing up the mountain to get to the lighthouse without flight
* Jinxy Clip:
  - Using Talon Trot at the edge of Jinxy to clip inside
* Reverse Bee Adventure:
  - Escaping Detransformation areas as the Bee and using the transformation to grab items
'''

###################
##### IMPORTS #####
###################

from enum import IntEnum, auto

########################
##### GLITCH ENUMS #####
########################

class GLITCH_ENUMS(IntEnum):
    # Casual
    simple_slope_abuse = auto()
    beak_buster_iframes = auto()
    beak_bomb_grabba = auto()
    # Intermediate
    prolonged_slope_abuse = auto()
    tickers_tower_termiteless = auto()
    mumbos_mountain_witch_switch_termiteless = auto()
    engine_room_iframe_abuse = auto()
    treehouse_hitbox_extend = auto()
    sarchophagus_hitbox_extend = auto()
    clankers_cavern_blades_gold_featherless = auto()
    wozzas_cave_backside_as_banjo = auto()
    # Expert
    lighthouse_early = auto()
    jinxy_clip = auto()
    reverse_bee_adventure = auto()
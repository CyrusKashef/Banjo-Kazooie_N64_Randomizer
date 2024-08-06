###################
##### IMPORTS #####
###################

from randomizer.logic.event_class import EVENT_CLASS
from randomizer.constants.int_values.item_type_enums import ITEM_TYPE_ENUMS as ITEM_TYPE
from randomizer.constants.int_values.logic_item_enums import LOGIC_ITEM_ENUMS as LOGIC_ITEM
from randomizer.constants.int_values.transformation_enums import TRANSFORMATION_ENUMS as TRANSFORMATION
from randomizer.constants.int_values.logic_difficulty_enums import LOGIC_DIFFICULTY_ENUMS as DIFFICULTY
from randomizer.constants.int_values.ability_enums import ABILITY_ENUMS as ABILITY
from randomizer.constants.int_values.empty_honeycomb_enums import EMPTY_HONEYCOMB_ENUMS as EMPTY_HONEYCOMB

######################
##### EVENT LIST #####
######################

EVENT_LIST:list = {
    # Spiral Mountain
    LOGIC_ITEM.spiral_mountain_jump_tutorial: EVENT_CLASS(
        debug_name="Jump Tutorial",
        event_enum=LOGIC_ITEM.spiral_mountain_jump_tutorial,
        event_requirements=[],
        event_unlock_list=[
            LOGIC_ITEM.ability_high_jump,
            LOGIC_ITEM.ability_feathery_flap,
            LOGIC_ITEM.ability_flap_flip],
    ),
    LOGIC_ITEM.spiral_mountain_attack_tutorial: EVENT_CLASS(
        debug_name="Attack Tutorial",
        event_enum=LOGIC_ITEM.spiral_mountain_attack_tutorial,
        event_requirements=[],
        event_unlock_list=[
            LOGIC_ITEM.ability_claw_swipe,
            LOGIC_ITEM.ability_roll,
            LOGIC_ITEM.ability_rat_a_tat_rap],
    )
}

# SPIRAL_MOUNTAIN_BRIDGE_COMPLETE_EVENT = None

# Mumbos Mountain

# MUMBOS_MOUNTAIN_COLLECT_JINJOS_EVENT = None
# MUMBOS_MOUNTAIN_DESTROY_HUTS_EVENT = None

# Treasure Trove Cove

# TREASURE_TROVE_COVE_COLLECT_JINJOS_EVENT = None
# TREASURE_TROVE_COVE_PATCH_LEAKY_EVENT = None

# Clankers Cavern

# CLANKERS_CAVERN_COLLECT_JINJOS_EVENT = None
# CLANKERS_CAVERN_RAISE_CLANKER_EVENT = None

# Bubblegloop Swamp

# BUBBLEGLOOP_SWAMP_COLLECT_JINJOS_EVENT = None
# BUBBLEGLOOP_SWAMP_BREAK_HUTS_EVENT = None

# Freezeezy Peak

# FREEZEEZY_PEAK_COLLECT_JINJOS_EVENT = None
# FREEZEEZY_PEAK_ESCORT_TWINKLIES_EVENT = None

# Gobis Valley

# GOBIS_VALLEY_COLLECT_JINJOS_EVENT = None
# GOBIS_VALLEY_DEFEAT_GRABBA_EVENT = None
# GOBIS_VALLEY_OPEN_JINXY_EVENT = None
# GOBIS_VALLEY_RAISE_KING_SANDYBUTTS_PYRAMID_EVENT = None

# Mad Monster Mansion

# MAD_MONSTER_MANSION_COLLECT_JINJOS_EVENT = None
# MAD_MONSTER_MANSION_FILL_FLOWER_POTS_EVENT = None

# Rusty Bucket Bay

# RUSTY_BUCKET_BAY_FLIGHT_PAD_BOAT_ROOM_EVENT = None

# Click Clock Wood

# CLICK_CLOCK_WOOD_COLLECT_JINJOS_EVENT = None
# CLICK_CLOCK_WOOD_SPRING_HATCH_EYRIE_EVENT = None
# CLICK_CLOCK_WOOD_SUMMER_FEED_EYRIE_EVENT = None
# CLICK_CLOCK_WOOD_AUTUMN_FEED_EYRIE_EVENT = None
# CLICK_CLOCK_WOOD_SUMMER_UNBLOCK_GNAWTY_EVENT = None

# Gruntildas Lair

# GRUNTILDAS_LAIR_OPEN_FIRST_WORLD_EVENT = None
# GRUNTILDAS_LAIR_OPEN_SECOND_WORLD_EVENT = None
# GRUNTILDAS_LAIR_OPEN_THIRD_WORLD_EVENT = None
# GRUNTILDAS_LAIR_OPEN_FOURTH_WORLD_EVENT = None
# GRUNTILDAS_LAIR_OPEN_FIFTH_WORLD_EVENT = None
# GRUNTILDAS_LAIR_OPEN_SIXTH_WORLD_EVENT = None
# GRUNTILDAS_LAIR_OPEN_SEVENTH_WORLD_EVENT = None
# GRUNTILDAS_LAIR_OPEN_EIGHTH_WORLD_EVENT = None
# GRUNTILDAS_LAIR_OPEN_NINTH_WORLD_EVENT = None
# GRUNTILDAS_LAIR_OPEN_FINAL_BATTLE_EVENT = None
# GRUNTILDAS_LAIR_OPEN_FIRST_NOTE_DOOR_EVENT = None
# GRUNTILDAS_LAIR_OPEN_SECOND_NOTE_DOOR_EVENT = None
# GRUNTILDAS_LAIR_OPEN_THIRD_NOTE_DOOR_EVENT = None
# GRUNTILDAS_LAIR_OPEN_FOURTH_NOTE_DOOR_EVENT = None
# GRUNTILDAS_LAIR_OPEN_FIFTH_NOTE_DOOR_EVENT = None
# GRUNTILDAS_LAIR_OPEN_SIXTH_NOTE_DOOR_EVENT = None
# GRUNTILDAS_LAIR_OPEN_SEVENTH_NOTE_DOOR_EVENT = None
# GRUNTILDAS_LAIR_OPEN_EIGHTH_NOTE_DOOR_EVENT = None
# GRUNTILDAS_LAIR_OPEN_NINTH_NOTE_DOOR_EVENT = None
# GRUNTILDAS_LAIR_OPEN_TENTH_NOTE_DOOR_EVENT = None
# GRUNTILDAS_LAIR_OPEN_ELEVENTH_NOTE_DOOR_EVENT = None
# GRUNTILDAS_LAIR_OPEN_TWELFTH_NOTE_DOOR_EVENT = None
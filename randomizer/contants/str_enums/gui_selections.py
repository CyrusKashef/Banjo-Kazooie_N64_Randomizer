'''
Purpose:
*
'''

###################
##### IMPORTS #####
###################

from enum import StrEnum, unique

##########################
##### ASSET ID ENUMS #####
##########################

@unique
class GUI_SELECTIONS(StrEnum):
    original_rom_path = "Original ROM Path"
    new_rom_path = "New ROM Path"
    # Quality Of Life
    boot_to_file_select = "Boot To File Select"
    skippable_cutscenes = "Skippable Cutscenes"
    skip_jiggy_jig = "Skip Jiggy Jig"
    # Difficulty
    starting_blue_egg_count = "Starting Blue Egg Count"
    starting_red_feather_count = "Starting Red Feather Count"
    starting_gold_feather_count = "Starting Gold Feather Count"
    starting_mumbo_token_count = "Starting Mumbo Token Count"
    enable_fallproof = "Enable Fallproof"
    # Logic
    select_starting_moves = "Select Starting Moves"
    beak_barge = "Beak Barge"
    beak_bomb = "Beak Bomb"
    beak_buster = "Beak Buster"
    claw_swipe = "Claw Swipe"
    climb = "Climb"
    egg_firing = "Egg Firing"
    feather_flap = "Feathery Flap"
    flap_flip = "Flap Flip"
    flight = "Flight"
    high_jump = "High Jump"
    rat_a_tap_rap = "Rat-A-Tap Rap"
    roll_attack = "Roll Attack"
    shock_jump = "Shock Jump"
    stilt_stride = "Stilt Stride"
    dive = "Dive"
    talon_trot = "Talon Trot"
    turbo_talon_trot = "Turbo Talon Trot"
    wonderwing = "Wonderwing"
    open_note_door = "Open Note Door"
    shock_jump_pad_anywhere = "Shock Jump Pad Anywhere"
    alternate_win_condition = "Alternate Win Condition"
    # NOTE DOORS
    note_door_50_cost = "Note Door 50 Cost"
    note_door_180_cost = "Note Door 180 Cost"
    note_door_260_cost = "Note Door 260 Cost"
    note_door_350_cost = "Note Door 350 Cost"
    note_door_450_cost = "Note Door 450 Cost"
    note_door_640_cost = "Note Door 640 Cost"
    note_door_765_cost = "Note Door 765 Cost"
    note_door_810_cost = "Note Door 810 Cost"
    note_door_828_cost = "Note Door 828 Cost"
    note_door_846_cost = "Note Door 846 Cost"
    note_door_864_cost = "Note Door 864 Cost"
    note_door_882_cost = "Note Door 882 Cost"
    # JIGSAW PUZZLES
    jigsaw_puzzle_1_cost = "Jigsaw Puzzle 1 Cost"
    jigsaw_puzzle_2_cost = "Jigsaw Puzzle 2 Cost"
    jigsaw_puzzle_3_cost = "Jigsaw Puzzle 3 Cost"
    jigsaw_puzzle_4_cost = "Jigsaw Puzzle 4 Cost"
    jigsaw_puzzle_5_cost = "Jigsaw Puzzle 5 Cost"
    jigsaw_puzzle_6_cost = "Jigsaw Puzzle 6 Cost"
    jigsaw_puzzle_7_cost = "Jigsaw Puzzle 7 Cost"
    jigsaw_puzzle_8_cost = "Jigsaw Puzzle 8 Cost"
    jigsaw_puzzle_9_cost = "Jigsaw Puzzle 9 Cost"
    jigsaw_puzzle_10_cost = "Jigsaw Puzzle 10 Cost"
    jigsaw_puzzle_11_cost = "Jigsaw Puzzle 11 Cost"
    # COSMETICS & SOUNDS
    low_poly_model = "Low Poly Model"
    high_poly_model = "High Poly Model"
'''
Purpose:
* Class of custom enumerators for the complex object actor ids
'''

###################
##### IMPORTS #####
###################

from randomizer.contants.str_enums.level_name_constants import LEVEL_NAME_ENUMS

#####################
##### CONSTANTS #####
#####################

UNKNOWN_STR:str = "UNKNOWN"

JIGGY_FLAG_STR:str = "Jiggy Flag"
EMPTY_HONEYCOMB_FLAG_STR:str = "Empty Honeycomb Flag"
MUMBO_TOKEN_FLAG_STR:str = "Mumbo Token Flag"

###############################
##### COMPLEX OBJECT DICT #####
###############################

COMPLEX_OBJECT_CATEGORY_DICT:dict = {
    0b000000: {
        0x0000: {
            0b000000000: UNKNOWN_STR,
            0b000000001: UNKNOWN_STR,
            0b000000010: UNKNOWN_STR,
            0b000000011: UNKNOWN_STR,
            0b000000110: UNKNOWN_STR,
            0b000000111: UNKNOWN_STR,
            0b000001000: UNKNOWN_STR,
            0b000001010: UNKNOWN_STR,
            0b000001101: UNKNOWN_STR,
            0b000001110: UNKNOWN_STR,
            0b000110010: UNKNOWN_STR,
            0b010001011: UNKNOWN_STR,
            0b101000000: UNKNOWN_STR,
            0b101010010: UNKNOWN_STR,
            0b101010111: UNKNOWN_STR,
            0b101011010: UNKNOWN_STR,
            0b101011100: UNKNOWN_STR,
            0b101011110: UNKNOWN_STR,
            0b101100000: UNKNOWN_STR,
            0b101100001: UNKNOWN_STR,
            0b101100011: UNKNOWN_STR,
        },
        0x0040: {
            0b000000000: UNKNOWN_STR,
        },
        0x0280: {
            0b000000000: UNKNOWN_STR,
        },
        0x0380: {
            0b000000000: UNKNOWN_STR,
        },
        0x09C0: {
            0b000000000: UNKNOWN_STR,
        },
        0x1840: {
            0b000000000: UNKNOWN_STR,
        },
        0x1F00: {
            0b000000000: UNKNOWN_STR,
        },
        0x1F40: {
            0b000000000: UNKNOWN_STR,
        },
        0x2200: {
            0b000000000: UNKNOWN_STR,
        },
        0x2300: {
            0b000000000: UNKNOWN_STR,
        },
        0x25C0: {
            0b000000000: UNKNOWN_STR,
            0b000001100: UNKNOWN_STR,
        },
        0x26C0: {
            0b000000000: UNKNOWN_STR,
        },
        0x2840: {
            0b000000000: UNKNOWN_STR,
        },
        0x2A00: {
            0b000000000: UNKNOWN_STR,
        },
        0x2FC1: {
            0b000000000: UNKNOWN_STR,
        },
        0x35C0: {
            0b000000000: UNKNOWN_STR,
        },
        0x3840: {
            0b000000000: UNKNOWN_STR,
        },
        0x7F0E: {
            0b100000001: UNKNOWN_STR,
        },
        0x8000: {
            0b100000000: UNKNOWN_STR,
        },
    },
    0b000010: {
        0x0280: {
            0b000000000: UNKNOWN_STR,
        },
        0x0D01: {
            0b000000000: UNKNOWN_STR,
        },
        0x1F81: {
            0b000000000: UNKNOWN_STR,
        },
        0x20C3: {
            0b000000000: UNKNOWN_STR,
        },
        0x2100: {
            0b000000000: UNKNOWN_STR,
        },
        0x21C0: {
            0b000000000: UNKNOWN_STR,
        },
        0x22C2: {
            0b000000000: UNKNOWN_STR,
        },
        0x24C0: {
            0b101011110: UNKNOWN_STR,
        },
        0x2580: {
            0b000000000: UNKNOWN_STR,
        },
        0x2800: {
            0b000000000: UNKNOWN_STR,
        },
        0x29C0: {
            0b000000000: UNKNOWN_STR,
        },
        0x2A80: {
            0b000000000: UNKNOWN_STR,
        },
        0x2C41: {
            0b000000000: UNKNOWN_STR,
        },
        0x2CC0: {
            0b000000000: UNKNOWN_STR,
        },
        0x2D80: {
            0b000000000: UNKNOWN_STR,
        },
        0x3200: {
            0b000000000: UNKNOWN_STR,
        },
        0x3300: {
            0b000000000: UNKNOWN_STR,
        },
        0x3583: {
            0b000000000: UNKNOWN_STR,
        },
        0x3600: {
            0b000000000: UNKNOWN_STR,
        },
        0x38C1: {
            0b000000000: UNKNOWN_STR,
        },
        0x3930: {
            0b000000000: UNKNOWN_STR,
        },
        0x3A40: {
            0b000000000: UNKNOWN_STR,
        },
        0x3AC0: {
            0b000000000: UNKNOWN_STR,
        },
        0x3B01: {
            0b000000000: UNKNOWN_STR,
        },
        0x3B80: {
            0b000000000: UNKNOWN_STR,
        },
        0x3CC0: {
            0b000000000: UNKNOWN_STR,
        },
        0x8000: {
            0b100000000: UNKNOWN_STR,
        },
    },
    0b000011: "Warp",
    0b000100: {
        0x0000: {
            0b000000000: UNKNOWN_STR,
            0b111110100: UNKNOWN_STR,
        },
        0x0016: {
            0b000111011: UNKNOWN_STR,
            0b001001011: UNKNOWN_STR,
            0b001010010: UNKNOWN_STR,
            0b001010011: UNKNOWN_STR,
            0b001011000: UNKNOWN_STR,
            0b001100000: UNKNOWN_STR,
            0b001110100: UNKNOWN_STR,
            0b001111011: UNKNOWN_STR,
            0b001111110: UNKNOWN_STR,
            0b010000000: UNKNOWN_STR,
            0b010000111: UNKNOWN_STR,
            0b010001010: UNKNOWN_STR,
            0b010010110: UNKNOWN_STR,
            0b010011100: UNKNOWN_STR,
            0b010011101: UNKNOWN_STR,
            0b010100000: UNKNOWN_STR,
            0b010101010: UNKNOWN_STR,
            0b010101011: UNKNOWN_STR,
            0b010101100: UNKNOWN_STR,
            0b010101110: UNKNOWN_STR,
            0b010101111: UNKNOWN_STR,
            0b010110000: UNKNOWN_STR,
            0b010110001: UNKNOWN_STR,
            0b010110100: UNKNOWN_STR,
            0b010111101: UNKNOWN_STR,
            0b010111110: UNKNOWN_STR,
            0b011000001: UNKNOWN_STR,
            0b011001000: UNKNOWN_STR,
            0b011001010: UNKNOWN_STR,
            0b011010000: UNKNOWN_STR,
            0b011010110: UNKNOWN_STR,
            0b011011111: UNKNOWN_STR,
            0b011100001: UNKNOWN_STR,
            0b011100010: UNKNOWN_STR,
            0b011100110: UNKNOWN_STR,
            0b011101001: UNKNOWN_STR,
            0b011101011: UNKNOWN_STR,
            0b011101100: UNKNOWN_STR,
            0b011111000: UNKNOWN_STR,
            0b011111010: UNKNOWN_STR,
            0b011111101: UNKNOWN_STR,
            0b011111111: UNKNOWN_STR,
            0b100010010: UNKNOWN_STR,
            0b100010110: UNKNOWN_STR,
            0b100011000: UNKNOWN_STR,
            0b100011110: UNKNOWN_STR,
            0b100100000: UNKNOWN_STR,
            0b100101100: UNKNOWN_STR,
            0b101010100: UNKNOWN_STR,
            0b110010000: UNKNOWN_STR,
            0b110010101: UNKNOWN_STR,
            0b110100000: UNKNOWN_STR,
            0b110100110: UNKNOWN_STR,
            0b110111100: UNKNOWN_STR,
            0b111001001: UNKNOWN_STR,
            0b111001100: UNKNOWN_STR,
            0b111110100: UNKNOWN_STR,
        },
        0x0017: {
            0b001011001: UNKNOWN_STR,
            0b001011010: UNKNOWN_STR,
            0b001101111: UNKNOWN_STR,
            0b001110110: UNKNOWN_STR,
            0b001110111: UNKNOWN_STR,
            0b001111000: UNKNOWN_STR,
            0b001111101: UNKNOWN_STR,
            0b010001110: UNKNOWN_STR,
            0b010010100: UNKNOWN_STR,
            0b010010110: UNKNOWN_STR,
            0b010011011: UNKNOWN_STR,
            0b010011110: UNKNOWN_STR,
            0b010100001: UNKNOWN_STR,
            0b010100111: UNKNOWN_STR,
            0b010101010: UNKNOWN_STR,
            0b010101111: UNKNOWN_STR,
            0b010110011: UNKNOWN_STR,
            0b011000011: UNKNOWN_STR,
            0b011001000: UNKNOWN_STR,
            0b011010101: UNKNOWN_STR,
            0b011011011: UNKNOWN_STR,
            0b011011100: UNKNOWN_STR,
            0b011011111: UNKNOWN_STR,
            0b011100001: UNKNOWN_STR,
            0b011101001: UNKNOWN_STR,
            0b011101011: UNKNOWN_STR,
            0b011101110: UNKNOWN_STR,
            0b011110000: UNKNOWN_STR,
            0b011111010: UNKNOWN_STR,
            0b011111101: UNKNOWN_STR,
            0b100101100: UNKNOWN_STR,
            0b100111011: UNKNOWN_STR,
            0b101101110: UNKNOWN_STR,
            0b110000001: UNKNOWN_STR,
            0b111010111: UNKNOWN_STR,
            0b111110100: UNKNOWN_STR,
        },
        0x0018: {
            0b001010100: UNKNOWN_STR,
            0b001010101: UNKNOWN_STR,
            0b001011010: UNKNOWN_STR,
            0b001111001: UNKNOWN_STR,
            0b001111110: UNKNOWN_STR,
            0b010010110: UNKNOWN_STR,
            0b010011011: UNKNOWN_STR,
            0b010100101: UNKNOWN_STR,
            0b010111111: UNKNOWN_STR,
            0b011001000: UNKNOWN_STR,
            0b011001001: UNKNOWN_STR,
            0b011001101: UNKNOWN_STR,
            0b011011110: UNKNOWN_STR,
            0b011100001: UNKNOWN_STR,
            0b011110000: UNKNOWN_STR,
            0b011111010: UNKNOWN_STR,
            0b101011110: UNKNOWN_STR,
        },
        0x0019: {
            0b001000001: UNKNOWN_STR,
            0b001111101: UNKNOWN_STR,
            0b011001000: UNKNOWN_STR,
            0b011001010: UNKNOWN_STR,
            0b011100001: UNKNOWN_STR,
            0b011101000: UNKNOWN_STR,
            0b011111010: UNKNOWN_STR,
        },
        0x001A: {
            0b001001100: UNKNOWN_STR,
            0b001010111: UNKNOWN_STR,
            0b001100100: UNKNOWN_STR,
            0b011000100: UNKNOWN_STR,
            0b011001000: UNKNOWN_STR,
            0b011111010: UNKNOWN_STR,
        },
        0x001B: {
            0b001010101: UNKNOWN_STR,
            0b001110000: UNKNOWN_STR,
        },
        0x001C: {
            0b001011010: UNKNOWN_STR,
            0b001111000: UNKNOWN_STR,
        },
        0x001D: {
            0b011100001: UNKNOWN_STR,
        },
        0x001E: {
            0b101011110: UNKNOWN_STR,
            0b111110100: UNKNOWN_STR,
        },
        0x001F: {
            0b001111101: UNKNOWN_STR,
        },
        0x002A: {
            0b000110111: UNKNOWN_STR,
            0b001010000: UNKNOWN_STR,
            0b001010111: UNKNOWN_STR,
            0b001100111: UNKNOWN_STR,
            0b001110011: UNKNOWN_STR,
            0b001111101: UNKNOWN_STR,
            0b010000110: UNKNOWN_STR,
            0b010000111: UNKNOWN_STR,
            0b010010110: UNKNOWN_STR,
            0b010011101: UNKNOWN_STR,
            0b010011111: UNKNOWN_STR,
            0b010100000: UNKNOWN_STR,
            0b010101010: UNKNOWN_STR,
            0b010101111: UNKNOWN_STR,
            0b010110001: UNKNOWN_STR,
            0b010110011: UNKNOWN_STR,
            0b010111001: UNKNOWN_STR,
            0b011000100: UNKNOWN_STR,
            0b011000111: UNKNOWN_STR,
            0b011001000: UNKNOWN_STR,
            0b011010111: UNKNOWN_STR,
            0b011011001: UNKNOWN_STR,
            0b011100001: UNKNOWN_STR,
            0b011101001: UNKNOWN_STR,
            0b011101011: UNKNOWN_STR,
            0b011101100: UNKNOWN_STR,
            0b011110110: UNKNOWN_STR,
            0b011111000: UNKNOWN_STR,
            0b011111010: UNKNOWN_STR,
            0b100000111: UNKNOWN_STR,
            0b100010010: UNKNOWN_STR,
            0b100010011: UNKNOWN_STR,
            0b100010100: UNKNOWN_STR,
            0b100011001: UNKNOWN_STR,
            0b100100010: UNKNOWN_STR,
            0b100100111: UNKNOWN_STR,
            0b100101000: UNKNOWN_STR,
            0b100101001: UNKNOWN_STR,
            0b100101011: UNKNOWN_STR,
            0b100101100: UNKNOWN_STR,
            0b100101101: UNKNOWN_STR,
            0b100111001: UNKNOWN_STR,
            0b101000101: UNKNOWN_STR,
            0b101001001: UNKNOWN_STR,
            0b101001110: UNKNOWN_STR,
            0b101001111: UNKNOWN_STR,
            0b101011100: UNKNOWN_STR,
            0b101011110: UNKNOWN_STR,
            0b101101000: UNKNOWN_STR,
            0b110000000: UNKNOWN_STR,
            0b110000001: UNKNOWN_STR,
            0b110001111: UNKNOWN_STR,
            0b110010000: UNKNOWN_STR,
            0b110101001: UNKNOWN_STR,
            0b111000010: UNKNOWN_STR,
            0b111010001: UNKNOWN_STR,
            0b111010100: UNKNOWN_STR,
            0b111011011: UNKNOWN_STR,
            0b111110100: UNKNOWN_STR,
        },
        0x002B: {
            0b011100001: UNKNOWN_STR,
        },
        0x0046: {
            0b010000000: UNKNOWN_STR,
        },
        0x0047: {
            0b001111000: UNKNOWN_STR,
        },
        0x0048: {
            0b001111000: UNKNOWN_STR,
        },
        0x0049: {
            0b001111000: UNKNOWN_STR,
        },
        0x004A: {
            0b001111000: UNKNOWN_STR,
        },
        0x004B: {
            0b010101010: UNKNOWN_STR,
        },
        0x004C: {
            0b010010110: UNKNOWN_STR,
            0b010101111: UNKNOWN_STR,
            0b011000111: UNKNOWN_STR,
            0b011001000: UNKNOWN_STR,
            0b011011010: UNKNOWN_STR,
            0b011101111: UNKNOWN_STR,
            0b011110011: UNKNOWN_STR,
            0b100101100: UNKNOWN_STR,
        },
        0x004D: {
            0b001010000: UNKNOWN_STR,
            0b010010110: UNKNOWN_STR,
            0b011001000: UNKNOWN_STR,
            0b011100001: UNKNOWN_STR,
            0b011101110: UNKNOWN_STR,
            0b011111100: UNKNOWN_STR,
            0b100101100: UNKNOWN_STR,
            0b111110100: UNKNOWN_STR,
        },
        0x00FA: {
            0b000000111: UNKNOWN_STR,
            0b000001000: UNKNOWN_STR,
            0b000100111: UNKNOWN_STR,
        },
        0x02C0: {
            0b000000000: UNKNOWN_STR,
        },
        0x03C0: {
            0b000000000: UNKNOWN_STR,
        },
        0x09C0: {
            0b000000000: UNKNOWN_STR,
        },
        0x0CC0: {
            0b000000000: UNKNOWN_STR,
        },
        0x1F00: {
            0b000000000: UNKNOWN_STR,
        },
        0x2240: {
            0b000000000: UNKNOWN_STR,
        },
        0x2300: {
            0b000000000: UNKNOWN_STR,
        },
        0x2580: {
            0b000000000: UNKNOWN_STR,
        },
        0x2AC1: {
            0b000000000: UNKNOWN_STR,
        },
        0x2C00: {
            0b000000000: UNKNOWN_STR,
        },
        0x2C80: {
            0b000000000: UNKNOWN_STR,
        },
        0x2D00: {
            0b000000000: UNKNOWN_STR,
        },
        0x3240: {
            0b000000000: UNKNOWN_STR,
        },
        0x34C0: {
            0b000000000: UNKNOWN_STR,
        },
        0x35C0: {
            0b000000000: UNKNOWN_STR,
        },
        0x3A80: {
            0b000000000: UNKNOWN_STR,
        },
        0x3B40: {
            0b000000000: UNKNOWN_STR,
        },
        0x3C41: {
            0b000000000: UNKNOWN_STR,
        },
        0x3CC0: {
            0b000000000: UNKNOWN_STR,
        },
        0x8000: {
            0b100000000: UNKNOWN_STR,
        },
    },
    0b000101: {
        0x8000: {
            0b100000000: UNKNOWN_STR,
        },
    },
    0b000110: "Typical Objects",
    0b000111: "Enemy Boundary",
    0b001000: "Path",
    0b001001: "Camera Trigger",
    0b001010: "Flags",
    0b001011: {
        0x7F07: {
            0b100010011: UNKNOWN_STR,
        },
        0x8000: {
            0b100000000: UNKNOWN_STR,
            0b101000011: UNKNOWN_STR,
            0b110011100: UNKNOWN_STR,
        },
    },
    0b010000: {
        0x0000: {
            0b000000000: UNKNOWN_STR,
        },
        0x8000: {
            0b000001010: UNKNOWN_STR,
        },
    },
    0b010010: {
        0x8000: {
            0b110110110: UNKNOWN_STR,
            0b111001100: UNKNOWN_STR,
        },
    },
    0b010011: {
        0x447A: {
            0b110110011: UNKNOWN_STR,
        },
        0x6C8E: {
            0b111001111: UNKNOWN_STR,
        },
        0x73DC: {
            0b110011010: UNKNOWN_STR,
        },
        0x8000: {
            0b110110110: UNKNOWN_STR,
            0b110111000: UNKNOWN_STR,
            0b111110100: UNKNOWN_STR,
            0b111110110: UNKNOWN_STR,
        },
    },
    0b010110: {
        0x8000: {
            0b000001010: UNKNOWN_STR,
        },
    },
    0b010111: {
        0x8000: {
            0b000001010: UNKNOWN_STR,
        },
    },
    0b011000: {
        0x0000: {
            0b000000000: UNKNOWN_STR,
            0b101100110: UNKNOWN_STR,
        },
        0x8000: {
            0b000001010: UNKNOWN_STR,
        },
    },
    0b011010: {
        0x8000: {
            0b101000001: UNKNOWN_STR,
        },
    },
    0b011011: {
        0x7601: {
            0b110110001: UNKNOWN_STR,
        },
        0x8000: {
            0b101001111: UNKNOWN_STR,
            0b111001111: UNKNOWN_STR,
        },
        0x84D9: {
            0b110101111: UNKNOWN_STR,
        },
    },
    0b011111: {
        0x8000: {
            0b000001000: UNKNOWN_STR,
            0b000001010: UNKNOWN_STR,
            0b000001110: UNKNOWN_STR,
            0b000010000: UNKNOWN_STR,
        },
    },
    0b100010: {
        0x8000: {
            0b110111001: UNKNOWN_STR,
        },
    },
    0b100011: {
        0x6E84: {
            0b101101100: UNKNOWN_STR,
        },
        0x8000: {
            0b011100011: UNKNOWN_STR,
            0b110010010: UNKNOWN_STR,
            0b111111110: UNKNOWN_STR,
        },
        0x814B: {
            0b100011100: UNKNOWN_STR,
        },
        0xD416: {
            0b101110110: UNKNOWN_STR,
        },
    },
    0b100111: {
        0x8000: {
            0b000000100: UNKNOWN_STR,
            0b000001000: UNKNOWN_STR,
        },
    },
    0b101000: {
        0x0000: {
            0b000000000: UNKNOWN_STR,
        },
    },
    0b101011: {
        0x770F: {
            0b111111110: UNKNOWN_STR,
        },
        0x7ED1: {
            0b100100011: UNKNOWN_STR,
        },
        0x8000: {
            0b111001100: UNKNOWN_STR,
        },
        0x8B11: {
            0b100100110: UNKNOWN_STR,
        },
    },
    0b101111: {
        0x8000: {
            0b000000100: UNKNOWN_STR,
            0b000001010: UNKNOWN_STR,
        },
    },
    0b110000: {
        0x0000: {
            0b000000000: UNKNOWN_STR,
            0b001011001: UNKNOWN_STR,
        },
        0x1FC0: {
            0b000000000: UNKNOWN_STR,
        },
        0x2580: {
            0b000000000: UNKNOWN_STR,
        },
        0x25C0: {
            0b000000000: UNKNOWN_STR,
        },
        0x2E40: {
            0b000000000: UNKNOWN_STR,
        },
    },
    0b110010: {
        0x8000: {
            0b100110001: UNKNOWN_STR,
            0b111001100: UNKNOWN_STR,
        },
    },
    0b110011: {
        0x6689: {
            0b111010100: UNKNOWN_STR,
        },
        0x6F97: {
            0b101000000: UNKNOWN_STR,
        },
        0x8000: {
            0b110000001: UNKNOWN_STR,
        },
        0x939D: {
            0b110001101: UNKNOWN_STR,
        },
    },
    0b110100: {
        0x0280: {
            0b000000000: UNKNOWN_STR,
        },
        0x03C0: {
            0b000000000: UNKNOWN_STR,
        },
        0x25C0: {
            0b101100111: UNKNOWN_STR,
        },
        0x2E00: {
            0b000000000: UNKNOWN_STR,
        },
        0x3C80: {
            0b000000000: UNKNOWN_STR,
        },
    },
    0b111000: {
        0x0000: {
            0b000000000: UNKNOWN_STR,
            0b000000001: UNKNOWN_STR,
            0b000000010: UNKNOWN_STR,
            0b000000011: UNKNOWN_STR,
            0b000000100: UNKNOWN_STR,
            0b000000101: UNKNOWN_STR,
            0b000000110: UNKNOWN_STR,
            0b000000111: UNKNOWN_STR,
            0b000001000: UNKNOWN_STR,
            0b000001001: UNKNOWN_STR,
            0b000001010: UNKNOWN_STR,
            0b000001011: UNKNOWN_STR,
            0b000001100: UNKNOWN_STR,
            0b000001101: UNKNOWN_STR,
            0b000001110: UNKNOWN_STR,
            0b000010001: UNKNOWN_STR,
            0b000010010: UNKNOWN_STR,
            0b000100000: UNKNOWN_STR,
            0b000100010: UNKNOWN_STR,
            0b000100101: UNKNOWN_STR,
            0b001001001: UNKNOWN_STR,
            0b001001010: UNKNOWN_STR,
            0b100001101: UNKNOWN_STR,
            0b100001110: UNKNOWN_STR,
            0b100011010: UNKNOWN_STR,
            0b100101101: UNKNOWN_STR,
            0b100111011: UNKNOWN_STR,
            0b101000011: UNKNOWN_STR,
            0b101001111: UNKNOWN_STR,
            0b101010000: UNKNOWN_STR,
            0b101010010: UNKNOWN_STR,
            0b101010100: UNKNOWN_STR,
            0b101010101: UNKNOWN_STR,
            0b101010110: UNKNOWN_STR,
            0b101010111: UNKNOWN_STR,
            0b101011000: UNKNOWN_STR,
            0b101011001: UNKNOWN_STR,
            0b101011010: UNKNOWN_STR,
            0b101011011: UNKNOWN_STR,
            0b101011100: UNKNOWN_STR,
            0b101011101: UNKNOWN_STR,
            0b101011110: UNKNOWN_STR,
            0b101011111: UNKNOWN_STR,
            0b101100000: UNKNOWN_STR,
            0b101100001: UNKNOWN_STR,
            0b101100010: UNKNOWN_STR,
            0b101100011: UNKNOWN_STR,
            0b101100100: UNKNOWN_STR,
            0b101100101: UNKNOWN_STR,
            0b101100110: UNKNOWN_STR,
            0b101100111: UNKNOWN_STR,
        },
        0x08C0: {
            0b000000000: UNKNOWN_STR,
        },
        0x0A00: {
            0b000000000: UNKNOWN_STR,
        },
        0x0B01: {
            0b000000000: UNKNOWN_STR,
        },
        0x0B40: {
            0b000000000: UNKNOWN_STR,
        },
        0x17C0: {
            0b000000000: UNKNOWN_STR,
        },
        0x1F80: {
            0b000000000: UNKNOWN_STR,
        },
        0x1F81: {
            0b000000000: UNKNOWN_STR,
        },
        0x2180: {
            0b000000000: UNKNOWN_STR,
        },
        0x2200: {
            0b000000000: UNKNOWN_STR,
        },
        0x2201: {
            0b000000000: UNKNOWN_STR,
        },
        0x2300: {
            0b000000000: UNKNOWN_STR,
        },
        0x2681: {
            0b000000000: UNKNOWN_STR,
        },
        0x2900: {
            0b000000000: UNKNOWN_STR,
        },
        0x2940: {
            0b001001101: UNKNOWN_STR,
        },
        0x2AC1: {
            0b000000000: UNKNOWN_STR,
        },
        0x2B40: {
            0b000000000: UNKNOWN_STR,
        },
        0x2E80: {
            0b000000000: UNKNOWN_STR,
        },
        0x2EC0: {
            0b000000000: UNKNOWN_STR,
        },
        0x2F40: {
            0b000000000: UNKNOWN_STR,
        },
        0x3040: {
            0b000000000: UNKNOWN_STR,
        },
        0x3080: {
            0b000000000: UNKNOWN_STR,
        },
        0x30C0: {
            0b000000000: UNKNOWN_STR,
        },
        0x3180: {
            0b000000000: UNKNOWN_STR,
        },
        0x31C0: {
            0b000000000: UNKNOWN_STR,
        },
        0x3280: {
            0b000000000: UNKNOWN_STR,
        },
        0x3640: {
            0b000000001: UNKNOWN_STR,
        },
        0x37C0: {
            0b000000000: UNKNOWN_STR,
        },
        0x3800: {
            0b000000000: UNKNOWN_STR,
        },
        0x3840: {
            0b000000000: UNKNOWN_STR,
        },
        0x3980: {
            0b000000000: UNKNOWN_STR,
        },
        0x3A00: {
            0b000000000: UNKNOWN_STR,
        },
        0x3BC0: {
            0b000000000: UNKNOWN_STR,
        },
        0x3C00: {
            0b000000000: UNKNOWN_STR,
        },
        0x3C41: {
            0b000000000: UNKNOWN_STR,
        },
        0x3CC0: {
            0b000000000: UNKNOWN_STR,
        },
    },
    0b111010: {
        0x0000: {
            0b000000000: UNKNOWN_STR,
        },
        0x0940: {
            0b000000000: UNKNOWN_STR,
        },
        0x0B40: {
            0b000000000: UNKNOWN_STR,
        },
        0x0D00: {
            0b000000000: UNKNOWN_STR,
        },
        0x1A80: {
            0b000000000: UNKNOWN_STR,
        },
        0x1AC0: {
            0b000000000: UNKNOWN_STR,
        },
        0x1AF0: {
            0b000000000: UNKNOWN_STR,
        },
        0x1EC0: {
            0b000000000: UNKNOWN_STR,
        },
        0x2001: {
            0b000000000: UNKNOWN_STR,
        },
        0x2041: {
            0b000000000: UNKNOWN_STR,
        },
        0x2143: {
            0b000000000: UNKNOWN_STR,
        },
        0x2180: {
            0b000000000: UNKNOWN_STR,
        },
        0x21C0: {
            0b000000000: UNKNOWN_STR,
        },
        0x2200: {
            0b000000000: UNKNOWN_STR,
        },
        0x2784: {
            0b000000000: UNKNOWN_STR,
        },
        0x2B40: {
            0b000000000: UNKNOWN_STR,
        },
        0x2DBA: {
            0b000000000: UNKNOWN_STR,
        },
        0x2F01: {
            0b000000000: UNKNOWN_STR,
        },
        0x2F81: {
            0b000000000: UNKNOWN_STR,
        },
        0x3380: {
            0b000000000: UNKNOWN_STR,
        },
        0x3441: {
            0b000000000: UNKNOWN_STR,
        },
        0x3500: {
            0b000000000: UNKNOWN_STR,
        },
        0x3540: {
            0b000000000: UNKNOWN_STR,
        },
        0x3580: {
            0b000000000: UNKNOWN_STR,
        },
        0x3601: {
            0b000000000: UNKNOWN_STR,
        },
        0x3681: {
            0b000000000: UNKNOWN_STR,
        },
        0x38C1: {
            0b000000000: UNKNOWN_STR,
        },
        0x3940: {
            0b000000000: UNKNOWN_STR,
        },
        0x39C0: {
            0b000000000: UNKNOWN_STR,
        },
        0x3A00: {
            0b000000000: UNKNOWN_STR,
        },
        0x8000: {
            0b110000010: UNKNOWN_STR,
        },
    },
    0b111011: {
        0x2A09: {
            0b111111111: UNKNOWN_STR,
        },
        0x5981: {
            0b111111111: UNKNOWN_STR,
        },
        0x5AE0: {
            0b111111111: UNKNOWN_STR,
        },
        0x6542: {
            0b111111111: UNKNOWN_STR,
        },
        0x73DC: {
            0b100010100: UNKNOWN_STR,
        },
        0x8000: {
            0b100111001: UNKNOWN_STR,
            0b111111111: UNKNOWN_STR,
        },
        0x854E: {
            0b011001011: UNKNOWN_STR,
        },
        0x9283: {
            0b111111111: UNKNOWN_STR,
        },
        0x9CEE: {
            0b111111111: UNKNOWN_STR,
        },
        0xA1E3: {
            0b111111111: UNKNOWN_STR,
        },
        0xCA16: {
            0b111111111: UNKNOWN_STR,
        },
        0xDDB3: {
            0b111111111: UNKNOWN_STR,
        },
    },
    0b111100: {
        0x0000: {
            0b000000000: UNKNOWN_STR,
        },
        0x0900: {
            0b000000000: UNKNOWN_STR,
        },
        0x0B01: {
            0b000000000: UNKNOWN_STR,
        },
        0x0B40: {
            0b000000000: UNKNOWN_STR,
        },
        0x1B00: {
            0b000000000: UNKNOWN_STR,
        },
        0x1B40: {
            0b000000000: UNKNOWN_STR,
        },
        0x1F81: {
            0b000000000: UNKNOWN_STR,
        },
        0x2280: {
            0b000000000: UNKNOWN_STR,
        },
        0x2300: {
            0b000000000: UNKNOWN_STR,
        },
        0x27C0: {
            0b000000000: UNKNOWN_STR,
        },
        0x2880: {
            0b000000000: UNKNOWN_STR,
        },
        0x28C0: {
            0b000000000: UNKNOWN_STR,
        },
        0x2A00: {
            0b000000000: UNKNOWN_STR,
        },
        0x2A40: {
            0b000000000: UNKNOWN_STR,
        },
        0x3080: {
            0b000000000: UNKNOWN_STR,
        },
        0x3100: {
            0b000000000: UNKNOWN_STR,
        },
        0x3240: {
            0b000000000: UNKNOWN_STR,
        },
        0x3341: {
            0b000000000: UNKNOWN_STR,
        },
        0x3400: {
            0b000000000: UNKNOWN_STR,
        },
        0x3480: {
            0b000000000: UNKNOWN_STR,
        },
        0x3600: {
            0b000000000: UNKNOWN_STR,
        },
        0x3681: {
            0b000000000: UNKNOWN_STR,
        },
        0x36C0: {
            0b000000000: UNKNOWN_STR,
        },
        0x36D9: {
            0b000000000: UNKNOWN_STR,
        },
        0x3700: {
            0b000000000: UNKNOWN_STR,
        },
        0x3741: {
            0b000000000: UNKNOWN_STR,
        },
        0x3780: {
            0b000000000: UNKNOWN_STR,
        },
        0x3840: {
            0b000000000: UNKNOWN_STR,
        },
        0x3880: {
            0b000000000: UNKNOWN_STR,
        },
        0x3980: {
            0b000000000: UNKNOWN_STR,
        },
        0x3A80: {
            0b000000000: UNKNOWN_STR,
        },
        0x3BC0: {
            0b000000000: UNKNOWN_STR,
        },
        0x3C80: {
            0b000000000: UNKNOWN_STR,
        },
    },
}

############################
##### WARP OBJECT DICT #####
############################

WARP_OBJECT_DICT:dict = {
    0x0000: UNKNOWN_STR,
    0x0002: UNKNOWN_STR,
    0x0003: UNKNOWN_STR,
    0x0004: UNKNOWN_STR,
    0x0005: f"Warp {LEVEL_NAME_ENUMS.gobis_valley} Main To {LEVEL_NAME_ENUMS.gobis_valley} Jinxy",
    0x0006: f"Warp {LEVEL_NAME_ENUMS.gobis_valley} Jinxy To {LEVEL_NAME_ENUMS.gobis_valley} Main",
    0x0007: UNKNOWN_STR,
    0x0008: UNKNOWN_STR,
    0x0009: f"Warp {LEVEL_NAME_ENUMS.bubblegloop_swamp} Main To {LEVEL_NAME_ENUMS.bubblegloop_swamp} Mumbo's Skull",
    0x000A: f"Warp {LEVEL_NAME_ENUMS.bubblegloop_swamp} Mumbo's Skull To {LEVEL_NAME_ENUMS.bubblegloop_swamp} Main",
    0x000B: f"Warp {LEVEL_NAME_ENUMS.treasure_trove_cove} Nipper's Shell To {LEVEL_NAME_ENUMS.treasure_trove_cove} Main",
    0x000C: UNKNOWN_STR,
    0x000D: UNKNOWN_STR,
    0x000E: UNKNOWN_STR,
    0x000F: UNKNOWN_STR,
    0x0010: UNKNOWN_STR,
    0x0011: UNKNOWN_STR,
    0x0012: f"Warp {LEVEL_NAME_ENUMS.click_clock_wood} Spring Main To {LEVEL_NAME_ENUMS.click_clock_wood} Spring Whipcrack Room",
    0x0013: f"Warp {LEVEL_NAME_ENUMS.click_clock_wood} Summer Main To {LEVEL_NAME_ENUMS.click_clock_wood} Summer Whipcrack Room",
    0x0014: f"Warp {LEVEL_NAME_ENUMS.click_clock_wood} Autumn Main To {LEVEL_NAME_ENUMS.click_clock_wood} Autumn Whipcrack Room",
    0x0015: UNKNOWN_STR,
    0x0016: f"Warp {LEVEL_NAME_ENUMS.mumbos_mountain} Main To {LEVEL_NAME_ENUMS.mumbos_mountain} Mumbo's Skull",
    0x0017: f"Warp {LEVEL_NAME_ENUMS.mumbos_mountain} Mumbo's Skull To {LEVEL_NAME_ENUMS.mumbos_mountain} Main",
    0x0018: f"Warp {LEVEL_NAME_ENUMS.mumbos_mountain} Main To {LEVEL_NAME_ENUMS.mumbos_mountain} Ticker's Tower Lower",
    0x0019: f"Warp {LEVEL_NAME_ENUMS.mumbos_mountain} Ticker's Tower Lower To {LEVEL_NAME_ENUMS.mumbos_mountain} Main",
    0x001A: f"Warp {LEVEL_NAME_ENUMS.mumbos_mountain} Main To {LEVEL_NAME_ENUMS.mumbos_mountain} Ticker's Tower Upper",
    0x001B: f"Warp {LEVEL_NAME_ENUMS.mumbos_mountain} Ticker's Tower Upper To {LEVEL_NAME_ENUMS.mumbos_mountain} Main",
    0x001C: UNKNOWN_STR,
    0x001D: UNKNOWN_STR,
    0x0022: UNKNOWN_STR,
    0x0023: UNKNOWN_STR,
    0x0025: UNKNOWN_STR,
    0x0026: UNKNOWN_STR,
    0x0027: UNKNOWN_STR,
    0x0028: UNKNOWN_STR,
    0x0029: UNKNOWN_STR,
    0x002A: f"Warp {LEVEL_NAME_ENUMS.click_clock_wood} Autumn Main To {LEVEL_NAME_ENUMS.click_clock_wood} Autumn Flooded Room",
    0x002B: UNKNOWN_STR,
    0x002C: UNKNOWN_STR,
    0x002D: UNKNOWN_STR,
    0x002E: UNKNOWN_STR,
    0x002F: f"Warp {LEVEL_NAME_ENUMS.clankers_cavern} Clanker's Left Gill To {LEVEL_NAME_ENUMS.clankers_cavern} Main",
    0x0030: f"Warp {LEVEL_NAME_ENUMS.clankers_cavern} Clanker's Right Gill To {LEVEL_NAME_ENUMS.clankers_cavern} Main",
    0x0031: f"Warp {LEVEL_NAME_ENUMS.clankers_cavern} Clanker's Left Tooth To {LEVEL_NAME_ENUMS.clankers_cavern} Main",
    0x0032: f"Warp {LEVEL_NAME_ENUMS.clankers_cavern} Clanker's Right Tooth To {LEVEL_NAME_ENUMS.clankers_cavern} Main",
    0x0036: UNKNOWN_STR,
    0x0038: UNKNOWN_STR,
    0x0039: UNKNOWN_STR,
    0x003A: UNKNOWN_STR,
    0x003B: UNKNOWN_STR,
    0x003C: UNKNOWN_STR,
    0x003D: UNKNOWN_STR,
    0x003E: UNKNOWN_STR,
    0x003F: UNKNOWN_STR,
    0x0040: f"Warp {LEVEL_NAME_ENUMS.freezeezy_peak} Main To {LEVEL_NAME_ENUMS.freezeezy_peak} Mumbo's Skull",
    0x0041: f"Warp {LEVEL_NAME_ENUMS.freezeezy_peak} Main To {LEVEL_NAME_ENUMS.freezeezy_peak} Igloo",
    0x0042: f"Warp {LEVEL_NAME_ENUMS.freezeezy_peak} Main To {LEVEL_NAME_ENUMS.freezeezy_peak} Christmas Tree",
    0x0043: f"Warp {LEVEL_NAME_ENUMS.freezeezy_peak} Mumbo's Skull To {LEVEL_NAME_ENUMS.freezeezy_peak} Main",
    0x0044: f"Warp {LEVEL_NAME_ENUMS.freezeezy_peak} Igloo To {LEVEL_NAME_ENUMS.freezeezy_peak} Main",
    0x0045: f"Warp {LEVEL_NAME_ENUMS.freezeezy_peak} Christmas Tree To {LEVEL_NAME_ENUMS.freezeezy_peak} Main",
    0x0046: f"Warp {LEVEL_NAME_ENUMS.bubblegloop_swamp} Main To {LEVEL_NAME_ENUMS.bubblegloop_swamp} Tanktup",
    0x0047: f"Warp {LEVEL_NAME_ENUMS.treasure_trove_cove} Main To {LEVEL_NAME_ENUMS.treasure_trove_cove} Nipper's Shell",
    0x0048: UNKNOWN_STR,
    0x0049: UNKNOWN_STR,
    0x004E: UNKNOWN_STR,
    0x004F: UNKNOWN_STR,
    0x0054: UNKNOWN_STR,
    0x0055: UNKNOWN_STR,
    0x0056: UNKNOWN_STR,
    0x0057: UNKNOWN_STR,
    0x0058: f"Warp {LEVEL_NAME_ENUMS.click_clock_wood} Spring Whipcrack Room To {LEVEL_NAME_ENUMS.click_clock_wood} Spring Main",
    0x0059: f"Warp {LEVEL_NAME_ENUMS.click_clock_wood} Summer Whipcrack Room To {LEVEL_NAME_ENUMS.click_clock_wood} Summer Main",
    0x005A: UNKNOWN_STR,
    0x005B: UNKNOWN_STR,
    0x005C: f"Warp {LEVEL_NAME_ENUMS.gobis_valley} Main To {LEVEL_NAME_ENUMS.gobis_valley} Matching Puzzle",
    0x005D: f"Warp {LEVEL_NAME_ENUMS.gobis_valley} Main To {LEVEL_NAME_ENUMS.gobis_valley} King Sandybutt Front",
    0x005E: f"Warp {LEVEL_NAME_ENUMS.gobis_valley} Main To {LEVEL_NAME_ENUMS.gobis_valley} Water Pyramid Upper",
    0x005F: f"Warp {LEVEL_NAME_ENUMS.gobis_valley} Main To {LEVEL_NAME_ENUMS.gobis_valley} Water Pyramid Lower",
    0x0060: f"Warp {LEVEL_NAME_ENUMS.gobis_valley} Main To {LEVEL_NAME_ENUMS.gobis_valley} Rubee",
    0x0061: f"Warp {LEVEL_NAME_ENUMS.gobis_valley} Matching Puzzle To {LEVEL_NAME_ENUMS.gobis_valley} Main",
    0x0062: f"Warp {LEVEL_NAME_ENUMS.gobis_valley} King Sandybutt Front To {LEVEL_NAME_ENUMS.gobis_valley} Main",
    0x0063: f"Warp {LEVEL_NAME_ENUMS.gobis_valley} Water Pyramid Lower To {LEVEL_NAME_ENUMS.gobis_valley} Main",
    0x0064: f"Warp {LEVEL_NAME_ENUMS.gobis_valley} Rubee To {LEVEL_NAME_ENUMS.gobis_valley} Main",
    0x0066: f"Warp {LEVEL_NAME_ENUMS.bubblegloop_swamp} Main To {LEVEL_NAME_ENUMS.bubblegloop_swamp} Mr. Vile Right Nostril",
    0x0067: f"Warp {LEVEL_NAME_ENUMS.bubblegloop_swamp} Main To {LEVEL_NAME_ENUMS.bubblegloop_swamp} Mr. Vile Left Nostril",
    0x0068: f"Warp {LEVEL_NAME_ENUMS.bubblegloop_swamp} Tanktup To {LEVEL_NAME_ENUMS.bubblegloop_swamp} Main",
    0x0069: f"Warp {LEVEL_NAME_ENUMS.bubblegloop_swamp} Mr. Vile Right Nostril To {LEVEL_NAME_ENUMS.bubblegloop_swamp} Main",
    0x006A: f"Warp {LEVEL_NAME_ENUMS.bubblegloop_swamp} Mr. Vile Left Nostril To {LEVEL_NAME_ENUMS.bubblegloop_swamp} Main",
    0x006B: f"Warp {LEVEL_NAME_ENUMS.treasure_trove_cove} Main To {LEVEL_NAME_ENUMS.treasure_trove_cove} Sandcastle",
    0x006C: f"Warp {LEVEL_NAME_ENUMS.treasure_trove_cove} Top Area To {LEVEL_NAME_ENUMS.treasure_trove_cove} Alcove",
    0x006D: f"Warp {LEVEL_NAME_ENUMS.treasure_trove_cove} Alcove To {LEVEL_NAME_ENUMS.treasure_trove_cove} Top Area",
    0x006E: f"Warp {LEVEL_NAME_ENUMS.treasure_trove_cove} Main To {LEVEL_NAME_ENUMS.treasure_trove_cove} Salty Hippo Upper",
    0x006F: f"Warp {LEVEL_NAME_ENUMS.treasure_trove_cove} Main To {LEVEL_NAME_ENUMS.treasure_trove_cove} Salty Hippo Lower",
    0x0070: UNKNOWN_STR,
    0x0071: f"Warp {LEVEL_NAME_ENUMS.treasure_trove_cove} Lighthouse Lower To {LEVEL_NAME_ENUMS.treasure_trove_cove} Lighthouse Upper",
    0x0072: f"Warp {LEVEL_NAME_ENUMS.treasure_trove_cove} Sandcastle To {LEVEL_NAME_ENUMS.treasure_trove_cove} Main",
    0x0073: UNKNOWN_STR,
    0x0074: UNKNOWN_STR,
    0x0075: f"Warp {LEVEL_NAME_ENUMS.treasure_trove_cove} Salty Hippo Upper To {LEVEL_NAME_ENUMS.treasure_trove_cove} Main",
    0x0076: f"Warp {LEVEL_NAME_ENUMS.treasure_trove_cove} Salty Hippo Lower To {LEVEL_NAME_ENUMS.treasure_trove_cove} Main",
    0x0077: UNKNOWN_STR,
    0x0078: UNKNOWN_STR,
    0x0079: f"Warp {LEVEL_NAME_ENUMS.mad_monster_mansion} Main To {LEVEL_NAME_ENUMS.mad_monster_mansion} Dining Room Front Door",
    0x007A: f"Warp {LEVEL_NAME_ENUMS.mad_monster_mansion} Main To {LEVEL_NAME_ENUMS.mad_monster_mansion} Dining Room Fireplace",
    0x007B: f"Warp {LEVEL_NAME_ENUMS.mad_monster_mansion} Main To {LEVEL_NAME_ENUMS.mad_monster_mansion} Well Top",
    0x007C: f"Warp {LEVEL_NAME_ENUMS.mad_monster_mansion} Main To {LEVEL_NAME_ENUMS.mad_monster_mansion} Tumblar",
    0x007D: f"Warp {LEVEL_NAME_ENUMS.mad_monster_mansion} Main To {LEVEL_NAME_ENUMS.mad_monster_mansion} Church",
    0x007E: f"Warp {LEVEL_NAME_ENUMS.mad_monster_mansion} Main To {LEVEL_NAME_ENUMS.mad_monster_mansion} Secret Church Room",
    0x007F: f"Warp {LEVEL_NAME_ENUMS.mad_monster_mansion} Main To {LEVEL_NAME_ENUMS.mad_monster_mansion} Water Barrel",
    0x0080: UNKNOWN_STR,
    0x0081: f"Warp {LEVEL_NAME_ENUMS.mad_monster_mansion} Main To {LEVEL_NAME_ENUMS.mad_monster_mansion} Cellar",
    0x0082: f"Warp {LEVEL_NAME_ENUMS.mad_monster_mansion} Main To {LEVEL_NAME_ENUMS.mad_monster_mansion} Red Feather Room",
    0x0083: f"Warp {LEVEL_NAME_ENUMS.mad_monster_mansion} Main To {LEVEL_NAME_ENUMS.mad_monster_mansion} Blue Egg Room",
    0x0084: f"Warp {LEVEL_NAME_ENUMS.mad_monster_mansion} Main To {LEVEL_NAME_ENUMS.mad_monster_mansion} Note Room",
    0x0085: f"Warp {LEVEL_NAME_ENUMS.mad_monster_mansion} Main To {LEVEL_NAME_ENUMS.mad_monster_mansion} Empty Honeycomb Room",
    0x0086: f"Warp {LEVEL_NAME_ENUMS.mad_monster_mansion} Main To {LEVEL_NAME_ENUMS.mad_monster_mansion} Bedroom",
    0x0087: f"Warp {LEVEL_NAME_ENUMS.mad_monster_mansion} Main To {LEVEL_NAME_ENUMS.mad_monster_mansion} Restroom",
    0x0088: f"Warp {LEVEL_NAME_ENUMS.mad_monster_mansion} Dining Room Front Door To {LEVEL_NAME_ENUMS.mad_monster_mansion} Main",
    0x008A: f"Warp {LEVEL_NAME_ENUMS.mad_monster_mansion} Well Top To {LEVEL_NAME_ENUMS.mad_monster_mansion} Main",
    0x008B: f"Warp {LEVEL_NAME_ENUMS.mad_monster_mansion} Tumblar To {LEVEL_NAME_ENUMS.mad_monster_mansion} Main",
    0x008C: f"Warp {LEVEL_NAME_ENUMS.mad_monster_mansion} Church To {LEVEL_NAME_ENUMS.mad_monster_mansion} Main",
    0x008D: f"Warp {LEVEL_NAME_ENUMS.mad_monster_mansion} Secret Church Room To {LEVEL_NAME_ENUMS.mad_monster_mansion} Main",
    0x008F: f"Warp {LEVEL_NAME_ENUMS.mad_monster_mansion} Water Barrel To {LEVEL_NAME_ENUMS.mad_monster_mansion} Main",
    0x0090: f"Warp {LEVEL_NAME_ENUMS.mad_monster_mansion} Cellar To {LEVEL_NAME_ENUMS.mad_monster_mansion} Main",
    0x0091: f"Warp {LEVEL_NAME_ENUMS.mad_monster_mansion} Red Feather To {LEVEL_NAME_ENUMS.mad_monster_mansion} Main",
    0x0092: f"Warp {LEVEL_NAME_ENUMS.mad_monster_mansion} Egg Room To {LEVEL_NAME_ENUMS.mad_monster_mansion} Main",
    0x0093: f"Warp {LEVEL_NAME_ENUMS.mad_monster_mansion} Bathroom To {LEVEL_NAME_ENUMS.mad_monster_mansion} Main",
    0x0094: f"Warp {LEVEL_NAME_ENUMS.mad_monster_mansion} Empty Honeycomb Room To {LEVEL_NAME_ENUMS.mad_monster_mansion} Main",
    0x0095: f"Warp {LEVEL_NAME_ENUMS.mad_monster_mansion} Bedroom To {LEVEL_NAME_ENUMS.mad_monster_mansion} Main",
    0x0096: f"Warp {LEVEL_NAME_ENUMS.mad_monster_mansion} Note Room To {LEVEL_NAME_ENUMS.mad_monster_mansion} Main",
    0x0097: f"Warp {LEVEL_NAME_ENUMS.mad_monster_mansion} Clock Tower Lower To {LEVEL_NAME_ENUMS.mad_monster_mansion} Clock Tower Upper",
    0x0098: f"Warp {LEVEL_NAME_ENUMS.mad_monster_mansion} Clock Tower Upper To {LEVEL_NAME_ENUMS.mad_monster_mansion} Clock Tower Lower",
    0x0099: f"Warp {LEVEL_NAME_ENUMS.mad_monster_mansion} Mumbo's Skull To {LEVEL_NAME_ENUMS.mad_monster_mansion} Main",
    0x009A: f"Warp {LEVEL_NAME_ENUMS.mad_monster_mansion} Main To {LEVEL_NAME_ENUMS.mad_monster_mansion} Mumbo's Skull",
    0x009B: f"Warp {LEVEL_NAME_ENUMS.clankers_cavern} Wonderwing To {LEVEL_NAME_ENUMS.clankers_cavern} Belly",
    0x009C: f"Warp {LEVEL_NAME_ENUMS.clankers_cavern} Blowhole To {LEVEL_NAME_ENUMS.clankers_cavern} Belly",
    0x009D: f"Warp {LEVEL_NAME_ENUMS.clankers_cavern} Blowhole To {LEVEL_NAME_ENUMS.clankers_cavern} Mouth",
    0x009E: f"Warp {LEVEL_NAME_ENUMS.clankers_cavern} Belly To {LEVEL_NAME_ENUMS.clankers_cavern} Wonderwing",
    0x009F: UNKNOWN_STR,
    0x00A0: f"Warp {LEVEL_NAME_ENUMS.rusty_bucket_bay} Main To {LEVEL_NAME_ENUMS.rusty_bucket_bay} Captain's Room Window",
    0x00A1: f"Warp {LEVEL_NAME_ENUMS.rusty_bucket_bay} Main To {LEVEL_NAME_ENUMS.rusty_bucket_bay} Seaman Grublin Cabin Window",
    0x00A2: f"Warp {LEVEL_NAME_ENUMS.rusty_bucket_bay} Main To {LEVEL_NAME_ENUMS.rusty_bucket_bay} Engine Control Pipe",
    0x00A3: f"Warp {LEVEL_NAME_ENUMS.rusty_bucket_bay} Main To {LEVEL_NAME_ENUMS.rusty_bucket_bay} Kitchen Pipe",
    0x00A4: f"Warp {LEVEL_NAME_ENUMS.rusty_bucket_bay} Main To {LEVEL_NAME_ENUMS.rusty_bucket_bay} Navigation Room Window",
    0x00A5: f"Warp {LEVEL_NAME_ENUMS.rusty_bucket_bay} Main To {LEVEL_NAME_ENUMS.rusty_bucket_bay} Middle Pipe",
    0x00A6: f"Warp {LEVEL_NAME_ENUMS.rusty_bucket_bay} Main To {LEVEL_NAME_ENUMS.rusty_bucket_bay} Engine Room",
    0x00A7: f"Warp {LEVEL_NAME_ENUMS.rusty_bucket_bay} Main To {LEVEL_NAME_ENUMS.rusty_bucket_bay} Chump Warehouse Window",
    0x00A8: f"Warp {LEVEL_NAME_ENUMS.rusty_bucket_bay} Main To {LEVEL_NAME_ENUMS.rusty_bucket_bay} Boat Room",
    0x00A9: f"Warp {LEVEL_NAME_ENUMS.rusty_bucket_bay} Main To {LEVEL_NAME_ENUMS.rusty_bucket_bay} Chompa Blue Container",
    0x00AA: f"Warp {LEVEL_NAME_ENUMS.rusty_bucket_bay} Main To {LEVEL_NAME_ENUMS.rusty_bucket_bay} Seaman Grublin Blue Container",
    0x00AB: f"Warp {LEVEL_NAME_ENUMS.rusty_bucket_bay} Main To {LEVEL_NAME_ENUMS.rusty_bucket_bay} Boom Box Blue Container",
    0x00AC: f"Warp {LEVEL_NAME_ENUMS.rusty_bucket_bay} Captain's Room Window To {LEVEL_NAME_ENUMS.rusty_bucket_bay} Main",
    0x00AD: f"Warp {LEVEL_NAME_ENUMS.rusty_bucket_bay} Seaman Grublin's Cabin To {LEVEL_NAME_ENUMS.rusty_bucket_bay} Main",
    0x00AE: f"Warp {LEVEL_NAME_ENUMS.rusty_bucket_bay} Engine Control Pipe To {LEVEL_NAME_ENUMS.rusty_bucket_bay} Main",
    0x00AF: f"Warp {LEVEL_NAME_ENUMS.rusty_bucket_bay} Kitchen Pipe To {LEVEL_NAME_ENUMS.rusty_bucket_bay} Main",
    0x00B0: f"Warp {LEVEL_NAME_ENUMS.rusty_bucket_bay} Navigation Room Window To {LEVEL_NAME_ENUMS.rusty_bucket_bay} Main",
    0x00B1: f"Warp {LEVEL_NAME_ENUMS.rusty_bucket_bay} Middle Pipe To {LEVEL_NAME_ENUMS.rusty_bucket_bay} Main",
    0x00B2: f"Warp {LEVEL_NAME_ENUMS.rusty_bucket_bay} Engine Room To {LEVEL_NAME_ENUMS.rusty_bucket_bay} Main",
    0x00B3: f"Warp {LEVEL_NAME_ENUMS.rusty_bucket_bay} Boat Room To {LEVEL_NAME_ENUMS.rusty_bucket_bay} Main",
    0x00B4: f"Warp {LEVEL_NAME_ENUMS.rusty_bucket_bay} Chompa Blue Container To {LEVEL_NAME_ENUMS.rusty_bucket_bay} Main",
    0x00B5: f"Warp {LEVEL_NAME_ENUMS.rusty_bucket_bay} Seaman Grublin Blue Container To {LEVEL_NAME_ENUMS.rusty_bucket_bay} Main",
    0x00B6: f"Warp {LEVEL_NAME_ENUMS.rusty_bucket_bay} Boom Box Blue Container To {LEVEL_NAME_ENUMS.rusty_bucket_bay} Main",
    0x00B7: f"Warp {LEVEL_NAME_ENUMS.rusty_bucket_bay} Boss Boom Box To {LEVEL_NAME_ENUMS.rusty_bucket_bay} Main",
    0x00B8: f"Warp {LEVEL_NAME_ENUMS.rusty_bucket_bay} Main To {LEVEL_NAME_ENUMS.rusty_bucket_bay} Boss Boom Box",
    0x00B9: f"Warp {LEVEL_NAME_ENUMS.rusty_bucket_bay} Main To {LEVEL_NAME_ENUMS.rusty_bucket_bay} Chump Warehouse Door",
    0x00BA: f"Warp {LEVEL_NAME_ENUMS.rusty_bucket_bay} Chump Warehouse Door To {LEVEL_NAME_ENUMS.rusty_bucket_bay} Main",
    0x00D6: UNKNOWN_STR,
    0x00D7: f"Warp {LEVEL_NAME_ENUMS.click_clock_wood} Spring Main To {LEVEL_NAME_ENUMS.click_clock_wood} Hub",
    0x00D8: UNKNOWN_STR,
    0x00D9: UNKNOWN_STR,
    0x00DA: f"Warp {LEVEL_NAME_ENUMS.click_clock_wood} Hub To {LEVEL_NAME_ENUMS.click_clock_wood} Winter Main",
    0x00DB: f"Warp {LEVEL_NAME_ENUMS.click_clock_wood} Hub To {LEVEL_NAME_ENUMS.click_clock_wood} Spring Main",
    0x00DC: f"Warp {LEVEL_NAME_ENUMS.click_clock_wood} Hub To {LEVEL_NAME_ENUMS.click_clock_wood} Summer Main",
    0x00DD: f"Warp {LEVEL_NAME_ENUMS.click_clock_wood} Hub To {LEVEL_NAME_ENUMS.click_clock_wood} Autumn Main",
    0x00DE: f"Warp {LEVEL_NAME_ENUMS.gobis_valley} King Sandybutt Back To {LEVEL_NAME_ENUMS.gobis_valley} Main",
    0x00DF: f"Warp {LEVEL_NAME_ENUMS.click_clock_wood} Spring Mumbo's Skull To {LEVEL_NAME_ENUMS.click_clock_wood} Spring Main",
    0x00E0: f"Warp {LEVEL_NAME_ENUMS.click_clock_wood} Summer Mumbo's Skull To {LEVEL_NAME_ENUMS.click_clock_wood} Summer Main",
    0x00E1: UNKNOWN_STR,
    0x00E2: UNKNOWN_STR,
    0x00E3: f"Warp {LEVEL_NAME_ENUMS.click_clock_wood} Spring Main To {LEVEL_NAME_ENUMS.click_clock_wood} Spring Mumbo's Skull",
    0x00E4: f"Warp {LEVEL_NAME_ENUMS.click_clock_wood} Summer Main To {LEVEL_NAME_ENUMS.click_clock_wood} Summer Mumbo's Skull",
    0x00E5: f"Warp {LEVEL_NAME_ENUMS.click_clock_wood} Autumn Main To {LEVEL_NAME_ENUMS.click_clock_wood} Autumn Mumbo's Skull",
    0x00E6: UNKNOWN_STR,
    0x00E7: f"Warp {LEVEL_NAME_ENUMS.click_clock_wood} Spring Main To {LEVEL_NAME_ENUMS.click_clock_wood} Spring Nabnut Door",
    0x00E8: f"Warp {LEVEL_NAME_ENUMS.click_clock_wood} Summer Main To {LEVEL_NAME_ENUMS.click_clock_wood} Summer Nabnut Door",
    0x00E9: f"Warp {LEVEL_NAME_ENUMS.click_clock_wood} Autumn Main To {LEVEL_NAME_ENUMS.click_clock_wood} Autumn Nabnut Door",
    0x00EB: f"Warp {LEVEL_NAME_ENUMS.click_clock_wood} Spring Nabnut Door To {LEVEL_NAME_ENUMS.click_clock_wood} Spring Main",
    0x00EC: f"Warp {LEVEL_NAME_ENUMS.click_clock_wood} Summer Nabnut Door To {LEVEL_NAME_ENUMS.click_clock_wood} Summer Main",
    0x00ED: UNKNOWN_STR,
    0x00EF: UNKNOWN_STR,
    0x00F0: UNKNOWN_STR,
    0x00F1: UNKNOWN_STR,
    0x00F9: f"Warp {LEVEL_NAME_ENUMS.treasure_trove_cove} Sharkfood Island To {LEVEL_NAME_ENUMS.treasure_trove_cove} Main",
    0x00FC: f"Warp {LEVEL_NAME_ENUMS.freezeezy_peak} Wozza To {LEVEL_NAME_ENUMS.freezeezy_peak} Main",
    0x00FD: f"Warp {LEVEL_NAME_ENUMS.freezeezy_peak} Main To {LEVEL_NAME_ENUMS.freezeezy_peak} Wozza",
    0x00FE: UNKNOWN_STR,
    0x00FF: UNKNOWN_STR,
    0x0100: UNKNOWN_STR,
    0x0101: UNKNOWN_STR,
    0x0102: UNKNOWN_STR,
    0x0103: UNKNOWN_STR,
    0x0104: UNKNOWN_STR,
    0x0105: UNKNOWN_STR,
    0x0106: UNKNOWN_STR,
    0x0107: UNKNOWN_STR,
    0x0108: UNKNOWN_STR,
    0x0109: UNKNOWN_STR,
    0x010A: UNKNOWN_STR,
    0x010B: UNKNOWN_STR,
    0x010C: UNKNOWN_STR,
    0x010D: f"Warp {LEVEL_NAME_ENUMS.click_clock_wood} Spring Main To {LEVEL_NAME_ENUMS.click_clock_wood} Spring Zubbas",
    0x010E: f"Warp {LEVEL_NAME_ENUMS.click_clock_wood} Summer Main To {LEVEL_NAME_ENUMS.click_clock_wood} Summer Zubbas",
    0x010F: f"Warp {LEVEL_NAME_ENUMS.click_clock_wood} Autumn Main To {LEVEL_NAME_ENUMS.click_clock_wood} Autumn Zubbas",
    0x0110: f"Warp {LEVEL_NAME_ENUMS.click_clock_wood} Spring Zubbas To {LEVEL_NAME_ENUMS.click_clock_wood} Spring Main",
    0x0111: f"Warp {LEVEL_NAME_ENUMS.click_clock_wood} Summer Zubbas To {LEVEL_NAME_ENUMS.click_clock_wood} Summer Main",
    0x0112: UNKNOWN_STR,
    0x0113: UNKNOWN_STR,
    0x0114: UNKNOWN_STR,
    0x0115: UNKNOWN_STR,
    0x0116: UNKNOWN_STR,
    0x0117: UNKNOWN_STR,
    0x0118: f"Warp {LEVEL_NAME_ENUMS.spiral_mountain} Main To {LEVEL_NAME_ENUMS.spiral_mountain} Banjo's House",
    0x0119: f"Warp {LEVEL_NAME_ENUMS.spiral_mountain} Banjo's House To {LEVEL_NAME_ENUMS.spiral_mountain} Main",
    0x011B: UNKNOWN_STR,
    0x011C: f"Warp {LEVEL_NAME_ENUMS.rusty_bucket_bay} Anchor Room To {LEVEL_NAME_ENUMS.rusty_bucket_bay} Main",
    0x011D: f"Warp {LEVEL_NAME_ENUMS.rusty_bucket_bay} Main To {LEVEL_NAME_ENUMS.rusty_bucket_bay} Anchor Room",
    0x011E: f"Warp {LEVEL_NAME_ENUMS.mad_monster_mansion} Main To {LEVEL_NAME_ENUMS.mad_monster_mansion} Well Bottom",
    0x011F: f"Warp {LEVEL_NAME_ENUMS.mad_monster_mansion} Well Bottom To {LEVEL_NAME_ENUMS.mad_monster_mansion} Main",
    0x0120: f"Warp {LEVEL_NAME_ENUMS.mad_monster_mansion} Inside Loggo To {LEVEL_NAME_ENUMS.mad_monster_mansion} Restroom",
    0x0122: UNKNOWN_STR,
    0x0123: f"Warp {LEVEL_NAME_ENUMS.click_clock_wood} Spring Main To {LEVEL_NAME_ENUMS.click_clock_wood} Spring Nabnut Window",
    0x0124: f"Warp {LEVEL_NAME_ENUMS.click_clock_wood} Summer Main To {LEVEL_NAME_ENUMS.click_clock_wood} Summer Nabnut Window",
    0x0125: f"Warp {LEVEL_NAME_ENUMS.click_clock_wood} Autumn Main To {LEVEL_NAME_ENUMS.click_clock_wood} Autumn Nabnut Window",
    0x0126: UNKNOWN_STR,
    0x0127: f"Warp {LEVEL_NAME_ENUMS.click_clock_wood} Spring Nabnut Window To {LEVEL_NAME_ENUMS.click_clock_wood} Spring Main",
    0x0128: f"Warp {LEVEL_NAME_ENUMS.click_clock_wood} Summer Nabnut Window To {LEVEL_NAME_ENUMS.click_clock_wood} Summer Main",
    0x0129: UNKNOWN_STR,
    0x012A: UNKNOWN_STR,
    0x012B: f"Warp {LEVEL_NAME_ENUMS.gobis_valley} Main To {LEVEL_NAME_ENUMS.gobis_valley} Stop N Swap",
    0x012C: f"Warp {LEVEL_NAME_ENUMS.gobis_valley} Stop N Swap To {LEVEL_NAME_ENUMS.gobis_valley} Main",
    0x012D: f"Warp {LEVEL_NAME_ENUMS.spiral_mountain} Main To {LEVEL_NAME_ENUMS.cutscenes} Enter Lair",
    0x8000: UNKNOWN_STR,
    0x8117: UNKNOWN_STR,
    0x9EC8: UNKNOWN_STR,
}

###############################
##### TYPICAL OBJECT DICT #####
###############################

TYPICAL_OBJECT_DICT:dict = {
    0x0000: {
        0b000110010: UNKNOWN_STR,
    },
    0x0001: {
        0b000110010: UNKNOWN_STR,
    },
    0x0002: {
        0b000110010: UNKNOWN_STR,
    },
    0x0004: {
        0b000110010: "Bigbutt",
    },
    0x0005: {
        0b000110010: "Ticker",
    },
    0x0006: {
        0b000110010: "Grublin",
    },
    0x0007: {
        0b000110010: UNKNOWN_STR,
    },
    0x0008: {
        0b000110010: "Conga",
    },
    0x0009: {
        0b000110010: f"{LEVEL_NAME_ENUMS.mumbos_mountain} Breakable Hut",
    },
    0x000A: {
        0b000110010: UNKNOWN_STR,
    },
    0x000B: {
        0b000110010: "Shock Jump Pad",
    },
    0x000C: {
        0b000110010: UNKNOWN_STR,
    },
    0x000F: {
        0b000110010: "Chimpy",
    },
    0x0011: {
        0b000110010: "Ju-Ju",
    },
    0x0012: {
        0b000110010: "Beehive",
    },
    0x0013: {
        0b000110010: UNKNOWN_STR,
    },
    0x0015: {
        0b000010100: UNKNOWN_STR,
        0b000011100: UNKNOWN_STR,
        0b000110010: UNKNOWN_STR,
    },
    0x0016: {
        0b000110010: UNKNOWN_STR,
    },
    0x0017: {
        0b000110010: UNKNOWN_STR,
    },
    0x0018: {
        0b000110010: UNKNOWN_STR,
    },
    0x001A: {
        0b000110010: UNKNOWN_STR,
    },
    0x001B: {
        0b000110010: UNKNOWN_STR,
    },
    0x001E: {
        0b000110010: UNKNOWN_STR,
    },
    0x0020: {
        0b000110010: UNKNOWN_STR,
    },
    0x0021: {
        0b000110010: UNKNOWN_STR,
    },
    0x0022: {
        0b000110010: UNKNOWN_STR,
    },
    0x0023: {
        0b000110010: UNKNOWN_STR,
    },
    0x0025: {
        0b000110010: UNKNOWN_STR,
    },
    0x0026: {
        0b000101101: UNKNOWN_STR,
        0b000110010: UNKNOWN_STR,
        0b000111100: UNKNOWN_STR,
        0b001000001: UNKNOWN_STR,
        0b001000110: UNKNOWN_STR,
        0b001001011: UNKNOWN_STR,
        0b001010000: UNKNOWN_STR,
        0b001010101: UNKNOWN_STR,
        0b001011111: UNKNOWN_STR,
        0b001100100: UNKNOWN_STR,
        0b001101110: UNKNOWN_STR,
        0b001111101: UNKNOWN_STR,
    },
    0x0027: {
        0b000110010: UNKNOWN_STR,
        0b000111100: UNKNOWN_STR,
        0b001000001: UNKNOWN_STR,
        0b001010000: UNKNOWN_STR,
        0b001010101: UNKNOWN_STR,
        0b001100100: UNKNOWN_STR,
        0b001101110: UNKNOWN_STR,
        0b001111101: UNKNOWN_STR,
    },
    0x0028: {
        0b000101101: UNKNOWN_STR,
        0b000110010: UNKNOWN_STR,
        0b000111100: UNKNOWN_STR,
        0b001000110: UNKNOWN_STR,
        0b001100100: UNKNOWN_STR,
    },
    0x0029: {
        0b000110010: "Orange (Collectable)",
    },
    0x002A: {
        0b000110010: UNKNOWN_STR,
    },
    0x002B: {
        0b101111100: UNKNOWN_STR,
    },
    0x002C: {
        0b000000001: UNKNOWN_STR,
        0b000110010: UNKNOWN_STR,
    },
    0x002D: {
        0b000011001: UNKNOWN_STR,
        0b000110010: "Mumbo Token",
    },
    0x002F: {
        0b000110010: UNKNOWN_STR,
    },
    0x0030: {
        0b000110010: UNKNOWN_STR,
    },
    0x0031: {
        0b000110010: UNKNOWN_STR,
    },
    0x0037: {
        0b000110010: UNKNOWN_STR,
    },
    0x0038: {
        0b000110010: UNKNOWN_STR,
    },
    0x0039: {
        0b000110010: UNKNOWN_STR,
    },
    0x003A: {
        0b000110010: UNKNOWN_STR,
    },
    0x003B: {
        0b000110010: UNKNOWN_STR,
    },
    0x003C: {
        0b000110010: UNKNOWN_STR,
    },
    0x003D: {
        0b000110010: UNKNOWN_STR,
    },
    0x003E: {
        0b000110010: UNKNOWN_STR,
    },
    0x0041: {
        0b000110010: UNKNOWN_STR,
    },
    0x0043: {
        0b000110010: UNKNOWN_STR,
    },
    0x0044: {
        0b000110010: UNKNOWN_STR,
    },
    0x0045: {
        0b000110010: UNKNOWN_STR,
    },
    0x0046: {
        0b000101101: UNKNOWN_STR,
        0b000110010: "Jiggy",
    },
    0x0047: {
        0b000101000: UNKNOWN_STR,
        0b000110010: "Empty Honeycomb",
    },
    0x0049: {
        0b000110010: "Extra Life",
    },
    0x0050: {
        0b000110010: UNKNOWN_STR,
    },
    0x0052: {
        0b000110010: UNKNOWN_STR,
    },
    0x0055: {
        0b000110010: UNKNOWN_STR,
    },
    0x0056: {
        0b000110010: "Shrapnel",
    },
    0x0057: {
        0b000110010: "Orange Pad",
    },
    0x005B: {
        0b000110010: UNKNOWN_STR,
    },
    0x005E: {
        0b000110010: "Yellow Jinjo",
    },
    0x005F: {
        0b000110010: "Orange Jinjo",
    },
    0x0060: {
        0b000110010: "Blue Jinjo",
    },
    0x0061: {
        0b000110010: "Magenta Jinjo",
    },
    0x0062: {
        0b000110010: UNKNOWN_STR,
    },
    0x0063: {
        0b000110010: UNKNOWN_STR,
    },
    0x0065: {
        0b000000001: UNKNOWN_STR,
        0b000110010: UNKNOWN_STR,
    },
    0x0066: {
        0b000000001: UNKNOWN_STR,
        0b000000010: UNKNOWN_STR,
        0b000110010: UNKNOWN_STR,
    },
    0x0067: {
        0b000000001: "Snippet",
        0b000110010: "Snippet",
    },
    0x0069: {
        0b000110010: "Yum-Yum",
    },
    0x006A: {
        0b000001010: UNKNOWN_STR,
        0b000010100: UNKNOWN_STR,
        0b000110010: UNKNOWN_STR,
    },
    0x006D: {
        0b000110111: UNKNOWN_STR,
    },
    0x006E: {
        0b000110010: UNKNOWN_STR,
    },
    0x006F: {
        0b000110010: UNKNOWN_STR,
    },
    0x0070: {
        0b000110010: UNKNOWN_STR,
    },
    0x0071: {
        0b000110010: UNKNOWN_STR,
    },
    0x0072: {
        0b000011001: UNKNOWN_STR,
        0b000110010: UNKNOWN_STR,
    },
    0x0073: {
        0b000011001: UNKNOWN_STR,
        0b000110010: UNKNOWN_STR,
    },
    0x0074: {
        0b000110010: UNKNOWN_STR,
    },
    0x0075: {
        0b000110010: UNKNOWN_STR,
    },
    0x0076: {
        0b000011110: UNKNOWN_STR,
        0b000110010: UNKNOWN_STR,
    },
    0x0077: {
        0b000110010: UNKNOWN_STR,
    },
    0x0078: {
        0b000100101: UNKNOWN_STR,
        0b000110010: UNKNOWN_STR,
    },
    0x0079: {
        0b000110010: UNKNOWN_STR,
    },
    0x007A: {
        0b000011111: UNKNOWN_STR,
        0b000110010: UNKNOWN_STR,
    },
    0x007B: {
        0b000110010: UNKNOWN_STR,
    },
    0x007C: {
        0b000110010: UNKNOWN_STR,
    },
    0x007D: {
        0b000100101: UNKNOWN_STR,
        0b000110010: UNKNOWN_STR,
    },
    0x007E: {
        0b000110010: UNKNOWN_STR,
    },
    0x007F: {
        0b000110010: UNKNOWN_STR,
    },
    0x0080: {
        0b000110010: UNKNOWN_STR,
    },
    0x0081: {
        0b000110010: UNKNOWN_STR,
    },
    0x0082: {
        0b000110010: UNKNOWN_STR,
    },
    0x0083: {
        0b000110010: UNKNOWN_STR,
    },
    0x0084: {
        0b000110010: UNKNOWN_STR,
    },
    0x0085: {
        0b000110010: UNKNOWN_STR,
    },
    0x0086: {
        0b000110010: UNKNOWN_STR,
    },
    0x0087: {
        0b000110010: UNKNOWN_STR,
    },
    0x0088: {
        0b000110010: UNKNOWN_STR,
    },
    0x0089: {
        0b000110010: UNKNOWN_STR,
    },
    0x008A: {
        0b000110010: UNKNOWN_STR,
    },
    0x008B: {
        0b000110010: UNKNOWN_STR,
    },
    0x008C: {
        0b000110010: UNKNOWN_STR,
    },
    0x008D: {
        0b000110010: UNKNOWN_STR,
    },
    0x008E: {
        0b000110010: UNKNOWN_STR,
    },
    0x008F: {
        0b000110010: UNKNOWN_STR,
    },
    0x0092: {
        0b000110010: UNKNOWN_STR,
    },
    0x0093: {
        0b000110010: UNKNOWN_STR,
    },
    0x0094: {
        0b000110010: UNKNOWN_STR,
    },
    0x0095: {
        0b000110010: UNKNOWN_STR,
    },
    0x009B: {
        0b000110010: UNKNOWN_STR,
    },
    0x009C: {
        0b000110010: UNKNOWN_STR,
    },
    0x009D: {
        0b000110010: UNKNOWN_STR,
    },
    0x009E: {
        0b000110010: UNKNOWN_STR,
    },
    0x00A5: {
        0b000110010: UNKNOWN_STR,
    },
    0x00A6: {
        0b000110010: UNKNOWN_STR,
    },
    0x00A7: {
        0b000110010: UNKNOWN_STR,
    },
    0x00A8: {
        0b000110010: UNKNOWN_STR,
    },
    0x00A9: {
        0b000110010: UNKNOWN_STR,
    },
    0x00AA: {
        0b000110010: UNKNOWN_STR,
    },
    0x00AB: {
        0b000110010: UNKNOWN_STR,
    },
    0x00AC: {
        0b000110010: UNKNOWN_STR,
    },
    0x00AE: {
        0b000110010: UNKNOWN_STR,
    },
    0x00AF: {
        0b000110010: UNKNOWN_STR,
    },
    0x00B0: {
        0b000010100: UNKNOWN_STR,
        0b000110010: UNKNOWN_STR,
    },
    0x00B1: {
        0b000110010: UNKNOWN_STR,
    },
    0x00B2: {
        0b000110010: UNKNOWN_STR,
    },
    0x00B4: {
        0b000110010: UNKNOWN_STR,
    },
    0x00B5: {
        0b000110010: UNKNOWN_STR,
    },
    0x00B6: {
        0b000110010: UNKNOWN_STR,
    },
    0x00B8: {
        0b000110010: UNKNOWN_STR,
    },
    0x00B9: {
        0b000110010: UNKNOWN_STR,
    },
    0x00BB: {
        0b000110010: UNKNOWN_STR,
    },
    0x00BC: {
        0b000110010: UNKNOWN_STR,
    },
    0x00C0: {
        0b000110010: UNKNOWN_STR,
    },
    0x00C2: {
        0b000110010: UNKNOWN_STR,
    },
    0x00C3: {
        0b000110010: UNKNOWN_STR,
    },
    0x00C5: {
        0b000101110: "Chimpy's Stump",
    },
    0x00C6: {
        0b000110010: UNKNOWN_STR,
    },
    0x00C7: {
        0b000000001: UNKNOWN_STR,
        0b000110010: UNKNOWN_STR,
    },
    0x00CA: {
        0b000110010: UNKNOWN_STR,
    },
    0x00CB: {
        0b000110010: UNKNOWN_STR,
    },
    0x00CC: {
        0b000110010: UNKNOWN_STR,
    },
    0x00CD: {
        0b000110010: UNKNOWN_STR,
    },
    0x00CE: {
        0b000110010: UNKNOWN_STR,
    },
    0x00CF: {
        0b000110010: UNKNOWN_STR,
    },
    0x00D0: {
        0b000110010: UNKNOWN_STR,
    },
    0x00D1: {
        0b000110010: UNKNOWN_STR,
    },
    0x00D2: {
        0b000110010: UNKNOWN_STR,
    },
    0x00D3: {
        0b000110010: UNKNOWN_STR,
    },
    0x00D4: {
        0b000110010: UNKNOWN_STR,
    },
    0x00D5: {
        0b000110010: UNKNOWN_STR,
    },
    0x00D7: {
        0b000110010: UNKNOWN_STR,
    },
    0x00E4: {
        0b000110010: "Flight Pad",
    },
    0x00E6: {
        0b000110010: UNKNOWN_STR,
    },
    0x00E8: {
        0b000110010: UNKNOWN_STR,
    },
    0x00F1: {
        0b000110010: UNKNOWN_STR,
    },
    0x00F2: {
        0b000110010: UNKNOWN_STR,
    },
    0x00F4: {
        0b000000001: UNKNOWN_STR,
    },
    0x00F5: {
        0b000000001: UNKNOWN_STR,
        0b000110010: UNKNOWN_STR,
    },
    0x00F6: {
        0b000110010: UNKNOWN_STR,
    },
    0x00F7: {
        0b000110010: UNKNOWN_STR,
    },
    0x00F9: {
        0b000110010: UNKNOWN_STR,
    },
    0x00FA: {
        0b000110010: UNKNOWN_STR,
    },
    0x00FB: {
        0b000110010: UNKNOWN_STR,
    },
    0x00FC: {
        0b000110010: UNKNOWN_STR,
    },
    0x00FD: {
        0b000110010: UNKNOWN_STR,
    },
    0x00FE: {
        0b000110010: UNKNOWN_STR,
    },
    0x00FF: {
        0b000110010: UNKNOWN_STR,
    },
    0x0100: {
        0b000110010: UNKNOWN_STR,
    },
    0x0101: {
        0b000110010: UNKNOWN_STR,
    },
    0x0102: {
        0b000110010: UNKNOWN_STR,
    },
    0x0103: {
        0b000101001: UNKNOWN_STR,
        0b000110010: UNKNOWN_STR,
    },
    0x0104: {
        0b000110010: UNKNOWN_STR,
    },
    0x0105: {
        0b000110010: UNKNOWN_STR,
    },
    0x0106: {
        0b000110010: UNKNOWN_STR,
    },
    0x0109: {
        0b000110010: UNKNOWN_STR,
    },
    0x010A: {
        0b000110010: UNKNOWN_STR,
    },
    0x010B: {
        0b000110010: UNKNOWN_STR,
    },
    0x010C: {
        0b000110010: UNKNOWN_STR,
    },
    0x010D: {
        0b000110010: UNKNOWN_STR,
    },
    0x010E: {
        0b000011110: UNKNOWN_STR,
    },
    0x010F: {
        0b000110010: UNKNOWN_STR,
    },
    0x0110: {
        0b000110010: UNKNOWN_STR,
    },
    0x0111: {
        0b000110010: UNKNOWN_STR,
    },
    0x0112: {
        0b000110010: UNKNOWN_STR,
    },
    0x0114: {
        0b000110010: UNKNOWN_STR,
    },
    0x0115: {
        0b000110010: "Blubber",
    },
    0x0116: {
        0b000001000: UNKNOWN_STR,
        0b101010101: UNKNOWN_STR,
        0b101010110: UNKNOWN_STR,
    },
    0x0117: {
        0b000110010: UNKNOWN_STR,
    },
    0x0118: {
        0b000000001: UNKNOWN_STR,
    },
    0x0119: {
        0b000110010: UNKNOWN_STR,
    },
    0x011A: {
        0b000110010: UNKNOWN_STR,
    },
    0x011B: {
        0b000110010: UNKNOWN_STR,
    },
    0x011C: {
        0b000110010: UNKNOWN_STR,
    },
    0x011D: {
        0b000110010: UNKNOWN_STR,
    },
    0x011E: {
        0b000101101: UNKNOWN_STR,
    },
    0x0120: {
        0b000110010: UNKNOWN_STR,
    },
    0x0121: {
        0b000110010: UNKNOWN_STR,
    },
    0x0123: {
        0b000110010: UNKNOWN_STR,
    },
    0x0124: {
        0b000110010: UNKNOWN_STR,
        0b000110011: UNKNOWN_STR,
    },
    0x0128: {
        0b000110010: UNKNOWN_STR,
    },
    0x0129: {
        0b000110010: UNKNOWN_STR,
    },
    0x012B: {
        0b000000001: "Bottles Molehill | Tutorial",
        0b000000010: "Bottles Molehill | Camera",
        0b000000011: "Bottles Molehill | Dive",
        0b000000100: "Bottles Molehill | Attack",
        0b000000101: "Bottles Molehill | Beak Barge",
        0b000000110: "Bottles Molehill | Jump",
        0b000000111: "Bottles Molehill | Climb",
        0b000001000: "Bottles Molehill | Bridge",
    },
    0x012E: {
        0b000110010: UNKNOWN_STR,
    },
    0x012F: {
        0b000110010: UNKNOWN_STR,
    },
    0x0130: {
        0b000110010: UNKNOWN_STR,
    },
    0x0131: {
        0b000110010: UNKNOWN_STR,
    },
    0x0132: {
        0b000110010: UNKNOWN_STR,
    },
    0x0133: {
        0b000110010: UNKNOWN_STR,
    },
    0x0134: {
        0b000110010: UNKNOWN_STR,
    },
    0x0135: {
        0b000110010: UNKNOWN_STR,
    },
    0x0136: {
        0b000110010: UNKNOWN_STR,
    },
    0x0137: {
        0b000110010: UNKNOWN_STR,
    },
    0x0138: {
        0b000110010: UNKNOWN_STR,
    },
    0x0139: {
        0b000110010: UNKNOWN_STR,
    },
    0x013A: {
        0b000110010: UNKNOWN_STR,
    },
    0x013B: {
        0b000110010: UNKNOWN_STR,
    },
    0x013E: {
        0b000110010: UNKNOWN_STR,
    },
    0x013F: {
        0b000110010: UNKNOWN_STR,
    },
    0x0140: {
        0b000110010: UNKNOWN_STR,
    },
    0x0142: {
        0b000110010: UNKNOWN_STR,
    },
    0x0143: {
        0b000110010: UNKNOWN_STR,
    },
    0x0144: {
        0b000110010: UNKNOWN_STR,
    },
    0x0145: {
        0b000110010: UNKNOWN_STR,
    },
    0x0146: {
        0b000110010: UNKNOWN_STR,
    },
    0x0147: {
        0b000000001: UNKNOWN_STR,
        0b000000010: UNKNOWN_STR,
        0b000000011: UNKNOWN_STR,
        0b000000100: UNKNOWN_STR,
        0b000000101: UNKNOWN_STR,
    },
    0x0148: {
        0b000110010: UNKNOWN_STR,
    },
    0x0149: {
        0b000110010: UNKNOWN_STR,
    },
    0x014A: {
        0b000110010: UNKNOWN_STR,
    },
    0x014B: {
        0b000110010: UNKNOWN_STR,
    },
    0x014C: {
        0b000110010: UNKNOWN_STR,
    },
    0x014D: {
        0b000110010: UNKNOWN_STR,
    },
    0x014E: {
        0b000110010: UNKNOWN_STR,
    },
    0x0150: {
        0b011001000: UNKNOWN_STR,
    },
    0x0151: {
        0b000110010: "Lockup | Blue Eggs",
    },
    0x0152: {
        0b000110010: "Lockup | Notes And Red Feathers",
    },
    0x0153: {
        0b000001010: "Lockup | Jiggy",
        0b000110010: "Lockup | Mumbo Tokens",
    },
    0x0154: {
        0b000110010: UNKNOWN_STR,
    },
    0x0155: {
        0b000110010: UNKNOWN_STR,
    },
    0x0156: {
        0b000110010: UNKNOWN_STR,
    },
    0x0157: {
        0b000110010: UNKNOWN_STR,
    },
    0x0158: {
        0b000110010: UNKNOWN_STR,
    },
    0x015E: {
        0b000110010: UNKNOWN_STR,
    },
    0x015F: {
        0b000110010: UNKNOWN_STR,
    },
    0x0160: {
        0b000110010: UNKNOWN_STR,
    },
    0x0161: {
        0b000000001: UNKNOWN_STR,
        0b000000010: UNKNOWN_STR,
        0b000000011: UNKNOWN_STR,
        0b000000100: UNKNOWN_STR,
        0b000000101: UNKNOWN_STR,
        0b000000110: UNKNOWN_STR,
        0b000000111: UNKNOWN_STR,
        0b000001000: UNKNOWN_STR,
        0b000001001: UNKNOWN_STR,
        0b000001010: UNKNOWN_STR,
        0b000001011: UNKNOWN_STR,
        0b000001100: UNKNOWN_STR,
        0b000001101: UNKNOWN_STR,
        0b000001110: UNKNOWN_STR,
        0b000001111: UNKNOWN_STR,
        0b000010000: UNKNOWN_STR,
        0b000010001: UNKNOWN_STR,
        0b000010010: UNKNOWN_STR,
        0b000010011: UNKNOWN_STR,
        0b000010100: UNKNOWN_STR,
        0b000010101: UNKNOWN_STR,
        0b000010110: UNKNOWN_STR,
        0b000010111: UNKNOWN_STR,
        0b000011000: UNKNOWN_STR,
        0b000011001: UNKNOWN_STR,
        0b000011010: UNKNOWN_STR,
        0b000011011: UNKNOWN_STR,
        0b000011100: UNKNOWN_STR,
        0b000011101: UNKNOWN_STR,
        0b000011110: UNKNOWN_STR,
        0b000011111: UNKNOWN_STR,
        0b000100000: UNKNOWN_STR,
        0b000100001: UNKNOWN_STR,
        0b000100010: UNKNOWN_STR,
        0b000100011: UNKNOWN_STR,
        0b000100100: UNKNOWN_STR,
        0b000100101: UNKNOWN_STR,
        0b000100110: UNKNOWN_STR,
        0b000100111: UNKNOWN_STR,
    },
    0x0162: {
        0b000000001: UNKNOWN_STR,
        0b000000010: UNKNOWN_STR,
        0b000000011: UNKNOWN_STR,
        0b000000100: UNKNOWN_STR,
        0b000000101: UNKNOWN_STR,
        0b000000110: UNKNOWN_STR,
        0b000000111: UNKNOWN_STR,
        0b000001000: UNKNOWN_STR,
        0b000001001: UNKNOWN_STR,
        0b000001010: UNKNOWN_STR,
        0b000001011: UNKNOWN_STR,
        0b000001100: UNKNOWN_STR,
        0b000001101: UNKNOWN_STR,
        0b000001110: UNKNOWN_STR,
        0b000001111: UNKNOWN_STR,
        0b000010000: UNKNOWN_STR,
        0b000010001: UNKNOWN_STR,
        0b000010010: UNKNOWN_STR,
        0b000010011: UNKNOWN_STR,
        0b000010100: UNKNOWN_STR,
        0b000010101: UNKNOWN_STR,
        0b000010110: UNKNOWN_STR,
        0b000010111: UNKNOWN_STR,
        0b000011000: UNKNOWN_STR,
        0b000011001: UNKNOWN_STR,
        0b000011010: UNKNOWN_STR,
        0b000011011: UNKNOWN_STR,
        0b000011100: UNKNOWN_STR,
        0b000011101: UNKNOWN_STR,
        0b000011110: UNKNOWN_STR,
        0b000011111: UNKNOWN_STR,
        0b000100000: UNKNOWN_STR,
        0b000100001: UNKNOWN_STR,
        0b000100010: UNKNOWN_STR,
        0b000100011: UNKNOWN_STR,
        0b000100100: UNKNOWN_STR,
        0b000100101: UNKNOWN_STR,
        0b000100110: UNKNOWN_STR,
        0b000100111: UNKNOWN_STR,
    },
    0x0163: {
        0b000110010: UNKNOWN_STR,
    },
    0x0167: {
        0b000110010: UNKNOWN_STR,
    },
    0x0168: {
        0b000110010: UNKNOWN_STR,
    },
    0x0169: {
        0b000110010: UNKNOWN_STR,
    },
    0x016A: {
        0b000110010: UNKNOWN_STR,
    },
    0x016B: {
        0b000110010: UNKNOWN_STR,
    },
    0x016C: {
        0b000110010: UNKNOWN_STR,
    },
    0x016D: {
        0b000110010: UNKNOWN_STR,
    },
    0x016E: {
        0b000110010: UNKNOWN_STR,
    },
    0x016F: {
        0b000110010: "Quarrie",
    },
    0x0172: {
        0b000110010: UNKNOWN_STR,
    },
    0x0173: {
        0b000110010: UNKNOWN_STR,
    },
    0x0174: {
        0b000110010: UNKNOWN_STR,
    },
    0x0175: {
        0b000110010: UNKNOWN_STR,
    },
    0x0176: {
        0b000110010: UNKNOWN_STR,
    },
    0x0177: {
        0b000110010: UNKNOWN_STR,
    },
    0x0178: {
        0b000110010: UNKNOWN_STR,
    },
    0x0179: {
        0b000110010: UNKNOWN_STR,
    },
    0x017A: {
        0b000110010: UNKNOWN_STR,
    },
    0x017B: {
        0b000110010: UNKNOWN_STR,
    },
    0x017C: {
        0b000110010: UNKNOWN_STR,
    },
    0x017D: {
        0b000110010: UNKNOWN_STR,
    },
    0x017E: {
        0b000110010: UNKNOWN_STR,
    },
    0x017F: {
        0b000110010: UNKNOWN_STR,
    },
    0x0180: {
        0b000110010: UNKNOWN_STR,
    },
    0x0181: {
        0b000110010: UNKNOWN_STR,
    },
    0x0182: {
        0b000110010: UNKNOWN_STR,
    },
    0x0183: {
        0b000110010: UNKNOWN_STR,
    },
    0x0184: {
        0b000110010: UNKNOWN_STR,
    },
    0x0185: {
        0b000110010: UNKNOWN_STR,
    },
    0x018B: {
        0b000110010: UNKNOWN_STR,
    },
    0x018F: {
        0b000110010: UNKNOWN_STR,
    },
    0x0190: {
        0b000110010: UNKNOWN_STR,
    },
    0x0191: {
        0b000110010: UNKNOWN_STR,
    },
    0x0192: {
        0b000110010: UNKNOWN_STR,
    },
    0x0193: {
        0b000110010: UNKNOWN_STR,
    },
    0x0194: {
        0b000110010: UNKNOWN_STR,
    },
    0x0195: {
        0b000110010: UNKNOWN_STR,
    },
    0x0196: {
        0b000110010: UNKNOWN_STR,
    },
    0x0197: {
        0b000110010: UNKNOWN_STR,
    },
    0x019E: {
        0b000110010: UNKNOWN_STR,
    },
    0x019F: {
        0b000110010: UNKNOWN_STR,
    },
    0x01A0: {
        0b000110010: UNKNOWN_STR,
    },
    0x01A1: {
        0b000110010: UNKNOWN_STR,
    },
    0x01A2: {
        0b000110010: UNKNOWN_STR,
    },
    0x01A3: {
        0b000110010: UNKNOWN_STR,
    },
    0x01A4: {
        0b000110010: UNKNOWN_STR,
    },
    0x01A5: {
        0b000110010: UNKNOWN_STR,
    },
    0x01A6: {
        0b000110010: UNKNOWN_STR,
    },
    0x01A7: {
        0b000110010: UNKNOWN_STR,
    },
    0x01A8: {
        0b000110010: UNKNOWN_STR,
    },
    0x01A9: {
        0b000110010: UNKNOWN_STR,
    },
    0x01AB: {
        0b000110010: UNKNOWN_STR,
    },
    0x01AC: {
        0b000110010: UNKNOWN_STR,
    },
    0x01AD: {
        0b000110010: UNKNOWN_STR,
    },
    0x01AE: {
        0b000110010: UNKNOWN_STR,
    },
    0x01AF: {
        0b000110010: UNKNOWN_STR,
    },
    0x01B0: {
        0b000110010: UNKNOWN_STR,
    },
    0x01BB: {
        0b000110010: UNKNOWN_STR,
    },
    0x01BC: {
        0b000110010: UNKNOWN_STR,
    },
    0x01BD: {
        0b000110010: UNKNOWN_STR,
    },
    0x01BE: {
        0b000110010: UNKNOWN_STR,
    },
    0x01BF: {
        0b000110010: UNKNOWN_STR,
    },
    0x01C0: {
        0b000110010: UNKNOWN_STR,
    },
    0x01C1: {
        0b000110010: UNKNOWN_STR,
    },
    0x01C2: {
        0b000110010: UNKNOWN_STR,
    },
    0x01C3: {
        0b000110010: UNKNOWN_STR,
    },
    0x01C4: {
        0b000110010: UNKNOWN_STR,
    },
    0x01C5: {
        0b000110010: UNKNOWN_STR,
    },
    0x01C6: {
        0b000000001: UNKNOWN_STR,
        0b000110010: UNKNOWN_STR,
    },
    0x01C7: {
        0b000110010: UNKNOWN_STR,
    },
    0x01C8: {
        0b000110010: UNKNOWN_STR,
    },
    0x01C9: {
        0b000110010: UNKNOWN_STR,
    },
    0x01CA: {
        0b000110010: UNKNOWN_STR,
    },
    0x01CB: {
        0b000110010: UNKNOWN_STR,
    },
    0x01CC: {
        0b000110010: UNKNOWN_STR,
    },
    0x01CD: {
        0b000110010: UNKNOWN_STR,
    },
    0x01CE: {
        0b000110010: UNKNOWN_STR,
    },
    0x01CF: {
        0b000110010: UNKNOWN_STR,
    },
    0x01D1: {
        0b000110010: UNKNOWN_STR,
    },
    0x01D5: {
        0b000110010: UNKNOWN_STR,
    },
    0x01D6: {
        0b000110010: UNKNOWN_STR,
    },
    0x01D7: {
        0b000110010: UNKNOWN_STR,
    },
    0x01D8: {
        0b000110010: UNKNOWN_STR,
    },
    0x01D9: {
        0b000110010: UNKNOWN_STR,
    },
    0x01DA: {
        0b000110010: UNKNOWN_STR,
    },
    0x01E1: {
        0b000110010: UNKNOWN_STR,
    },
    0x01E2: {
        0b000110010: UNKNOWN_STR,
    },
    0x01E3: {
        0b000110010: UNKNOWN_STR,
    },
    0x01E4: {
        0b000110010: UNKNOWN_STR,
    },
    0x01E6: {
        0b000101100: UNKNOWN_STR,
    },
    0x01E7: {
        0b000000011: UNKNOWN_STR,
        0b000000100: UNKNOWN_STR,
        0b000000111: UNKNOWN_STR,
        0b000001010: UNKNOWN_STR,
        0b000001100: UNKNOWN_STR,
        0b000001111: UNKNOWN_STR,
        0b000010000: UNKNOWN_STR,
        0b000010001: UNKNOWN_STR,
        0b000010010: UNKNOWN_STR,
        0b000010011: UNKNOWN_STR,
        0b000101010: UNKNOWN_STR,
        0b000101011: UNKNOWN_STR,
        0b000101100: UNKNOWN_STR,
        0b000101101: UNKNOWN_STR,
    },
    0x01E8: {
        0b000110010: UNKNOWN_STR,
    },
    0x01E9: {
        0b000000110: UNKNOWN_STR,
        0b000110010: UNKNOWN_STR,
    },
    0x01EA: {
        0b000110010: UNKNOWN_STR,
    },
    0x01EB: {
        0b000110010: UNKNOWN_STR,
    },
    0x01EC: {
        0b000110010: UNKNOWN_STR,
    },
    0x01ED: {
        0b000110010: UNKNOWN_STR,
    },
    0x01EE: {
        0b000110010: UNKNOWN_STR,
    },
    0x01EF: {
        0b000110010: UNKNOWN_STR,
    },
    0x01F0: {
        0b000110010: UNKNOWN_STR,
    },
    0x01F1: {
        0b000110010: UNKNOWN_STR,
    },
    0x01F2: {
        0b000110010: UNKNOWN_STR,
    },
    0x01F3: {
        0b000110010: UNKNOWN_STR,
    },
    0x01F4: {
        0b000110010: UNKNOWN_STR,
    },
    0x01F5: {
        0b000110010: UNKNOWN_STR,
    },
    0x01F6: {
        0b000011001: UNKNOWN_STR,
        0b000110010: UNKNOWN_STR,
    },
    0x01F7: {
        0b000110010: UNKNOWN_STR,
    },
    0x01F9: {
        0b000110010: UNKNOWN_STR,
    },
    0x01FA: {
        0b000000001: UNKNOWN_STR,
        0b000000010: UNKNOWN_STR,
        0b000000011: UNKNOWN_STR,
        0b000000100: UNKNOWN_STR,
        0b000000101: UNKNOWN_STR,
    },
    0x01FB: {
        0b000110010: UNKNOWN_STR,
    },
    0x01FC: {
        0b000110010: UNKNOWN_STR,
    },
    0x01FD: {
        0b000110010: UNKNOWN_STR,
    },
    0x01FE: {
        0b000110010: UNKNOWN_STR,
    },
    0x0201: {
        0b000110010: UNKNOWN_STR,
    },
    0x0202: {
        0b000110010: UNKNOWN_STR,
    },
    0x0203: {
        0b000000001: UNKNOWN_STR,
        0b000000010: UNKNOWN_STR,
        0b000000011: UNKNOWN_STR,
        0b000000100: UNKNOWN_STR,
        0b000000101: UNKNOWN_STR,
        0b000000110: UNKNOWN_STR,
        0b000000111: UNKNOWN_STR,
        0b000001000: UNKNOWN_STR,
        0b000001001: UNKNOWN_STR,
        0b000001010: UNKNOWN_STR,
        0b000001011: UNKNOWN_STR,
        0b000001100: UNKNOWN_STR,
    },
    0x0204: {
        0b000110010: f"Witch Switch | {LEVEL_NAME_ENUMS.mumbos_mountain}",
    },
    0x0205: {
        0b000110010: UNKNOWN_STR,
    },
    0x0206: {
        0b000110010: UNKNOWN_STR,
    },
    0x0207: {
        0b000110010: UNKNOWN_STR,
    },
    0x0208: {
        0b000110010: f"Witch Switch | {LEVEL_NAME_ENUMS.treasure_trove_cove}",
    },
    0x0209: {
        0b000110010: UNKNOWN_STR,
    },
    0x020A: {
        0b000110010: UNKNOWN_STR,
    },
    0x020B: {
        0b000110010: UNKNOWN_STR,
    },
    0x020C: {
        0b000110010: UNKNOWN_STR,
    },
    0x020D: {
        0b000000001: UNKNOWN_STR,
        0b000000010: UNKNOWN_STR,
    },
    0x020E: {
        0b000110010: UNKNOWN_STR,
    },
    0x020F: {
        0b000110010: UNKNOWN_STR,
    },
    0x0210: {
        0b000110010: UNKNOWN_STR,
    },
    0x0211: {
        0b000110010: UNKNOWN_STR,
    },
    0x0212: {
        0b000110010: UNKNOWN_STR,
    },
    0x0213: {
        0b000110010: UNKNOWN_STR,
    },
    0x0214: {
        0b000110010: UNKNOWN_STR,
    },
    0x0215: {
        0b000110010: UNKNOWN_STR,
    },
    0x0216: {
        0b000110010: UNKNOWN_STR,
    },
    0x0217: {
        0b000110010: UNKNOWN_STR,
    },
    0x0218: {
        0b000110010: UNKNOWN_STR,
    },
    0x0219: {
        0b000110010: UNKNOWN_STR,
    },
    0x021A: {
        0b000110010: UNKNOWN_STR,
    },
    0x021B: {
        0b000110010: UNKNOWN_STR,
    },
    0x021C: {
        0b000110010: UNKNOWN_STR,
    },
    0x021D: {
        0b000110010: UNKNOWN_STR,
    },
    0x021E: {
        0b000110010: UNKNOWN_STR,
    },
    0x021F: {
        0b000110010: UNKNOWN_STR,
    },
    0x0220: {
        0b000110010: UNKNOWN_STR,
    },
    0x0221: {
        0b000110010: UNKNOWN_STR,
    },
    0x0222: {
        0b000110010: UNKNOWN_STR,
    },
    0x0223: {
        0b000110010: UNKNOWN_STR,
    },
    0x0224: {
        0b000110010: UNKNOWN_STR,
    },
    0x0225: {
        0b001011000: UNKNOWN_STR,
    },
    0x0226: {
        0b000110010: UNKNOWN_STR,
    },
    0x0227: {
        0b000110010: UNKNOWN_STR,
    },
    0x0228: {
        0b000110010: UNKNOWN_STR,
    },
    0x0229: {
        0b000000001: UNKNOWN_STR,
        0b000110010: UNKNOWN_STR,
    },
    0x022A: {
        0b000010100: UNKNOWN_STR,
        0b000110010: UNKNOWN_STR,
    },
    0x022B: {
        0b000110010: UNKNOWN_STR,
    },
    0x022C: {
        0b000110010: UNKNOWN_STR,
    },
    0x0230: {
        0b000000001: UNKNOWN_STR,
        0b000000010: UNKNOWN_STR,
    },
    0x0231: {
        0b000110010: UNKNOWN_STR,
    },
    0x0233: {
        0b000110010: UNKNOWN_STR,
    },
    0x0234: {
        0b000110010: UNKNOWN_STR,
    },
    0x0235: {
        0b000110010: UNKNOWN_STR,
    },
    0x0236: {
        0b000110010: UNKNOWN_STR,
    },
    0x0237: {
        0b000110010: UNKNOWN_STR,
    },
    0x0238: {
        0b000110010: UNKNOWN_STR,
    },
    0x0239: {
        0b000110010: UNKNOWN_STR,
    },
    0x023A: {
        0b000110010: UNKNOWN_STR,
    },
    0x023B: {
        0b000000001: UNKNOWN_STR,
        0b000000010: UNKNOWN_STR,
        0b000000011: UNKNOWN_STR,
        0b000000100: UNKNOWN_STR,
        0b000000101: UNKNOWN_STR,
        0b000000110: UNKNOWN_STR,
        0b000001001: UNKNOWN_STR,
        0b000001010: UNKNOWN_STR,
    },
    0x023C: {
        0b000110010: UNKNOWN_STR,
    },
    0x023D: {
        0b000000101: UNKNOWN_STR,
        0b000001010: UNKNOWN_STR,
        0b000001111: UNKNOWN_STR,
        0b000010100: UNKNOWN_STR,
        0b000011001: UNKNOWN_STR,
        0b000110010: UNKNOWN_STR,
    },
    0x023E: {
        0b000110010: UNKNOWN_STR,
    },
    0x023F: {
        0b000110010: UNKNOWN_STR,
    },
    0x0240: {
        0b000110010: UNKNOWN_STR,
    },
    0x0241: {
        0b000110010: UNKNOWN_STR,
    },
    0x0242: {
        0b000110010: UNKNOWN_STR,
        0b010101011: UNKNOWN_STR,
    },
    0x0243: {
        0b000110010: UNKNOWN_STR,
    },
    0x0244: {
        0b000110010: UNKNOWN_STR,
    },
    0x0245: {
        0b000110010: UNKNOWN_STR,
    },
    0x0246: {
        0b000110010: UNKNOWN_STR,
    },
    0x0247: {
        0b000110010: UNKNOWN_STR,
    },
    0x0248: {
        0b000110010: UNKNOWN_STR,
    },
    0x0249: {
        0b100100111: UNKNOWN_STR,
    },
    0x0253: {
        0b000010100: UNKNOWN_STR,
    },
    0x0254: {
        0b000010100: UNKNOWN_STR,
    },
    0x0255: {
        0b000110010: UNKNOWN_STR,
    },
    0x0256: {
        0b000110010: UNKNOWN_STR,
    },
    0x0257: {
        0b000110010: UNKNOWN_STR,
    },
    0x0259: {
        0b000110010: UNKNOWN_STR,
    },
    0x025B: {
        0b000110010: UNKNOWN_STR,
    },
    0x025C: {
        0b000110010: "Sharkfood Island",
    },
    0x025D: {
        0b000110010: UNKNOWN_STR,
    },
    0x025E: {
        0b000000001: UNKNOWN_STR,
        0b000000010: UNKNOWN_STR,
        0b000000011: UNKNOWN_STR,
        0b000000100: UNKNOWN_STR,
        0b000000101: UNKNOWN_STR,
        0b000000110: UNKNOWN_STR,
    },
    0x0261: {
        0b000110010: UNKNOWN_STR,
    },
    0x0262: {
        0b000110010: UNKNOWN_STR,
    },
    0x0263: {
        0b000110010: UNKNOWN_STR,
    },
    0x0264: {
        0b000110010: UNKNOWN_STR,
    },
    0x0265: {
        0b000110010: UNKNOWN_STR,
    },
    0x0266: {
        0b000110010: UNKNOWN_STR,
    },
    0x0267: {
        0b000110010: UNKNOWN_STR,
    },
    0x0268: {
        0b000110010: UNKNOWN_STR,
    },
    0x0269: {
        0b000110010: UNKNOWN_STR,
    },
    0x026A: {
        0b000110010: UNKNOWN_STR,
    },
    0x026B: {
        0b000110010: UNKNOWN_STR,
    },
    0x026C: {
        0b000110010: UNKNOWN_STR,
    },
    0x026D: {
        0b000110010: UNKNOWN_STR,
    },
    0x026E: {
        0b000110010: UNKNOWN_STR,
    },
    0x026F: {
        0b000110010: UNKNOWN_STR,
    },
    0x027A: {
        0b000110010: UNKNOWN_STR,
    },
    0x027B: {
        0b000110010: UNKNOWN_STR,
    },
    0x027C: {
        0b000110010: UNKNOWN_STR,
    },
    0x027D: {
        0b000110010: UNKNOWN_STR,
    },
    0x027E: {
        0b000110010: UNKNOWN_STR,
    },
    0x027F: {
        0b000110010: UNKNOWN_STR,
    },
    0x0280: {
        0b000110010: UNKNOWN_STR,
    },
    0x0285: {
        0b000110010: UNKNOWN_STR,
    },
    0x0286: {
        0b000110010: UNKNOWN_STR,
    },
    0x0287: {
        0b000110010: UNKNOWN_STR,
    },
    0x0288: {
        0b000110010: UNKNOWN_STR,
    },
    0x028A: {
        0b000000001: UNKNOWN_STR,
        0b000110010: UNKNOWN_STR,
    },
    0x028B: {
        0b000110010: UNKNOWN_STR,
    },
    0x028C: {
        0b000110010: UNKNOWN_STR,
    },
    0x028D: {
        0b000110010: UNKNOWN_STR,
    },
    0x028E: {
        0b000110010: UNKNOWN_STR,
    },
    0x0292: {
        0b000110010: UNKNOWN_STR,
    },
    0x0296: {
        0b000110010: UNKNOWN_STR,
    },
    0x0297: {
        0b000110010: UNKNOWN_STR,
    },
    0x0298: {
        0b000110010: UNKNOWN_STR,
    },
    0x0299: {
        0b000110010: UNKNOWN_STR,
    },
    0x029C: {
        0b000110010: UNKNOWN_STR,
    },
    0x029D: {
        0b000110010: UNKNOWN_STR,
    },
    0x029E: {
        0b000110010: UNKNOWN_STR,
    },
    0x029F: {
        0b000000001: UNKNOWN_STR,
        0b000110010: UNKNOWN_STR,
    },
    0x02A0: {
        0b000110010: UNKNOWN_STR,
    },
    0x02A1: {
        0b000110010: UNKNOWN_STR,
    },
    0x02A2: {
        0b000110010: UNKNOWN_STR,
    },
    0x02A3: {
        0b000110010: UNKNOWN_STR,
    },
    0x02A4: {
        0b000110010: UNKNOWN_STR,
    },
    0x02A5: {
        0b000110010: UNKNOWN_STR,
    },
    0x02A6: {
        0b000110010: UNKNOWN_STR,
    },
    0x02A7: {
        0b000110010: UNKNOWN_STR,
    },
    0x02A8: {
        0b000110010: UNKNOWN_STR,
    },
    0x02A9: {
        0b000110010: UNKNOWN_STR,
    },
    0x02AA: {
        0b000110010: UNKNOWN_STR,
    },
    0x02AB: {
        0b000110010: UNKNOWN_STR,
    },
    0x02AC: {
        0b000110010: UNKNOWN_STR,
    },
    0x02AD: {
        0b000110010: UNKNOWN_STR,
    },
    0x02AE: {
        0b000110010: UNKNOWN_STR,
    },
    0x02AF: {
        0b000110010: UNKNOWN_STR,
    },
    0x02B0: {
        0b000110010: UNKNOWN_STR,
    },
    0x02B1: {
        0b000110010: UNKNOWN_STR,
    },
    0x02B2: {
        0b000110010: UNKNOWN_STR,
    },
    0x02B3: {
        0b000110010: UNKNOWN_STR,
    },
    0x02D8: {
        0b000110010: UNKNOWN_STR,
    },
    0x02DB: {
        0b000000111: UNKNOWN_STR,
    },
    0x02DC: {
        0b000110010: UNKNOWN_STR,
    },
    0x02DD: {
        0b000110010: UNKNOWN_STR,
    },
    0x02DE: {
        0b000110010: UNKNOWN_STR,
    },
    0x02E0: {
        0b000110010: UNKNOWN_STR,
    },
    0x02E1: {
        0b000110010: UNKNOWN_STR,
    },
    0x02E2: {
        0b011001101: "Lighthouse",
    },
    0x02E3: {
        0b000000001: UNKNOWN_STR,
        0b000000010: UNKNOWN_STR,
        0b000000011: UNKNOWN_STR,
        0b000000100: UNKNOWN_STR,
        0b000000101: UNKNOWN_STR,
        0b000000110: UNKNOWN_STR,
        0b000000111: UNKNOWN_STR,
        0b000001000: UNKNOWN_STR,
        0b000001001: UNKNOWN_STR,
    },
    0x02E4: {
        0b000000001: UNKNOWN_STR,
        0b000000010: UNKNOWN_STR,
        0b000000011: UNKNOWN_STR,
        0b000000100: UNKNOWN_STR,
        0b000000101: UNKNOWN_STR,
        0b000000110: UNKNOWN_STR,
        0b000000111: UNKNOWN_STR,
        0b000001000: UNKNOWN_STR,
        0b000001001: UNKNOWN_STR,
    },
    0x02E5: {
        0b000110010: UNKNOWN_STR,
    },
    0x02E6: {
        0b000110010: UNKNOWN_STR,
    },
    0x02E7: {
        0b000110010: UNKNOWN_STR,
    },
    0x02E8: {
        0b000110010: UNKNOWN_STR,
    },
    0x02E9: {
        0b000110010: UNKNOWN_STR,
    },
    0x02EA: {
        0b000110010: UNKNOWN_STR,
    },
    0x02ED: {
        0b000110010: UNKNOWN_STR,
    },
    0x02EE: {
        0b000110010: UNKNOWN_STR,
    },
    0x02EF: {
        0b000110010: UNKNOWN_STR,
    },
    0x02F0: {
        0b000110010: UNKNOWN_STR,
    },
    0x02F1: {
        0b000110010: UNKNOWN_STR,
    },
    0x02F2: {
        0b000110010: UNKNOWN_STR,
    },
    0x02F3: {
        0b000110010: UNKNOWN_STR,
    },
    0x02F4: {
        0b000110010: UNKNOWN_STR,
    },
    0x02F5: {
        0b000110010: UNKNOWN_STR,
    },
    0x02FA: {
        0b000110010: UNKNOWN_STR,
    },
    0x02FB: {
        0b000110010: UNKNOWN_STR,
    },
    0x02FC: {
        0b000110010: UNKNOWN_STR,
    },
    0x02FE: {
        0b000110010: UNKNOWN_STR,
    },
    0x02FF: {
        0b000110010: UNKNOWN_STR,
        0b000110011: UNKNOWN_STR,
    },
    0x0300: {
        0b000110010: UNKNOWN_STR,
    },
    0x0301: {
        0b000110010: UNKNOWN_STR,
    },
    0x0302: {
        0b000110010: UNKNOWN_STR,
    },
    0x030B: {
        0b000110010: UNKNOWN_STR,
    },
    0x030D: {
        0b000110010: UNKNOWN_STR,
    },
    0x030E: {
        0b000110010: UNKNOWN_STR,
    },
    0x030F: {
        0b000000001: UNKNOWN_STR,
        0b000110010: UNKNOWN_STR,
    },
    0x0310: {
        0b000110010: UNKNOWN_STR,
    },
    0x0311: {
        0b000110010: UNKNOWN_STR,
    },
    0x0312: {
        0b000110010: UNKNOWN_STR,
    },
    0x0313: {
        0b000110010: UNKNOWN_STR,
    },
    0x0314: {
        0b000110010: UNKNOWN_STR,
    },
    0x0315: {
        0b000110010: UNKNOWN_STR,
    },
    0x0316: {
        0b000110010: UNKNOWN_STR,
    },
    0x0317: {
        0b000110010: UNKNOWN_STR,
    },
    0x0318: {
        0b000110010: UNKNOWN_STR,
    },
    0x0319: {
        0b000110010: UNKNOWN_STR,
    },
    0x031A: {
        0b000110010: UNKNOWN_STR,
    },
    0x031B: {
        0b000110010: UNKNOWN_STR,
    },
    0x031C: {
        0b000110010: UNKNOWN_STR,
    },
    0x031D: {
        0b000110010: UNKNOWN_STR,
    },
    0x032B: {
        0b000110010: UNKNOWN_STR,
    },
    0x032C: {
        0b000110010: UNKNOWN_STR,
    },
    0x032D: {
        0b000110010: UNKNOWN_STR,
    },
    0x032E: {
        0b000110010: UNKNOWN_STR,
    },
    0x032F: {
        0b000110010: UNKNOWN_STR,
    },
    0x0330: {
        0b000110010: UNKNOWN_STR,
    },
    0x0331: {
        0b000110010: UNKNOWN_STR,
    },
    0x0336: {
        0b000110010: UNKNOWN_STR,
    },
    0x0337: {
        0b000000010: UNKNOWN_STR,
    },
    0x033A: {
        0b000110010: UNKNOWN_STR,
    },
    0x033B: {
        0b000110010: UNKNOWN_STR,
    },
    0x033C: {
        0b000110010: UNKNOWN_STR,
    },
    0x033D: {
        0b000110010: UNKNOWN_STR,
    },
    0x033E: {
        0b000110010: UNKNOWN_STR,
    },
    0x033F: {
        0b000110010: UNKNOWN_STR,
    },
    0x0340: {
        0b000110010: UNKNOWN_STR,
    },
    0x0341: {
        0b000101000: UNKNOWN_STR,
    },
    0x0348: {
        0b000000001: UNKNOWN_STR,
        0b000000010: UNKNOWN_STR,
        0b000000011: UNKNOWN_STR,
        0b000000100: UNKNOWN_STR,
        0b000000101: UNKNOWN_STR,
        0b000000110: UNKNOWN_STR,
        0b000000111: UNKNOWN_STR,
        0b000001000: UNKNOWN_STR,
        0b000001001: UNKNOWN_STR,
        0b000001010: UNKNOWN_STR,
    },
    0x0349: {
        0b011111010: UNKNOWN_STR,
        0b100101100: UNKNOWN_STR,
        0b110000110: UNKNOWN_STR,
    },
    0x034D: {
        0b000001111: UNKNOWN_STR,
        0b000010100: UNKNOWN_STR,
        0b000010110: UNKNOWN_STR,
        0b000011001: UNKNOWN_STR,
        0b000011110: UNKNOWN_STR,
    },
    0x034E: {
        0b000110010: UNKNOWN_STR,
    },
    0x034F: {
        0b000110010: UNKNOWN_STR,
    },
    0x0350: {
        0b000110010: UNKNOWN_STR,
    },
    0x0351: {
        0b000110010: UNKNOWN_STR,
    },
    0x0353: {
        0b000000001: UNKNOWN_STR,
    },
    0x0354: {
        0b000110010: UNKNOWN_STR,
    },
    0x0355: {
        0b000110010: UNKNOWN_STR,
    },
    0x0356: {
        0b000110010: UNKNOWN_STR,
    },
    0x0357: {
        0b000110010: UNKNOWN_STR,
    },
    0x0358: {
        0b000110010: UNKNOWN_STR,
    },
    0x0359: {
        0b000000001: UNKNOWN_STR,
    },
    0x035A: {
        0b000000001: UNKNOWN_STR,
    },
    0x035B: {
        0b000000001: UNKNOWN_STR,
    },
    0x035C: {
        0b000000001: UNKNOWN_STR,
    },
    0x0361: {
        0b000110010: UNKNOWN_STR,
    },
    0x0362: {
        0b000110010: UNKNOWN_STR,
    },
    0x0363: {
        0b000110010: UNKNOWN_STR,
    },
    0x0364: {
        0b000110010: UNKNOWN_STR,
    },
    0x0365: {
        0b000110010: UNKNOWN_STR,
    },
    0x0366: {
        0b000110010: UNKNOWN_STR,
    },
    0x0367: {
        0b000110010: UNKNOWN_STR,
    },
    0x0368: {
        0b000110010: UNKNOWN_STR,
    },
    0x0369: {
        0b000110010: UNKNOWN_STR,
    },
    0x036A: {
        0b000110010: UNKNOWN_STR,
    },
    0x036B: {
        0b000110010: UNKNOWN_STR,
    },
    0x036C: {
        0b000110010: UNKNOWN_STR,
    },
    0x036D: {
        0b000110010: "Colliwobble (Not Tutorial)",
    },
    0x036E: {
        0b000110010: "Bawl (Not Tutorial)",
    },
    0x036F: {
        0b000110010: "Topper (Not Tutorial)",
    },
    0x0370: {
        0b000110010: UNKNOWN_STR,
    },
    0x0372: {
        0b000110010: UNKNOWN_STR,
    },
    0x0373: {
        0b000000001: UNKNOWN_STR,
        0b000000010: UNKNOWN_STR,
        0b000000011: UNKNOWN_STR,
        0b000000100: UNKNOWN_STR,
        0b000000101: UNKNOWN_STR,
        0b000000110: UNKNOWN_STR,
        0b000000111: UNKNOWN_STR,
        0b000001000: UNKNOWN_STR,
        0b000001001: UNKNOWN_STR,
    },
    0x0374: {
        0b000110010: UNKNOWN_STR,
    },
    0x0375: {
        0b000110010: UNKNOWN_STR,
    },
    0x0376: {
        0b000110010: UNKNOWN_STR,
    },
    0x0377: {
        0b000110010: UNKNOWN_STR,
    },
    0x0379: {
        0b000000001: UNKNOWN_STR,
        0b000000010: UNKNOWN_STR,
        0b000000011: UNKNOWN_STR,
        0b000000100: UNKNOWN_STR,
        0b000000101: UNKNOWN_STR,
        0b000000110: UNKNOWN_STR,
        0b000000111: UNKNOWN_STR,
        0b000001000: UNKNOWN_STR,
        0b000001001: UNKNOWN_STR,
        0b000001010: UNKNOWN_STR,
        0b000001011: UNKNOWN_STR,
        0b000001100: UNKNOWN_STR,
        0b000001101: UNKNOWN_STR,
        0b000001110: UNKNOWN_STR,
        0b000110010: UNKNOWN_STR,
    },
    0x037A: {
        0b000001001: "Bottles Molehill | Beak Bomb",
        0b000001010: "Bottles Molehill | Egg Firing",
        0b000001011: "Bottles Molehill | Beak Buster",
        0b000001100: "Bottles Molehill | Talon Trot",
        0b000001101: "Bottles Molehill | Shock Jump",
        0b000001110: "Bottles Molehill | Flight",
        0b000001111: "Bottles Molehill | Wonderwing",
        0b000010000: "Bottles Molehill | Stilt Stride",
        0b000010001: "Bottles Molehill | Turbo Talon Trot",
        0b000010010: "Bottles Molehill | Open Notedoors",
    },
    0x037B: {
        0b000110010: UNKNOWN_STR,
    },
    0x037C: {
        0b000000100: UNKNOWN_STR,
        0b000000110: UNKNOWN_STR,
    },
    0x037D: {
        0b000000010: UNKNOWN_STR,
        0b000110010: UNKNOWN_STR,
    },
    0x037E: {
        0b000000110: UNKNOWN_STR,
        0b000110010: UNKNOWN_STR,
    },
    0x037F: {
        0b000110010: UNKNOWN_STR,
    },
    0x0380: {
        0b000110010: UNKNOWN_STR,
    },
    0x0381: {
        0b000110010: UNKNOWN_STR,
        0b000110011: UNKNOWN_STR,
        0b000110100: UNKNOWN_STR,
        0b000110101: UNKNOWN_STR,
        0b000110110: UNKNOWN_STR,
    },
    0x0382: {
        0b000110010: UNKNOWN_STR,
    },
    0x0383: {
        0b000000100: UNKNOWN_STR,
        0b000100100: UNKNOWN_STR,
        0b000110001: UNKNOWN_STR,
        0b000110010: UNKNOWN_STR,
    },
    0x0387: {
        0b000110010: UNKNOWN_STR,
    },
    0x038B: {
        0b000110010: UNKNOWN_STR,
    },
    0x038C: {
        0b000110010: UNKNOWN_STR,
    },
    0x038D: {
        0b000110010: UNKNOWN_STR,
    },
    0x038E: {
        0b000110010: UNKNOWN_STR,
    },
    0x038F: {
        0b000110010: UNKNOWN_STR,
    },
    0x0390: {
        0b000110010: UNKNOWN_STR,
    },
    0x0391: {
        0b000110010: UNKNOWN_STR,
    },
    0x0392: {
        0b000110010: UNKNOWN_STR,
    },
    0x0393: {
        0b000110010: UNKNOWN_STR,
    },
    0x0394: {
        0b000110010: UNKNOWN_STR,
    },
    0x0395: {
        0b000110010: UNKNOWN_STR,
    },
    0x0396: {
        0b000110010: UNKNOWN_STR,
    },
    0x0397: {
        0b000110010: UNKNOWN_STR,
    },
    0x0398: {
        0b000110010: UNKNOWN_STR,
    },
    0x0399: {
        0b000110010: UNKNOWN_STR,
    },
    0x039A: {
        0b000110010: UNKNOWN_STR,
    },
    0x039B: {
        0b000110010: UNKNOWN_STR,
    },
    0x039C: {
        0b000110010: UNKNOWN_STR,
    },
    0x039D: {
        0b000110010: UNKNOWN_STR,
    },
    0x039E: {
        0b000110010: UNKNOWN_STR,
    },
    0x03A5: {
        0b000110010: UNKNOWN_STR,
    },
    0x03A6: {
        0b000110010: UNKNOWN_STR,
    },
    0x03A7: {
        0b000110010: UNKNOWN_STR,
    },
    0x03A8: {
        0b000110010: UNKNOWN_STR,
    },
    0x03AE: {
        0b000110010: UNKNOWN_STR,
    },
    0x03B0: {
        0b000110010: UNKNOWN_STR,
    },
    0x03B7: {
        0b000000001: UNKNOWN_STR,
        0b000000011: UNKNOWN_STR,
        0b000000100: UNKNOWN_STR,
        0b000000101: UNKNOWN_STR,
        0b000000110: UNKNOWN_STR,
        0b000000111: UNKNOWN_STR,
        0b000001000: UNKNOWN_STR,
        0b000001001: UNKNOWN_STR,
        0b000001010: UNKNOWN_STR,
        0b000001011: UNKNOWN_STR,
    },
    0x03B9: {
        0b000110010: UNKNOWN_STR,
    },
    0x03BA: {
        0b000110010: UNKNOWN_STR,
    },
    0x03BC: {
        0b000000010: UNKNOWN_STR,
    },
    0x03BD: {
        0b100000100: UNKNOWN_STR,
    },
    0x03BE: {
        0b000110010: UNKNOWN_STR,
    },
    0x03BF: {
        0b000110010: UNKNOWN_STR,
    },
    0x03C0: {
        0b000110010: UNKNOWN_STR,
    },
    0x03C1: {
        0b000110010: UNKNOWN_STR,
    },
    0x03C2: {
        0b000110010: UNKNOWN_STR,
    },
    0x03C3: {
        0b000110010: UNKNOWN_STR,
    },
    0x03C4: {
        0b000110010: UNKNOWN_STR,
    },
    0x03C5: {
        0b000110010: UNKNOWN_STR,
    },
    0x03C6: {
        0b000110010: UNKNOWN_STR,
    },
    0x03C7: {
        0b000110010: UNKNOWN_STR,
    },
    0x03C8: {
        0b000110010: UNKNOWN_STR,
    },
    0x03C9: {
        0b000110010: UNKNOWN_STR,
    },
    0x03CA: {
        0b000110010: UNKNOWN_STR,
    },
    0x03CB: {
        0b000110010: UNKNOWN_STR,
    },
    0x8000: {
        0b100000000: UNKNOWN_STR,
    },
}

############################
##### FLAG OBJECT DICT #####
############################

FLAG_OBJECT_DICT:dict = {
    # Mumbo's Mountain Jiggies
    0x0000: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.mumbos_mountain} | Jinjo",
    0x0001: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.mumbos_mountain} | Ticker's Tower",
    0x0002: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.mumbos_mountain} | Mumbo's Skull Eye",
    0x0003: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.mumbos_mountain} | Ju-Ju",
    0x0004: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.mumbos_mountain} | Breakable Huts 1",
    0x0005: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.mumbos_mountain} | Stonehenge",
    0x0006: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.mumbos_mountain} | Hill",
    0x0007: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.mumbos_mountain} | Orange Pad",
    0x0008: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.mumbos_mountain} | Chimpy",
    0x0009: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.mumbos_mountain} | Conga",
    # Treasure Trove Cove Jiggies
    0x000A: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.treasure_trove_cove} | Jinjo",
    0x000B: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.treasure_trove_cove} | Lighthouse",
    0x000C: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.treasure_trove_cove} | Shock Jump Alcove",
    0x000D: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.treasure_trove_cove} | Backside Alcove",
    0x000E: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.treasure_trove_cove} | Pool",
    0x000F: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.treasure_trove_cove} | Sandcastle",
    0x0010: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.treasure_trove_cove} | Treasure Hunt",
    0x0011: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.treasure_trove_cove} | Nipper",
    0x0012: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.treasure_trove_cove} | Lockup",
    0x0013: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.treasure_trove_cove} | Blubber",
    # Clanker's Cavern Jiggies
    0x0014: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.clankers_cavern} | Jinjo",
    0x0015: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.clankers_cavern} | Mutie Snippet",
    0x0017: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.clankers_cavern} | Tail",
    0x0018: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.clankers_cavern} | Bolt",
    0x0019: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.clankers_cavern} | Long Pipe",
    0x001A: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.clankers_cavern} | Tooth",
    0x001B: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.clankers_cavern} | Rings",
    0x001C: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.clankers_cavern} | Blowhole",
    0x001D: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.clankers_cavern} | Wonderwing",
    # Bubblegloop Swamp Jiggies
    0x001E: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.bubblegloop_swamp} | Jinjo",
    0x001F: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.bubblegloop_swamp} | Central Button",
    0x0020: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.bubblegloop_swamp} | Pink Egg",
    0x0021: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.bubblegloop_swamp} | Croctus",
    0x0022: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.bubblegloop_swamp} | Huts",
    0x0023: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.bubblegloop_swamp} | Yellow Flibbits",
    0x0024: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.bubblegloop_swamp} | Maze Button",
    0x0025: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.bubblegloop_swamp} | Tanktup",
    0x0026: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.bubblegloop_swamp} | Tiptup",
    0x0027: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.bubblegloop_swamp} | Mr Vile",
    # Freezeezy Peak Jiggies
    0x0028: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.freezeezy_peak} | Jinjo",
    0x0029: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.freezeezy_peak} | Save Boggy",
    0x002A: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.freezeezy_peak} | Smoke Pipe",
    0x002B: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.freezeezy_peak} | Race Boggy As Banjo-Kazooie",
    0x002C: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.freezeezy_peak} | Snowman Buttons",
    0x002D: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.freezeezy_peak} | Presents",
    0x002E: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.freezeezy_peak} | Christmas Tree",
    0x002F: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.freezeezy_peak} | Race Boggy As Walrus",
    0x0030: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.freezeezy_peak} | Sir Slushes",
    0x0031: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.freezeezy_peak} | Wozza",
    # Gruntilda's Lair Jiggies
    0x0032: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.gruntildas_lair} | Mumbo's Mountain Entrance",
    0x0033: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.gruntildas_lair} | Mumbo's Mountain Witch Switch",
    0x0034: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.gruntildas_lair} | Clanker's Cavern Witch Switch",
    0x0035: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.gruntildas_lair} | Treasure Trove Cove Witch Switch",
    0x0036: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.gruntildas_lair} | Bubblegloop Swamp Witch Switch",
    0x0037: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.gruntildas_lair} | Freezeezy Peak Witch Switch",
    0x0038: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.gruntildas_lair} | Mad Monster Mansion Witch Switch",
    0x0039: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.gruntildas_lair} | Gobi's Valley Witch Switch",
    0x003A: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.gruntildas_lair} | Rusty Bucket Bay Witch Switch",
    0x003B: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.gruntildas_lair} | Click Clock Wood Witch Switch",
    # Gobi's Valley Jiggies
    0x003C: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.gobis_valley} | Jinjo",
    0x003D: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.gobis_valley} | Grabba",
    0x003E: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.gobis_valley} | Jinxy",
    0x003F: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.gobis_valley} | Matching Puzzle",
    0x0040: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.gobis_valley} | King Sandybutt",
    0x0041: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.gobis_valley} | Water Pyramid",
    0x0042: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.gobis_valley} | Rubee",
    0x0043: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.gobis_valley} | Free Gobi",
    0x0044: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.gobis_valley} | Trunker",
    0x0045: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.gobis_valley} | Ancient Ones",
    # Click Clock Wood Jiggies
    0x0046: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.click_clock_wood} | Jinjo",
    0x0047: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.click_clock_wood} | Treehouse",
    0x0048: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.click_clock_wood} | Eyrie",
    0x0049: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.click_clock_wood} | Nabnut",
    0x004A: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.click_clock_wood} | Gnawty",
    0x004B: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.click_clock_wood} | Zubbas",
    0x004C: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.click_clock_wood} | Flower",
    0x004D: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.click_clock_wood} | Leaf Jumps",
    0x004E: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.click_clock_wood} | Tree Top",
    0x004F: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.click_clock_wood} | Whipcracks",
    # Rusty Bucket Bay Jiggies
    0x0050: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.rusty_bucket_bay} | Jinjo",
    0x0051: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.rusty_bucket_bay} | Chump Warehouse",
    0x0052: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.rusty_bucket_bay} | Snorkel",
    0x0053: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.rusty_bucket_bay} | Whistles",
    0x0054: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.rusty_bucket_bay} | Atop Funnel",
    0x0055: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.rusty_bucket_bay} | Boss Boom Box",
    0x0056: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.rusty_bucket_bay} | Propeller",
    0x0057: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.rusty_bucket_bay} | Captain's Cabin",
    0x0058: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.rusty_bucket_bay} | Crane Cage",
    0x0059: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.rusty_bucket_bay} | Engine Room",
    # Mad Monster Mansion Jiggies
    0x005A: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.mad_monster_mansion} | Jinjo",
    0x005B: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.mad_monster_mansion} | Well",
    0x005C: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.mad_monster_mansion} | Napper",
    0x005D: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.mad_monster_mansion} | Cellar",
    0x005E: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.mad_monster_mansion} | Church Roof",
    0x005F: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.mad_monster_mansion} | Motzand",
    0x0060: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.mad_monster_mansion} | Rain Barrel",
    0x0061: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.mad_monster_mansion} | Tumblar",
    0x0062: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.mad_monster_mansion} | Flower Pots",
    0x0063: f"{JIGGY_FLAG_STR} | {LEVEL_NAME_ENUMS.mad_monster_mansion} | Loggo",
    # Mumbo's Mountain Empty Honeycombs
    0x0064: f"{EMPTY_HONEYCOMB_FLAG_STR} | {LEVEL_NAME_ENUMS.mumbos_mountain} | Alcove",
    0x0065: f"{EMPTY_HONEYCOMB_FLAG_STR} | {LEVEL_NAME_ENUMS.mumbos_mountain} | Ju-Ju",
    # Treasure Trove Cove Empty Honeycombs
    0x0066: f"{EMPTY_HONEYCOMB_FLAG_STR} | {LEVEL_NAME_ENUMS.treasure_trove_cove} | Underwater",
    0x0067: f"{EMPTY_HONEYCOMB_FLAG_STR} | {LEVEL_NAME_ENUMS.treasure_trove_cove} | Crate",
    # Clanker's Cavern Empty Honeycombs
    0x0068: f"{EMPTY_HONEYCOMB_FLAG_STR} | {LEVEL_NAME_ENUMS.clankers_cavern} | Underwater",
    0x0069: f"{EMPTY_HONEYCOMB_FLAG_STR} | {LEVEL_NAME_ENUMS.clankers_cavern} | Grated Pipe",
    # Bubblegloop Swamp Empty Honeycombs
    0x006A: f"{EMPTY_HONEYCOMB_FLAG_STR} | {LEVEL_NAME_ENUMS.bubblegloop_swamp} | Grated Pipe",
    0x006B: f"{EMPTY_HONEYCOMB_FLAG_STR} | {LEVEL_NAME_ENUMS.bubblegloop_swamp} | Tiptup",
    # Freezeezy Peak Empty Honeycombs
    0x006C: f"{EMPTY_HONEYCOMB_FLAG_STR} | {LEVEL_NAME_ENUMS.freezeezy_peak} | Wozza",
    0x006D: f"{EMPTY_HONEYCOMB_FLAG_STR} | {LEVEL_NAME_ENUMS.freezeezy_peak} | Sir Slush",
    # Gobi's Valley Empty Honeycombs
    0x006E: f"{EMPTY_HONEYCOMB_FLAG_STR} | {LEVEL_NAME_ENUMS.gobis_valley} | Cactus",
    0x006F: f"{EMPTY_HONEYCOMB_FLAG_STR} | {LEVEL_NAME_ENUMS.gobis_valley} | Gobi",
    # Click Clock Wood Empty Honeycombs
    0x0070: f"{EMPTY_HONEYCOMB_FLAG_STR} | {LEVEL_NAME_ENUMS.click_clock_wood} | Gnawty",
    0x0071: f"{EMPTY_HONEYCOMB_FLAG_STR} | {LEVEL_NAME_ENUMS.click_clock_wood} | Acorn Storage",
    # Rusty Bucket Bay Empty Honeycombs
    0x0072: f"{EMPTY_HONEYCOMB_FLAG_STR} | {LEVEL_NAME_ENUMS.rusty_bucket_bay} | Boat Room",
    0x0073: f"{EMPTY_HONEYCOMB_FLAG_STR} | {LEVEL_NAME_ENUMS.rusty_bucket_bay} | Engine Room",
    # Mad Monster Mansion Empty Honeycombs
    0x0074: f"{EMPTY_HONEYCOMB_FLAG_STR} | {LEVEL_NAME_ENUMS.mad_monster_mansion} | Rafters",
    0x0075: f"{EMPTY_HONEYCOMB_FLAG_STR} | {LEVEL_NAME_ENUMS.mad_monster_mansion} | Floorboard",
    # Spiral Mountain Empty Honeycombs
    0x0076: f"{EMPTY_HONEYCOMB_FLAG_STR} | {LEVEL_NAME_ENUMS.spiral_mountain} | Stump",
    0x0077: f"{EMPTY_HONEYCOMB_FLAG_STR} | {LEVEL_NAME_ENUMS.spiral_mountain} | Waterfall",
    0x0078: f"{EMPTY_HONEYCOMB_FLAG_STR} | {LEVEL_NAME_ENUMS.spiral_mountain} | Underwater",
    0x0079: f"{EMPTY_HONEYCOMB_FLAG_STR} | {LEVEL_NAME_ENUMS.spiral_mountain} | Tree",
    0x007A: f"{EMPTY_HONEYCOMB_FLAG_STR} | {LEVEL_NAME_ENUMS.spiral_mountain} | Colliwobble",
    0x007B: f"{EMPTY_HONEYCOMB_FLAG_STR} | {LEVEL_NAME_ENUMS.spiral_mountain} | Quarrie",
    # Mumbo's Mountain Mumbo Tokens
    0x00C8: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.mumbos_mountain} | Conga",
    0x00C9: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.mumbos_mountain} | Stonehenge",
    0x00CA: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.mumbos_mountain} | Mumbo's Skull Bridge",
    0x00CB: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.mumbos_mountain} | Magenta Jinjo",
    0x00CC: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.mumbos_mountain} | Ticker's Tower",
    # Treasure Trove Cove Mumbo Tokens
    0x00CD: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.treasure_trove_cove} | Insite Salty Hippo",
    0x00CE: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.treasure_trove_cove} | Lockup 1",
    0x00CF: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.treasure_trove_cove} | Lockup 2",
    0x00D0: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.treasure_trove_cove} | Crow's Nest",
    0x00D1: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.treasure_trove_cove} | Lighthouse",
    0x00D2: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.treasure_trove_cove} | Crate",
    0x00D3: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.treasure_trove_cove} | Treasure Hunt",
    0x00D4: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.treasure_trove_cove} | Pool",
    0x00D5: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.treasure_trove_cove} | Shock Jump",
    0x00D6: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.treasure_trove_cove} | Behind Nipper",
    # Clanker's Cavern Mumbo Tokens
    0x00D7: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.clankers_cavern} | Tail",
    0x00D8: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.clankers_cavern} | Entrance",
    0x00D9: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.clankers_cavern} | Underwater Pipe",
    0x00DA: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.clankers_cavern} | Climbable Pipe Alcove",
    0x00DB: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.clankers_cavern} | Tooth",
    # Bubblegloop Swamp Mumbo Tokens
    0x00DC: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.bubblegloop_swamp} | Beneath Huts 1",
    0x00DD: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.bubblegloop_swamp} | Beneath Huts 2",
    0x00DE: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.bubblegloop_swamp} | Cattail",
    0x00DF: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.bubblegloop_swamp} | Yellow Jinjo",
    0x00E0: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.bubblegloop_swamp} | Above Huts",
    0x00E1: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.bubblegloop_swamp} | Behind Mumbo's Skull",
    0x00E2: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.bubblegloop_swamp} | Central Area",
    0x00E3: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.bubblegloop_swamp} | Behind Tiptup",
    0x00E4: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.bubblegloop_swamp} | Mr. Vile",
    0x00E5: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.bubblegloop_swamp} | Behind Mumbo",
    # Freezeezy Peak Mumbo Tokens
    0x00E6: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.freezeezy_peak} | Snowman Leg 1",
    0x00E7: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.freezeezy_peak} | Snowman Leg 2",
    0x00E8: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.freezeezy_peak} | Christmas Presents",
    0x00E9: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.freezeezy_peak} | Chimney",
    0x00EA: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.freezeezy_peak} | Sir Slush 1",
    0x00EB: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.freezeezy_peak} | Sir Slush 2",
    0x00EC: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.freezeezy_peak} | Christmas Tree Pot",
    0x00ED: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.freezeezy_peak} | Snowman Scarf",
    0x00EE: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.freezeezy_peak} | Freezing Water",
    0x00EF: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.freezeezy_peak} | Igloo",
    # Gobi's Valley Mumbo Tokens
    0x00F0: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.gobis_valley} | Jinxy Nose",
    0x00F1: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.gobis_valley} | Behind Jinxy",
    0x00F2: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.gobis_valley} | Moat",
    0x00F3: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.gobis_valley} | Atop King Sandybutt's Maze",
    0x00F4: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.gobis_valley} | Water Pyramid Lower Entrance",
    0x00F5: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.gobis_valley} | Matching Puzzle",
    0x00F6: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.gobis_valley} | King Sandybutt's Pot",
    0x00F7: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.gobis_valley} | Inside Water Pyramid",
    0x00F8: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.gobis_valley} | Rubee",
    0x00F9: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.gobis_valley} | Inside Jinxy",
    # Mad Monster Mansion Mumbo Tokens
    0x00FA: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.mad_monster_mansion} | Near Green Pool",
    0x00FB: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.mad_monster_mansion} | Near Tumblar's Shed",
    0x00FC: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.mad_monster_mansion} | Clock Tower",
    0x00FD: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.mad_monster_mansion} | Hedge Maze Pumpkin Ramp",
    0x00FE: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.mad_monster_mansion} | Hedge Maze Dead End",
    0x00FF: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.mad_monster_mansion} | Cemetery",
    0x0100: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.mad_monster_mansion} | Inside Green Pool",
    0x0101: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.mad_monster_mansion} | Rafters",
    0x0102: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.mad_monster_mansion} | Piano Stool",
    0x0103: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.mad_monster_mansion} | Atop Tumblar's Shed",
    0x0104: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.mad_monster_mansion} | Inside Loggo/Cellar",
    0x0105: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.mad_monster_mansion} | Dinning Room",
    0x0106: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.mad_monster_mansion} | Inside Well",
    0x0107: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.mad_monster_mansion} | Bedroom",
    0x0108: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.mad_monster_mansion} | Restroom",
    # Rusty Bucket Bay Mumbo Tokens
    0x0109: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.rusty_bucket_bay} | Atop Funnel",
    0x010A: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.rusty_bucket_bay} | Boat Bow",
    0x010B: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.rusty_bucket_bay} | Safety Boat",
    0x010C: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.rusty_bucket_bay} | Toll 2",
    0x010D: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.rusty_bucket_bay} | Toxic Pool",
    0x010E: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.rusty_bucket_bay} | Near Witch Switch",
    0x010F: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.rusty_bucket_bay} | Chompa Blue Container",
    0x0110: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.rusty_bucket_bay} | Seaman Grublin Blue Container",
    0x0111: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.rusty_bucket_bay} | Seaman Grublin Cabins",
    0x0112: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.rusty_bucket_bay} | Navigation Room",
    0x0113: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.rusty_bucket_bay} | Kitchen",
    0x0114: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.rusty_bucket_bay} | Engine Room Pipe 1",
    0x0115: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.rusty_bucket_bay} | Engine Room Pipe 2",
    0x0116: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.rusty_bucket_bay} | Engine Room Platform",
    0x0117: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.rusty_bucket_bay} | Middle Pipe",
    # Gruntilda's Lair Mumbo Tokens
    0x0118: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.gruntildas_lair} | Behind Pink Cauldron",
    0x0119: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.gruntildas_lair} | Click Clock Wood Puzzle",
    0x011A: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.gruntildas_lair} | Pipe Room",
    0x011B: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.gruntildas_lair} | Above Clanker's Cavern Entrance",
    0x011C: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.gruntildas_lair} | Behind Sarcophagus",
    0x011D: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.gruntildas_lair} | Advent Calendar",
    0x011E: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.gruntildas_lair} | Crypt Behind Mumbo",
    0x011F: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.gruntildas_lair} | Above 640 Note Door",
    0x0120: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.gruntildas_lair} | Rusty Bucket Bay Entrance",
    0x0121: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.gruntildas_lair} | Near Mad Monster Mansion Puzzle",
    # Click Clock Wood Mumbo Tokens
    0x0122: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.click_clock_wood} | Spring Treehouse",
    0x0123: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.click_clock_wood} | Spring Branches",
    0x0124: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.click_clock_wood} | Spring Near Eyrie",
    0x0125: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.click_clock_wood} | Spring Bramble",
    0x0126: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.click_clock_wood} | Spring Snarebear Flower",
    0x0127: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.click_clock_wood} | Spring Snarebear Entrance",
    0x0128: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.click_clock_wood} | Spring Atop Zubba",
    0x0129: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.click_clock_wood} | Spring Nabnut's Room",
    0x012A: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.click_clock_wood} | Summer Path To Eyrie",
    0x012B: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.click_clock_wood} | Summer Tall Grass Corner",
    0x012C: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.click_clock_wood} | Summer Snarebear",
    0x012D: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.click_clock_wood} | Summer Branches",
    0x012E: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.click_clock_wood} | Summer Gnawty Entrance",
    0x012F: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.click_clock_wood} | Summer Leaf Jump",
    0x0130: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.click_clock_wood} | Summer Mumbo Skull",
    0x0131: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.click_clock_wood} | Autumn Leaf Jump",
    0x0132: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.click_clock_wood} | Autumn Snarebear Entrance",
    0x0133: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.click_clock_wood} | Autumn Snarebear Treetop",
    0x0134: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.click_clock_wood} | Autumn Near Treehouse",
    0x0135: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.click_clock_wood} | Autumn Branches",
    0x0136: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.click_clock_wood} | Winter Dead Flower",
    0x0137: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.click_clock_wood} | Winter Frozen Lake",
    0x0138: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.click_clock_wood} | Winter Zubba Hive",
    0x0139: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.click_clock_wood} | Winter Near Nabnut",
    0x013A: f"{MUMBO_TOKEN_FLAG_STR} | {LEVEL_NAME_ENUMS.click_clock_wood} | Winter Sir Slush",
}

################
##### PATH #####
################

PATH_OBJECT_DICT:dict = {
    0x0000: {
        0b000000000: UNKNOWN_STR,
        0b000000001: UNKNOWN_STR,
        0b000001101: UNKNOWN_STR,
        0b000010000: UNKNOWN_STR,
        0b000010001: UNKNOWN_STR,
        0b000010010: UNKNOWN_STR,
        0b000010011: UNKNOWN_STR,
        0b000010100: UNKNOWN_STR,
        0b000010101: UNKNOWN_STR,
        0b000010110: UNKNOWN_STR,
        0b000010111: UNKNOWN_STR,
        0b000011000: UNKNOWN_STR,
        0b000011001: UNKNOWN_STR,
        0b000011010: UNKNOWN_STR,
        0b000011011: UNKNOWN_STR,
        0b000011100: UNKNOWN_STR,
        0b000011101: UNKNOWN_STR,
        0b000011110: UNKNOWN_STR,
        0b000011111: UNKNOWN_STR,
        0b000100000: UNKNOWN_STR,
        0b000100001: UNKNOWN_STR,
        0b000100010: UNKNOWN_STR,
        0b000100011: UNKNOWN_STR,
        0b000100100: UNKNOWN_STR,
        0b000100101: UNKNOWN_STR,
        0b000100110: UNKNOWN_STR,
        0b000100111: UNKNOWN_STR,
        0b000101001: UNKNOWN_STR,
        0b000101010: UNKNOWN_STR,
        0b000101101: UNKNOWN_STR,
        0b000101110: UNKNOWN_STR,
        0b000101111: UNKNOWN_STR,
        0b000110000: UNKNOWN_STR,
        0b000110001: UNKNOWN_STR,
        0b000110010: UNKNOWN_STR,
        0b000110011: UNKNOWN_STR,
        0b000110100: UNKNOWN_STR,
        0b000110101: UNKNOWN_STR,
        0b000110111: UNKNOWN_STR,
        0b000111010: UNKNOWN_STR,
        0b111110100: UNKNOWN_STR,
    },
    0x0001: {
        0b000011100: UNKNOWN_STR,
        0b000110011: UNKNOWN_STR,
    },
    0x0002: {
        0b000110010: UNKNOWN_STR,
    },
    0x0012: {
        0b000110010: UNKNOWN_STR,
    },
    0x0017: {
        0b000110010: UNKNOWN_STR,
        0b000111100: UNKNOWN_STR,
    },
}
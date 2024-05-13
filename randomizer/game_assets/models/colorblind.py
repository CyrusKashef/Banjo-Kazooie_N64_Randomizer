'''
This module provides functions to adjust RGB values of a color for different types of color blindness.
'''

###################
##### IMPORTS #####
###################

from enum import IntEnum, unique, auto

###################
##### CLASSES #####
###################

@unique
class COLORS(IntEnum):
    red = auto()
    green = auto()
    blue = auto()

@unique
class COLOR_BLINDNESS(IntEnum):
    deuteranomaly = auto()
    deuteranopia = auto()
    protanomaly = auto()
    protanopia = auto()
    tritanomaly = auto()
    tritanopia = auto()
    monochromacy = auto()

#################
##### DICTS #####
#################

COLOR_BLINDNESS_DICT:dict = {
    COLOR_BLINDNESS.deuteranomaly: {
        COLORS.red: lambda red, green, blue: int((red * 0.625) + (green * 0.375)),
        COLORS.green: lambda red, green, blue: int((red * 0.7) + (green * 0.3)),
        COLORS.blue: lambda red, green, blue: int(blue),
    },
    COLOR_BLINDNESS.deuteranopia: {
        COLORS.red: lambda red, green, blue: int((red * 0.625) + (green * 0.375)),
        COLORS.green: lambda red, green, blue: int((red * 0.7) + (green * 0.3)),
        COLORS.blue: lambda red, green, blue: int(blue),
    },
    COLOR_BLINDNESS.protanomaly: {
        COLORS.red: lambda red, green, blue: int((red * 0.567) + (green * 0.433)),
        COLORS.green: lambda red, green, blue: int((red * 0.558) + (green * 0.442)),
        COLORS.blue: lambda red, green, blue: int(blue),
    },
    COLOR_BLINDNESS.protanopia: {
        COLORS.red: lambda red, green, blue: int((red * 0.567) + (green * 0.433)),
        COLORS.green: lambda red, green, blue: int((red * 0.558) + (green * 0.442)),
        COLORS.blue: lambda red, green, blue: int(blue),
    },
    COLOR_BLINDNESS.tritanomaly: {
        COLORS.red: lambda red, green, blue: int((red * 0.967) + (green * 0.033)),
        COLORS.green: lambda red, green, blue: int((red * 0.733) + (green * 0.267)),
        COLORS.blue: lambda red, green, blue: int((green * 0.183) + (blue * 0.817)),
    },
    COLOR_BLINDNESS.tritanopia: {
        COLORS.red: lambda red, green, blue: int((red * 0.95) + (green * 0.05)),
        COLORS.green: lambda red, green, blue: int((red * 0.43) + (green * 0.57) + (blue * 0.1)),
        COLORS.blue: lambda red, green, blue: int((red * 0.43) + (green * 0.57) + (blue * 0.1)),
    },
    COLOR_BLINDNESS.monochromacy: {
        COLORS.red: lambda red, green, blue: int((red * 0.299) + (green * 0.587) + (blue * 0.114)),
        COLORS.green: lambda red, green, blue: int((red * 0.299) + (green * 0.587) + (blue * 0.114)),
        COLORS.blue: lambda red, green, blue: int((red * 0.299) + (green * 0.587) + (blue * 0.114)),
    },
}

#####################
##### FUNCTIONS #####
#####################

def adjust_for_colorblindness(
        red:int, green:int, blue:int,
        color_blindness:COLOR_BLINDNESS):
    '''
    Adjusts the RGB values of a color for a given colorblindness
    '''
    new_red:int = int(COLOR_BLINDNESS_DICT[color_blindness][COLORS.red](red, green, blue))
    new_green:int = int(COLOR_BLINDNESS_DICT[color_blindness][COLORS.green](red, green, blue))
    new_blue:int = int(COLOR_BLINDNESS_DICT[color_blindness][COLORS.blue](red, green, blue))
    return new_red, new_green, new_blue

################
##### MAIN #####
################

if __name__ == '__main__':
    red:int = 0xA0
    green:int = 0x20
    blue:int = 0x40
    for color_blindness in COLOR_BLINDNESS:
        new_red, new_green, new_blue = adjust_for_colorblindness(red, green, blue, color_blindness)
        print(f"{color_blindness}: #{new_red:02X}{new_green:02X}{new_blue:02X}")
'''
Purpose:
*
'''

###################
##### IMPORTS #####
###################

from randomizer.constants.int_values.color_enums import COLOR_BLINDNESS
from randomizer.constants.str_values.color_str import COLORS

########################
##### DICTIONARIES #####
########################

COLOR_BLINDNESS_SIMULATION_DICT:dict = {
    # Not Color Blind
    COLOR_BLINDNESS.trichromacy: {
        COLORS.red: lambda red, green, blue, degree: int(red),
        COLORS.green: lambda red, green, blue, degree: int(green),
        COLORS.blue: lambda red, green, blue, degree: int(blue),
    },
    # Green Blind
    COLOR_BLINDNESS.deuteranomaly: {
        COLORS.red: lambda red, green, blue, degree: int(red * 0.625 + green * 0.375),
        COLORS.green: lambda red, green, blue, degree: int(red * 0.7 + green * 0.3),
        COLORS.blue: lambda red, green, blue, degree: int(blue),
    },
    COLOR_BLINDNESS.deuteranopia: {
        COLORS.red: lambda red, green, blue, degree: int(red * 0.625 + green * 0.375),
        COLORS.green: lambda red, green, blue, degree: int(red * 0.7 + green * 0.3),
        COLORS.blue: lambda red, green, blue, degree: int(blue),
    },
    # Red Blind
    COLOR_BLINDNESS.protanomaly: {
        COLORS.red: lambda red, green, blue, degree: int(red * 0.567 + green * 0.433),
        COLORS.green: lambda red, green, blue, degree: int(red * 0.558 + green * 0.442),
        COLORS.blue: lambda red, green, blue, degree: int(blue),
    },
    COLOR_BLINDNESS.protanopia: {
        COLORS.red: lambda red, green, blue, degree: int(red * 0.567 + green * 0.433),
        COLORS.green: lambda red, green, blue, degree: int(red * 0.558 + green * 0.442),
        COLORS.blue: lambda red, green, blue, degree: int(blue),
    },
    # Blue Blind
    COLOR_BLINDNESS.tritanomaly: {
        COLORS.red: lambda red, green, blue, degree: int(red * 0.967 + green * 0.033),
        COLORS.green: lambda red, green, blue, degree: int(red * 0.733 + green * 0.267),
        COLORS.blue: lambda red, green, blue, degree: int(green * 0.183 + blue * 0.817),
    },
    COLOR_BLINDNESS.tritanopia: {
        COLORS.red: lambda red, green, blue, degree: int(red * 0.95 + green * 0.05),
        COLORS.green: lambda red, green, blue, degree: int(red * 0.43 + green * 0.57 + blue * 0.1),
        COLORS.blue: lambda red, green, blue, degree: int(red * 0.43 + green * 0.57 + blue * 0.1),
    },
    # Grayscale
    COLOR_BLINDNESS.monochromacy: {
        COLORS.red: lambda red, green, blue, degree: int(red * 0.299 + green * 0.587 + blue * 0.114),
        COLORS.green: lambda red, green, blue, degree: int(red * 0.299 + green * 0.587 + blue * 0.114),
        COLORS.blue: lambda red, green, blue, degree: int(red * 0.299 + green * 0.587 + blue * 0.114),
    },
}

COLOR_BLINDNESS_CORRECTION_DICT:dict = {
    # Not Color Blind
    COLOR_BLINDNESS.trichromacy: {
        COLORS.red: lambda red, green, blue, degree: int(red * degree),
        COLORS.green: lambda red, green, blue, degree: int(green * degree),
        COLORS.blue: lambda red, green, blue, degree: int(blue * degree),
    },
    # Green Blind
    COLOR_BLINDNESS.deuteranomaly: {
        COLORS.red: lambda red, green, blue, degree: int((1 - degree / 2) * blue + (degree / 2) * green),
        COLORS.green: lambda red, green, blue, degree: int(green),
        COLORS.blue: lambda red, green, blue, degree: int((1 - degree / 4) * red + (degree / 4) * green),
    },
    COLOR_BLINDNESS.deuteranopia: {
        COLORS.red: lambda red, green, blue, degree: int((1 - degree / 4) * blue + (degree / 4) * green),
        COLORS.green: lambda red, green, blue, degree: int(green),
        COLORS.blue: lambda red, green, blue, degree: int((1 - degree / 2) * red + (degree / 2) * green),
    },
    # Red Blind
    COLOR_BLINDNESS.protanomaly: {
        COLORS.red: lambda red, green, blue, degree: int(red),
        COLORS.green: lambda red, green, blue, degree: int((1 - degree / 2) * green + (degree / 2) * red),
        COLORS.blue: lambda red, green, blue, degree: int((1 - degree / 4) * blue + (degree / 4) * red),
    },
    COLOR_BLINDNESS.protanopia: {
        COLORS.red: lambda red, green, blue, degree: int(red),
        COLORS.green: lambda red, green, blue, degree: int((1 - degree / 4) * green + (degree / 4) * red),
        COLORS.blue: lambda red, green, blue, degree: int((1 - degree / 2) * blue + (degree / 2) * red),
    },
    # Blue Blind
    COLOR_BLINDNESS.tritanomaly: {
        COLORS.red: lambda red, green, blue, degree: int((1 - degree / 4) * red + (degree / 4) * blue),
        COLORS.green: lambda red, green, blue, degree: int((1 - degree / 2) * green + (degree / 2) * blue),
        COLORS.blue: lambda red, green, blue, degree: int(blue),
    },
    COLOR_BLINDNESS.tritanopia: {
        COLORS.red: lambda red, green, blue, degree: int((1 - degree / 4) * red + (degree / 4) * blue),
        COLORS.green: lambda red, green, blue, degree: int((1 - degree / 2) * green + (degree / 2) * blue),
        COLORS.blue: lambda red, green, blue, degree: int(blue),
    },
    # Grayscale
    COLOR_BLINDNESS.monochromacy: {
        COLORS.red: lambda red, green, blue, degree: int((0.2126 * red + 0.7152 * green + 0.0722 * blue) / (0.2126 + 0.7152 + 0.0722)),
        COLORS.green: lambda red, green, blue, degree: int((0.2126 * red + 0.7152 * green + 0.0722 * blue) / (0.2126 + 0.7152 + 0.0722)),
        COLORS.blue: lambda red, green, blue, degree: int((0.2126 * red + 0.7152 * green + 0.0722 * blue) / (0.2126 + 0.7152 + 0.0722)),
    },
}
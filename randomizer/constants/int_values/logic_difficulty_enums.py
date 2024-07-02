'''
Enumerators from the following class are arbitrary values used to make each instance unique.

Logic Difficulties Explained:
* Beginner (Hasn't Play Game In Long Time):
  - Developer Intended Strategies
* Casual (Plays Occassionally):
  - Simple Strategies (Very Manageable)
  - Little/No Risk (Unlikely To Take Damage/Die)
* Intermediate (Performs Some Glitches/Exploits):
  - Tough/Knowledge-Based Strategies (Somewhat Manageable)
  - Somewhat Risk (Could Take Damage/Die)
* Expert (Can Execute Tough Glitches/Exploits):
  - Hard Strategies (Hard To Execute Without Practice)
  - High Risk (Could Die) Or Hard To Know (Niche)
'''

###################
##### IMPORTS #####
###################

from enum import IntEnum, auto

##################################
##### LOGIC DIFFICULTY ENUMS #####
##################################

class LOGIC_DIFFICULTY_ENUMS(IntEnum):
    beginner = auto()
    casual = auto()
    intermediate = auto()
    expert = auto()
###################
##### IMPORTS #####
###################

from randomizer.constants.int_values.logic_item_enums import LOGIC_ITEM_ENUMS as LOGIC_ITEM
from randomizer.constants.int_values.transformation_enums import TRANSFORMATION_ENUMS as TRANSFORMATION
from randomizer.constants.int_values.item_type_enums import ITEM_TYPE_ENUMS as ITEM_TYPE
from randomizer.constants.int_values.logic_difficulty_enums import LOGIC_DIFFICULTY_ENUMS as DIFFICULTY
from randomizer.constants.int_values.level_enums import LEVEL_ID_ENUMS as LEVEL

######################
##### ITEM CLASS #####
######################

class ITEM_CLASS():
    def __init__(self,
            debug_name:str,
            item_enum:LOGIC_ITEM,
            obtain_requirements:dict,
            item_type:ITEM_TYPE,
            item_flag:int|None):
        '''
        Pass
        '''
        # DEVELOPER VALUES
        self.debug_name:str = debug_name
        self.item_enum:int = item_enum
        # ACCESS/OBTAIN REQUIREMENTS
        self.obtain_requirements:dict = obtain_requirements
        # CONSTANT PRIOR TO LOGIC
        self.item_type:ITEM_TYPE = item_type
        self.item_flag:int|None = item_flag
        # SET, BUT MUTABLE
        self.has_been_placed:bool = False
        self.has_been_obtained:bool = False
        # SET DURING LOGIC

    ###################
    ##### GETTERS #####
    ###################
    
    def get_debug_name(self):
        '''
        Pass
        '''
        return self.debug_name

    def get_item_enum(self):
        '''
        Pass
        '''
        return self.item_enum
    
    def get_original_level(self):
        '''
        Pass
        '''
        pass

    def get_item_type(self):
        '''
        Pass
        '''
        return self.item_type

    def get_item_flag(self):
        '''
        Pass
        '''
        return self.item_flag
    
    def is_item_placed(self):
        '''
        Pass
        '''
        return self.has_been_placed
    
    def is_item_obtained(self):
        '''
        Pass
        '''
        return self.has_been_obtained

    ###################
    ##### SETTERS #####
    ###################

    def reset_item(self):
        '''
        Pass
        '''
        self.has_been_place:bool = False
        self.has_been_obtained:bool = False

    def set_item_as_placed(self):
        '''
        Pass
        '''
        self.has_been_placed:bool = True
    
    def set_item_as_obtained(self):
        '''
        Pass
        '''
        self.has_been_obtained:bool = True

    ###################
    ##### UTILITY #####
    ###################

    def _requirements_met(self,
            requirements:tuple,
            items:dict):
        '''
        Checks each requirement in the requirements list
        to see if the player has reached that requirement.
        If the requirement is a tuple itself, perform recursive.

        Returns whether the player has met enough requirements.
        '''
        for requirement in requirements:
            if(isinstance(requirement, tuple)):
                tuple_requirements_met:bool = \
                    self._requirements_met(requirement, items)
                if(tuple_requirements_met is False):
                    return False
                continue
            curr_item:ITEM_CLASS = items[requirement]
            item_obtained:bool = curr_item.is_item_obtained()
            if(item_obtained is False):
                return False
        return True

    def is_item_obtainable(self,
            transformation:TRANSFORMATION,
            items:dict):
        '''
        Pass
        '''
        transformation_obtain_requirement:function = self.obtain_requirements[transformation]
        is_item_obtainable:bool = self._requirements_met(transformation_obtain_requirement, items)
        return is_item_obtainable
###################
##### IMPORTS #####
###################

from randomizer.constants.int_values.logic_item_enums import LOGIC_ITEM_ENUMS as LOGIC_ITEM

#######################
##### EVENT CLASS #####
#######################

class EVENT_CLASS():
    def __init__(self,
            debug_name:str,
            event_enum:LOGIC_ITEM,
            event_requirements:list,
            event_unlock_list:list):
        self.debug_name:str = debug_name
        self.event_enum:LOGIC_ITEM = event_enum
        self.event_requirements:list = event_requirements
        self.event_unlocks:list = event_unlock_list

    ###################
    ##### GETTERS #####
    ###################

    def get_debug_name(self):
        '''
        Pass
        '''
        return self.debug_name

    def get_event_enum(self):
        '''
        Pass
        '''
        return self.event_enum

    def get_event_requirements(self):
        '''
        Pass
        '''
        return self.event_requirements

    def get_event_unlocks(self):
        '''
        Pass
        '''
        return self.event_unlocks
    
    ###################
    ##### SETTERS #####
    ###################

    def set_event_requirements(self, event_requirements:list):
        '''
        Pass
        '''
        self.event_requirements:list = event_requirements

    ###################
    ##### UTILITY #####
    ###################

    def check_event_requirement(self, items:dict):
        '''
        Pass
        '''
        event_requirements_met:bool = self.event_requirements(items)
        return event_requirements_met
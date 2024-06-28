#################
##### CLASS #####
#################

class REGION_CLASS():
    def __init__(self):
        self.debug_name:str = None
        self.region_enum:int = None
        self.location_dict:dict = None
        self.exit_region_dict:dict = None
        self.transformation_pad:bool = None
        self.detransformation_zone:bool = None
        self.allowed_transformations:list = None
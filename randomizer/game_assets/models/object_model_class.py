'''
Purpose:
*
'''

###################
##### IMPORTS #####
###################

from randomizer.game_assets.models.object_3d_model_class import OBJECT_3D_MODEL_CLASS
from randomizer.constants.int_values.object_model_constants import OBJECT_MODEL_CONSTANTS as CONSTANT

##############################
##### OBJECT MODEL CLASS #####
##############################

class OBJECT_MODEL_CLASS(OBJECT_3D_MODEL_CLASS):
    '''
    Class for reading and modifying object model files.
    '''
    def __init__(self, file_path:str):
        '''
        Constructor
        '''
        # Constant
        self._3d_model_header:int = 0x0000000B

        # Variables
        self._file_path = file_path
        self._file_content = None
        self._object_model_dict:dict = {}
        self._model_type:int = None
    
    def _determine_model_type(self):
        '''
        Pass
        '''
        model_header:int = self._read_bytes_as_int(0x0, byte_count=4)
        if(model_header == self._3d_model_header):
            self._model_type:int = CONSTANT.object_3d_model
        else:
            self._model_type:int = CONSTANT.object_2d_model

    ##########################
    ##### MAIN FUNCTIONS #####
    ##########################
        
    def read_object_model_file(self):
        '''
        Pass
        '''
        super()._read_file()
        self._determine_model_type()
        if(self._model_type == CONSTANT.object_3d_model):
            self.setup_object_3d_model_class()
            self.read_object_3d_model_file()
        elif(self._model_type == CONSTANT.object_2d_model):
            pass
        else:
            print("Fucking blowing my load")
            exit(0)
    
    def save_object_model_file(self, file_path:str|None=None):
        '''
        Pass
        '''
        super()._read_file()
        self._determine_model_type()
        if(self._model_type == CONSTANT.object_3d_model):
            self.save_object_3d_model_file()
        elif(self._model_type == CONSTANT.object_2d_model):
            pass
        else:
            print("Fucking blowing your load")
            exit(0)

################
##### MAIN #####
################
    
if __name__ == '__main__':
    old_file_path:str = "C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/test2/"
    new_file_path:str = "C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/test/"
    file_list:list = [
        # "19D530", # Banjo Kazooie High Poly Model
        # "3AAA50", # Secret SNS Egg
        # "3B4E20", # Iron Gate (No Lock)
        # "1466E8", # MM Chimpy's Orange
        # "146BD8", # MM Conga Tree
        # "1484D0", # FP Blue Present (No Eyes)
        # "153698", # MM Orange Pad
        "1B4C40", # Walrus Banjo
        ]
    import filecmp
    for file_name in file_list:
        old_file_name:str = f"{old_file_path}{file_name}.bin"
        new_file_name:str = f"{new_file_path}{file_name}-TEST.bin"
        object_model_obj = OBJECT_MODEL_CLASS(old_file_name)
        object_model_obj.read_object_model_file()
        object_model_obj.save_object_model_file(new_file_name)
        files_are_copies:bool = filecmp.cmp(old_file_name, new_file_name)
        if(files_are_copies):
            print("Copies")
        else:
            print(f"Not Copies: {file_name}")
            exit(0)
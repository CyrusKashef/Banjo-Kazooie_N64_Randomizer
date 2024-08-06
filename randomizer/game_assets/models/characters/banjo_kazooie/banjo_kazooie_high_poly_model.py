'''
Purpose:
*
'''

###################
##### IMPORTS #####
###################

from enum import StrEnum, auto, unique
from randomizer.game_assets.models.object_3d_model_class import OBJECT_3D_MODEL_CLASS

#################
##### CLASS #####
#################

@unique
class MODEL_ENUMS(StrEnum):
    skip = auto()
    banjo_fur = auto()
    banjo_skin = auto()
    banjo_eyelids = auto()
    banjo_eyes = auto()
    banjo_nose = auto()
    banjo_shorts = auto()
    banjo_belt = auto()
    banjo_necklace_tooth = auto()
    banjo_necklace_string = auto()
    backpack = auto()
    kazooie_feathers_primary = auto()
    kazooie_feathers_secondary = auto()
    kazooie_head_feather = auto()
    kazooie_eyes = auto()
    kazooie_beak_legs = auto()
    mouths = auto()
    turbo_talon_trainers = auto()
    wading_boots = auto()

class BANJO_KAZOOIE_HIGH_POLY_MODEL_CLASS(OBJECT_3D_MODEL_CLASS):
    '''
    Class for reading and modifying the BK High Poly Model.
    '''
    def __init__(self, file_path:str):
        super().__init__(file_path)
        self._json_file_dir:str = "characters/banjo_kazooie/"
        self._texture_dict:dict = {
            MODEL_ENUMS.skip: (1,),
            MODEL_ENUMS.banjo_belt: (0,),
            MODEL_ENUMS.banjo_skin: (3, 8,),
            MODEL_ENUMS.banjo_fur: (2,),
            MODEL_ENUMS.banjo_nose: (4,),
            MODEL_ENUMS.banjo_shorts: (5, 6, 7, 10,),
            MODEL_ENUMS.banjo_necklace_string: (9,),
            MODEL_ENUMS.backpack: (11, 12,),
            MODEL_ENUMS.banjo_eyelids: (13,),
            MODEL_ENUMS.banjo_eyes: (14,18,),
            MODEL_ENUMS.kazooie_feathers_primary: (15,),
            MODEL_ENUMS.banjo_belt: (16,),
            MODEL_ENUMS.kazooie_eyes: (17,),
            MODEL_ENUMS.kazooie_feathers_secondary: (15,19,),
            MODEL_ENUMS.turbo_talon_trainers: (20, 21, 22,),
            MODEL_ENUMS.wading_boots: (23,),
        }
        self._texture_specific_dict:dict = {
            3: {
                MODEL_ENUMS.banjo_skin: (0, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15,),
                MODEL_ENUMS.skip: (1, 7,),
            },
            8: {
                MODEL_ENUMS.banjo_skin: (0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,),
                MODEL_ENUMS.skip: (1, 10,),
            },
            15: {
                MODEL_ENUMS.kazooie_feathers_primary: (0, 1, 2, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15,),
                MODEL_ENUMS.kazooie_feathers_secondary: (3, 8, 9,),
            },
        }
        self._vertex_dict:dict = {
            (0x00, 0x00, 0x00, 0xFF): MODEL_ENUMS.skip, # Unk?
            (0x00, 0x1A, 0x4E, 0xFF): MODEL_ENUMS.backpack,
            (0x00, 0x22, 0x68, 0xFF): MODEL_ENUMS.backpack,
            (0x00, 0x30, 0x92, 0xFF): MODEL_ENUMS.backpack,
            (0x00, 0x4A, 0xE0, 0xFF): MODEL_ENUMS.backpack,
            (0x13, 0x19, 0x12, 0xFF): MODEL_ENUMS.wading_boots,
            (0x20, 0x20, 0x20, 0xFF): MODEL_ENUMS.turbo_talon_trainers,
            (0x21, 0x31, 0x1E, 0xFF): MODEL_ENUMS.wading_boots,
            (0x27, 0x0E, 0x00, 0xFF): MODEL_ENUMS.banjo_fur,
            (0x2B, 0x71, 0xFF, 0xFF): MODEL_ENUMS.backpack,
            (0x2D, 0x00, 0x32, 0xFF): MODEL_ENUMS.kazooie_feathers_primary,
            (0x36, 0x4F, 0x32, 0xFF): MODEL_ENUMS.wading_boots,
            (0x38, 0x38, 0x38, 0xFF): MODEL_ENUMS.turbo_talon_trainers,
            (0x3C, 0x0D, 0x22, 0xFF): MODEL_ENUMS.mouths,
            (0x41, 0x17, 0x00, 0xFF): MODEL_ENUMS.banjo_fur,
            (0x45, 0x25, 0x1F, 0xFF): MODEL_ENUMS.banjo_skin,
            (0x4F, 0x4F, 0x4F, 0xFF): MODEL_ENUMS.skip, # Unk?
            (0x52, 0x00, 0x00, 0xFF): MODEL_ENUMS.kazooie_feathers_primary,
            (0x55, 0x8D, 0xFF, 0xFF): MODEL_ENUMS.backpack,
            (0x5C, 0x87, 0x54, 0xFF): MODEL_ENUMS.wading_boots,
            (0x63, 0x25, 0x01, 0xFF): MODEL_ENUMS.banjo_fur,
            (0x66, 0x23, 0x00, 0xFF): MODEL_ENUMS.kazooie_beak_legs,
            (0x66, 0x37, 0x2F, 0xFF): MODEL_ENUMS.banjo_skin,
            (0x7A, 0x7A, 0x7A, 0xFF): MODEL_ENUMS.skip, # Unk?
            (0x7F, 0xA9, 0xFF, 0xFF): MODEL_ENUMS.backpack,
            (0x80, 0x1F, 0x4B, 0xFF): MODEL_ENUMS.mouths,
            (0x83, 0x32, 0x03, 0xFF): MODEL_ENUMS.banjo_fur,
            (0x87, 0x47, 0x08, 0xFF): MODEL_ENUMS.banjo_fur,
            (0x88, 0x00, 0x00, 0xFF): MODEL_ENUMS.kazooie_feathers_primary,
            (0x92, 0x39, 0x00, 0xFF): MODEL_ENUMS.kazooie_beak_legs,
            (0x99, 0x54, 0x47, 0xFF): MODEL_ENUMS.banjo_skin,
            (0xA3, 0x10, 0x36, 0xFF): MODEL_ENUMS.mouths,
            (0xA7, 0xA7, 0xA7, 0xFF): MODEL_ENUMS.skip, # Unk?
            (0xAE, 0x47, 0x07, 0xFF): MODEL_ENUMS.banjo_fur,
            (0xB3, 0x2C, 0x69, 0xFF): MODEL_ENUMS.mouths,
            (0xBA, 0x55, 0x00, 0xFF): MODEL_ENUMS.banjo_shorts,
            (0xBA, 0x7F, 0x4B, 0xFF): MODEL_ENUMS.mouths,
            (0xC6, 0x6E, 0x5C, 0xFF): MODEL_ENUMS.banjo_skin,
            (0xC7, 0x47, 0x00, 0xFF): MODEL_ENUMS.kazooie_beak_legs,
            (0xCC, 0x56, 0x0B, 0xFF): MODEL_ENUMS.banjo_fur,
            (0xCE, 0x87, 0x00, 0xFF): MODEL_ENUMS.banjo_shorts,
            (0xD0, 0x00, 0x00, 0xFF): MODEL_ENUMS.kazooie_feathers_primary,
            (0xDB, 0xDB, 0xDB, 0xFF): MODEL_ENUMS.turbo_talon_trainers,
            (0xEA, 0xEA, 0x00, 0xFF): MODEL_ENUMS.banjo_shorts,
            (0xEB, 0x83, 0x6D, 0xFF): MODEL_ENUMS.banjo_skin,
            (0xF6, 0xB4, 0x00, 0xFF): MODEL_ENUMS.banjo_shorts,
            (0xFA, 0x6F, 0x12, 0xFF): MODEL_ENUMS.banjo_fur,
            (0xFE, 0xA1, 0x31, 0xFF): MODEL_ENUMS.kazooie_beak_legs,
            (0xFF, 0x33, 0x00, 0xFF): MODEL_ENUMS.kazooie_feathers_primary,
            (0xFF, 0x34, 0x52, 0xFF): MODEL_ENUMS.mouths,
            (0xFF, 0x5F, 0x00, 0xFF): MODEL_ENUMS.kazooie_feathers_primary,
            (0xFF, 0x74, 0x25, 0xFF): MODEL_ENUMS.kazooie_beak_legs,
            (0xFF, 0x89, 0x00, 0xFF): MODEL_ENUMS.kazooie_feathers_primary,
            (0xFF, 0xA3, 0x85, 0xFF): MODEL_ENUMS.banjo_skin,
            (0xFF, 0xBE, 0x97, 0xFF): MODEL_ENUMS.banjo_skin,
            (0xFF, 0xC7, 0x00, 0xFF): MODEL_ENUMS.kazooie_feathers_secondary,
            (0xFF, 0xCF, 0x3D, 0xFF): MODEL_ENUMS.kazooie_beak_legs,
            (0xFF, 0xEA, 0xB4, 0xFF): MODEL_ENUMS.banjo_skin,
            (0xFF, 0xFF, 0x28, 0xFF): MODEL_ENUMS.banjo_shorts,
            (0xFF, 0xFF, 0x9F, 0xFF): MODEL_ENUMS.kazooie_beak_legs,
            (0xFF, 0xFF, 0xFF, 0xFF): MODEL_ENUMS.skip, # Unk?
        }
        self._vertex_count_dict:dict = {}
        for vert_count in range(0x4EC, 0x4F5 + 0x1):
            self._vertex_count_dict[vert_count] = MODEL_ENUMS.banjo_necklace_tooth
        for vert_count in range(0x640, 0x64F + 0x1):
            self._vertex_count_dict[vert_count] = MODEL_ENUMS.kazooie_head_feather
        for vert_count in range(0x1225, 0x122F + 0x1):
            self._vertex_count_dict[vert_count] = MODEL_ENUMS.kazooie_head_feather

if __name__ == '__main__':
    from randomizer.constants.str_values.string_constants import STRING_CONSTANTS as STR_CONST
    load_file:str = "C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/temp/bk_model_test/original.bin"
    save_file_path:str = "C:/Users/Cyrus/Desktop/N64/ROMs/GEDecompressor_Files/temp/bk_model_test/"
    json_file:str = "wario_and_waluigi"
    asset_id:int = 0x034E
    byte_count:int = 2
    file_name:str = (str(hex(asset_id))[2:]).zfill(byte_count * 2).upper()
    file_path:str = STR_CONST.extracted_files_dir + file_name + STR_CONST.decompressed_bin_extension
    high_poly_bk_model = BANJO_KAZOOIE_HIGH_POLY_MODEL_CLASS(load_file)
    high_poly_bk_model.read_object_3d_model_file()
    high_poly_bk_model.color_by_json(json_file)
    high_poly_bk_model.save_object_3d_model_file(file_path=(save_file_path + json_file + ".bin"))
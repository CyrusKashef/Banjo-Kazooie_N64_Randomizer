###################
##### IMPORTS #####
###################

from randomizer.patching.bk_rom_class import BK_ROM_CLASS
from randomizer.assembly.assembly import ASSEMBLY_CLASS
from randomizer.contants.variables.patching_variables import BIN_EXTENSION

#####################
##### CONSTANTS #####
#####################

ORIGINAL_ROM_PATH_STR:str = "Original ROM Path"
NEW_ROM_PATH_STR:str = "New ROM Path"
BOOT_TO_FILE_SELECT_STR:str = "Boot To File Select"

######################################
##### MODIFICATION PROCESS CLASS #####
######################################

class MODIFICATION_PROCESS_CLASS():
    '''
    Pass
    '''
    def __init__(self):
        pass

    def _hardcoded_settings(self):
        '''
        Pass
        '''
        self._settings_dict:dict = {
            ORIGINAL_ROM_PATH_STR: "C:/Users/Cyrus/Documents/VS_Code/Banjo-Kazooie_Randomizer/Banjo-Kazooie_N64_Randomizer/Banjo-Kazooie.z64",
            NEW_ROM_PATH_STR: "C:/Users/Cyrus/Documents/VS_Code/Banjo-Kazooie_Randomizer/Banjo-Kazooie_N64_Randomizer/Banjo-Kazooie-TEST.z64",
            BOOT_TO_FILE_SELECT_STR: 1,
        }

    def _modification_setup(self):
        '''
        Pass
        '''
        self._bk_rom = BK_ROM_CLASS(self._settings_dict[ORIGINAL_ROM_PATH_STR])
        self._bk_rom.extract_asset_table_pointers()
        self._bk_rom.extract_assembly_files()
    
    def _logic_process(self):
        '''
        Pass
        '''
        pass

    def _asset_modifications(self):
        '''
        Pass
        '''
        pass

    def _assembly_modifications(self):
        '''
        Pass
        '''
        asm_obj = ASSEMBLY_CLASS()
        asm_obj.disable_anti_tamper()
        asm_obj.patch_yum_yum_crash_fix()
        if(BOOT_TO_FILE_SELECT_STR):
            asm_obj.boot_to_file_select()
        asm_obj.save_all_assembly_changes()
    
    def _modification_finalization(self):
        '''
        Pass
        '''
        self._bk_rom.append_asset_table_pointers()
        self._bk_rom.insert_assembly_files()
        self._bk_rom.rename_bk_rom()
        self._bk_rom.calculate_new_crc()
        self._bk_rom.save_as_new_rom(self._settings_dict[NEW_ROM_PATH_STR])

    def _cleanup(self):
        '''
        Pass
        '''
        self._bk_rom.clear_extracted_files_dir(BIN_EXTENSION)

    ################
    ##### MAIN #####
    ################

    def main(self):
        '''
        Pass
        '''
        self._hardcoded_settings()
        self._modification_setup()
        self._logic_process()
        self._asset_modifications()
        self._assembly_modifications()
        self._modification_finalization()
        self._cleanup()
    
if __name__ == '__main__':
    modification_process_obj = MODIFICATION_PROCESS_CLASS()
    modification_process_obj.main()
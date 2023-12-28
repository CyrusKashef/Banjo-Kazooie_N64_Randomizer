'''
Purpose:
*
'''

###################
##### IMPORTS #####
###################

from randomizer.assembly.c_libraries.c_libraries_code import C_LIBRARIES_CODE_CLASS
from randomizer.assembly.c_libraries.c_libraries_data import C_LIBRARIES_DATA_CLASS
from randomizer.assembly.game_engine.game_engine_code import GAME_ENGINE_CODE_CLASS
from randomizer.assembly.game_engine.game_engine_data import GAME_ENGINE_DATA_CLASS
from randomizer.assembly.spiral_mountain.spiral_mountain_code import SPIRAL_MOUNTAIN_CODE_CLASS
from randomizer.assembly.spiral_mountain.spiral_mountain_data import SPIRAL_MOUNTAIN_DATA_CLASS
from randomizer.assembly.mumbos_mountain.mumbos_mountain_code import MUMBOS_MOUNTAIN_CODE_CLASS
from randomizer.assembly.mumbos_mountain.mumbos_mountain_data import MUMBOS_MOUNTAIN_DATA_CLASS
from randomizer.assembly.treasure_trove_cove.treasure_trove_cove_code import TREASURE_TROVE_COVE_CODE_CLASS
from randomizer.assembly.treasure_trove_cove.treasure_trove_cove_data import TREASURE_TROVE_COVE_DATA_CLASS
from randomizer.assembly.clankers_cavern.clankers_cavern_code import CLANKERS_CAVERN_CODE_CLASS
from randomizer.assembly.clankers_cavern.clankers_cavern_data import CLANKERS_CAVERN_DATA_CLASS
from randomizer.assembly.bubblegloop_swamp.bubblegloop_swamp_code import BUBBLEGLOOP_SWAMP_CODE_CLASS
from randomizer.assembly.bubblegloop_swamp.bubblegloop_swamp_data import BUBBLEGLOOP_SWAMP_DATA_CLASS
from randomizer.assembly.freezeezy_peak.freezeezy_peak_code import FREEZEEZY_PEAK_CODE_CLASS
from randomizer.assembly.freezeezy_peak.freezeezy_peak_data import FREEZEEZY_PEAK_DATA_CLASS
from randomizer.assembly.gobis_valley.gobis_valley_code import GOBIS_VALLEY_CODE_CLASS
from randomizer.assembly.gobis_valley.gobis_valley_data import GOBIS_VALLEY_DATA_CLASS
from randomizer.assembly.mad_monster_mansion.mad_monster_mansion_code import MAD_MONSTER_MANSION_CODE_CLASS
from randomizer.assembly.mad_monster_mansion.mad_monster_mansion_data import MAD_MONSTER_MANSION_DATA_CLASS
from randomizer.assembly.rusty_bucket_bay.rusty_bucket_bay_code import RUSTY_BUCKET_BAY_CODE_CLASS
from randomizer.assembly.rusty_bucket_bay.rusty_bucket_bay_data import RUSTY_BUCKET_BAY_DATA_CLASS
from randomizer.assembly.click_clock_wood.click_clock_wood_code import CLICK_CLOCK_WOOD_CODE_CLASS
from randomizer.assembly.click_clock_wood.click_clode_wood_data import CLICK_CLOCK_WOOD_DATA_CLASS
from randomizer.assembly.gruntildas_lair.gruntildas_lair_code import GRUNTILDAS_LAIR_CODE_CLASS
from randomizer.assembly.gruntildas_lair.gruntildas_lair_data import GRUNTILDAS_LAIR_DATA_CLASS
from randomizer.assembly.final_battle.final_battle_code import FINAL_BATTLE_CODE_CLASS
from randomizer.assembly.final_battle.final_battle_data import FINAL_BATTLE_DATA_CLASS
from randomizer.assembly.cutscenes.cutscenes_code import CUTSCENES_CODE_CLASS
from randomizer.assembly.cutscenes.cutscenes_data import CUTSCENES_DATA_CLASS


####################
##### ASSEMBLY #####
####################

class ASSEMBLY_CLASS():
    '''
    Pass
    '''
    def __init__(self):
        '''
        Pass
        '''
        self._create_assembly_file_objects()

    ################################
    ##### ALWAYS RUN FUNCTIONS #####
    ################################

    def _create_assembly_file_objects(self):
        '''
        Pass
        '''
        self._c_libraries_code_obj = C_LIBRARIES_CODE_CLASS(file_name="F19250")
        self._c_libraries_data_obj = C_LIBRARIES_DATA_CLASS(file_name="F362EB")
        self._game_engine_code_obj = GAME_ENGINE_CODE_CLASS(file_name="F37F90")
        self._game_engine_data_obj = GAME_ENGINE_DATA_CLASS(file_name="F9CAE0")
        self._spiral_mountain_code_obj = SPIRAL_MOUNTAIN_CODE_CLASS(file_name="FC4810")
        self._spiral_mountain_data_obj = SPIRAL_MOUNTAIN_DATA_CLASS(file_name="FC6C0F")
        self._mumbos_mountain_code_obj = MUMBOS_MOUNTAIN_CODE_CLASS(file_name="FB24A0")
        self._mumbos_mountain_data_obj = MUMBOS_MOUNTAIN_DATA_CLASS(file_name="FB42D9")
        self._treasure_trove_cove_code_obj = TREASURE_TROVE_COVE_CODE_CLASS(file_name="FAE860")
        self._treasure_trove_cove_data_obj = TREASURE_TROVE_COVE_DATA_CLASS(file_name="FB1AEB")
        self._clankers_cavern_code_obj = CLANKERS_CAVERN_CODE_CLASS(file_name="FA3FD0")
        self._clankers_cavern_data_obj = CLANKERS_CAVERN_DATA_CLASS(file_name="FA5D96")
        self._bubblegloop_swamp_code_obj = BUBBLEGLOOP_SWAMP_CODE_CLASS(file_name="FB44E0")
        self._bubblegloop_swamp_data_obj = BUBBLEGLOOP_SWAMP_DATA_CLASS(file_name="FB9610")
        self._freezeezy_peak_code_obj = FREEZEEZY_PEAK_CODE_CLASS(file_name="FBEBE0")
        self._freezeezy_peak_data_obj = FREEZEEZY_PEAK_DATA_CLASS(file_name="FC3FEF")
        self._gobis_valley_code_obj = GOBIS_VALLEY_CODE_CLASS(file_name="FA9150")
        self._gobis_valley_data_obj = GOBIS_VALLEY_DATA_CLASS(file_name="FAE27E")
        self._mad_monster_mansion_code_obj = MAD_MONSTER_MANSION_CODE_CLASS(file_name="FA5F50")
        self._mad_monster_mansion_data_obj = MAD_MONSTER_MANSION_DATA_CLASS(file_name="FA8CE6")
        self._rusty_bucket_bay_code_obj = RUSTY_BUCKET_BAY_CODE_CLASS(file_name="FB9A30")
        self._rusty_bucket_bay_data_obj = RUSTY_BUCKET_BAY_DATA_CLASS(file_name="FBE5E2")
        self._click_clock_wood_code_obj = CLICK_CLOCK_WOOD_CODE_CLASS(file_name="FD6190")
        self._click_clock_wood_data_obj = CLICK_CLOCK_WOOD_DATA_CLASS(file_name="FDA2FF")
        self._gruntildas_lair_code_obj = GRUNTILDAS_LAIR_CODE_CLASS(file_name="FC9150")
        self._gruntildas_lair_data_obj = GRUNTILDAS_LAIR_DATA_CLASS(file_name="FCF698")
        self._final_battle_code_obj = FINAL_BATTLE_CODE_CLASS(file_name="FD0420")
        self._final_battle_data_obj = FINAL_BATTLE_DATA_CLASS(file_name="FD5A60")
        self._cutscenes_code_obj = CUTSCENES_CODE_CLASS(file_name="FC6F20")
        self._cutscenes_data_obj = CUTSCENES_DATA_CLASS(file_name="FC8AFC")

    def disable_anti_tamper(self):
        '''
        Pass
        '''
        self._c_libraries_code_obj.disable_anti_tamper()
    
    def patch_yum_yum_crash_fix(self):
        '''
        Pass
        '''
        self._c_libraries_code_obj.patch_yum_yum_crash_fix()
        self._treasure_trove_cove_code_obj.patch_yum_yum_crash_fix()
    
    def save_all_assembly_changes(self):
        '''
        Pass
        '''
        self._c_libraries_code_obj._save_changes()
        self._c_libraries_data_obj._save_changes()
        self._game_engine_code_obj._save_changes()
        self._game_engine_data_obj._save_changes()
        self._spiral_mountain_code_obj._save_changes()
        self._spiral_mountain_data_obj._save_changes()
        self._mumbos_mountain_code_obj._save_changes()
        self._mumbos_mountain_data_obj._save_changes()
        self._treasure_trove_cove_code_obj._save_changes()
        self._treasure_trove_cove_data_obj._save_changes()
        self._clankers_cavern_code_obj._save_changes()
        self._clankers_cavern_data_obj._save_changes()
        self._bubblegloop_swamp_code_obj._save_changes()
        self._bubblegloop_swamp_data_obj._save_changes()
        self._freezeezy_peak_code_obj._save_changes()
        self._freezeezy_peak_data_obj._save_changes()
        self._gobis_valley_code_obj._save_changes()
        self._gobis_valley_data_obj._save_changes()
        self._mad_monster_mansion_code_obj._save_changes()
        self._mad_monster_mansion_data_obj._save_changes()
        self._rusty_bucket_bay_code_obj._save_changes()
        self._rusty_bucket_bay_data_obj._save_changes()
        self._click_clock_wood_code_obj._save_changes()
        self._click_clock_wood_data_obj._save_changes()
        self._gruntildas_lair_code_obj._save_changes()
        self._gruntildas_lair_data_obj._save_changes()
        self._final_battle_code_obj._save_changes()
        self._final_battle_data_obj._save_changes()
        self._cutscenes_code_obj._save_changes()
        self._cutscenes_data_obj._save_changes()

    #############################
    ##### FEATURE FUNCTIONS #####
    #############################
    
    def boot_to_file_select(self):
        '''
        Pass
        '''
        file_select_map_id:int = 0x91
        self._c_libraries_code_obj.booting_up_map(file_select_map_id)
        self._game_engine_code_obj.booting_up_map(file_select_map_id)
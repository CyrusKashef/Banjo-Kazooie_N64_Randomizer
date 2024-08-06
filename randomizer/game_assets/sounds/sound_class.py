'''
Purpose:
* 

Decomp:
 * https://gitlab.com/banjo.decomp/banjo-kazooie/-/blob/master/include/2.0L/PR/libaudio.h
'''

###################
##### IMPORTS #####
###################

from randomizer.generic_bin_file_class import Generic_Bin_File_Class

#######################
##### SOUND CLASS #####
#######################

class SOUND_CLASS(Generic_Bin_File_Class):
    '''
    Class for reading and modifying object model files.
    '''
    def __init__(self, file_path:str):
        '''
        Constructor
        '''
        # Constant
        # Variables
        self._file_path:str = file_path
        self._tracks:dict = {}

    def read_meta_event(self):
        '''
        Pass
        '''
        # If Meta Event is 0x51, Set Tempo
        # If Meta Event is 0x2F, End Flag
        pass
    
    def read_midi_file_header(self):
        '''
        Pass
        '''
        track_interval:int = 0x4
        for track_count in range(0x10):
            track_header_address:int = track_count * track_interval
            track_address:int = self._read_bytes_as_int(track_header_address, byte_count=4)
            self._tracks[track_count] = 0
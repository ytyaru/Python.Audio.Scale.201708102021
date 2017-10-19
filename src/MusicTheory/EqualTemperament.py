import math
import MusicTheory.Key
#十二平均律
class EqualTemperament:
    def __init__(self):
        self.__ids = (0,1,2,3,4,5,6,7,8,9,10,11)
        self.__names = ('C','C#','D','D#','E','F','F#','G','G#','A','A#','B')
        self.__diffs = (-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2)
        self.__frequencies = []
        self.__base_pitch = 4
        self.__CreateFrequencies()
    def __CreateFrequencies(self):
        self.__frequencies.clear()
        for diff in self.__diffs: self.__frequencies.append(440 * math.pow(2, diff * (1/12.0)))
    def __calc_frequency(self, key_id, pitch):
#        print('f0', key_id, pitch, 440 * math.pow(2, self.__diffs[key_id] * (1/12.0)))
#        print('{0:>2} {1:>3} {2:f}'.format(key_id, pitch, 440 * math.pow(2, self.__diffs[key_id] * (1/12.0))))
        print('{0:<2} {1:>2} {2:>3} {3:f}'.format(self.__names[key_id], key_id, pitch, 440 * math.pow(2, self.__diffs[key_id] * (1/12.0))))
        if 4 == pitch: return 440 * math.pow(2, self.__diffs[key_id] * (1/12.0))
        elif pitch < 4: return ( 440 * math.pow(2, self.__diffs[key_id] * (1/12.0)) ) / ((4 - pitch) + 1)
        elif 4 < pitch: return ( 440 * math.pow(2, self.__diffs[key_id] * (1/12.0)) ) * ((pitch - 4) + 1)
        else: raise Exception('実行されることのないelse文。')
    def FromId(self, key_id, pitch=4): return self.__calc_frequency(key_id, pitch)
    def FromKey(self, key:MusicTheory.Key.Key, pitch=4): return self.__calc_frequency(key.Id, pitch)
    @property
    def Ids(self): return self.__ids
    @property
    def Names(self): return self.__names
    @property
    def Frequencies(self): return self.__frequencies

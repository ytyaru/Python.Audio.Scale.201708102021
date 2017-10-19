#https://ja.wikipedia.org/wiki/%E9%9F%B3%E9%9A%8E
import MusicTheory.EqualTemperament
import MusicTheory.Key
#Scale,Key,KeyPitchの3つを指定して周波数の絶対値を算出する。（12平均律）
class Scale:
    def __init__(self):
#        self.__major = [2,2,1,2,2,2,1]
#        self.__minor = [2,1,2,2,1,2,2]
        self.__scales = []
        self.__frequencies = []
        self.__key = 'C' #変化記号は+,-
        self.__key_pitch = 4 # キーの音の高さ(C4等)
        self.__et = MusicTheory.EqualTemperament.EqualTemperament()

    @property
    def Scales(self): return self.__scales
    @Scales.setter
    def Scales(self, v):
        if hasattr(v, 'Intervals'):
            self.__scales = v
            self.__SetIntervals()
    @property
    def Key(self): return self.__scales[0]
    @property
    def Key(self, v): self.__key = MusicTheory.Key.Key().Get(v)
    @property
    def KeyPitch(self): return self.__key_pitch
    @property
    def Frequencies(self): return self.__frequencies

    def __SetIntervals(self, scale, key):
        k = MusicTheory.Key.Key()
        v = k.Get(key)
        self.Scales.clear()
        self.Frequencies.clear()
        self.Scales.append(v)
        k.Get(MusicTheory.Key.Key.ValueToName(v))
        self.Frequencies.append(self.__et.FromKey(k, pitch))
        for interval in scale.Intervals:
            v += interval
            if v < 0: v = len(self.__et.Keys) - abs(v)
            elif len(self.__et.Ids)-1 < v:
                pitch += 1
                v %= len(self.__et.Ids)
            self.__scales.append(v)
            k.Get(MusicTheory.Key.Key.ValueToName(v))
            self.__frequencies.append(self.__et.FromKey(k, pitch))
    
    # ドレミファソラシド(C,D,E,F,G,A,B)
#    def Major(self, key='C', pitch=4): return self.__create_scales(self.__major, key, pitch)
#    def Minor(self, key='C', pitch=4): return self.__create_scales(self.__minor, key, pitch)
    def __create_scales(self, scales, key, pitch):
        self.__scales.clear()
        self.__frequencies.clear()
        k = MusicTheory.Key.Key()
        v = k.Get(key)
        self.__scales.append(v)
        k.Get(MusicTheory.Key.Key.ValueToName(v))
        self.__frequencies.append(self.__et.FromKey(k, pitch))
        for interval in scales:
            #0-11
            #-1-->11
            #-2-->10
            #12-->0
            #13-->1
            v += interval
            if v < 0: v = len(self.__et.Keys) - abs(v)
            elif len(self.__et.Ids)-1 < v:
                pitch += 1
                v %= len(self.__et.Ids)
            self.__scales.append(v)
            k.Get(MusicTheory.Key.Key.ValueToName(v))
            self.__frequencies.append(self.__et.FromKey(k, pitch))
            
#        print('self.__scales:', self.__scales)
#        print('self.__frequencies:', self.__frequencies)
        return self.__scales


if __name__ == '__main__':
    s = Scale()
    print('---------- メジャー・スケール ----------')
    for key in ['C','C+','D','D+','E','F','F+','G','G+','A','A+','B']:
        print(key, 'メジャー・スケール')
        print(s.Major(key=key))
        print(','.join([Key.Key.ValueToName(k) for k in s.Scales]))
    print('---------- マイナー・スケール ----------')
    for key in ['C','C+','D','D+','E','F','F+','G','G+','A','A+','B']:
        print(s.Minor(key=key))
        print(','.join([Key.Key.ValueToName(k) for k in s.Scales]))

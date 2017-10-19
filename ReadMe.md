# このソフトウェアについて

音名と変化記号から音高(pitch)を算出できるようにした。C=0, B=11, C+=1, C-=11(pitch-1), B3+=0(pitch+1)

* 幹音の表記名を`C`,`D`,`E`,`F`,`G`,`A`,`B`と定義した
* 変化記号`♭`,`♯`の表記名を`-`,`+`と定義した
* 変化記号`-`,`+`の変化量を`-1`,`+1`と定義した
* 12平均律における12音の絶対値を`0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11`と定義した(`C,C+,D,D+,E,F,F+,G,G+,A,A+,B`)
* 幹音と変化記号の表記名を、12音の絶対値と音高(pitch)に変換する `C+`=1(pitch=4), `C-`=11(pitch=3)

# 対象ファイル名

ファイル名|説明
----------|----
NaturalTone.py|幹音の定義
Accidental.py|変化記号の定義
ToneAccidentaler.py|幹音と変化記号の表記名を、12音の絶対値と音高(pitch)に変換する

# 実行

```sh
$ cd src/MusicTheory
$ python ToneAccidentaler.py
```

```sh
C (0, 4)
D (2, 4)
E (4, 4)
F (5, 4)
G (7, 4)
A (9, 4)
B (11, 4)

C+ (1, 4)
D+ (3, 4)
E+ (5, 4)
F+ (6, 4)
G+ (8, 4)
A+ (10, 4)
B+ (0, 5)

C- (11, 3)
D- (1, 4)
E- (3, 4)
F- (4, 4)
G- (6, 4)
A- (8, 4)
B- (10, 4)

C (0, 4)
C- (11, 3)
C-- (10, 3)
C--- (9, 3)
C---- (8, 3)
C----- (7, 3)
C------ (6, 3)
C------- (5, 3)
C-------- (4, 3)
C--------- (3, 3)
C---------- (2, 3)
C----------- (1, 3)
C------------ (0, 3)
C------------- (11, 2)
C-------------- (10, 2)
C--------------- (9, 2)
C---------------- (8, 2)
C----------------- (7, 2)
C------------------ (6, 2)
C------------------- (5, 2)
C-------------------- (4, 2)
C--------------------- (3, 2)
C---------------------- (2, 2)
C----------------------- (1, 2)
C------------------------ (0, 2)

C (0, -1)
C+ (1, -1)
C++ (2, -1)
C+++ (3, -1)
C++++ (4, -1)
C+++++ (5, -1)
C++++++ (6, -1)
C+++++++ (7, -1)
C++++++++ (8, -1)
C+++++++++ (9, -1)
C++++++++++ (10, -1)
C+++++++++++ (11, -1)
C++++++++++++ (0, 0)
C+++++++++++++ (1, 0)
C++++++++++++++ (2, 0)
C+++++++++++++++ (3, 0)
C++++++++++++++++ (4, 0)
C+++++++++++++++++ (5, 0)
C++++++++++++++++++ (6, 0)
C+++++++++++++++++++ (7, 0)
C++++++++++++++++++++ (8, 0)
C+++++++++++++++++++++ (9, 0)
C++++++++++++++++++++++ (10, 0)
C+++++++++++++++++++++++ (11, 0)
C++++++++++++++++++++++++ (0, 1)
```

# 開発環境

* Linux Mint 17.3 MATE 32bit
* [libav](http://ytyaru.hatenablog.com/entry/2018/08/24/000000)
    * [各コーデック](http://ytyaru.hatenablog.com/entry/2018/08/23/000000)
* [pyenv](https://github.com/pylangstudy/201705/blob/master/27/Python%E5%AD%A6%E7%BF%92%E7%92%B0%E5%A2%83%E3%82%92%E7%94%A8%E6%84%8F%E3%81%99%E3%82%8B.md) 1.0.10
    * Python 3.6.1
        * [pydub](http://ytyaru.hatenablog.com/entry/2018/08/25/000000)
        * [PyAudio](http://ytyaru.hatenablog.com/entry/2018/07/27/000000) 0.2.11
            * [ALSA lib pcm_dmix.c:1022:(snd_pcm_dmix_open) unable to open slave](http://ytyaru.hatenablog.com/entry/2018/07/29/000000)
        * [matplotlib](http://ytyaru.hatenablog.com/entry/2018/07/22/000000)
            * [matplotlibでのグラフ表示を諦めた](http://ytyaru.hatenablog.com/entry/2018/08/05/000000)

# 参考

音名。

* https://ja.wikipedia.org/wiki/%E9%9F%B3%E5%90%8D%E3%83%BB%E9%9A%8E%E5%90%8D%E8%A1%A8%E8%A8%98

ほぼ丸パクリした。感謝。

* http://www.non-fiction.jp/2015/08/17/sin_wave/
* http://aidiary.hatenablog.com/entry/20110607/1307449007
* http://ism1000ch.hatenablog.com/entry/2013/11/15/182442

# ライセンス

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

Library|License|Copyright
-------|-------|---------
[pydub](https://github.com/jiaaro/pydub)|[MIT](https://github.com/jiaaro/pydub/blob/master/LICENSE)|[Copyright (c) 2011 James Robert, http://jiaaro.com](https://github.com/jiaaro/pydub/blob/master/LICENSE)
[pygame](http://www.pygame.org/)|[LGPL](https://www.pygame.org/docs/)|[pygame](http://www.pygame.org/)


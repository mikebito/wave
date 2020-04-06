#プロット関係のライブラリ
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
import sys
from time import time

#音声関係のライブラリ
import pyaudio
import struct


#マイクインプット設定
CHUNK=1024             #1度に読み取る音声のデータ幅
RATE=44100             #サンプリング周波数
audio=pyaudio.PyAudio()
stream=audio.open(
                format=pyaudio.paInt16,
                channels=1,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK,
                input_device_index=2)


try:
    while stream.is_active():
        start1 = time()
        ret=stream.read(CHUNK,)    #音声の読み取り(バイナリ)
        #バイナリ → 数値(int16)に変換
        #32768.0=2^16で割ってるのは正規化(絶対値を1以下にすること)
        ret=np.frombuffer(ret, dtype="int16")
        ret2=np.array(ret)
        ret3=ret2*-1
        ret4=ret3.tobytes()
        output = stream.write(ret4)
        proc_time = time() - start1
        print(proc_time)
except KeyboardInterrupt:
    stream.stop_stream()
    stream.close()
    audio.terminate()
    print("Stop Streaming")
    soku = 1 / 440
    print(soku)

    
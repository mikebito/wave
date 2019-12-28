#使うモジュール
import pyaudio                      #録音    
import numpy as np                  #計算
import matplotlib.pyplot as plt     #グラフ化

#設定
chunk = 1024
FORMAT = pyaudio.paInt16        #整数型
CHANNELS = 1                    #チャンネル数
RATE = 44100                    #441.kHz
RECORD_SECONDS = 3              #３秒録音

p = pyaudio.PyAudio()           

stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                frames_per_buffer = chunk
)

print("Now Recording...")
all = []
for i in range (0,int(RATE / chunk * RECORD_SECONDS)): 
    data = stream.read(chunk)
    all.append(data)

print("Finished Recording.")

stream.close()
p.terminate()

data = b"".join(all)
result = np.frombuffer(data,dtype="int16") / float (2**15)
minus = result * -1


plt.plot(result, color = "blue", linestyle = "-")
plt.plot(minus, color = "cyan", linestyle = "--")
plt.savefig('wave.png')
plt.savefig('wave.pdf')
plt.show()


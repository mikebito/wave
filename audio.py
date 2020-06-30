#使うモジュール
import pyaudio                      #録音用    
import numpy as np                  #計算用
import matplotlib.pyplot as plt     #グラフ化用

#設定
chunk = 2048             #音声データメモリーサイズ指定
FORMAT = pyaudio.paInt16        #16進数に指定
CHANNELS = 1                    #モノラルに指定
RATE = 96000                     #サンプリング速度
RECORD_SECONDS = 3              #３秒録音

p = pyaudio.PyAudio()           #!!!要調べ！！！

 #!!!要調べ！！！
stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                frames_per_buffer = chunk
)
 #!!!要調べ！！！
print("Now Recording...")
all = [] #リスト作成
for i in range (0,int(RATE / chunk * RECORD_SECONDS)): 
    data = stream.read(chunk)
    all.append(data)

print(all)
print("Finished Recording.")

stream.close()              
p.terminate()

 #!!!要調べ！！！
data = b"".join(all)
result = np.frombuffer(data,dtype="int32") / float (2**15)
minus = result * -1

 #!!!要調べ！！！
plt.plot(result, color = "blue", linestyle = "-")
# plt.plot(minus, color = "orange", linestyle = "-")
plt.savefig('wave.png')
plt.savefig('wave.pdf')
plt.show()

plt.plot(result, color = "blue", linestyle = "-")
plt.plot(minus, color = "orange", linestyle = "-")

plt.show()
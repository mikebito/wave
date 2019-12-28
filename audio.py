import pyaudio
import numpy as np
import matplotlib.pyplot as plt 

chunk = 1024
FORMAT = pyaudio.paInt16

CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 3
p = pyaudio.PyAudio()

stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                output = True,
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


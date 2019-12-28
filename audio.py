import pyaudio
import numpy as np
import matplotlib.pyplot as plt 
import wave

chunk = 1024
FORMAT = pyaudio.paInt16

CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 3
WAVE_OUTPUT_FILENAME = "output.wav"
r= 1.059463094
r12=r*r*r*r
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



a = np.frombuffer(data,dtype="int16")
result2 = np.frombuffer(data,dtype="int8") / float (2**15)
result3 = np.frombuffer(data,dtype="int32") / float (2**15)
result4 = np.frombuffer(data,dtype="int64") / float (2**15)
minus = result * -1
try:
    with open ('file.txt', 'w') as f:
        print(a, result, result2, result3, minus, file=ｆ)
        b = type(result),type(a),
        c = result.dtype, a.dtype,
        d = float (2**15)
        e = type(d)
        f = result.ndim, a.ndim,
        g = result.real, a.real,
        h = result.imag, a.imag,

        print(b)
        print(c) 
        print(d)
        print(e)
        print(f)
        print(g)
        print(h)
except FileExistsError:
    pass


plt.plot(result, color = "blue", linestyle = "-")
plt.plot(minus, color = "cyan", linestyle = "--")
# plt.plot(result2, color = "red", linestyle = "--")
# plt.plot(result3, color = "green", linestyle = "-.")
# plt.plot(a, color = "magenta", linestyle = "-")
plt.savefig('wave.png')
plt.savefig('wave.pdf')
plt.show()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(all)) 
wf.close()

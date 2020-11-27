import wave #встроенная
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math #встроенная
import wavio #импортируется pip install
import soundfile as sf #импортируется pip install
from int3 import sign_int3
from distortion import distortion

"""
Предупреждение! Последняя строчка файла - создание файла с перегруженной гитарой
"""

def format_time(x, pos=None):
    global duration, nframes
    progress = int(x / float(nframes) * duration)
    mins, secs = divmod(progress, 60)
    hours, mins = divmod(mins, 60)
    out = "%d:%02d" % (mins, secs)
    if hours > 0:
        out = "%d:" % hours
    return out

def format_db(x, pos=None):
    if pos == 0:
        return ""
    global roof
    if x == 0:
        return "-inf"
    db = 20 * math.log10(abs(x) / float(roof))
    return int(db)

wav = wave.open("sample1.wav", mode="r")
(nchannels, sampwidth, framerate, nframes, comp_type, comp_name) = wav.getparams()
content = wav.readframes(nframes)
print(nchannels, sampwidth, framerate, nframes, comp_type, comp_name)
print(len(content))

sample_b = sign_int3(content)

sample1 = np.fromstring(content, dtype=np.int8)
print(sample1[0], sample_b[0], content[0])
print(sample1[1], sample_b[1], content[1])
print(sample1[2], sample_b[2], content[2])
print(sample1[3], sample_b[3])
print(sample1[4], sample_b[4])
print(sample1[5], sample_b[5])
print(sample1[6], sample_b[6])
print(sample1[7], sample_b[7])
print(sample1[8], sample_b[8])
print(sample1[9], sample_b[9])
print(sample1[10], sample_b[10])

duration = nframes / framerate 
w, h = 800, 300
DPI = 72
roof = 256 ** sampwidth // 2
k = nframes/w/32

sample = []

for i in range(len(sample_b) // 3):
    sample.append(sample_b[3 * i + 2] * (256**2) + sample_b[3 * i + 1] * 256 + sample_b[3 * i])

channel = sample[0::nchannels]
print(channel[0], channel[1], channel[2], channel[3], channel[4], channel[110000], channel[110001], channel[110002])
print(roof)

d_channel = distortion(channel, roof, 100)

plt.figure(1, figsize=(float(w)/DPI, float(h)/DPI), dpi=DPI)

axes = plt.subplot(2, 1, 1, facecolor="k")
axes.plot(channel, "g")
axes.yaxis.set_major_formatter(ticker.FuncFormatter(format_db))
plt.grid(True, color="w")
axes.xaxis.set_major_formatter(ticker.NullFormatter())

axes = plt.subplot(2, 1, 2, facecolor="k")
axes.plot(d_channel, "g")
axes.yaxis.set_major_formatter(ticker.FuncFormatter(format_db))
plt.grid(True, color="w")
axes.xaxis.set_major_formatter(ticker.NullFormatter())

axes.xaxis.set_major_formatter(ticker.FuncFormatter(format_time))
plt.show()

"""
Чтобы дисторшн-файл создался, надо закрыть график
Если закрыть консоль до закрытия графика, файл не создастся
"""

wavio.write("gain100.wav", np.array(d_channel), rate=framerate, sampwidth=3)

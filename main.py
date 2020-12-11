import wave #встроенная
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math #встроенная

import wavio # импортируется pip install
import soundfile as sf # импортируется pip install

from int3 import sign_int3
from distortion import distortion
from fourier import fourier_transform
from int_channel import WavFile
from equalizer import equalize
"""
Предупреждение! Последняя строчка файла - создание файла с перегруженной гитарой
"""

w, h = 800, 300
DPI = 72

WavFile_1 = WavFile("D:\Stossgebet_acoustic.wav")
d_channel = distortion(WavFile_1.channel(), WavFile_1.roof // 2, 5)

WavFile_2 = WavFile("D:\Stossgebet.wav")

"""
plt.figure(1, figsize=(float(w)/DPI, float(h)/DPI), dpi=DPI)

axes = plt.subplot(3, 1, 1, facecolor="k")
axes.plot(WavFile_1.channel(), "g")
axes.yaxis.set_major_formatter(ticker.FuncFormatter(WavFile_1.format_db))
plt.grid(True, color="w")
axes.xaxis.set_major_formatter(ticker.FuncFormatter(WavFile_1.format_time))

axes = plt.subplot(3, 1, 2, facecolor="k")
axes.plot(d_channel, "g")
axes.yaxis.set_major_formatter(ticker.FuncFormatter(WavFile_1.format_db))
plt.grid(True, color="w")
axes.xaxis.set_major_formatter(ticker.NullFormatter())

axes = plt.subplot(3, 1, 3, facecolor="k")
axes.plot(WavFile_2.channel(), "g")
axes.yaxis.set_major_formatter(ticker.FuncFormatter(WavFile_2.format_db))
plt.grid(True, color="w")
axes.xaxis.set_major_formatter(ticker.FuncFormatter(WavFile_2.format_time))
"""

"""
Чтобы дисторшн-файл создался, надо закрыть график
Если закрыть консоль до закрытия графика, файл не создастся
"""
point = 48000 * 8
point2 = int(48000 * (8 - 1.68))


chan = WavFile_1.channel()[point:point+2000] #отрезок, который хотим разложить в Фурье
chan2 = WavFile_2.channel()[point2:point2+2000]
fourier_transform([chan, WavFile_1.duration*len(chan)/len(d_channel)],
                  [chan2, WavFile_2.duration*len(chan2)/len(WavFile_2.channel())])

eq_channel = equalize(WavFile_1.channel(), WavFile_1.duration, 'high_shelf', f0=70)
d_channel = distortion(eq_channel, WavFile_1.roof // 8, 3)

# wavio.write("Stossgebet_distortion.wav", np.array(d_channel), rate=WavFile_1.framerate, sampwidth=3)

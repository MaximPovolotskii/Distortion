import wave #встроенная
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math #встроенная
import scipy

import wavio # импортируется pip install
import soundfile as sf # импортируется pip install

from int3 import sign_int3
from distortion import distortion
from fourier import fourier_transform, smooth
from int_channel import WavFile
from equalizer import equalize
from filters import Filter
"""
Предупреждение! Последняя строчка файла - создание файла с перегруженной гитарой
"""

w, h = 800, 300
DPI = 72

WavFile_1 = WavFile("D:\Stossgebet_acoustic.wav")

WavFile_2 = WavFile("D:\D5 chord distortion.wav")

"""
plt.figure(1, figsize=(float(w)/DPI, float(h)/DPI), dpi=DPI)


axes = plt.subplot(3, 1, 1, facecolor="k")
axes.plot(WavFile_1.channel(), "g")
axes.yaxis.set_major_formatter(ticker.FuncFormatter(WavFile_1.format_db))
plt.grid(True, color="w")
axes.xaxis.set_major_formatter(ticker.FuncFormatter(WavFile_1.format_time))
"""

"""
axes = plt.subplot(3, 1, 2, facecolor="k")
axes.plot(d_channel, "g")
axes.yaxis.set_major_formatter(ticker.FuncFormatter(WavFile_1.format_db))
plt.grid(True, color="w")
axes.xaxis.set_major_formatter(ticker.NullFormatter())
"""

"""
axes = plt.subplot(3, 1, 3, facecolor="k")
axes.plot(WavFile_2.channel(), "g")
axes.yaxis.set_major_formatter(ticker.FuncFormatter(WavFile_2.format_db))
plt.grid(True, color="w")
axes.xaxis.set_major_formatter(ticker.FuncFormatter(WavFile_2.format_time))
plt.show()
"""

"""
Чтобы дисторшн-файл создался, надо закрыть график
Если закрыть консоль до закрытия графика, файл не создастся
"""


point = 48000 * 3
point2 = 48000 * 2

filter1 = Filter('low_pass', 8000, 3.5, 1)
filter2 = Filter('high_pass', 200, 5.5, 1)
filter3 = Filter('peak', 2080, 0.03, 0.1)
filter4 = Filter('peak', 4160, 0.2, 0.05)
filter5 = Filter('peak', 600, -0.15, 0.07)
filter6 = Filter('peak', 3100, -0.01, 0.02)
filter7 = Filter('peak', 1600, -0.008, 0.006)
filter8 = Filter('low_pass', 5000, 3.5, 1)
filter9 = Filter('peak', 450, 0.01, 0.02)



chan = WavFile_1.channel() #отрезок, который хотим разложить в Фурье
chan2 = WavFile_2.channel()[point2:point2+2000]
chan_dur = WavFile_1.duration * len(chan) / len(WavFile_1.channel())
chan2_dur = WavFile_2.duration * len(chan2) / len(WavFile_2.channel())

eq_channel = equalize(chan, chan_dur, filter2)
d_channel_pre = distortion(eq_channel, WavFile_1.roof // 4, 50)
d_channel = equalize(d_channel_pre, chan_dur, filter2, filter4, filter3, filter5, filter7, filter1, filter8, filter9)

# yf_mas = fourier_transform([chan2, chan2_dur], [d_channel, chan_dur])
"""
N = len(d_channel)
dT = 1 / 48000
yf = scipy.fft.rfft(d_channel)
tf = np.linspace(0.0, dT*N, N)
xf = np.linspace(0.0, 1.0/(2.0*dT), N//2)

fig, ax = plt.subplots()
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

ax.plot(tf, d_channel)
ax.set_title('d_channel')
# рисуем разложение по спектру
ax1.plot(xf[0:N//4], 2.0/N * np.abs(yf[0:N//4])) 
ax1.set_title('spectrum')
ax2.plot(xf[0:N//4], 2.0/N * np.abs(smooth(yf)[0:N//4])) 
ax2.set_title('smooth spectrum')

plt.show()
"""
wavio.write("Stossgebet_once_more.wav", np.array(d_channel), rate=WavFile_1.framerate, sampwidth=3)

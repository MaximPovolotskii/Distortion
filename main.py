import wave #встроенная
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math #встроенная
import scipy

import wavio # импортируется pip install

from int3 import sign_int3
from distortion import distortion
from fourier import fourier_transform, fourier_transform_graph
from int_channel import WavFile
from equalizer import equalize
from filters import Filter

"""
Предупреждение! Последняя строчка файла - создание файла с перегруженной гитарой
"""

w, h = 800, 300
DPI = 72

WavFile_1 = WavFile("D:\D5 acoustic.wav")

WavFile_2 = WavFile("D:\D5 chord distortion.wav")


point = int(48000 * 3)
point2 = int(48000 * 2)


chan = WavFile_1.channel() 
chan2 = WavFile_2.channel()[point2:point2+2000]
chan_dur = WavFile_1.duration * len(chan) / len(WavFile_1.channel())
chan2_dur = WavFile_2.duration * len(chan2) / len(WavFile_2.channel())

d_channel = distortion(chan, chan_dur, WavFile_1.roof // 4, 50)

chan3 = d_channel[point:point+2000]
chan3_dur = WavFile_1.duration * len(chan3) / len(WavFile_1.channel())

yf_mas = fourier_transform_graph(True, [chan2, chan2_dur], [chan3, chan3_dur])

# wavio.write("D5 D5.wav", np.array(d_channel), rate=WavFile_1.framerate, sampwidth=3)

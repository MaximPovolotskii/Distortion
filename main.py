import wave #встроенная
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math #встроенная
import scipy
import os.path

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



print("Инструкция.")
print("1) Введите имя wav-файла, с которым будете работать.")
print("2) Введите параметры фильтров в виде type (peak, high_shelf или т.п.) f0 a0 b0.")
print("Чтобы прекратить ввод фильтров, введите stop (слово).")
print("3) Введите после distortion параметр gain (gain - число), чтобы использовать дисторшн с этим гейном.")
print("Введите gain = 0, если не хотите перегруз.")
"""
print("4) Введите 1 после wave draw, если хотите нарисовать дорожку изначального аудиофайла.")
print("Введите 0, если не хотите.")
"""
print("5) Введите 1 и название (без .wav), если хотите сохранить канал. Если не хотите, введите первым 0.\n")

flag = True

while flag:
    caption = input("Введите название файла: ")
    if not os.path.exists(caption) or not os.path.isfile(caption):
        print("Неправильное имя файла")
        caption = input("Введите название файла: ")
    else:
        strl = len(caption)
        if caption[strl - 4 : strl] != '.wav':
            print("Неправильное расширение файла")
            caption = input("Введите название файла: ")
        else:
            WavFile_1 = WavFile(caption)
            flag = False


# ввод фильтров
a = True
n = 1
filter_array = []
while a:
    str = input("filter" + str(n) + ": ")
    if str == "stop":
        a = False
    else:
        if a in ('peak', 'high_pass', 'low_pass', 'high_shelf', 'low_shelf'):
            param = str.split()
            for i in range(1, 4):
                param[i] =  float(param[i])
            filter_array.append(Filter(param[0], param[1], param[2], param[3]))
            n += 1
        else:
            print("Это не является типом фильтра или словом stop")
        

# эквализация
channel = WavFile_1.channel()
dur = WavFile_1.duration

if n > 1:
    for filter_cell in filter_array:
        channel = equalize(channel, dur, filter_cell)

# дисторшн
gain = float(input("distortion: "))
if gain != 0:
    channel = distortion(channel, dur, WavFile_1.roof // 4, gain)

# сохранение
str = input("save: ").split()
print(str)
if str[0] == "1":
    wavio.write(str[1] + ".wav", np.array(channel), rate=WavFile_1.framerate, sampwidth=WavFile_1.sampwidth)

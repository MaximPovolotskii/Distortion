import wave #встроенная
import numpy as np
import math #встроенная
from int3 import sign_int3


class WavFile():
    """
    класс WAVE-file
    содержит всю информацию о дорожке
    может предоставить содержимое канала в виде массива интов
    """
    def __init__(self, name):
        wav = wave.open(name, mode="r")
        (nchannels, sampwidth, framerate,
         nframes, comp_type, comp_name) = wav.getparams()
        
        self.wav = wav
        self.nchannels = nchannels # число каналов
        self.sampwidth = sampwidth # размер сэмпла в байтах
        self.framerate = framerate # частота дикретизации (фреймов в секунду)
        self.nframes = nframes     # общее число фреймов
        self.comp_type = comp_type # тип компрессии
        self.comp_name = comp_name # название компрессора
        
        self.content = wav.readframes(nframes) # содержимое файла
        
        self.duration = nframes / framerate # длительность
        self.roof = 256 ** sampwidth // 2 # максимальная амплитуда
        
        wav.close()
        
    def channel(self):
        """
        возвращает один из каналов contents в виде удобного массива знаковых интов
        """
        sample_b = sign_int3(self.content)
        
        sample = []
        for i in range(len(sample_b) // 3):
            sample.append(sample_b[3 * i + 2] * (256**2) + sample_b[3 * i + 1] * 256 + sample_b[3 * i])

        channel = sample[0::self.nchannels]
        return channel

    def format_time(self, x, pos=None):
        """
        функция для отрисовки оси времени в draw_wave
        """
        progress = int(x / float(self.nframes) * self.duration)
        mins, secs = divmod(progress, 60)
        hours, mins = divmod(mins, 60)
        out = "%d:%02d" % (mins, secs)
        if hours > 0:
            out = "%d:" % hours
        return out

    def format_db(self, x, pos=None):
        """
        функция для отрисовки оси амплитуды в дБ в draw_wave
        """
        if pos == 0:
            return ""
        if x == 0:
            return "-inf"
        db = 20 * math.log10(abs(x) / float(self.roof))
        return int(db)

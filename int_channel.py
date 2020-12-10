import wave #встроенная
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math #встроенная
'''
import wavio #импортируется pip install
import soundfile as sf #импортируется pip install
'''
from int3 import sign_int3
from distortion import distortion
from fourier import fourier_transform

class WavFile():
    """
    WAVE-file class
    has all data about the file and its contents
    can present contents as an array of integers
    """
    def __init__(self, name):
        wav = wave.open(name, mode="r")
        (nchannels, sampwidth, framerate,
         nframes, comp_type, comp_name) = wav.getparams()
        
        self.wav = wav
        self.nchannels = nchannels
        self.sampwidth = sampwidth
        self.framerate = framerate
        self.nframes = nframes
        self.comp_type = comp_type
        self.comp_name = comp_name
        
        self.content = wav.readframes(nframes)
        
        self.duration = nframes / framerate
        self.roof = 256 ** sampwidth // 2
        
        wav.close()
        
    def channel(self):
        """
        returns an integer array of contsnts data
        """
        sample_b = sign_int3(self.content)
        
        sample = []
        for i in range(len(sample_b) // 3):
            sample.append(sample_b[3 * i + 2] * (256**2) + sample_b[3 * i + 1] * 256 + sample_b[3 * i])

        channel = sample[0::self.nchannels]
        return channel

    def format_time(self, x, pos=None):
        progress = int(x / float(self.nframes) * self.duration)
        mins, secs = divmod(progress, 60)
        hours, mins = divmod(mins, 60)
        out = "%d:%02d" % (mins, secs)
        if hours > 0:
            out = "%d:" % hours
        return out

    def format_db(self, x, pos=None):
        if pos == 0:
            return ""
        if x == 0:
            return "-inf"
        db = 20 * math.log10(abs(x) / float(self.roof))
        return int(db)

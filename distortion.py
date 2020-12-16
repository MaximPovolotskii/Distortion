import numpy as np
import copy
from fourier import fourier_transform
import scipy
import matplotlib.pyplot as plt
from filters import Filter
from equalizer import piece_equalize, equalize

"""
Ich tu dir weh
Tut mir nicht leid
Das tut mir gut
Hört wie es schreit
Если бы эта функция пела песню, она бы пела бы это в мой адрес
"""

def distortion (channel, duration, roof, set_gain=1):
    """
    функция, делающая дисторшн
    """
    gain = set_gain
    d_channel_fresh = copy.copy(channel)
    
    filter1 = Filter('low_pass', 8000, 3.5, 1)
    filter2 = Filter('high_pass', 40, 5.5, 1)
    filter3 = Filter('peak', 2080, 0.03, 0.1)
    filter4 = Filter('peak', 4160, 0.5, 0.5)
    
    filter5 = Filter('peak', 470, -0.13, 0.07)
    filter6 = Filter('peak', 3100, -0.01, 0.02)
    filter7 = Filter('peak', 1600, -0.008, 0.006)
    filter8 = Filter('low_pass', 5000, 3.5, 1)
    filter9 = Filter('peak', 250, -0.05, 0.001)
    
    filter10 = Filter('peak', 5000, 0.25, 0.2)
    filter11 = Filter('low_pass', 7000, 4, 2)
    filter12 = Filter('peak', 150, -0.003, 0.002)
    filter13 = Filter('peak', 1300, -0.05, 0.07)
    
    filter14 = Filter('peak', 200, -0.003, 0.002)
    filter15 = Filter('peak', 2300, 0.001, 0.002)
    filter16 = Filter('peak', 650, -0.08, 0.07)
    
    d_channel = equalize(d_channel_fresh, duration, filter2, filter9) #предэквализация
        
    for i in range(len(d_channel)):
        d_channel[i] = int(roof * np.tanh(gain * d_channel[i] / roof)) #перегруз

    #постэквализация
    d_channel_post = equalize(d_channel, duration, filter5, filter10, filter11, filter12, filter13, filter14, filter15, filter16, filter2)
    
    return d_channel_post

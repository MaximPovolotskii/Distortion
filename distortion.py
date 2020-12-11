import numpy as np
import copy
from fourier import fourier_transform
import scipy
import matplotlib.pyplot as plt

def clipping(value, roof):
    x = value / roof
    cl_value = np.tanh(x) * roof
    return cl_value

def distortion (channel, roof, set_gain=1):
    gain = set_gain
    d_channel = copy.copy(channel)
    for i in range(len(d_channel)):
        d_channel[i] = gain * d_channel[i]
        d_channel[i] = int(clipping(abs(d_channel[i]), roof)) * np.sign(d_channel[i])
    return d_channel

"""
T = 0.01
N = int(48000 * T)
frec = 200

t = np.linspace(0.0, T, N)
w1 = 2*np.pi * frec * 2
w2 = 2*np.pi * frec * 5
w3 = 2*np.pi * frec * 13
channel = (256**2 - 1) * (0.6 * np.sin(w1 * t) + 0.3 * np.sin(w2 * t) + 0.1 * np.sin(w3 * t))
d_channel = distortion(channel, 256**2 - 1, 5)
fourier_transform([channel, T], [d_channel, T])
"""

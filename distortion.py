import numpy as np
import copy
from fourier import fourier_transform
import scipy
import matplotlib.pyplot as plt
from filters import Filter
from equalizer import piece_equalize, equalize


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

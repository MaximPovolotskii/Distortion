import numpy as np
import copy

def distortion (channel, roof, set_gain=1):
    gain = set_gain
    d_channel = copy.copy(channel)
    for i in range(len(d_channel)):
        d_channel[i] = d_channel[i] * gain
        if abs(d_channel[i]) >= roof:
            d_channel[i] = np.sign(d_channel[i]) * (roof - 1)
    return d_channel

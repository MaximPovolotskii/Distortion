import numpy as np
import copy
from fourier import fourier_transform
import scipy
import matplotlib.pyplot as plt

def distortion (channel, roof, set_gain=1):
    gain = set_gain
    d_channel = copy.copy(channel)
    for i in range(len(d_channel)):
        d_channel[i] = d_channel[i] * gain
        if i > 0:
            if abs(d_channel[i]) >= 0.9 * roof:
                if abs(d_channel[i - 1]) < 0.9 * roof:
                    d_channel[i] = np.sign(d_channel[i]) * int(0.95 * (roof - 1))
                else:
                    d_channel[i] = np.sign(d_channel[i]) * (roof - 1)
    return d_channel

def high_filter (channel, duration):
    f_channel = copy.copy(channel)
    # Number of samplepoints
    N = len(f_channel)
    # sample spacing
    dT = duration / N
    yf = scipy.fft.fft(f_channel)
    tf = np.linspace(0.0, dT*N, N)
    xf = np.linspace(0.0, 1.0/(2.0*dT), N//2) #массив частот
    x = xf / 250
    filt = (1.2 + 0.8 * scipy.special.erf(- x + 4800.0/(2.0)/500)) * 0.5 - np.exp(- 1.5 * x - 0.2)
    yf_filt = yf[0:N//2] * filt
    
    fig1, ax1 = plt.subplots()
    ax1.plot(xf[0:N//16], filt[0:N//16])
    plt.grid("True")
    """
    fig2, ax2 = plt.subplots()
    ax2.plot(xf, yf[0:N//2])
    plt.grid("True")
    """
    return np.array(yf_filt.tolist() * 2)


"""
T = 0.02
N = int(48000 * T)
frec = 100

t = np.linspace(0.0, T, N)
w1 = 2*np.pi * frec * 2
w2 = 2*np.pi * frec * 5
w3 = 2*np.pi * frec * 13
channel = 255 * np.sin(w1 * t) + 255 * np.sin(w2 * t) + 255 * np.sin(w3 * t)
d_channel = distortion(channel, 256, 5)
#fourier_transform([channel, T], [d_channel, T])
filt_ch_sp = high_filter(channel, T)
filt_ch = scipy.fft.ifft(filt_ch_sp)
fourier_transform([channel, T], [filt_ch, T])
"""


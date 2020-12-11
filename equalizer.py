import copy
import numpy as np
import matplotlib.pyplot as plt
from fourier import fourier_transform, reverse_transform
from filters import spectr_filter

def equalize(channel, duration, filter_type='peak', f0=440):
    spectrum = fourier_transform([channel, duration])[0]
    N = len(channel)
    a = spectr_filter(1 / duration * ((N+2)//2), (N+2)//2, filter_type, f0)
    spectrum = spectrum * a
    dT = duration / N
    xf = np.linspace(0.0, 1.0/(2.0*dT), (N+2)//2)
    fig, ax = plt.subplots()
    ax.plot(xf[0:N//8], 2.0/N * np.abs(spectrum)[0:N//8]) 
    ax.set_title('new spectrum')        
    new_channel = reverse_transform(spectrum, duration)
    return new_channel

"""
T = 0.1
N = int(48000 * T)
frec = 300

t = np.linspace(0.0, T, N)
w1 = 2*np.pi * frec * 2
w2 = 2*np.pi * frec * 3
w3 = 2*np.pi * frec * 4
w4 = 2*np.pi * frec * 7
w5 = 2*np.pi * frec * 5
channel = (255//2 * np.sin(w1 * t) + 255//3 * np.sin(w2 * t) + 255//6 * np.sin(w3 * t) +
           +255//9 * np.sin(w4 * t) + 255//3 * np.sin(w5 * t))
new_channel = equalize(channel, T, f0=2100)
"""



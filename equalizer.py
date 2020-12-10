import copy
import numpy as np
import matplotlib.pyplot as plt
from fourier import fourier_transform, reverse_transform
from filters import spectr_filter

def equalize(channel, duration):
    new_channel = copy.copy(channel)
    spectrum = fourier_transform([new_channel, duration])[0]
    N = len(channel)
    a = spectr_filter(1 / duration * ((N+2)//2), (N+2)//2, 'high_shelf', 300)
    spectrum = spectrum * a
    dT = duration / N
    xf = np.linspace(0.0, 1.0/(2.0*dT), (N+2)//2)
    fig, ax = plt.subplots()
    ax.plot(xf, 2.0/N * np.abs(spectrum)) 
    ax.set_title('new spectrum')        
    new_channel = reverse_transform(spectrum, duration)
    

T = 10
N = 10**4*3
frec = 100

t = np.linspace(0.0, T, N)
w1 = 2*np.pi * frec * 2
w2 = 2*np.pi * frec * 3
w3 = 2*np.pi * frec * 4
w4 = 2*np.pi * frec * 7
w5 = 2*np.pi * frec * 5
channel = (255//2 * np.sin(w1 * t) + 255//3 * np.sin(w2 * t) + 255//6 * np.sin(w3 * t) +
           +255//9 * np.sin(w4 * t) + 255//3 * np.sin(w5 * t))
equalize(channel, T)
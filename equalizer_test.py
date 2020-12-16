import copy
import numpy as np
import matplotlib.pyplot as plt
from fourier import fourier_transform, reverse_transform, fourier_transform_graph
from filters import Filter
from equalizer import equalize, piece_equalize


# тестирующая программа
T = 0.05
N = int(48000 * T)
frec = 100

filter1 = Filter('peak', 800, -0.5, 0.1)

t = np.linspace(0.0, T, N)

w1 = 2*np.pi * frec * 1
w2 = 2*np.pi * frec * 2
w3 = 2*np.pi * frec * 5
w4 = 2*np.pi * frec * 10
w5 = 2*np.pi * frec * 15
w6 = 2*np.pi * frec * 20

channel = (255**3 * np.sin(w1 * t) + 255**3 * np.sin(w2 * t) + 255**3 * np.sin(w3 * t) +
           + 255**3 * np.sin(w4 * t) + 255**3 * np.sin(w5 * t) + 255**3 * np.sin(w6 * t))
new_channel = equalize(channel, T, filter1)
fourier_transform_graph(True, [new_channel, T])

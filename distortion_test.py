import numpy as np
import copy
from fourier import fourier_transform, fourier_transform_graph
import scipy
import matplotlib.pyplot as plt
from filters import Filter
from equalizer import piece_equalize, equalize
from distortion import distortion


# тестирующая программа
T = 0.01
N = int(48000 * T)
frec = 200

t = np.linspace(0.0, T, N)
w1 = 2*np.pi * frec * 2
w2 = 2*np.pi * frec * 5
w3 = 2*np.pi * frec * 13

channel = (256**3 - 1) * np.sin(w1 * t)
d_channel_10 = distortion(channel, T, 256**3 // 4, 2)

fourier_transform_graph(True, [channel, T])
# fourier_transform([d_channel_5, T])
fourier_transform_graph(True, [d_channel_10, T])

plt.show()

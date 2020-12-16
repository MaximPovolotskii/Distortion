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

filter1 = Filter('peak', 4000, 0.03, 0.001)
filter2 = Filter('peak', 2500, 0.15, 0.1)
filter3 = Filter('peak', 1000, -0.01, 0.001)

t = np.linspace(0.0, T, N)
w1 = 2*np.pi * frec * 2
w2 = 2*np.pi * frec * 5
w3 = 2*np.pi * frec * 13

channel = (256**2 - 1) * np.sin(w1 * t)
# d_channel_5 = piece_equalize(distortion(channel, 256**2 , 5), T, filter1)
d_channel_10 = distortion(channel, 256**2, 10)

fourier_transform_graph(True, [channel, T])
# fourier_transform([d_channel_5, T])
fourier_transform_graph(True, [d_channel_10, T])

plt.show()

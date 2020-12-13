import copy
import numpy as np
import matplotlib.pyplot as plt
from fourier import fourier_transform, reverse_transform
from filters import Filter


def equalize(channel, duration, *filter_cell):
    """
    функция эквалайзера: получая на вход канал channel и его длительность duration
    в секундах, возвращает отфильтрованный через все фильтры в массиве filter_cell
    новый канал new_channel
    """
    spectrum = fourier_transform([channel, duration])[0]
    N = len(channel)
    
    for cell in filter_cell:
        spectrum = spectrum * cell.get_table(1 / duration * ((N+2)//2), (N+2)//2)
        
    dT = duration / N
    xf = np.linspace(0.0, 1.0/(2.0*dT), (N+2)//2)
    
    # здесь начинается рисование нового спектра
    fig, ax = plt.subplots()
    ax.plot(xf[0:N//8], 2.0/N * np.abs(spectrum)[0:N//8]) 
    ax.set_title('new spectrum')
    # закончилось
    
    new_channel = reverse_transform(spectrum, duration)
    return new_channel


"""
# тестирующая программа
T = 0.1
N = int(48000 * T)
frec = 300

filter1 = Filter('peak', frec*3, 0.1, 0.1)

t = np.linspace(0.0, T, N)
w1 = 2*np.pi * frec * 2
w2 = 2*np.pi * frec * 3
w3 = 2*np.pi * frec * 4
w4 = 2*np.pi * frec * 7
w5 = 2*np.pi * frec * 5
channel = (255//2 * np.sin(w1 * t) + 255//3 * np.sin(w2 * t) + 255//6 * np.sin(w3 * t) +
           +255//9 * np.sin(w4 * t) + 255//3 * np.sin(w5 * t))
new_channel = equalize(channel, T, filter1)
"""





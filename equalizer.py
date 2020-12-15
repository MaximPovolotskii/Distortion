import copy
import numpy as np
import matplotlib.pyplot as plt
from fourier import fourier_transform, reverse_transform
from filters import Filter


def piece_equalize(channel, duration, *filter_cell):
    """
    функция эквалайзера: получая на вход канал channel и его длительность duration
    в секундах, возвращает отфильтрованный через все фильтры в массиве filter_cell
    новый канал new_channel
    """
    spectrum = fourier_transform([channel, duration])[1]
    N = len(channel)
    
    for cell in filter_cell:
        spectrum = spectrum * cell.get_table(1 / duration * ((N+2)//2), (N+2)//2)
        
    dT = duration / N
    xf = np.linspace(0.0, 1.0/(2.0*dT), (N+2)//2)
    """
    # здесь начинается рисование нового спектра
    fig, ax = plt.subplots()
    ax.plot(xf[0:N//32], 2.0/N * np.abs(spectrum)[0:N//32]) 
    ax.set_title('new spectrum')
    # закончилось
    """
    new_channel = reverse_transform(spectrum, duration)
    new_channel_ps = new_channel.tolist()
    
    for i in range(len(new_channel_ps)):
        new_channel_ps[i] = int(new_channel_ps[i])
        
    return new_channel_ps


def equalize(channel, duration, *filter_cell):
    """
    общая функция эквалайзера, которая сначала разбивает канал на части по 960 сэмплов (0.02 с),
    выполняет на каждом из них эквализацию, а потом опять склеивает
    """
    new_channel = []
    number = len(channel) // 960
    
    for i in range(number):
        new_channel = new_channel + piece_equalize(channel[960*i : 960*(i + 1)], duration * 960 / len(channel),
                                                   *filter_cell)
        
    new_channel = new_channel + piece_equalize(channel[960*number : len(channel)],
                                               duration * (len(channel) - 960 * number) / len(channel),
                                               *filter_cell)

    return new_channel


"""
лонгрид о предпочтительных настройках эквалайзера:
1) для заглушения "плохих" нижних частот при distortion надо использовать
    Filter('high_pass', 150, 3, 1)
2)
"""







import numpy as np
import matplotlib.pyplot as plt
import scipy.special
import copy


def fourier_transform(*tracks_with_durations): #[track, duration]
    fig, ax = plt.subplots()
    fig1, ax1 = plt.subplots()
    #fig2, ax2 = plt.subplots()
    for channel in tracks_with_durations:
        d_channel = copy.copy(channel[0])
        # Number of samplepoints
        N = len(d_channel)
        # sample spacing
        dT = channel[1] / N
        yf = scipy.fft.rfft(d_channel)
        tf = np.linspace(0.0, dT*N, N)
        xf = np.linspace(0.0, 1.0/(2.0*dT), N//2)
        # рисуем график самого отрезка
        ax.plot(tf, d_channel)
        ax.set_title('d_channel')
        # рисуем разложение по спектру
        ax1.plot(xf[0:N//16], 2.0/N * np.abs(yf[0:N//16])) 
        ax1.set_title('spectrum')                          
        #zf = scipy.fft.ifft(yf) # в идеале эта функция обратно преобразовывает
        #ax2.plot(tf, zf) # рисуем график обратного преобразования
        
    plt.show()
    return [yf, channel[1]]

def reverse_transform(yf, duration):
    channel_zf =  scipy.fft.irfft(yf)
    N = len(channel_zf)
    dT = duration / N
    tf = np.linspace(0.0, dT*N, N)
    fig2, ax2 = plt.subplots()
    ax2.plot(tf, channel_zf)
    ax2.set_title('reverse_transform')
    plt.show()
    
    return channel_zf

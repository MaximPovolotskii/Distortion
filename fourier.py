import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
import copy

def fourier_transform(channel, duration):
    d_channel = copy.copy(channel)
    # Number of samplepoints
    N = len(d_channel)
    # sample spacing
    T = duration
    yf = scipy.fftpack.fft(d_channel)
    tf = np.linspace(0.0, T, N)
    xf = np.linspace(0.0, 1.0/(2.0*T), N//16) #тут можно N//2, так высокие частоты обрезаются
    
    #рисуем график самого отрезка
    fig, ax = plt.subplots()
    ax.plot(tf, channel)
    
    #рисуем разложение по спектру
    fig1, ax1 = plt.subplots()
    ax1.plot(xf, 2.0/N * np.abs(yf[:N//16]))
    
    zf = scipy.fftpack.ifft(yf)
    #ax1.plot(xf, zf)
    plt.show()
    
    
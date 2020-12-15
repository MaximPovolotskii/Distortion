import numpy as np
import matplotlib.pyplot as plt
import scipy.special
import copy

def smooth(yf):
    yf_sm = copy.copy(yf)
    abs_yf = np.abs(yf)
    max_value = abs_yf.max()
    for i in range(len(yf)):
        if np.abs(yf[i]) < 0.05 * max_value:
           yf_sm[i] = 0
    return yf_sm

def fourier_transform(*tracks_with_durations): #[track, duration]
    # fig, ax = plt.subplots()
    # fig1, ax1 = plt.subplots()
    # fig2, ax2 = plt.subplots()
    yf_mas = [] # массив из пар обычного и сглаженного Фурье для каждого из треков
    for channel in tracks_with_durations:
        d_channel = copy.copy(channel[0])
        # Number of samplepoints
        N = len(d_channel)
        # sample spacing
        dT = channel[1] / N
        yf = scipy.fft.rfft(d_channel)
        tf = np.linspace(0.0, dT*N, N)
        xf = np.linspace(0.0, 1.0/(2.0*dT), N//2)
        yf_mas.append([yf, smooth(yf)]) # добавляем пару в общий массив
        """
        # рисуем график самого отрезка
        ax.plot(tf, d_channel)
        ax.set_title('d_channel')
        # рисуем разложение по спектру
        ax1.plot(xf[0:N//4], 2.0/N * np.abs(yf[0:N//4])) 
        ax1.set_title('spectrum')

        ax2.plot(xf[0:N//4], 2.0/N * np.abs(smooth(yf)[0:N//4])) 
        ax2.set_title('smooth spectrum')
        #zf = scipy.fft.ifft(yf) # в идеале эта функция обратно преобразовывает
        #ax2.plot(tf, zf) # рисуем график обратного преобразования
        """
        
    # plt.show()
    return yf_mas

def reverse_transform(yf, duration):
    channel_zf =  scipy.fft.irfft(yf)
    N = len(channel_zf)
    dT = duration / N
    tf = np.linspace(0.0, dT*N, N)
    """
    fig2, ax2 = plt.subplots()
    ax2.plot(tf, channel_zf)
    ax2.set_title('reverse_transform')
    plt.show()
    """
    
    return channel_zf

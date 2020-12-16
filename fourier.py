import numpy as np
import matplotlib.pyplot as plt
import scipy.special
import copy


def smooth(yf, N):
    """
    функция очистки спектра от бесполезных частот с малыми амплитудами
    """
    yf_sm = []
    abs_yf = np.abs(yf)
    max_value = abs_yf.max()
    
    for i in range(len(yf)):
        if 2.0 / N * abs_yf[i] < 4000:
           yf_sm.append(0)
        else:
           yf_sm.append(yf[i])
    return yf_sm


def fourier_transform(*tracks_with_durations): # массив из [track, duration]
    """
    функция разложения в спектр по Фурье
    возвращает массив из пар спектров - обычного и очищенного
    """
    yf_mas = [] # массив из пар обычного и сглаженного Фурье для каждого из треков
    
    for channel in tracks_with_durations:
        d_channel = copy.copy(channel[0])
        N = len(d_channel) # количество сэмплов
        dT = channel[1] / N # временной промежуток между соседними сэмплами
        yf = scipy.fft.rfft(d_channel) 
        tf = np.linspace(0.0, dT*N, N)
        xf = np.linspace(0.0, 1.0/(2.0*dT), N//2)
        yf_mas.append([yf, smooth(yf, N)]) # добавляем пару в общий массив
        
    return yf_mas


def fourier_transform_graph(plt_show_usage=False, *tracks_with_durations): #[track, duration]
    """
    то же, что и функция выше, но с рисованием графиков
    plt_show_usage (bool type) отвечает за то, вызвать ли plt.show() сразу из функции или нет
    """
    fig, ax = plt.subplots()
    fig1, ax1 = plt.subplots()
    fig2, ax2 = plt.subplots()
    
    yf_mas = [] # массив из пар обычного и сглаженного Фурье для каждого из треков
    
    for channel in tracks_with_durations:
        d_channel = copy.copy(channel[0])
        # количество сэмплов
        N = len(d_channel)
        # временной промежуток между соседними сэмплами
        dT = channel[1] / N
        
        yf = scipy.fft.rfft(d_channel)
        tf = np.linspace(0.0, dT*N, N)
        xf = np.linspace(0.0, 1.0/(2.0*dT), N//2)
        yf_mas.append([yf, smooth(yf, N)]) # добавляем пару в общий массив
        
        # рисуем график самого отрезка
        ax.plot(tf, d_channel)
        ax.set_title('d_channel')
        
        # рисуем разложение по спектру
        ax1.plot(xf[0:N//4], 2.0/N * np.abs(yf[0:N//4])) 
        ax1.set_title('spectrum')

        # рисуем очищенное разложение по спектру
        ax2.plot(xf[0:N//4], 2.0/N * np.abs(smooth(yf, N)[0:N//4])) 
        ax2.set_title('smooth spectrum')

    if plt_show_usage:
            plt.show()

    return yf_mas


def reverse_transform(yf, duration):
    """
    функция восстановления аудиодорожки по спектру
    """
    channel_zf =  scipy.fft.irfft(yf)
    N = len(channel_zf)
    dT = duration / N
    tf = np.linspace(0.0, dT*N, N)
    
    return channel_zf


def reverse_transform_graph(yf, duration, plt_show_usage=False):
    """
    то же, что и выше, но с рисование графиков
    plt_show_usage (bool type) отвечает за то, вызвать ли plt.show() сразу из функции или нет
    """
    channel_zf =  scipy.fft.irfft(yf)
    N = len(channel_zf)
    dT = duration / N
    tf = np.linspace(0.0, dT*N, N)
    
    fig2, ax2 = plt.subplots()
    ax2.plot(tf, channel_zf)
    ax2.set_title('reverse_transform')

    if plt_show_usage:
        plt.show()
    
    return channel_zf

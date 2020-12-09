import numpy as np
import matplotlib.pyplot as plt

def spectr_filter(fmax, N, filter_type='peak', f0=-1):
    if f0 == -1: # f0 - характерная частота пропускания
        f0= fmax//5
    numbers = np.arange(N)
    fn = fmax*(numbers - 1)/(N - 1)
    if filter_type == 'peak': 
        a0 = 0.1 # регулирует высоту всего
        b0 = 0.1 # регулирует толщину пика
        a = np.exp(a0*((np.log(fn) - np.log(f0))**2 + b0)**(-1))

    if filter_type == 'low_pass':
        a0 = 3 # a0 > 0, при увеличении a0 увеличивается резкость отрубания
        a = np.exp(-np.exp(a0*(np.log(fn)-np.log(f0))))
        
    if filter_type == 'high_pass':
        a0 = -3 # a0 < 0, при увеличении модуля a0 увеличивается резкость отрубания
        a = np.exp(-np.exp(a0*(np.log(fn)-np.log(f0))))
        
    if filter_type == 'high_shelf':
        h0 = 1 # >0, высота полки
        a0 = 3 # >0, регулирует резкость полки
        a = np.exp(h0*(np.tanh(a0*(np.log(fn)-np.log(f0)))) + 1)
        
    if filter_type == 'low_shelf':
        h0 = -1 #<0 высота полки
        a0 = 3 #>0 регулирует резкость полки
        a = np.exp(h0*(np.tanh(a0*(np.log(fn)-np.log(f0)))) + 1)
        
    # нарисуем графики для демонстрации
    fig, ax = plt.subplots()
    ax.plot(np.log(fn), np.log(a))
    ax.set_title(filter_type)
    ax.set_xlabel('ln(f)')
    ax.set_ylabel('ln(a)')
        
    fig1, ax1 = plt.subplots()
    ax1.plot(fn, a)
    ax1.set_title(filter_type)
    ax1.set_xlabel('f')
    ax1.set_ylabel('a')
        
    return a


fmax = 100
N = 1000
a = spectr_filter(fmax, N, 'low_shelf')


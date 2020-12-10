import numpy as np
import matplotlib.pyplot as plt

def spectr_filter(fmax, N, filter_type='peak', f0=-1, peak_a0=0.1, peak_b0=0.1, 
                  pass_a0=3, pass_h0=1, shelf_h0=1, shelf_a0=3):
    if f0 == -1: # f0 - характерная частота пропускания
        f0 = fmax//5
    numbers = np.arange(N)
    fn = fmax*(numbers)/(N - 1)
    
    if filter_type == 'peak': 
        #peak_a0 = 0.1 # регулирует высоту всего
        #peak_b0 = 0.1 # регулирует толщину пика
        a = np.exp(peak_a0*((np.log(fn) - np.log(f0))**2 + peak_b0)**(-1))

    if filter_type == 'low_pass':
        #pass_a0 = 3 # a0 > 0, при увеличении a0 увеличивается резкость отрубания
        #pass h0 влияет на амплитуду
        a = np.exp(pass_a0*(-np.exp(pass_a0*(np.log(fn)-np.log(f0)))))
        
    if filter_type == 'high_pass':
        #pass_a0 = 3 # a0 < 0, при увеличении модуля a0 увеличивается резкость отрубания
        #pass h0 влияет на амплитуду
        a = np.exp(pass_a0*(-np.exp(-pass_a0*(np.log(fn)-np.log(f0)))))
        
    if filter_type == 'high_shelf':
        #shelf_h0 = 1 # > 0, высота полки
        #shelf_a0 = 3 # > 0, регулирует резкость полки
        a = np.exp(shelf_h0*(np.tanh(shelf_a0*(np.log(fn)-np.log(f0)))) + 1)
        
    if filter_type == 'low_shelf':
        #shelf_h0 = -1 # < 0 высота полки
        #shelf_a0 = 3 # > 0 регулирует резкость полки
        a = np.exp(-shelf_h0*(np.tanh(shelf_a0*(np.log(fn)-np.log(f0)))) + 1)
        
    # нарисуем графики для демонстрации
    '''
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
    '''
    return a

'''
fmax = 100
N = 1000
a = spectr_filter(fmax, N, 'low_shelf')
'''

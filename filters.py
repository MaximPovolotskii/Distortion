import numpy as np
import matplotlib.pyplot as plt

class Filter():
    """
    класс фильтра
    """
    def __init__(self, filter_type, f0, a0, b0):
        self.type = filter_type
        self.f0 = f0 # f0 - характерная частота фильтрации
        self.a0 = a0
        self.b0 = b0

    def get_table(self, fmax, N):
        """
        метод, возвращающий массив преобразования спектра для N частот от 0 до fmax
        """
        numbers = np.arange(N)
        fn = fmax * numbers / N
    
        if self.type == 'peak':
            peak_a0 = self.a0
            peak_b0 = self.b0
            #peak_a0 = 0.1 # регулирует высоту всего
            #peak_b0 = 0.1 # регулирует толщину пика
            a = np.exp(peak_a0*((np.log(fn) - np.log(self.f0))**2 + peak_b0)**(-1))

        if self.type == 'low_pass':
            pass_a0 = self.a0
            pass_h0 = self.b0
            #pass_a0 = 3 # a0 > 0, при увеличении a0 увеличивается резкость отрубания
            #pass h0 влияет на амплитуду
            a = np.exp(pass_a0*(-np.exp(pass_a0*(np.log(fn)-np.log(self.f0)))))
        
        if self.type == 'high_pass':
            pass_a0 = self.a0
            pass_h0 = self.b0
            #pass_a0 = 3 # a0 < 0, при увеличении модуля a0 увеличивается резкость отрубания
            #pass h0 влияет на амплитуду
            a = np.exp(pass_a0*(-np.exp(-pass_a0*(np.log(fn)-np.log(self.f0)))))
        
        if self.type == 'high_shelf':
            shelf_h0 = self.a0
            shelf_a0 = self.b0
            #shelf_h0 = 1 # > 0, высота полки
            #shelf_a0 = 3 # > 0, регулирует резкость полки
            a = np.exp(shelf_h0*(np.tanh(shelf_a0*(np.log(fn)-np.log(self.f0))) + 1))
        
        if self.type == 'low_shelf':
            shelf_h0 = self.a0
            shelf_a0 = self.b0
            #shelf_h0 = -1 # < 0 высота полки
            #shelf_a0 = 3 # > 0 регулирует резкость полки
            a = np.exp(-shelf_h0*(np.tanh(shelf_a0*(np.log(fn)-np.log(self.f0))) - 1))
        
        # нарисуем графики для демонстрации
        """
        fig, ax = plt.subplots()
        ax.plot(np.log(fn), np.log(a))
        ax.set_title(self.type)
        ax.set_xlabel('ln(f)')
        ax.set_ylabel('ln(a)')
        
        fig1, ax1 = plt.subplots()
        ax1.plot(fn, a)
        ax1.set_title(self.type)
        ax1.set_xlabel('f')
        ax1.set_ylabel('a')
        """        
        return a


"""
def spectr_filter(fmax, N, filter_type='peak', f0=-1, peak_a0=0.1, peak_b0=0.1, 
                  pass_a0=3, pass_h0=1, shelf_h0=1, shelf_a0=3):
    if f0 == -1: # f0 - характерная частота пропускания
        f0 = fmax//5
    numbers = np.arange(N)
    fn = fmax * numbers / N
    
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
    """

"""
# тест для функции
fmax = 200
N = 1000
a = spectr_filter(fmax, N, 'high_pass', f0=80, pass_a0=5)
plt.show()
"""
"""
# тест для класса
filter1 = Filter('peak', 450, 0.01, 0.02)
mas1 = filter1.get_table(1000, 10000)
filter2 = Filter('high_pass', 100, 0.5, 1)
mas2 = filter2.get_table(10000, 10000)


a = mas1

numbers = np.arange(10000)
fn = 1000 * numbers / 10000

fig, ax = plt.subplots()
ax.plot(np.log(fn), np.log(a))
ax.set_xlabel('ln(f)')
ax.set_ylabel('ln(a)')
ax.grid(True)
        
fig1, ax1 = plt.subplots()
ax1.plot(fn, a)
ax1.set_xlabel('f')
ax1.set_ylabel('a')


plt.show()
"""

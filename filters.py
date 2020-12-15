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
                
        return a






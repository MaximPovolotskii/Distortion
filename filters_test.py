import numpy as np
import matplotlib.pyplot as plt
from filters import Filter


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

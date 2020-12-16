import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from int_channel import WavFile


def draw_wave(w, h, DPI, WavFile_1):
    """
    функция, рисующая волну wave-файла
    """
    plt.figure(1, figsize=(float(w)/DPI, float(h)/DPI), dpi=DPI)
    
    axes = plt.subplot(facecolor="k")
    axes.plot(WavFile_1.channel(), "g")
    axes.yaxis.set_major_formatter(ticker.FuncFormatter(WavFile_1.format_db))
    plt.grid(True, color="w")
    axes.xaxis.set_major_formatter(ticker.FuncFormatter(WavFile_1.format_time))

    plt.show()

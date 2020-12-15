import numpy as np
import pyaudio

FSAMP = 22050       # Частота сэмплов Hz
SAMPLES_PER_FRAME = 2048   # Сэмплов за фрейм
FRAMES_PER_FFT = 16 # За сколько усредняем
LOWEST = 60
HIGHEST = 70

SAMPLES_PER_FFT = SAMPLES_PER_FRAME*FRAMES_PER_FFT
FREQ_STEP = float(FSAMP)/SAMPLES_PER_FFT

class Audio():
    
    def __init__(self):
        self.stream = pyaudio.PyAudio().open(format=pyaudio.paInt16,
                                channels=1,
                                rate=FSAMP,
                                input=True,
                                frames_per_buffer=SAMPLES_PER_FRAME)

class Calculator():
    
    def __init__(self, lowest_note=60, highest_note=69):
        self.lowest = lowest_note
        self.highest = highest_note
        self.frec = 1
        self.number = 0
        self.note_name = ''
        self.samples = np.zeros(SAMPLES_PER_FFT)
        self.spectrum = []
        

class Manager():
    
    def __init__(self):
        self.audio = Audio()
        self.calc = Calculator(LOWEST, HIGHEST)
    
mgr = Manager()
num_frames = 0
while mgr.audio.stream.is_active():

    # смещаем данные
    mgr.calc.samples[:-SAMPLES_PER_FRAME] = mgr.calc.samples[SAMPLES_PER_FRAME:]
    mgr.calc.samples[-SAMPLES_PER_FRAME:] = np.fromstring(mgr.audio.stream.read(SAMPLES_PER_FRAME),
                                                           np.int16)

    # делаем Фурье-преобразование
    mgr.calc.spectrum = np.fft.rfft(mgr.calc.samples)

    # частота с максимальной амплитудой
    mgr.calc.freq = (np.abs(mgr.calc.spectrum).argmax()) * FREQ_STEP


    num_frames += 1
    if num_frames >= FRAMES_PER_FFT:
        print( 'freq:',  mgr.calc.freq)
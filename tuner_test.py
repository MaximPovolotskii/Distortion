import numpy as np
import pyaudio


FSAMP = 22050       # Sampling frequency in Hz
FRAME_SIZE = 2048   # How many samples per frame?
FRAMES_PER_FFT = 16 # FFT takes average across how many frames?
LOWEST = 60
HIGHEST = 69

NOTE_NAMES = 'C C# D D# E F F# G G# A A# B'.split()
SAMPLES_PER_FFT = FRAME_SIZE*FRAMES_PER_FFT
FREQ_STEP = float(FSAMP)/SAMPLES_PER_FFT

class Listener():
    
    def __init__(self):
        self.stream = pyaudio.PyAudio().open(format=pyaudio.paInt16,
                                channels=1,
                                rate=FSAMP,
                                input=True,
                                frames_per_buffer=FRAME_SIZE)

class Calculator():
    
    def __init__(self, lowest_note=60, highest_note=69):
        self.lowest = lowest_note
        self.highest = highest_note
        self.frec = 1
        self.number = 0
        self.note_name = ''
        self.samples = np.zeros(SAMPLES_PER_FFT)
        self.spectrum = []
        
    def freq_to_number(self):
        self.number = 69 + 12*np.log2(self.frec/440.0)
        
    def number_to_freq(self):
        self.frec = 440 * 2.0**((self.number - 69)/12.0)
        
    def number_to_note_name(self, int_n):
        self.note_name = NOTE_NAMES[int_n % 12] + str(int_n/12 - 1)


class Manager():
    
    def __init__(self):
        self.audio = Listener()
        self.calc = Calculator(LOWEST, HIGHEST)
    
mgr = Manager()
num_frames = 0
while mgr.audio.stream.is_active():

    # Shift the buffer down and new data in
    mgr.calc.samples[:-FRAME_SIZE] = mgr.calc.samples[FRAME_SIZE:]
    mgr.calc.samples[-FRAME_SIZE:] = np.fromstring(mgr.audio.stream.read(FRAME_SIZE), np.int16)

    # Run the FFT on the buffer
    mgr.calc.spectrum = np.fft.rfft(mgr.calc.samples)

    # Get frequency of maximum response 
    mgr.calc.freq = (np.abs(mgr.calc.spectrum).argmax()) * FREQ_STEP

    # Get note number and nearest note
    #doesn't work yet
    '''
    mgr.calc.freq_to_number()
    int_n = int(round(mgr.calc.number))
    mgr.calc.number_to_note_name(int_n)

    '''
    # Console output once we have a full buffer
    num_frames += 1
    if num_frames >= FRAMES_PER_FFT:
        print( 'freq:',  mgr.calc.freq)
import numpy as np
import pyaudio as pa
import pygame as pg
'''
у меня лично с установкой pyaudio возникли проблемы, если что, смотрите ссылку:
https://ru.stackoverflow.com/questions/927657/pyaudio-не-устанавливается
'''

FSAMP = 22050       # Частота сэмплирования, Hz
SAMPLES_PER_FRAME = 1024  # Сэмплов за фрейм
FRAMES_PER_FFT = 16 # За сколько фреймов усредняем Фурье
TICK_TIME = 50
LOWEST = 60
HIGHEST = 70
NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

W = 100
SCREEN_SIZE = (12*W, 100)
COLOR = (100, 100, 151)
SCREEN_COLOR = (0, 0, 51)
P_COLOR = (128,255,191)

SAMPLES_PER_FFT = SAMPLES_PER_FRAME * FRAMES_PER_FFT
FREQ_STEP = FSAMP / SAMPLES_PER_FFT

class Audio():
    
    def __init__(self):
        self.stream = pa.PyAudio().open(format=pa.paInt16,
                                channels=1,
                                rate=FSAMP,
                                input=True,
                                frames_per_buffer=SAMPLES_PER_FRAME)
                

class Calculator():
    
    def __init__(self, lowest_note=60, highest_note=69):
        self.lowest = lowest_note
        self.highest = highest_note
        self.freq = 1
        self.p = 0
        self.note_number = 0
        self.note_name = ''
        self.samples = np.zeros(SAMPLES_PER_FFT)
        self.spectrum = []
        
    def calculate_freq(self):
        '''
        делает Фурье-преобразование и находит частоту с максимальной амплитудой
        '''
        self.spectrum = np.fft.rfft(self.samples)
        self.freq = (np.abs(self.spectrum).argmax()) * FREQ_STEP

        
    def calculate_nearest_note(self):
        '''
        рассчитывает ближайшую ноту из частоты по формулам из
        фейковой Википедии
        https://wikichi.ru/wiki/Musical_note
        и отсюда
        https://webhamster.ru/mytetrashare/index/mtb0/1343982148vkmqs7k7ig
        '''
        self.p = 69 + 12*(np.log2(self.freq / 440))
        self.note_number = int(round(self.p))
        self.note_name = NOTE_NAMES[self.note_number % 12]
    
class Drawer():
    
    def __init__(self):
        self.screen = pg.display.set_mode(SCREEN_SIZE)
        
    def draw_initial(self):
        '''
        рисует фон и шкалу

        '''
        self.screen.fill(SCREEN_COLOR)
        for i in range(12):
            font = pg.font.Font(None, 40)
            text_score = font.render(NOTE_NAMES[i], False, COLOR)
            self.screen.blit(text_score, (W*i, 0)) 
            pg.draw.line(self.screen, COLOR, [W*i, 10], [W*i, 100])
            
    def draw_p(self, p, note_number):
        '''
        рисует маркер
        '''
        
        x_coord = W * (note_number%12) + int(round(W * (p - note_number)))
        print('fuck', note_number, (W * (p - note_number)), x_coord)
        if x_coord < 0:
            x_coord += SCREEN_SIZE[0]
        pg.draw.circle(self.screen, P_COLOR, (x_coord, 50), 5)
    
class Manager():
    
    def __init__(self):
        self.audio = Audio()
        self.calc = Calculator(LOWEST, HIGHEST)
        self.drawer = Drawer()
        self.done = False
    
    def move(self):
        '''
        смещает данные и получает новые
        '''
        self.calc.samples[:-SAMPLES_PER_FRAME] = self.calc.samples[SAMPLES_PER_FRAME:]
        self.calc.samples[-SAMPLES_PER_FRAME:] = np.fromstring(self.audio.stream.read(SAMPLES_PER_FRAME),
                                                               np.int16)
        
    def calculate(self):
        self.calc.calculate_freq()
        self.calc.calculate_nearest_note()
        
    def draw(self):
        self.drawer.draw_initial()
        self.drawer.draw_p(self.calc.p, self.calc.note_number)
        
    
    def handle_events(self, events):
        '''
        закрывает окно, а затем и все остальное
        '''
        for event in events:
            if event.type == pg.QUIT:
                self.done = True
                self.audio.stream.stop_stream()
                self.audio.stream.close()
    
    
pg.init()        
clock = pg.time.Clock()
mgr = Manager()

number_frames = 0
while not mgr.done:
    mgr.move()
    mgr.calculate()
    mgr.handle_events(pg.event.get())
    pg.display.flip()
    number_frames += 1

    if number_frames >= FRAMES_PER_FFT:
        print( 'freq:',  mgr.calc.freq, mgr.calc.p, mgr.calc.note_name)
        mgr.draw()
        clock.tick(100)
pg.quit()

#232.8277587890625 57.981114593331725 A#


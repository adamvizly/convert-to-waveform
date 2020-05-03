import sys
from os import path
from pydub import AudioSegment
import matplotlib.pyplot as plt
import numpy as np
import wave

def show_wave(audio):
    spf = wave.open(f"{audio}.wav", 'r')
    sound = spf.readframes(-1)
    sound = np.fromstring(sound, 'Int16')
    f = spf.getframerate()
    Time = np.linspace(0, len(sound) / f, num=len(sound))
    plt.figure(1)
    plt.plot(Time, sound)
    plt.show()
    spf.close()


def convert(audio):                                                                             
    src = f"{audio}.ogg"
    dst = f"{audio}.wav"
                                                            
    sound = AudioSegment.from_ogg(src)
    sound.export(dst, format="wav")

fil = sys.argv[1]
convert(fil)
show_wave(fil)
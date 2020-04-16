import pyaudio
import wave
import sys
from scipy.io import wavfile


def get_sound_file(soundpath):
    fs, wf = wavfile.read(soundpath)
    return fs, wf
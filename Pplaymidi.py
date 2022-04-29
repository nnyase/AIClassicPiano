import music21
import os
import numpy as np
import itertools
import pretty_midi
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
#import moviepy.editor as mpy
from IPython.core.display import Video
from IPython import display
import seaborn as sns
import pickle
import seaborn as sns
import glob

def playmidi(filename):
    mf = music21.midi.MidiFile()
    mf.open(filename)
    mf.read()
    mf.close()
    s = music21.midi.translate.midiFileToStream(mf)
    s.show('midi')


playmidi("test_output.mid") 
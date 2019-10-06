# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 11:16:00 2019

@author: Daniel
"""
import numpy as np #for complex math and matrix math
import pandas as pd #for storage of large data sets
import matplotlib.pyplot as plt #for plotting

from glob import glob #For reading Files
import librosa as lr #For audio analysis
import librosa.display #explicitly say you want the display attribute of librosa


#in what directory are our audio files?
path = './Ambient_Audio'
#Read the files into an array audio_files
audio_files = glob(path + '/*.wav') #adds anthing with extension .wav


#y refers to amplitude
#sr refers to sample rate
#load a specific file audio_files[i]
y, sr = lr.core.load(audio_files[13])
#open a figure
plt.figure()
#specify dimensions
plt.subplot(3,1,1)
#attach the plot with amplitude and sample rate as parameters
lr.display.waveplot(y, sr = sr)
#add a title
plt.title('Ambient Noise');



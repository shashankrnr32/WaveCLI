#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 23:51:59 2019

@author: varun
"""
import argparse
import matplotlib.pyplot as plot
import Utilities as util
import numpy as np
from scipy import signal
import os

parser = argparse.ArgumentParser(description = 'Compare pitch shifted wav files')

parser.add_argument('-i', nargs = '?', required = True, type = str, help = 'Input File (.wav)')
parser.add_argument('-o', nargs = '?', required = True, type = str, help = 'Output Folder')
parser.add_argument('-isolate',default = False, action = 'store_true', help = 'Plot Only Spectrogram without .wav')
args = parser.parse_args()

pit = [-5,-2,+2,+5]
for i in range(len(pit)):
    cmd = 'soundstretch {} {}/Wave_{}.wav -pitch={} -tempo=-5 > log.txt'.format(args.i,args.o,pit[i],pit[i])
    os.system(cmd)
    os.system('cp {} {}'.format(args.i,args.o))
    os.system('rm log.txt')
    file = '{}_{}.wav'.format((args.i).split('.')[0],i)
    [fs,y_axis] = util.WavRead('{}_{}.wav'.format((args.i).split('.')[0],i))
    x_axis = np.arange(0,len(y_axis)/fs,1/fs)
    f, t, spectrogram = signal.spectrogram(y_axis,fs, window = signal.get_window('hamming',1024), noverlap = 100)
    if not args.isolate:
        plot.subplot(211)
        plot.plot(x_axis,y_axis)
        plot.grid()
        plot.title(args.i.split('/')[-1]+ ' Signal')
        plot.xlabel('Time (s)')
        plot.ylabel('Amplitude')
        plot.subplot(212)
    plot.pcolormesh(t, f, spectrogram, cmap = 'tab20')
    plot.ylabel('Frequency (Hz)')
    plot.yscale('symlog')
    plot.xlabel('Time (s)')
    plot.grid()
    plot.title(args.i.split('/')[-1]+ ' Spectrogram')
    plot.tight_layout()
    plot.savefig('{}/File_{}.png'.format(args.o,pit[i]), dpi = 360)
    plot.show()
    plot.close()
    
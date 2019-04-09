#!/usr/bin/env python3

# =============================================================================
# Developer : Shashank Sharma(shashankrnr32@gmail.com)
# License : MIT License
# Year : 2019
# =============================================================================
# =============================================================================
# Description:
#     Plot Spectrogram of a .wav file
# =============================================================================
import argparse
import matplotlib.pyplot as plot
import Utilities as util
import numpy as np
from scipy import signal

parser = argparse.ArgumentParser(description = 'Plot Spectrogram of a .wav File')

parser.add_argument('-i', nargs = '?', required = True, type = str, help = 'Input File (.wav)')
parser.add_argument('-o', nargs = '?', type = str, help = 'Output Image File (Optional)')
parser.add_argument('-isolate',default = False, action = 'store_true', help = 'Plot Only Spectrogram without .wav')
args = parser.parse_args()

[fs,y_axis] = util.WavRead(args.i)

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
if args.o:
    plot.savefig(args.o, dpi = 360)
else:
    plot.show()
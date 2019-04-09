#!/usr/bin/env python3

# =============================================================================
# Developer : Shashank Sharma(shashankrnr32@gmail.com)
# License : MIT License
# Year : 2019
# =============================================================================
# =============================================================================
# Description:
#     Python File to Plot Pitch Contour of a wav file
#     Uses SPTK (pysptk)
# =============================================================================

import pysptk.sptk as sptk
import argparse
import matplotlib.pyplot as plot
import Utilities as util
import numpy as np

def smooth_pitch(pitch):
    start_frame = 1
    end_frame = 0
    flag = False
    for index in range(len(pitch)):
        if pitch[index] != 0 and not flag:
            start_frame = index
            flag = True
        if pitch[index] == 0 and flag:
            end_frame = index
            mean_frame = sum(pitch[start_frame : end_frame])/(end_frame-start_frame)
            smooth = np.full((1,(end_frame-start_frame)),mean_frame)
            pitch[start_frame : end_frame] = smooth
            flag = False
    return pitch

parser = argparse.ArgumentParser(description = 'Plot Pitch Contour of a .wav file')

parser.add_argument('-i', nargs = '?', required = True, type = str, help = 'Input File (.wav)')
parser.add_argument('-o', nargs = '?', type = str, help = 'Output Image File (Optional)')
parser.add_argument('-isolate',default = False, action = 'store_true', help = 'Plot Only Pitch Countour without signal (.wav)')
parser.add_argument('-fmin',type = int, default = 60,help = 'Minimum Fundamental Frequency in Hz(60-80 For males and 120-150 for Females)')
parser.add_argument('-fmax',type = int, default = 240,help = 'Maximum Fundamental Frequency in Hz(200 for Males and 300-400 for Females) ')
parser.add_argument('-smooth',default = False, action = 'store_true', help = 'Apply Pitch Smoothing Algorithm')
parser.add_argument('-mean',default = False, action = 'store_true', help = 'Draw an Average Line on the Plot')
args = parser.parse_args()

[fs,sig] = util.WavRead(args.i)
sig = sig.astype('float32')
if not args.isolate:
    x_axis = np.arange(0,len(sig)/fs,1/fs)
    plot.subplot(211)
    plot.plot(x_axis,sig)
    plot.grid()
    plot.title(args.i.split('/')[-1]+ ' Signal')
    plot.xlabel('Time (s)')
    plot.ylabel('Amplitude')
    plot.subplot(212)

fmin = float(args.fmin)
fmax = float(args.fmax)
pitch = sptk.rapt(sig,fs,250,float(120),float(400))
x_axis = np.linspace(0,len(sig)/fs,len(pitch))

if args.smooth:
    pitch = smooth_pitch(pitch)
    plot.title(args.i.split('/')[-1]+ ' Pitch Contour(Smoothed)')
else:
    plot.title(args.i.split('/')[-1]+ ' Pitch Contour')

plot.plot(x_axis,pitch)
plot.ylim([fmin,fmax])
plot.grid()

if args.mean:
    length = 0
    add = 0
    for x in pitch:
        if x!=0:
            add += x
            length += 1
    mean = add/length
    print('Mean Pitch = {} Hz'.format(mean))
    plot.plot((0,len(sig)/fs),(mean,mean),'k-',dashes = [3,3])
    plot.legend(['Pitch Contour','Average Pitch'])

plot.tight_layout()
if args.o:
    plot.savefig(args.o, dpi = 360)
else:
    plot.show()
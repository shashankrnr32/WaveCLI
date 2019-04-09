#!/usr/bin/env python3

# =============================================================================
# Developer : Shashank Sharma(shashankrnr32@gmail.com)
# License : MIT License
# Year : 2019
# =============================================================================
# =============================================================================
# Description:
#     Plot .wav file
# =============================================================================

import argparse
import matplotlib.pyplot as plot
import Utilities as util
import numpy as np

parser = argparse.ArgumentParser(description = 'Plot Signal of a .wav File')

parser.add_argument('-i', nargs = '?', required = True, type = str, help = 'Input File (.wav)')
parser.add_argument('-o', nargs = '?', type = str, help = 'Output Image File (Optional)')
parser.add_argument('-norm',default = False, action = 'store_true', help = 'Normalize Amplitude Values')
args = parser.parse_args()

[fs,y_axis] = util.WavRead(args.i)

#Normalize the Amplitude
if args.n:
    y_axis = y_axis/max(y_axis)
    
x_axis = np.arange(0,len(y_axis)/fs,1/fs)

plot.plot(x_axis,y_axis)

plot.grid()
plot.title(args.i.split('/')[-1])
plot.xlabel('Time (s)')
if args.n:
    plot.ylabel('Amplitude (Normalized)')
else:
    plot.ylabel('Amplitude')

plot.tight_layout()

if args.o:
    plot.savefig(args.o, dpi = 360)
else:
    plot.show()
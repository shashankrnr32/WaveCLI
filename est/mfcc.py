#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# Developer : Shashank Sharma(shashankrnr32@gmail.com)
# License : MIT License
# Year : 2019
# =============================================================================
# =============================================================================
# Description:
#     Plot MFCC Colormap
# =============================================================================

import speech_tools as est
import numpy as np
import argparse
import matplotlib.pyplot as plot
from matplotlib import cm

parser = argparse.ArgumentParser(description = 'Plot colormap of MFCC vectors')

parser.add_argument('-i', nargs = '?', required = True, type = str, help = 'Input File (.wav)')
parser.add_argument('-o', nargs = '?', type = str, help = 'Output Image File (Optional)')
parser.add_argument('-flen', nargs = '?', type = float, default = 0.02, help = 'Frame Length in seconds (0.02)')
parser.add_argument('-fshift', nargs = '?', type = float, default = 0.01, help = 'Frame Shift in seconds (0.01)')
parser.add_argument('-order', nargs = '?', type = int, default = 13, help = 'MFCC vector order (13)')
args = parser.parse_args()


#Find MFCC Array
mfcc_array = est.mfcc(input_file = args.i, frame_length = args.flen, frame_shift = args.fshift,
                      order = args.order)

#Transpose
mfcc_array= np.swapaxes(mfcc_array, 0 ,1)

#Show in colormap
plot.imshow(mfcc_array, interpolation='nearest', 
                cmap=cm.magma, origin='lower', aspect = 'auto')

plot.title('MFCC {}'.format(args.i.split('/')[-1]))
plot.xlabel('Frames')
plot.ylabel('Index')
if args.o:
    plot.savefig(args.o, dpi = 360)
else:
    plot.show()


#!/usr/bin/env python3

# =============================================================================
# Developer : Shashank Sharma(shashankrnr32@gmail.com)
# License : MIT License
# Year : 2019
# =============================================================================
# =============================================================================
# Description:
#     Comparison of 2 wav files by plotting the mfcc vectors
# =============================================================================


import argparse
import matplotlib.pyplot as plot
import Utilities as util
import numpy as np
import pysptk

parser = argparse.ArgumentParser(description = 'MFCC of an Audio Signal')

parser.add_argument('-i1', nargs = '?', required = True, type = str, help = 'Input File 1')
parser.add_argument('-i2', nargs = '?', required = True, type = str, help = 'Input File 2')
parser.add_argument('-o', nargs = '?', type = str, help = 'Output Image File (Optional)')
args = parser.parse_args()

fs, sig1 = util.WavRead(args.i1)
sig1 = sig1/max(sig1)
mfcc1 = pysptk.mfcc(x = sig1,order =  17, fs = fs,
                    window_len = 128, frame_len = 1024, use_dft = True,
                    czero = False, power = False)

fs, sig2 = util.WavRead(args.i2)
sig2 = sig2/max(sig2)
mfcc2 = pysptk.mfcc(x = sig2,order =  17, fs = fs,
                    window_len = 128, frame_len = 1024, use_dft = True,
                    czero = False, power = False)

plot.plot(np.abs(mfcc1))
plot.plot(np.abs(mfcc2))
plot.legend([args.i1.split('/')[-1],args.i2.split('/')[-1]])
plot.title('MFCC Plots')
#print(np.sum(mfcc1-mfcc2))

plot.grid()

if args.o:
    plot.savefig(args.o, dpi = 360)
else:
    plot.show()

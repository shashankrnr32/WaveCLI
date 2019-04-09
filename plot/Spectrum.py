#!/usr/bin/env python3

# =============================================================================
# Developer : Shashank Sharma(shashankrnr32@gmail.com)
# License : MIT License
# Year : 2019
# =============================================================================
# =============================================================================
# Description:
#     Plot Spectrum of a .wav file
# =============================================================================

import argparse
import matplotlib.pyplot as plot
import Utilities as util
import numpy as np
parser = argparse.ArgumentParser(description = 'Plot Frequency Spectrum of a .wav file')

parser.add_argument('-i', nargs = '?', required = True, type = str, help = 'Input File (.wav)')
parser.add_argument('-o', nargs = '?', type = str, help = 'Output Image File (Optional)')
args = parser.parse_args()

[fs,sig] = util.WavRead(args.i)
sig = sig/max(sig)
spectrum, freqs, line = plot.magnitude_spectrum(sig, Fs = fs, scale = 'dB')
spectrum_db = 20*np.log10(spectrum)

y_max = max(spectrum_db)+5
y_min = max(min(spectrum_db)-5,-100)
plot.ylim([y_min,y_max])
plot.title(args.i.split('/')[-1] + ' Spectrum')

#Fill Plot Like Audacity
plot.fill_between(freqs,spectrum_db,-110)
plot.grid()

if args.o:
    plot.savefig(args.o, dpi = 360)
else:
    plot.show()
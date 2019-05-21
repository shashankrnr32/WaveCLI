#!/usr/bin/env python3

# =============================================================================
# Developer : Shashank Sharma(shashankrnr32@gmail.com)
# License : MIT License
# Year : 2019
# =============================================================================
# =============================================================================
# Description:
#     Compare 2 WavFiles for similarity
# =============================================================================

import argparse
import matplotlib.pyplot as plot
import Utilities as util
import numpy as np
import sys
import math

def highestPowerof2(n): 
    p = int(math.log(n, 2)); 
    return int(pow(2, p));  

parser = argparse.ArgumentParser(description = 'Compare 2 audio files for their Similarity')

parser.add_argument('-i1', nargs = '?', required = True, type = str, help = 'Input File 1(.wav)[ORIGINAL]')
parser.add_argument('-i2', nargs = '?', required = True, type = str, help = 'Input File 2(.wav)[ESTIMATE]')
parser.add_argument('-o', nargs = '?', type = str, help = 'Output Image File (Optional)')
args = parser.parse_args()

#Read wave files
[fs1, sig1] = util.WavRead(args.i1)
[fs2, sig2] = util.WavRead(args.i2)

#Make Equal length Spectrums
pad_to1 = highestPowerof2(len(sig1))
pad_to2 = highestPowerof2(len(sig2))

pad_to = min(pad_to1,pad_to2)

if fs1 != fs2:
    print('Unable to Calculate. (Sampling Freqs are different)')
    sys.exit(0)

#Signal 1   
sig1 = sig1/max(sig1)
spectrum1, freqs1, line1 = plot.magnitude_spectrum(sig1, Fs = fs1, scale = 'dB', pad_to = pad_to)
spectrum_db1 = 20*np.log10(spectrum1)

phase1,freqs_phase1,line_phase1 = plot.phase_spectrum(sig1, Fs = fs1, pad_to = pad_to)

#Signal 2
sig2 = sig2/max(sig2)
spectrum2, freqs2, line2 = plot.magnitude_spectrum(sig2, Fs = fs2, scale = 'dB', pad_to = pad_to)
spectrum_db2 = 20*np.log10(spectrum2)

phase2,freqs_phase2,line_phase2 = plot.phase_spectrum(sig2, Fs = fs2, pad_to = pad_to)


#1st Spectrum Plot
plot.subplot(221)
y_max1 = max(spectrum_db1)+5
y_min1 = max(min(spectrum_db1)-5,-100)
plot.ylim([y_min1,y_max1])
plot.title(args.i1.split('/')[-1] + ' Spectrum')
plot.xlabel('Frequency (Hz)')
plot.ylabel('Magnitude')

#Fill Plot Like Audacity
plot.fill_between(freqs1,spectrum_db1,-110)
plot.grid()

#2nd Spectrum
plot.subplot(222)
y_max2 = max(spectrum_db2)+5
y_min2 = max(min(spectrum_db2)-5,-100)
plot.ylim([y_min2,y_max2])
plot.title(args.i2.split('/')[-1] + ' Spectrum')
plot.xlabel('Frequency (Hz)')
plot.ylabel('Magnitude')

#Fill Plot Like Audacity
plot.fill_between(freqs2,spectrum_db2,-110)
plot.grid()


local_size = len(freqs2)//1
#For good comparison local ratio line must not vary very much

ratio = np.divide(spectrum_db1, spectrum_db2)
ratio_line = list()
plot.subplot(212)

for i in range(len(freqs1)//local_size):
    temp = ratio[i*local_size : i*local_size + local_size]
    temp_freqs = freqs1[i*local_size : i*local_size + local_size]
    uniq_line = list(np.poly1d(np.polyfit(temp_freqs, temp, 1))(np.unique(temp_freqs)))
    ratio_line = ratio_line + uniq_line

slope = (ratio_line[-1] - ratio_line[0])/(freqs1[-1] - freqs1[0])
plot.plot(freqs1, ratio_line)
plot.title('Best Fit Line of comparison (Slope = {:.5})'.format(slope))
plot.xlabel('Frquency (Hz)')
plot.ylabel('Ratio (Best Fit)')
plot.ylim([0,1])
plot.grid()


if args.o:
    plot.savefig(args.o, dpi = 360)
else:
    plot.tight_layout()
    plot.show()




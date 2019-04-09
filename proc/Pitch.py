#!/usr/bin/env python3
    
# =============================================================================
# Developer : Shashank Sharma(shashankrnr32@gmail.com)
# License : MIT License
# Year : 2019
# =============================================================================
# =============================================================================
# Description:
#     Shift Pitch of a wav file by +/- x semitones
# =============================================================================

import argparse
import apt
import os
try:
    cache = apt.Cache()
    if not cache['soundstretch'].is_installed:
        raise Exception()
except:
    print('A debian package `soundstretch` is required for the pitch shift operation. Installing it now on this system...')
    value = os.system('sudo apt install soundstretch')
finally:
    parser = argparse.ArgumentParser(description = 'Shift Pitch of a .wav file by `SHIFT` semitones')

    parser.add_argument('-i', nargs = '?', required = True, type = str, help = 'Input File (.wav)')
    parser.add_argument('-o', nargs = '?', required = True, type = str, help = 'Output File (.wav)')
    parser.add_argument('-x',type = float, required = True, help = 'Pitch shift value in semitones[Min = -60.0 and Max = +60.0]')
    args = parser.parse_args()
    os.system('soundstretch {} {} -pitch={}'.format(args.i,args.o,args.x))
    
    
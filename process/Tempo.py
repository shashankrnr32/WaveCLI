#!/usr/bin/env python3
    
# =============================================================================
# Developer : Shashank Sharma(shashankrnr32@gmail.com)
# License : MIT License
# Year : 2019
# =============================================================================
# =============================================================================
# Description:
#     Change Tempo without affecting Pitch
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
    parser = argparse.ArgumentParser(description = 'Change Tempo of a .wav file by `TEMPO` semitones without affecting Pitch')

    parser.add_argument('-i', nargs = '?', required = True, type = str, help = 'Input File (.wav)')
    parser.add_argument('-o', nargs = '?', required = True, type = str, help = 'Output File (.wav)')
    parser.add_argument('-x',type = float, required = True, help = 'Tempo Change Percentage')
    args = parser.parse_args()
    os.system('soundstretch {} {} -tempo={}'.format(args.i,args.o,args.shift))
    
    
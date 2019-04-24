#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# Developer : Shashank Sharma(shashankrnr32@gmail.com)
# License : MIT License
# Year : 2019
# =============================================================================
# =============================================================================
# Description:
#     Clip Audio from start to end
# =============================================================================

import speech_tools as est
import argparse

parser = argparse.ArgumentParser(description = 'Clip an Audio file')

parser.add_argument('-i', nargs = '?', required = True, type = str, help = 'Input File (.wav)')
parser.add_argument('-o', nargs = '?', type = str, help = 'Output Image File (Optional)')
parser.add_argument('-start', nargs = '?', type = float, default = 0, help = 'Starting point in seconds')
parser.add_argument('-end', nargs = '?', type = float, default = -1, help = 'Starting point in seconds')
args = parser.parse_args()

#Clip Audio
est.clip_audio(args.i, args.o, args.start, args.end)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# Developer : Shashank Sharma(shashankrnr32@gmail.com)
# License : MIT License
# Year : 2019
# =============================================================================
# =============================================================================
# Description:
#     Dynamic Range Compression of an audio file
# =============================================================================

import speech_tools as est
import argparse

parser = argparse.ArgumentParser(description = 'Resample a Wave file')

parser.add_argument('-i', nargs = '?', required = True, type = str, help = 'Input File (.wav)')
parser.add_argument('-o', nargs = '?', required = True, type = str, help = 'Output File (.wav)')
parser.add_argument('-c', nargs = '?', default = 50, type = float, help = 'Compression Factor (50)')
parser.add_argument('-scale', nargs = '?', default = 0.65, type = float, help = 'Amplitude Scaling Factor (0.65)')
parser.add_argument('-info',default = False, action = 'store_true', help = 'Print Info of Output Wave')
args = parser.parse_args()

est.drc(args.i, args.o, args.c, args.scale)
if args.info:
    est.info(args.o)
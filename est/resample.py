#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# Developer : Shashank Sharma(shashankrnr32@gmail.com)
# License : MIT License
# Year : 2019
# =============================================================================
# =============================================================================
# Description:
#     Resample a .wav file
# =============================================================================

import speech_tools as est
import argparse

parser = argparse.ArgumentParser(description = 'Resample a Wave file')

parser.add_argument('-i', nargs = '?', required = True, type = str, help = 'Input File (.wav)')
parser.add_argument('-o', nargs = '?', required = True, type = str, help = 'Output File (.wav)')
parser.add_argument('-f', nargs = '?', required = True, type = int, help = 'Output Sampling Frequency in Hz')

args = parser.parse_args()

est.resample(args.i, args.o, args.f)
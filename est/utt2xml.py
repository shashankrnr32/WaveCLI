#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# Developer : Shashank Sharma(shashankrnr32@gmail.com)
# License : MIT License
# Year : 2019
# =============================================================================
# =============================================================================
# Description:
#     Convert Utterance file (.utt) to XML
# =============================================================================

import speech_tools as est
import argparse

parser = argparse.ArgumentParser(description = 'Convert Utterance to XML')

parser.add_argument('-i', nargs = '?', required = True, type = str, help = 'Input File (.utt)')
parser.add_argument('-o', nargs = '?', type = str, help = 'Output File (.xml) - Outputs to stdout by default ')
args = parser.parse_args()

out = est.utt2xml(args.i, args.o)
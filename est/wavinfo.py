#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# Developer : Shashank Sharma(shashankrnr32@gmail.com)
# License : MIT License
# Year : 2019
# =============================================================================
# =============================================================================
# Description:
#     Print Information of a Wave file
# =============================================================================

import speech_tools as est
import argparse

parser = argparse.ArgumentParser(description = 'Print Information of a Wave File')

parser.add_argument('-i', nargs = '?', required = True, type = str, help = 'Input File (.wav)')
args = parser.parse_args()

est.info(args.i)
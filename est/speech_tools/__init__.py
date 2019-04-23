#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# Developer : Shashank Sharma(shashankrnr32@gmail.com)
# License : MIT License
# Year : 2019
# =============================================================================
# =============================================================================
# Description:
#     Wrapper for EST
# =============================================================================

import os
import subprocess
import numpy as np

ESTDIR = os.path.dirname(os.path.realpath(__file__))
os.environ['ESTDIR'] = ESTDIR

def mfcc(input_file, frame_length = 0.02, 
        frame_shift = 0.01, order = 13, window_type = 'hamming',
        pre_emphasis = 0.97):
    
    '''  
    Parameters :
        input_file : 
            .wav File [Required] \n
        frame_length = `0.02` : 
            Analysis Frame Length in seconds \n
        frame_shift = `0.01` :
            Anaysis Window Shift for each frame in seconds \n
        order = `12` : 
            Order of the MFCC Vector \n
        window_type = `'hamming'` : 
            Type of window to be used
            [rectange, triangle, hanning, hamming] \n
        pre_emphasis = `0.97` :
            Perform pre-emphasis with this factor
            
    Returns :
        Numpy Array :
            Shape = (X, order)\n
            X = Duration of Input / frame_shift
     
    Raises :
        IOError : 
            If input_file is not found
    '''
    
    command = '{0}/bin/sig2fv {1} -S {2} -shift {3} -coefs "melcep" -otype ascii -window_type {4} -melcep_order {5} -preemph {6}'.format(
            ESTDIR, input_file, float(frame_shift), float(frame_length), window_type, int(order), pre_emphasis)
    std_out = subprocess.Popen(command, stdout = subprocess.PIPE, shell = True, stderr = subprocess.PIPE)
    
    output , error = std_out.communicate()
    error = error.decode()
    if 'Cannot open file' in error:
        raise IOError('Wave File Not Found ({})'.format(input_file))
    
    output = output.decode().split('\n')[1:-1]
    mfcc = list()
    for frame in output:
        mfcc.append([float(coeff) for coeff in frame.split()])   
    
    return np.asarray(mfcc)

def resample(input_file, output_file = None, output_frequency = 44000, channel = 0):
    '''
    Parameters :
        input_file :
            Input .wav file
        output_file :
            Output .wav file
        output_frequency = 44000 :
            Output frequency in Hz
        channel = 0 :
            Select Channel
            
    Returns :
        `True` if conversion is successfull
    
    Raises :
        IOError :
            If Input File is not found
    '''
    command = '{0}/bin/ch_wave {1} -o {2} -F {3}'.format(ESTDIR, input_file, output_file, int(output_frequency))
    std_out = subprocess.Popen(command, stdout = subprocess.PIPE, shell = True, stderr = subprocess.PIPE)
    output, error = std_out.communicate()
    
    error = error.decode()
    if 'Cannot open file' in error:
        raise IOError('Wave File Not Found ({})'.format(input_file))
    
    return True
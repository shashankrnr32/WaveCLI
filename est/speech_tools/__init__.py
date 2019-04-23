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
    Calculate the MFCC vectors of a Wave file
    
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
    Resample a Wave file
    
    Parameters :
        input_file :
            Input .wav file
        output_file :
            Output .wav file
        output_frequency = `44000` :
            Output frequency in Hz
        channel = `0` :
            Select Channel
            
    Returns :
        `True` if conversion is successfull\n
    
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

def drc(input_file, output_file, factor = 50, scale = 0.65):
    '''
    Dynamic range compression of a Wave file
    
    Parameters :
        input_file :
            Input .wav file
        output_file :
            Output .wav file
        factor = `50` :
            Dynamic Range compression factor
        scale = `0.65` :
            The dynamically compressed wave is scaled by this factor in amplitude

    Returns :
        `True` if compression was successfull
        
    Raises :
        IOError :
            If Input file is not found
    '''
    command = '{0}/bin/ch_wave {1} -compress {2} -scaleN {3} -o {4}'.format(
            ESTDIR, input_file, float(factor), scale, output_file)
    std_out = subprocess.Popen(command, stdout = subprocess.PIPE, shell = True, stderr = subprocess.PIPE)
    output, error = std_out.communicate()

    #If File Not Found
    error = error.decode()
    if 'Cannot open file' in error:
        raise IOError('Wave File Not Found ({})'.format(input_file))

    return True

def info(input_file):
    '''
    Print Information about a wave file
    
    Parameters :
        input_file :
            Input .wav file
            
    Returns :
        None
    
    Raises :
        IOError :
            If Input File is not found
    '''
    #Execute ch_wave script with -info arg
    command = '{0}/bin/ch_wave {1} -info'.format(ESTDIR, input_file)
    std_out = subprocess.Popen(command, stdout = subprocess.PIPE, shell = True, stderr = subprocess.PIPE)
    output, error = std_out.communicate()
    
    #If File Not Found
    error = error.decode()
    if 'Cannot open file' in error:
        raise IOError('Wave File Not Found ({})'.format(input_file))
    
    print('File: {}'.format(input_file))
    print(output.decode().strip())

import xml.etree.ElementTree as et
def utt2xml(input_file, output_file = None):
    '''
    Convert Utterance File to XML
    
    Parameters:
        input_file:
            .utt Utterance File
        output_file = None:
            .xml XML file (Prints to stdout if no file)
    
    Returns :
        XML object if output_file = None
        
    Raises :
        IOError :
            Utterance File not found
    '''
    if not output_file:
        output_file = ''
    else:
        output_file = '-o ' + output_file
    
    command = '{0}/bin/ch_utt {1} -otype genxml {2}'.format(ESTDIR, input_file, output_file).strip()
    
    std_out = subprocess.Popen(command, stdout = subprocess.PIPE, shell = True, stderr = subprocess.PIPE)
    output, error = std_out.communicate()
    
    #If File Not Found
    error = error.decode()
    if 'Cannot open file' in error:
        raise IOError('Utterance File Not Found ({})'.format(input_file))
    
    output = output.decode()
    if output:
        print(output)
        return et.fromstring(output)
        
    
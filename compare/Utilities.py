#!/usr/bin/env python3
# =============================================================================
# Developer : Shashank Sharma(shashankrnr32@gmail.com)
# License : MIT License
# Year : 2019
# =============================================================================
# =============================================================================
# Description:
#     Utilities File. Helper Script for other scripts
# =============================================================================
import scipy.io.wavfile as wav
import colorama
colorama.init(autoreset = True)

def error_log(msg):
    print(colorama.Fore.RED + msg)

def warning_log(msg):
    print(colorama.Fore.YELLOW + msg)
    
def WavRead(file_path = ''):
    try:
        fs,samples = wav.read(file_path)
        return [fs,samples]
    except:
        error_log('Cannot Read File : '+file_path)
        exit()
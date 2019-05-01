# WaveCLI

WaveCL or Wave Command Line is a command line interface tool to manipulate, plot and analyze .wav files. This was developed by [Shashank Sharma](mailto:shashankrnr32@gmail.com) as a part of `Kannada Speech Synthesis` Project. 

[Kannada Speech Synthesis](https://github.com/shashankrnr32/KannadaTTS-Application) is the final year project by students of the Department of ECE, Ramaiah Institute of Technology under the guidance of Sadashiva V Chakrasali

## Usage

To use any script in this project

	python3 <File>.py -h

## Available Wave Utilities

1. Plotting
	- Wave
	- Spectrogram
	- Magnitude Spectrum
	- Pitch Contour
2. Manipulation
	- Pitch Shift (without affecting Tempo)
	- Change Tempo (without affecting Pitch)
	- Change Pitch of an audio signal for 5 different values together (Varun S S)
3. Compare
	- Find Mean error between Original and Synthesized File


## Utilities using EST
Audio Utilities using Edinburgh speech tools in the folder named `est`. Also contains python wrapper for EST

### Usage
	
	python3 <File>.py -h

### Available scripts

1. MFCC colormap(`mfcc.py`)
2. Resample a Wave(`resample.py`)
3. Dynamic Range Compression (`drc.py`)
4. Print Information of a wave file (`wavinfo.py`)
5. Convert Utterance files to XML (`utt2xml.py`)
6. Clip Audio(`clip.py`)

## License

Free MIT License held by [Shashank Sharma](mailto:shashankrnr32@gmail.com)

## Credits

1. Edinburgh Speech Tools
2. SPTK


# Examples for using Python Wrapper for Edinburgh Speech Tools

# Find MFCC

		#Import Python Wrapper for EST
		import est

		#Sample Input File
		input_file = 'some_sample_file.wav'

		#Find MFCC Array
		mfcc_array = est.mfcc(input_file = input_file)

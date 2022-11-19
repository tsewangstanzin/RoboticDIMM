'''
Lucid  Camera fast Image Grabber and Create 3d Cube
Created Nov 2021
@author Tsewang Stanzin, IIA-IAO Hanle
'''
from pypylon import pylon
import numpy as np
dtype=np.float64
from astropy.io import fits
import datetime
import time
import ctypes  # ctypes.cast(), ctypes.POINTER(), ctypes.c_ushort
import os  # os.getcwd()
from pathlib import Path
import numpy as np  # pip install numpy
from PIL import Image as PIL_Image  # pip install Pillow
import sys,select,os
from arena_api.system import system

class ImageGrab:
	def __init__(self, number_of_images):
		self.number_of_images = number_of_images
		tries = 0
		tries_max = 6
		sleep_time_secs = 10
		while tries < tries_max:  # Wait for device for 60 seconds
			devices = system.create_device()
			if not devices:
				print(
					f'Try {tries + 1} of {tries_max}: waiting for {sleep_time_secs} '
					f'secs for a device to be connected!')
				for sec_count in range(sleep_time_secs):
					time.sleep(1)
					print(f'{sec_count + 1} seconds passed ',
						  '.' * sec_count, end='\r')
				tries += 1
			else:
				#print(f'Created {len(devices)} device(s)')
				break
			# return devices
		else:
			raise Exception(f'No device found! Please connect a device and run '
							f'the example again.')
		self.device = devices[0]
		return None
	def single_image(self):
		#print(f'Device used:\n\t{self.device}')
		# Get device stream nodemap
		tl_stream_nodemap = self.device.tl_stream_nodemap
		# Enable stream auto negotiate packet size
		tl_stream_nodemap['StreamAutoNegotiatePacketSize'].value = True
		# Enable stream packet resend
		tl_stream_nodemap['StreamPacketResendEnable'].value = True

		# Get nodes ---------------------------------------------------------------
		nodes = self.device.nodemap.get_node(
			['Gain', 'AcquisitionFrameRateEnable', 'AcquisitionFrameRate', 'ExposureTime', 'Width', 'Height',
			 'PixelFormat', 'ExposureAuto', 'ExposureTime', 'ExposureIntervalRaw', 'ExposureInterval','BinningHorizontal','BinningVertical','BinningSelector','BinningHorizontalMode','BinningVerticalMode','GainAuto','GainSelector'])
		nodes['GainSelector'].value = 'All'
		#nodes['GainAuto'].value = 'Continuous'
		nodes['GainAuto'].value = 'Off'
		nodes['Gain'].value = float(48.0)
		#nodes['Gain'].value = nodes['Gain'].max
		nodes['BinningSelector'].value = 'Digital'
		nodes['BinningHorizontalMode'].value = 'Average'
		#other option is SUM
		nodes['BinningVerticalMode'].value = 'Average'
		nodes['BinningVertical'].value = 2
		nodes['BinningHorizontal'].value = 2

		nodes['AcquisitionFrameRateEnable'].value = True
		#nodes['AcquisitionFrameRate'].value = nodes['AcquisitionFrameRate'].min
		nodes['AcquisitionFrameRate'].value = 10.0
		'''
        If the frame rate is 30 FPS, the maximum allowable exposure would be 1/30 = 0.0333 seconds = 33.3 milliseconds.
        So, a decrease in the frame rate is necessary for increasing the exposure time.
        '''
		nodes['ExposureAuto'].value = str('Off')
		nodes['ExposureTime'].value = 30000.0
		#nodes['ExposureTime'].value = nodes['ExposureTime'].max

		nodes['Width'].value = nodes['Width'].max
		height = nodes['Height']
		height.value = height.max

		#nodes['Width'].value =400
		#height = nodes['Height']
		#height.value = 400
		# Set pixel format to Mono12, most cameras should support this pixel format
		pixel_format_name = 'Mono16'
		# other options  [Mono8, Mono10, Mono10p, Mono10Packed, Mono12, Mono12p, Mono12Packed, Mono16]
		nodes['PixelFormat'].value = pixel_format_name

		#print("Expsoure Time: ", nodes['ExposureTime'].value)
		#print("Frame Rate: ", nodes['AcquisitionFrameRate'].value)
		#print("Width: ", nodes['Width'].value)
		#print("Height: ", nodes['Height'].value)
		#print("Pixel Format: ", nodes['PixelFormat'].value)
		#print("Gain: ", nodes['Gain'].value)

		with self.device.start_stream(1):
			# Optional args
			#print('Grabbing an image buffer')
			image_buffer = self.device.get_buffer()

			#print(f' Width X Height = '
			#	  f'{image_buffer.width} x {image_buffer.height}')

			# To save an image Pillow needs an array that is shaped to
			# (height, width). In order to obtain such an array we use numpy
			# library
			#print('Converting image buffer to a numpy array')

			# Buffer.pdata is a (uint8, ctypes.c_ubyte) type
			# Buffer.data is a list of elements each represents one byte.
			# Since Mono12 uses 16Bits (2 bytes), It is easier to user Buffer.pdata
			# over Buffer.data. Buffer.pdata must be cast to (uint16, c_ushort)
			# so every element in the array would represent one pixel.
			pdata_as16 = ctypes.cast(image_buffer.pdata,
									 ctypes.POINTER(ctypes.c_ushort))
			nparray_reshaped = np.ctypeslib.as_array(
				pdata_as16,
				(image_buffer.height, image_buffer.width))
					
			current_time = datetime.datetime.now()
			filename2 = str(current_time.year) + str("_") + str(current_time.month) + str("_") + str(
				current_time.day) + str("_") + str(current_time.hour) + str("_") + str(current_time.minute) + str(
				"_") + str(current_time.second) + str("_") + str(current_time.microsecond) + ".fits"
			hdr22 = fits.Header()
			hdr22['EXP'] = (nodes['ExposureTime'].value, 'microsecond *300 cube data')
			hdr22['Gain'] = (nodes['Gain'].value, 'Gain Set')
			hdr22['Site'] = "IAO Hanle"
			hdr22['CAM'] = "ThinkLucid PHX016S-M"
			hdr22['Time'] = (str(current_time), 'Date and time of observation')
			#fits.writeto(filename2, nparray_reshaped, header=hdr22)
			#print(filename2)
			
			# Saving --------------------------------------------------------------
			#print('Saving image')

			png_name = 'Main_Single_image.png'

			# ---------------------------------------------------------------------
			# These steps are due to a bug in Pillow saving 16bits png images
			# more : https://github.com/python-pillow/Pillow/issues/2970

			nparray_reshaped_as_bytes = nparray_reshaped.tobytes()
			png_array = PIL_Image.new('I', nparray_reshaped.T.shape)
			png_array.frombytes(nparray_reshaped_as_bytes, 'raw', 'I;16')
			# ---------------------------------------------------------------------
			png_array.save(png_name)
			#print(f'Saved image path is: {Path(os.getcwd()) / png_name}')

			self.device.requeue_buffer(image_buffer)
		
		#system.destroy_device()
		#print('Destroyed all created devices')
		return None
	def create_cube(self,wd):
		#print(f'Device used:\n\t{self.device}')
		# Get device stream nodemap
		tl_stream_nodemap = self.device.tl_stream_nodemap
		# Enable stream auto negotiate packet size
		tl_stream_nodemap['StreamAutoNegotiatePacketSize'].value = True
		# Enable stream packet resend
		tl_stream_nodemap['StreamPacketResendEnable'].value = True

		# Get nodes ---------------------------------------------------------------
		nodes = self.device.nodemap.get_node(
			['Gain', 'AcquisitionFrameRateEnable', 'AcquisitionFrameRate', 'ExposureTime', 'Width', 'Height',
			 'PixelFormat', 'ExposureAuto', 'ExposureTime', 'ExposureIntervalRaw', 'ExposureInterval',
			 'BinningHorizontal', 'BinningVertical', 'BinningSelector', 'BinningHorizontalMode', 'BinningVerticalMode',
			 'GainAuto', 'GainSelector'])
		nodes['GainSelector'].value = 'All'
		nodes['GainAuto'].value = 'Off'
		nodes['Gain'].value = float(10.0)
		# nodes['Gain'].value = nodes['Gain'].max
		nodes['BinningSelector'].value = 'Digital'
		nodes['BinningHorizontalMode'].value = 'Average'
		# other option is SUM
		nodes['BinningVerticalMode'].value = 'Average'
		nodes['BinningVertical'].value = 2
		nodes['BinningHorizontal'].value = 2


		nodes['AcquisitionFrameRateEnable'].value = True
		#nodes['AcquisitionFrameRate'].value = nodes['AcquisitionFrameRate'].max
		nodes['AcquisitionFrameRate'].value = 30.0
		'''
        If the frame rate is 30 FPS, the maximum allowable exposure would be 1/30 = 0.0333 seconds = 33.3 milliseconds.
        So, a decrease in the frame rate is necessary for increasing the exposure time.
        '''

		nodes['ExposureAuto'].value = str('Off')

		nodes['ExposureTime'].value = 10000.0
		#nodes['ExposureTime'].value = nodes['ExposureTime'].min
		nodes['Width'].value=nodes['Width'].max
		nodes['Height'].value=nodes['Height'].max
		#nodes['Width'].value=400
		#nodes['Height'].value=400
		# Set pixel format to Mono12, most cameras should support this pixel format
		pixel_format_name = 'Mono16'
		# other options  [Mono8, Mono10, Mono10p, Mono10Packed, Mono12, Mono12p, Mono12Packed, Mono16]
		nodes['PixelFormat'].value = pixel_format_name

		print("Expsoure Time: ", nodes['ExposureTime'].value)
		print("Frame Rate: ", nodes['AcquisitionFrameRate'].value)
		print("Width: ", nodes['Width'].value)
		print("Height: ", nodes['Height'].value)
		print("Pixel Format: ", nodes['PixelFormat'].value)
		print("Gain: ", nodes['Gain'].value)


		# Grab and save an image buffer -------------------------------------------
		#print('Starting stream')
		img_list = []
		img_array2 = []
		i = 0
		with self.device.start_stream(1):
			#print('Stream started')
			for i in range(self.number_of_images):
				print(str("Capturing 3D cube of 10ms*300| Image number :") + str(i + 1), end="\r")
				i += 1
				image_buffer = self.device.get_buffer()
				pdata_as16 = ctypes.cast(image_buffer.pdata,ctypes.POINTER(ctypes.c_ushort))
				nparray_reshaped = np.ctypeslib.as_array(pdata_as16,(image_buffer.height, image_buffer.width))
				nparray_reshaped = np.array(nparray_reshaped)
				img_list.append(nparray_reshaped)
				img_array2 = np.array(img_list)
				self.device.requeue_buffer(image_buffer)
		current_time = datetime.datetime.now()
		filename2 = str(current_time.year) + str("_") + str(current_time.month) + str("_") + str(
			current_time.day) + str("_") + str(current_time.hour) + str("_") + str(current_time.minute) + str(
			"_") + str(current_time.second) + str("_") + str(current_time.microsecond) + ".fits"
		hdr22 = fits.Header()
		hdr22['EXP'] = (nodes['ExposureTime'].value, 'microsecond *300 cube data')
		hdr22['Gain'] = (nodes['Gain'].value, 'Gain Set')
		hdr22['Site'] = "IAO Hanle"
		hdr22['CAM'] = "ThinkLucid TRI023S"
		hdr22['Time'] = (str(current_time), 'Date and time of observation')
		print('\n')
		print(filename2)
		fits.writeto(str(wd) + "/" + filename2, img_array2, header=hdr22)
		# Clean up ---------------------------------------------------------------
		#system.destroy_device()
		print('\n')
		return img_array2,filename2

def main():
	#pass
	#For StandAlone Grabber operation, Uncomment the below and comment the pass
	print("-----------Image Grabber----------")
	grabber=ImageGrab(300)
	i=0
	while (1):
		 grabber.single_image()
		 print(
			 str("......Check:") + str(
				 i + 1), end="\r")
		 if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
			 line = input()
			 break
		 i += 1
		 time.sleep(1)
	#while(1):
	
	#time.sleep(1)	
	grabber.create_cube('DIMMoffline')
if __name__ == "__main__":
	main()








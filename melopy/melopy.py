#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wave, random, math
from struct import pack
import os

try:
	from cStringIO import StringIO

except ImportError:
	from StringIO import StringIO

def frequency_from_key(key):
	return 440 * 2 ** ((key - 49) / 12.0)

def frequency_from_note(note):
	return frequency_from_key(key_from_note(note))

def key_from_note(note):
	indices = { 'C':0, 'D':2, 'E':4, 'F':5, 'G':7, 'A':9, 'B':11 }

	octave = 4

	if note[-1] in '012345678':
		octave = int(note[-1])

	tone = indices[note[0].upper()]
	key = 12 * octave + tone

	if len(note) > 1 and note[1] == '#':
		key += 1
	elif len(note) > 1 and note[1] == 'b':
		key -= 1

	return key - 8;

def note_from_key(key):
	notes = ['a','a#','b','c','c#','d','d#','e','f','f#','g','g#']
	octave = (key+8) / 12
	note = notes[(key-1) % 12]

	return note.upper() + str(octave)
	
def iterate(start, pattern):
	start_key = key_from_note(start)
	ret = [start_key]
	for step in pattern:
		ret.append(ret[-1] + step)
		
	ret = map(note_from_key, ret)
	return ret
	
def generate_major_scale(start):
	major_steps = [2,2,1,2,2,2]
	return iterate(start, major_steps)
	
def generate_minor_scale(start):
	minor_steps = [2,1,2,2,1,2]
	return iterate(start, minor_steps)
	
def generate_major_triad(start):
	major_triad = [4, 3]
	return iterate(start, major_triad)
	
def generate_minor_triad(start):
	minor_triad = [3, 4]
	return iterate(start, minor_triad)

class Melopy:
	def __init__(self, title='sound', volume=50, tempo=120, octave=4):
		if title == '':
			raise Exception('Title must be non-null.')
			
		self.title = title.lower()
		self.rate = 44100
		self.volume = volume / 100.0 * 32767
		self.data = []
		
		self.tempo = tempo
		self.octave = octave
		self.wave_type = 'sine'
		
	def __del__(self):
		self.render()
		
	def add_wave(self, frequency, length, location='END'):
		if location == 'END':
			location = len(self.data)
		elif location < 0:
			location = 0
		elif location * 44100 > len(self.data):
			location = len(self.data) / 44100.0
		
		# location is a time, so let's adjust
		location = int(location * 44100)
		
		for n in range(0, int(44100 * length)):
			period = 44100.0 / frequency
			
			if self.wave_type == 'square':
				val = ((n % int(period) >= (int(period)/2)) * self.volume * 2) - self.volume
			elif self.wave_type == 'sawtooth':
				val = ((n % int(period)) / period * self.volume * 2) - self.volume
			elif self.wave_type == 'triangle':
				val = 2 * (n % int(period)) / period * self.volume
				if n % int(period) >= (int(period) / 2):
					val = 2 * self.volume - val
				val = 2 * val - self.volume
			else: # default to sine
				val = self.volume * math.sin(2 * math.pi * n / period)
			
			if location + n >= len(self.data):
				self.data.append(val)
			else:
				self.data[location + n] += val
				# check that we're not above the volume
				if self.data[location + n] > self.volume:
					self.data[location + n] = self.volume
					
	def add_note(self, note, length, location='END'):
		if note[-1] not in '0123456789':
			note += str(self.octave)
		self.add_wave(frequency_from_note(note), length, location)
		
	def add_melody(self, melody, length):
		for note in melody:
			if note[-1] not in '0123456789':
				note += self.octave
			self.add_wave(frequency_from_note(note), length)
			
	def add_whole_note(self, note):
		self.add_note(note, 60.0 / self.tempo * 4)
		
	def add_half_note(self, note):
		self.add_note(note, 60.0 / self.tempo * 2)
		
	def add_quarter_note(self, note):
		self.add_note(note, 60.0 / self.tempo)
		
	def add_eighth_note(self, note):
		self.add_note(note, 60.0 / self.tempo / 2)
		
	def add_sixteenth_note(self, note):
		self.add_note(note, 60.0 / self.tempo / 4)
		
	def add_fractional_note(self, note, fraction):
		self.add_note(note, 60.0 / self.tempo * (fraction * 4))
		
	def add_rest(self, length):
		for i in range(int(self.rate * length)):
			self.data.append(0)
			
	def add_whole_rest(self):
		self.add_rest(60.0 / self.tempp * 4)
		
	def add_half_rest(self):
		self.add_rest(60.0 / self.tempo * 2)
			
	def add_quarter_rest(self):
		self.add_rest(60.0 / self.tempo)
		
	def add_eighth_rest(self):
		self.add_rest(60.0 / self.tempo / 2)
		
	def add_sixteenth_rest(self):
		self.add_rest(60.0 / self.tempo / 4)
		
	def add_fractional_rest(self, fraction):
		self.add_rest(60.0 / self.tempo * (fraction * 4))
		
	def render(self):
		"""
		Render the calculated music to a .wav file.

		"""

		# create a file like object in memory
		file_obj = StringIO()

		# generate the filename based on the title given when initializing
		# the class
		filename = '%s.wav' % self.title

		melopy_writer = wave.open(file_obj, 'w')
		melopy_writer.setparams((2, 2, 44100, 0, 'NONE', 'not compressed'))

		# Cache the writeframes method location before starting the loop,
		# and freeze the data into a faster, immutable data structure.
		writeframes = melopy_writer.writeframes
		frozen = tuple(self.data)

		for item in frozen:
			packed_val = pack('h', int(item))
			writeframes(packed_val)
			writeframes(packed_val)

		# Make certain the header is written correctly
		melopy_writer._ensure_header_written(0)

		if melopy_writer._datalength != melopy_writer._datawritten:
			melopy_writer._patchheader()

		# Flush the file object and seek to the beginning.
		file_obj.flush()
		file_obj.seek(0)

		# Now that all the work has been done, dump it to disk.
		with open(filename, 'wb') as save:
			save.write(file_obj.read())

		file_obj.close()
		del file_obj

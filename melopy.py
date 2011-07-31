import wave, struct, random, math
import os

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
	minor_steps = [2,1,2,2,2,1]
	return iterate(start, minor_steps)
	
def generate_major_triad(start):
	major_triad = [4, 3]
	return iterate(start, major_triad)
	
def generate_minor_triad(start):
	minor_triad = [3, 4]
	return iterate(start, minor_triad)

class Melopy:
	def __init__(self, title='sound', volume=50):
		if title == '':
			raise Exception('Title must be non-null.')
			
		self.melopy_writer = wave.open(title + '.wav', 'w')
		self.melopy_writer.setparams((2, 2, 44100, 0, 'NONE', 'not compressed'))
		self.rate = 44100
		self.volume = volume / 100.0 * 32767
		self.data = []
		
	def add_wave(self, wave_type, frequency, length, location='END'):
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
			
			if wave_type == 'square':
				val = (n % int(period) >= (int(period)/2)) * self.volume
			elif wave_type == 'triangle':
				val = (n % int(period)) / period * self.volume
			
			if location + n >= len(self.data):
				self.data.append(val)
			else:
				self.data[location + n] += val
				# check that we're not above the volume
				if self.data[location + n] > self.volume:
					self.data[location + n] = self.volume
					
	def add_note(self, note, length, wave_type='square', location='END'):
		if wave_type == 'square':
			self.add_square_wave(frequency_from_note(note), length, location)
		elif wave_type == 'triangle':
			self.add_triangle_wave(frequency_from_note(note), length, location)
					
	def add_square_wave(self, frequency, length, location='END'):
		self.add_wave('square', frequency, length, location)
		
	def add_triangle_wave(self, frequency, length, location='END'):
		self.add_wave('triangle', frequency, length, location)
		
	def add_melody(self, melody, length, wave_form='square'):
		for note in melody:
			self.add_wave(wave_form, frequency_from_note(note), length)
			
	def add_rest(self, length):
		for i in range(int(self.rate * length)):
			self.data.append(0)
	
	def render(self):
		for item in self.data:
			packed_val = struct.pack('h', int(item))
			self.melopy_writer.writeframes(packed_val)
			self.melopy_writer.writeframes(packed_val)

		self.melopy_writer.close()

			
			
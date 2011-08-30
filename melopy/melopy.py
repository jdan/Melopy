#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wave, struct, random, math
import os, sys 

class MelopyGenericError(Exception): pass
class MelopyValueError(ValueError): pass

def bReturn(output, Type):
    """Returns a selected output assuming input is a list"""
    if isinstance(output, list):
        if Type.lower() == "list":
            return output
        elif Type.lower() == "tuple":
            return tuple([i for i in output])
        elif Type.lower() == "dict":
            O = {}
            for i in range(len(output)):
                O[i] = output[i]
            return O
        elif Type.lower() == "string":
            return ','.join(output)
        elif Type.lower() == "stringspace":
            return ' '.join(output)
        else:
            raise MelopyGenericError("Unknown type: " + Type)
    else:
        raise MelopyGenericError("Input to bReturn is not a list! Input: " + str(output))

def frequency_from_key(key):
    """Returns the frequency of the note (key) keys from A0"""
    return 440 * 2 ** ((key - 49) / 12.0)

def frequency_from_note(note):
    """Returns the frequency of a note represented by a string"""
    return frequency_from_key(key_from_note(note))

def key_from_note(note):
    """Returns the key number (keys from A0) from a note represented by a string"""
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
    """Returns a string representing a note which is (key) keys from A0"""
    ## TODO: On generating scales and triad, they return 
    ## TODO: ['C4', 'C#4', 'D#4', 'E4', 'F#4', 'G4', 'A4', 'A#4', 'C5'] instead ['C4', 'Db4', 'E4', 'F#4', 'G4', 'G#4', 'A#4', 'B4', 'C5']
    ## TODO: In fact, they sound equal, but have different notation
    notes = ['a','a#','b','c','c#','d','d#','e','f','f#','g','g#']
    octave = (key + 8) / 12
    note = notes[(key -1 ) % 12]

    return note.upper() + str(octave)
    
def iterate(start, pattern, rType="list"):
    """Iterates over a pattern starting at a given note"""
    start_key = key_from_note(start)
    ret = [start_key]
    for step in pattern:
        ret.append(ret[-1] + step)
    ret = map(note_from_key, ret)
    return bReturn(ret, rType)
    
def generate_major_scale(start, rType="list"):
    """Generates a major scale using the pattern [2,2,1,2,2,2] (Returns: List)"""
    major_steps = [2,2,1,2,2,2]
    return iterate(start, major_steps, rType)

def generate_minor_scale(start, rType="list"): #Natural minor
    """Generates a minor scale using the pattern [2,1,2,2,1,2] (Returns: List)"""
    minor_steps = [2,1,2,2,1,2]
    return iterate(start, minor_steps, rType)
    #To be added: Harmonic and Melodic minor scales. Patterns: [2,1,2,2,2,1,2] | [2,1,2,2,2,2,1]

def generate_melodic_minor_scale(start, rType="list"):
    """Generates a melodic minor scale using the pattern [2,1,2,2,2,2,1]"""
    mminor_steps = [2,1,2,2,2,2,1]
    return iterate(start, mminor_steps,rType)

def generate_harmonic_minor_scale(start, rType="list"):
    """Generates a harmonic minor scale using the patter [2,1,2,2,2,1,2]"""
    hminor_steps = [2,1,2,2,2,1,2]
    return iterate(start, hminor_steps,rType)

def generate_octatonic_scale_half(start, rType="list"):
    """Generates a octatonic scale starting with half step"""
    octatonicScale = [1,2,1,2,1,2,1,2]    
    return iterate(start, octatonicScale, rType)

def generate_octatonic_scale_whole(start, rType="list"):
    """Generates a octatonic scale starting with whole step"""
    octatonicScale = [2,1,2,1,2,1,2,1]    
    return iterate(start, minor_steps ,rType)
    #To be added: Harmonic and Melodic minor scales. Patterns: [2,1,2,2,2,1,2] | [2,1,2,2,2,2,1]

def generate_chromatic_scale(start, rType="list"):
    """Generates a chromatic scale using the pattern [1,1,1,1,1,1,1,1,1,1,1] (Returns: List)"""
    chromatic_steps = [1,1,1,1,1,1,1,1,1,1,1]
    return iterate(start, chromatic_steps, rType)

def generate_major_pentatonic_scale(start, rType="list"):
    """Generates a major pentatonic scale using the pattern [2,2,3,2] (Returns: List)"""
    major_pentatonic_steps = [2,2,3,2]
    return iterate(start, major_pentatonic_steps, rType)

def generate_minor_pentatonic_scale(start, rType="list"):
    """Generates a minor pentatonic scale using the pattern [3,2,2,3] (Returns: List)"""
    minor_pentatonic_steps = [3,2,2,3]
    return iterate(start, minor_pentatonic_steps, rType)

def generate_major_triad(start,rType="list"):
    """Generates a major triad using the pattern [4,3] (Returns: List)"""
    major_triad = [4, 3]
    return iterate(start, major_triad, rType)

def generate_minor_triad(start,rType="list"):
    """Generates a minor triad using the pattern [3,4] (Returns: List)"""
    minor_triad = [3, 4]
    return iterate(start, minor_triad, rType)

def genScale(scale, note, rType="list"): #scale, start, type
    """Example of better way to do scale generation @NOTE: Please don't use this in production! It might be taken out at a later time..."""
    scales = {
        "major":generate_major_scale,
        "minor":generate_minor_scale,
        "melodic_minor":generate_melodic_minor_scale,
        "harmonic_minor":generate_harmonic_minor_scale,
        "chromatic":generate_chromatic_scale,
        "major_pentatonic":generate_major_pentatonic_scale,
        "octatonic_half":generate_octatonic_half,
        "octatonic_whole":generate_octatonic_whole,
    }
    if scale in scales:
        return scales[scale](note, rType) #Places each individual argument into function call
    else:
        raise MelopyGenericError("Unknown scale type:"+str(scale))

class Melopy:
    def __init__(self, title='sound', volume=50, tempo=120, octave=4):
        if not title:
            raise MelopyValueError('Title must be non-null.')
            
        self.title = title.lower()
        self.rate = 44100
        self.volume = volume
        self.data = []
        
        self.tempo = tempo
        self.octave = octave
        self.wave_type = 'sine'
        
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
                val = ((n % int(period) >= (int(period)/2)) * 2) - 1
            elif self.wave_type == 'sawtooth':
                val = ((n % int(period)) / period * 2) - 1
            elif self.wave_type == 'triangle':
                val = 2 * (n % int(period)) / period
                if n % int(period) >= (int(period) / 2):
                    val = 2 * 1 - val
                val = 2 * val - 1
            else: # default to sine
                val = math.sin(2 * math.pi * n / period)
                
            val *= self.volume / 100.0 * 32767
            
            if location + n >= len(self.data):
                self.data.append(val)
            else:
                current_val = self.data[location + n]
                if current_val + val > 32767:
                    val = 32767
                elif current_val + val < -32768:
                    val = -32768
                else:
                    val += current_val
                    
                self.data[location + n] = val
                    
    def add_note(self, note, length, location='END'):
        """Add a note, or if a list, add a chord."""
        if not isinstance(note, list):
            note = [note]

        if location == 'END':
            location = len(self.data) / 44100.0

        for item in note:
            if item[-1] not in '0123456789':
                item += str(self.octave)

            self.add_wave(frequency_from_note(item), length, location)
        
    def add_melody(self, melody, length):
        for note in melody:
            self.add_note(note, length)
            
    def add_whole_note(self, note):
        """Add a whole note"""
        self.add_note(note, 60.0 / self.tempo * 4)
        
    def add_half_note(self, note):
        """Add a half note"""
        self.add_note(note, 60.0 / self.tempo * 2)
        
    def add_quarter_note(self, note):
        """Add a quarter note"""
        self.add_note(note, 60.0 / self.tempo)
        
    def add_eighth_note(self, note):
        """Add a eigth note"""
        self.add_note(note, 60.0 / self.tempo / 2)
        
    def add_sixteenth_note(self, note):
        """Add a sixteenth note"""
        self.add_note(note, 60.0 / self.tempo / 4)
        
    def add_fractional_note(self, note, fraction):
        """Add a fractional note (smaller then 1/16 notes)"""
        self.add_note(note, 60.0 / self.tempo * (fraction * 4))
        
    def add_rest(self, length):
        for i in range(int(self.rate * length)):
            self.data.append(0)
            
    def add_whole_rest(self):
        self.add_rest(60.0 / self.tempo * 4)
        
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
        """Render a playable song out to a .wav file"""
        melopy_writer = wave.open(self.title + '.wav', 'w')
        melopy_writer.setparams((2, 2, 44100, 0, 'NONE', 'not compressed'))
        
        for item in self.data:
            packed_val = struct.pack('h', int(item))
            melopy_writer.writeframes(packed_val)
            melopy_writer.writeframes(packed_val)

        melopy_writer.close()
        
# Licensed under The MIT License (MIT)
# See LICENSE file for more

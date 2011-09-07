#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
import wave, struct, random, math
import os, sys

from melopy.utility import *
from melopy.scales  import *

class Melopy:
    def __init__(self, title='sound', volume=50, tempo=120, octave=4):
        self.title = title.lower()
        self.rate = 44100
        self.volume = volume
        self.data = []
        
        self.tempo = tempo
        self.octave = octave
        self.wave_type = 'sine'
        
    def isithere(self):
        print 'lol'
        
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
                val *= 0.6
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
        p = -1
        
        for i in range(len(self.data)):
            q = 100 * i / len(self.data)
            if p != q:
                sys.stdout.write("\r[%s] %d%%" % (('='*int((float(i)/len(self.data)*50))+'>').ljust(50), 100 * i / len(self.data)))
                sys.stdout.flush()
                p = q
            packed_val = struct.pack('h', int(self.data[i]))
            melopy_writer.writeframes(packed_val)
            melopy_writer.writeframes(packed_val)
            
        sys.stdout.write("\r[%s] 100%%" % ('='*50))
        sys.stdout.flush()
        sys.stdout.write("\nDone\n")
        melopy_writer.close()
        
# Licensed under The MIT License (MIT)
# See LICENSE file for more
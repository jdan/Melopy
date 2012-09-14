#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wave, struct, random, math
import os, sys

from utility import *
from scales  import *

# same included wave functions
# a function of frequency and tick
#   each function accepts the frequency and tick,
#   and returns a value from -1 to 1

sine     = lambda f, t: math.sin(2 * math.pi * t * f / 44100.0)
square   = lambda f, t: 0.6 * ((t % (44100 / f) >= ((44100 / f)/2)) * 2 - 1)
sawtooth = lambda f, t: (t % (44100 / f)) / (44100 / f) * 2 - 1
def triangle(f, t):
    v = 2 * (t % (44100 / f)) / (44100 / f)
    if t % (44100 / f) >= (44100 / (2 * f)):
        v = 2 * 1 - v
    v = 2 * v - 1
    return v

class Melopy:
    def __init__(self, title='sound', volume=20, tempo=120, octave=4):
        self.title = title.lower()
        self.rate = 44100
        self.volume = volume
        self.data = []

        self.tempo = tempo
        self.octave = octave
        self.wave_type = sine

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
            val = self.wave_type(frequency, n)
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

            self.add_wave(note_to_frequency(item, self.octave), length, location)

    def add_melody(self, melody, length):
        for note in melody:
            if note[-1] not in '0123456789':
                note += self.octave
            self.add_wave(note_to_frequency(note), length)

    def add_whole_note(self, note, location='END'):
        """Add a whole note"""
        self.add_fractional_note(note, 1.0, location)

    def add_half_note(self, note, location='END'):
        """Add a half note"""
        self.add_fractional_note(note, 1.0 / 2, location)

    def add_quarter_note(self, note, location='END'):
        """Add a quarter note"""
        self.add_fractional_note(note, 1.0 / 4, location)

    def add_eighth_note(self, note, location='END'):
        """Add a eigth note"""
        self.add_fractional_note(note, 1.0 / 8, location)

    def add_sixteenth_note(self, note, location='END'):
        """Add a sixteenth note"""
        self.add_fractional_note(note, 1.0 / 16, location)

    def add_fractional_note(self, note, fraction, location='END'):
        """Add a fractional note (smaller then 1/16 notes)"""
        self.add_note(note, 60.0 / self.tempo * (fraction * 4), location)

    def add_rest(self, length):
        for i in range(int(self.rate * length)):
            self.data.append(0)

    def add_whole_rest(self):
        self.add_fractional_rest(1.0)

    def add_half_rest(self):
        self.add_fractional_rest(1.0 / 2)

    def add_quarter_rest(self):
        self.add_fractional_rest(1.0 / 4)

    def add_eighth_rest(self):
        self.add_fractional_rest(1.0 / 8)

    def add_sixteenth_rest(self):
        self.add_fractional_rest(1.0 / 16)

    def add_fractional_rest(self, fraction):
        self.add_rest(60.0 / self.tempo * (fraction * 4))

    def parse(self, string, location='END'):
        tracks = string.split('&&&')

        # special case for multiple tracks
        if len(tracks) > 1:
            t = len(self.data) / 44100.0
            for track in tracks:
                self.parse(track, t)
            return

        cf = 0.25                    # start with a quarter note, change accordingly
        in_comment = False

        for i, char in enumerate(string):        # divide melody into fragments
            # / this is a comment /
            if char == '/':
                in_comment = not in_comment

            if in_comment:
                continue
            elif char in 'ABCDEFG':
                if (i+1 < len(string)) and (string[i+1] in '#b'):
                    # check if the next item in the array is
                    #    a sharp or flat, make sure we include it
                    char += string[i+1]

                self.add_fractional_note(char, cf, location)
                if location != 'END':
                    location += (60.0 / self.tempo * (cf * 4))
            elif char in map(str, range(0, 20)):
                self.octave = int(char)
            elif char == '+' or char == '^':
                self.octave += 1
            elif char == 'V' or char == 'v' or char == '-':
                self.octave -= 1
            elif char == '(' or char == ']':
                cf /= 2
            elif char == ')' or char == '[':
                cf *= 2
            elif char == '_':
                self.add_fractional_rest(cf)
                if location != 'END':
                    location += (60.0 / self.tempo * (cf * 4))

    def parsefile(self, filename, location='END'):
        fr = open(filename, 'r')
        s = fr.read()
        fr.close()

        self.parse(s, location)

    def render(self):
        """Render a playable song out to a .wav file"""
        melopy_writer = wave.open(self.title + '.wav', 'w')
        melopy_writer.setparams((2, 2, 44100, 0, 'NONE', 'not compressed'))
        p = -1
        data_frames = []

        for i in range(len(self.data)):
            q = 100 * i / len(self.data)
            if p != q:
                sys.stdout.write("\r[%s] %d%%" % (('='*int((float(i)/len(self.data)*50))+'>').ljust(50), 100 * i / len(self.data)))
                sys.stdout.flush()
                p = q
            packed_val = struct.pack('h', int(self.data[i]))
            data_frames.append(packed_val)
            data_frames.append(packed_val)

        melopy_writer.writeframes(''.join(data_frames))

        sys.stdout.write("\r[%s] 100%%" % ('='*50))
        sys.stdout.flush()
        sys.stdout.write("\nDone\n")
        melopy_writer.close()

# Licensed under The MIT License (MIT)
# See LICENSE file for more

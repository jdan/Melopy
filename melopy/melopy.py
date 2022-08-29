#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, absolute_import

import wave, struct, random, math
import os, sys

from melopy.utility import *
from melopy.scales  import *

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

    def add_wave(self, frequency, length, location='END', level=None):
        if location == 'END':
            location = len(self.data)
        elif location < 0:
            location = 0
        elif location * 44100 > len(self.data):
            location = len(self.data) / 44100.0

        # location is a time, so let's adjust
        location = int(location * 44100)

        if level == None:
            level = self.volume
        elif level > 100:
            level = 100
        elif level < 0:
            level = 0

        num_samples = int(44100 * length)
        fade_in_count = 0.005 * 44100
        fade_out_count = 0.005 * 44100
        fade_level = level

        #reduce the fade counts if the note isn't at least 8 times longer than the fade length
        if (fade_in_count * 8) > num_samples:
            fade_in_count = num_samples / 8
        if (fade_out_count * 8) > num_samples:
            fade_out_count = num_samples / 8

        for n in range(0, num_samples):
            fade_level = level

            #fade in
            if (n < fade_in_count):
                fade_level = n * level / fade_in_count

            #fade out
            samples_left = num_samples - n
            if samples_left < fade_out_count:
                fade_level = samples_left * level / fade_out_count

            wave_val = self.wave_type(frequency, n)
            val = wave_val * (fade_level / 100.0 * 32767)

            new_location = location + n

            if new_location >= len(self.data):
                self.data.append(val)
            else:
                current_val = self.data[new_location]
                if current_val + val > 32767:
                    val = 32767
                elif current_val + val < -32768:
                    val = -32768
                else:
                    val += current_val

                self.data[new_location] = val

    def add_note(self, note, length, location='END', volume=None):
        """Add a note, or if a list, add a chord."""
        if not isinstance(note, list):
            note = [note]

        if location == 'END':
            location = len(self.data) / 44100.0

        if not isinstance(volume, list):
            volume = [volume]
        if volume[0] == None:
            volume = [float(self.volume)/len(note)] * len(note)
            #By default, when adding a chord, set equal level for each
            #component note, such that the sum volume is self.volume
        else:
            volume = volume + [volume[-1]]*(len(note) - len(volume))
            #Otherwise, pad volume by repeating the final level so that we have
            #enough level values for each note

        for item, level in zip(note, volume):
            if not item[-1].isdigit():
                item += str(self.octave)

            self.add_wave(note_to_frequency(item, self.octave), length, location, level)

    def add_melody(self, melody, length):
        for note in melody:
            if not note[-1].isdigit():
                note += self.octave
            self.add_wave(note_to_frequency(note), length)

    def add_whole_note(self, note, location='END', volume=None):
        """Add a whole note"""
        self.add_fractional_note(note, 1.0, location, volume)

    def add_half_note(self, note, location='END', volume=None):
        """Add a half note"""
        self.add_fractional_note(note, 1.0 / 2, location, volume)

    def add_quarter_note(self, note, location='END', volume=None):
        """Add a quarter note"""
        self.add_fractional_note(note, 1.0 / 4, location, volume)

    def add_eighth_note(self, note, location='END', volume=None):
        """Add a eighth note"""
        self.add_fractional_note(note, 1.0 / 8, location, volume)

    def add_sixteenth_note(self, note, location='END', volume=None):
        """Add a sixteenth note"""
        self.add_fractional_note(note, 1.0 / 16, location, volume)

    def add_fractional_note(self, note, fraction, location='END', volume=None):
        """Add a fractional note (smaller then 1/16 notes)"""
        self.add_note(note, 60.0 / self.tempo * (fraction * 4), location, volume)

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

    def stdout_progress(percent):
        sys.stdout.write("\r[%s] %d%%" % (('='*int(percent * 0.5)+'>').ljust(50), percent))
        sys.stdout.flush()
        if (percent >= 100):
            sys.stdout.write("\r[%s] 100%%" % ('='*51))
            sys.stdout.flush()
            sys.stdout.write("\nDone\n")

    def render(self, update_callback=stdout_progress):
        """Render a playable song out to a .wav file"""
        melopy_writer = wave.open(self.title + '.wav', 'w')
        melopy_writer.setparams((2, 2, 44100, 0, 'NONE', 'not compressed'))
        last_percent = -1
        data_frames = []
        callback_present = callable(update_callback)

        for i in range(len(self.data)):
            percent = 100 * i // len(self.data)
            if callback_present and last_percent != percent:
                update_callback(percent)
                last_percent = percent 
            packed_val = struct.pack('h', int(self.data[i]))
            data_frames.append(packed_val)
            data_frames.append(packed_val)

        melopy_writer.writeframes(b''.join(data_frames))

        if callback_present:
            update_callback(100)

        melopy_writer.close()

    def play(self):
        """Opens the song in the os default program"""
        os.startfile(self.title + '.wav')

# Licensed under The MIT License (MIT)
# See LICENSE file for more

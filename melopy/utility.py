#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import log

def key_to_frequency(key):
    """Returns the frequency of the note (key) keys from A0"""
    return 440 * 2 ** ((key - 49) / 12.0)

def key_to_note(key, octaves=True):
    """Returns a string representing a note which is (key) keys from A0"""
    notes = ['a','a#','b','c','c#','d','d#','e','f','f#','g','g#']
    octave = (key + 8) / 12
    note = notes[(key - 1) % 12]

    if octaves:
        return note.upper() + str(octave)
    else:
        return note.upper()

def note_to_frequency(note, default=4):
    """Returns the frequency of a note represented by a string"""
    return key_to_frequency(note_to_key(note, default))

def note_to_key(note, default=4):
    """Returns the key number (keys from A0) from a note represented by a string"""
    indices = { 'C':0, 'D':2, 'E':4, 'F':5, 'G':7, 'A':9, 'B':11 }

    octave = default

    if note[-1] in '012345678':
        octave = int(note[-1])

    tone = indices[note[0].upper()]
    key = 12 * octave + tone

    if len(note) > 1 and note[1] == '#':
        key += 1
    elif len(note) > 1 and note[1] == 'b':
        key -= 1

    return key - 8;

def frequency_to_key(frequency):
    return int(12 * log(frequency/440.0) / log(2) + 49)

def frequency_to_note(frequency):
    return key_to_note(frequency_to_key(frequency))

# Licensed under The MIT License (MIT)
# See LICENSE file for more

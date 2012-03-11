#!/usr/bin/python

from melopy import *

def frequency_up_fifth(f):
    # returns a frequency of the fifth note up from the given frequency
    return key_to_frequency(frequency_to_key(f) + 5)

def fifth_saw(f, t):
    # sawtooth wave representing a note and its fifth
    return sawtooth(f, t) + sawtooth(frequency_up_fifth(f), t)

if __name__ == '__main__':
    m = Melopy('fifths')

    # change the wave_type
    m.wave_type = fifth_saw

    m.parse('C Eb G G Eb [C]')
    m.render()

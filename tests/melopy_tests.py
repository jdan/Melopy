#!/usr/bin/env
# -*- coding: utf-8 -*-

import unittest

from nose.tools import *

from melopy import *

def data_provider(data):
    def decorator(fn):
        def repl(self, *args):
            for i in data():
                fn(self, *i)
        return repl
    return decorator

class LibraryFunctionsTests(unittest.TestCase):
    def test_key_to_frequency(self):
        key = 49
        self.assertEqual(440, utility.key_to_frequency(key))

    def test_note_to_frequency(self):
        note = 'A4'
        self.assertEqual(440, utility.note_to_frequency(note))

    def test_note_to_key(self):
        note = 'A4'
        self.assertEqual(49, utility.note_to_key(note))

    def test_key_to_note(self):
        key = 49
        self.assertEqual('A4', utility.key_to_note(key))

    def test_iterate(self):
        start = 'D4'
        pattern = [2, 2, 1, 2, 2, 2]
        should_be = ['D4', 'E4', 'F#4', 'G4', 'A4', 'B4', 'C#5']
        self.assertEqual(should_be, iterate(start, pattern))

    def test_generate_major_scales(self):
        start = 'D4'
        should_be = ['D4', 'E4', 'F#4', 'G4', 'A4', 'B4', 'C#5']
        self.assertEqual(should_be, scales.generateScale('major', start))

    def test_generate_minor_scales(self):
        start = 'C4'
        should_be = ['C4', 'D4', 'D#4', 'F4', 'G4', 'G#4', 'A#4']
        self.assertEqual(should_be, scales.generateScale('minor', start))

    def test_generate_chromatic_scales(self):
        start = 'C5'
        should_be= ['C5', 'C#5', 'D5', 'D#5', 'E5', 'F5', 'F#5', 'G5', 'G#5', 'A5', 'A#5', 'B5']
        self.assertEqual(should_be, scales.generateScale('chromatic', start))

    def test_generate_major_pentatonic_scales(self):
        start = 'C5'
        should_be = ['C5', 'D5', 'E5', 'G5', 'A5']
        self.assertEqual(should_be, scales.generateScale('major_pentatonic', start))

    def test_generate_minor_pentatonic_scales(self):
        start = 'A5'
        should_be = ['A5', 'C6', 'D6', 'E6', 'G6']
        self.assertEqual(should_be, scales.generateScale('minor_pentatonic', start))
       
    def test_generate_major_triad(self):
        start = 'A4'
        should_be = ['A4', 'C#5', 'E5']
        self.assertEqual(should_be, scales.major_triad(start))

    def test_generate_minor_triad(self):
        start = 'C5'
        should_be = ['C5', 'D#5', 'G5']
        self.assertEqual(should_be, scales.minor_triad(start))


if __name__ == '__main__':
    unittest.main()

# Licensed under The MIT License (MIT)
# See LICENSE file for more

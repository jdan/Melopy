#!/usr/bin/env
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, nested_scopes

import unittest

from melopy import chords, scales, utility, exceptions

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
        self.assertEqual(should_be, utility.iterate(start, pattern))

    def test_generate_major_scales(self):
        start = 'D4'
        should_be = ['D4', 'E4', 'F#4', 'G4', 'A4', 'B4', 'C#5','D5']
        self.assertEqual(should_be, scales.generateScale('major', start))

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

    def test_generate_dorian_mode(self):
        start = 'D5'
        should_be = ['D5','E5','F5','G5','A5','B5','C6','D6']
        self.assertEqual(should_be, scales.generateScale('major', start, mode=2))

    def test_generate_phrygian_mode(self):
        start = 'E5'
        should_be = ['E5','F5','G5','A5','B5','C6','D6','E6']
        self.assertEqual(should_be, scales.generateScale('major', start, mode=3))

    def test_generate_lydian_mode(self):
        start = 'C5'
        should_be = ['C5','D5','E5','F#5','G5','A5','B5','C6']
        self.assertEqual(should_be, scales.generateScale('major', start, mode=4))

    def test_generate_mixolydian_mode(self):
        start = 'C5'
        should_be = ['C5','D5','E5','F5','G5','A5','A#5','C6']
        self.assertEqual(should_be, scales.generateScale('major', start, mode=5))

    def test_generate_dorian_flat_nine(self):
        start = 'D5'
        should_be = ['D5','D#5','F5','G5','A5','B5','C6','D6']
        self.assertEqual(should_be, scales.generateScale('melodic_minor', start, mode=2))

    def test_generate_lydian_augmented(self):
        start = 'C5'
        should_be = ['C5','D5','E5','F#5','G#5','A5','B5','C6']
        self.assertEqual(should_be, scales.generateScale('melodic_minor', start, mode=3))

    def test_generate_lydian_dominant(self):
        start = 'C5'
        should_be = ['C5','D5','E5','F#5','G5','A5','A#5','C6']
        self.assertEqual(should_be, scales.generateScale('melodic_minor', start, mode=4))

    def test_generate_major_triad(self):
        start = 'C5'
        should_be = ['C5','E5','G5']
        self.assertEqual(should_be, chords.generateChord('maj', start))

    def test_generate_min_triad(self):
        start = 'C5'
        should_be = ['C5','D#5','G5']
        self.assertEqual(should_be, chords.generateChord('min', start))

    def test_generate_maj_first_inversion(self):
        start = 'C5'
        should_be = ['E5','G5','C5']
        self.assertEqual(should_be, chords.generateChord('maj', start, inversion=1))

    def test_generate_maj_second_inversion(self):
        start = 'C5'
        should_be = ['G5','C5','E5']
        self.assertEqual(should_be, chords.generateChord('maj', start, inversion=2))

    def test_generate_maj_seven(self):
        start = 'C5'
        should_be = ['C5','E5','G5','B5']
        self.assertEqual(should_be, chords.generateChord('maj7', start))

    def test_generate_maj_seven(self):
        start = 'C5'
        should_be = ['C5','E5','G5','B5']
        self.assertEqual(should_be, chords.generateChord('maj7', start))

    def test_generate_aug(self):
        start = 'C5'
        should_be = ['C5','E5','G#5']
        self.assertEqual(should_be, chords.generateChord('aug', start))

    def test_generate_dim(self):
        start = 'C5'
        should_be = ['C5','D#5','F#5']
        self.assertEqual(should_be, chords.generateChord('dim', start))

    def test_generate_seven(self):
        start = 'C5'
        should_be = ['C5','E5','G5','A#5']
        self.assertEqual(should_be, chords.generateChord('7', start))


if __name__ == '__main__':
    unittest.main()

# Licensed under The MIT License (MIT)
# See LICENSE file for more

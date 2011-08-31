#!/usr/bin/env
# -*- coding: utf-8 -*-

from unittest import TestCase

from nose.tools import *

from melopy import *

class LibraryFunctionsTests(TestCase):
    def test_frequency_from_key(self):
        key = 49
        assert frequency_from_key(key) == 440

    def test_frequency_from_note(self):
        note = 'A4'
        assert frequency_from_note(note) == 440

    def test_key_from_note(self):
        note = 'A4'
        assert key_from_note(note) == 49

    def test_note_from_key(self):
        key = 49
        assert note_from_key(key) == 'A4'

    def test_iterate(self):
        start = 'D4'
        pattern = [2, 2, 1, 2, 2, 2]
        should_be = ['D4', 'E4', 'F#4', 'G4', 'A4', 'B4', 'C#5']
        assert iterate(start, pattern) == should_be

    def test_generate_major_scale(self):
        start = 'D4'
        should_be = ['D4', 'E4', 'F#4', 'G4', 'A4', 'B4', 'C#5']
        assert generate_major_scale(start) == should_be

    def test_generate_minor_scale(self):
        start = 'C4'
        should_be = ['C4', 'D4', 'D#4', 'F4', 'G4', 'G#4', 'A#4']
        assert generate_minor_scale(start) == should_be

    def test_generate_chromatic_scale(self):
        start = 'C5'
        should_be= ['C5', 'C#5', 'D5', 'D#5', 'E5', 'F5', 'F#5', 'G5', 'G#5', 'A5', 'A#5', 'B5']
        assert generate_chromatic_scale(start) == should_be

    def test_generate_major_pentatonic_scale(self):
        start = 'C5'
        should_be = ['C5', 'D5', 'E5', 'G5', 'A5']
        assert generate_major_pentatonic_scale(start) == should_be

    def test_generate_minor_pentatonic_scale(self):
        start = 'A5'
        should_be = ['A5', 'C6', 'D6', 'E6', 'G6']
        assert generate_minor_pentatonic_scale(start) == should_be
	

    def test_generate_ionian_mode(self):
        start = 'D4'
        should_be = ['D4', 'E4', 'F#4', 'G4', 'A4', 'B4', 'C#5']
        assert generate_mode(start, 'ionian') == should_be

    def test_generate_dorian_mode(self):
        start = 'E4'
        should_be = ['E4', 'F#4', 'G4', 'A4', 'B4', 'C#5', 'D5']
        assert generate_mode(start, 'dorian') == should_be

    def test_generate_phrygian_mode(self):
        start = 'F#4'
        should_be = ['F#4', 'G4', 'A4', 'B4', 'C#5', 'D5', 'E5']
        assert generate_mode(start, 'phrygian') == should_be

    def test_generate_lydian_mode(self):
        start = 'G4'
        should_be = ['G4', 'A4', 'B4', 'C#5', 'D5', 'E5','F#5']
        assert generate_mode(start, 'lydian') == should_be

    def test_generate_mixolydian_mode(self):
        start = 'A4'
        should_be = ['A4', 'B4', 'C#5', 'D5', 'E5','F#5', 'G5']
        assert generate_mode(start, 'mixolydian') == should_be

    def test_generate_aeolian_mode(self):
        start = 'B4'
        should_be = ['B4', 'C#5', 'D5', 'E5','F#5', 'G5', 'A5']
        assert generate_mode(start, 'aeolian') == should_be

    def test_generate_locrian_mode(self):
        start = 'C#5'
        should_be = ['C#5', 'D5', 'E5','F#5', 'G5', 'A5', 'B5']
        assert generate_mode(start, 'locrian') == should_be
    
    
    
    def test_generate_major_triad(self):
        start = 'A4'
        should_be = ['A4', 'C#5', 'E5']
        assert generate_major_triad(start) == should_be

    def test_generate_minor_triad(self):
        start = 'C5'
        should_be = ['C5', 'D#5', 'G5']
        assert generate_minor_triad(start) == should_be


class MelopyTests(TestCase):
    def test_dummy(self):
        assert True

# Licensed under The MIT License (MIT)
# See LICENSE file for more

#!/usr/bin/env
# -*- coding: utf-8 -*-

from unittest import TestCase

from nose.tools import *

from melopy import *

class LibraryFunctionsTests(TestCase):
    def test_key_to_frequency(self):
        key = 49
        assert utility.key_to_frequency(key) == 440

    def test_note_to_frequency(self):
        note = 'A4'
        assert utility.note_to_frequency(note) == 440

    def test_note_to_key(self):
        note = 'A4'
        assert utility.note_to_key(note) == 49

    def test_key_to_note(self):
        key = 49
        assert utility.key_to_note(key) == 'A4'

    def test_iterate(self):
        start = 'D4'
        pattern = [2, 2, 1, 2, 2, 2]
        should_be = ['D4', 'E4', 'F#4', 'G4', 'A4', 'B4', 'C#5']
        assert iterate(start, pattern) == should_be

    def test_generate_major_scales(self):
        start = 'D4'
        should_be = ['D4', 'E4', 'F#4', 'G4', 'A4', 'B4', 'C#5']
        assert scales.generateScale('major', start) == should_be

    def test_generate_minor_scales(self):
        start = 'C4'
        should_be = ['C4', 'D4', 'D#4', 'F4', 'G4', 'G#4', 'A#4']
        assert scales.generateScale('minor', start) == should_be

    def test_generate_chromatic_scales(self):
        start = 'C5'
        should_be= ['C5', 'C#5', 'D5', 'D#5', 'E5', 'F5', 'F#5', 'G5', 'G#5', 'A5', 'A#5', 'B5']
        assert scales.generateScale('chromatic', start) == should_be

    def test_generate_major_pentatonic_scales(self):
        start = 'C5'
        should_be = ['C5', 'D5', 'E5', 'G5', 'A5']
        assert scales.generateScale('major_pentatonic', start) == should_be

    def test_generate_minor_pentatonic_scales(self):
        start = 'A5'
        should_be = ['A5', 'C6', 'D6', 'E6', 'G6']
        assert scales.generateScale('minor_pentatonic', start) == should_be
       
    def test_generate_major_triad(self):
        start = 'A4'
        should_be = ['A4', 'C#5', 'E5']
        assert scales.major_triad(start) == should_be

    def test_generate_minor_triad(self):
        start = 'C5'
        should_be = ['C5', 'D#5', 'G5']
        assert scales.minor_triad(start) == should_be


class MelopyTests(TestCase):
    def test_dummy(self):
        assert True

# Licensed under The MIT License (MIT)
# See LICENSE file for more
